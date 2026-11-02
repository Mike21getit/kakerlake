#!/usr/bin/env python3
"""Ganzseiten-Screenshot per Chrome DevTools Protocol.
Aufruf: python3 tools/screenshot.py URL BREITE AUSGABE.png"""
import json, subprocess, sys, time, base64, urllib.request, websocket, tempfile
url, width, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
mobile = width < 600
port = 9333
prof = tempfile.mkdtemp()
p = subprocess.Popen(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                      f'--remote-debugging-port={port}', f'--user-data-dir={prof}', f'--window-size={width},900', 'about:blank'],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            tabs = json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json')); break
        except Exception: time.sleep(.2)
    ws = websocket.create_connection([t for t in tabs if t['type'] == 'page'][0]['webSocketDebuggerUrl'], suppress_origin=True)
    n = [0]
    def call(method, **params):
        n[0] += 1; ws.send(json.dumps({'id': n[0], 'method': method, 'params': params}))
        while True:
            m = json.loads(ws.recv())
            if m.get('id') == n[0]: return m.get('result', {})
    vh = 844 if mobile else 900
    call('Emulation.setDeviceMetricsOverride', width=width, height=vh, deviceScaleFactor=1, mobile=mobile)
    call('Page.enable')
    call('Page.navigate', url=url)
    time.sleep(4)
    # durch die Seite scrollen, damit alle Reveal-Animationen auslösen
    h = call('Runtime.evaluate', expression='document.documentElement.scrollHeight', returnByValue=True)['result']['value']
    for y in range(0, h, 400):
        call('Runtime.evaluate', expression=f'window.scrollTo(0,{y})'); time.sleep(.12)
    call('Runtime.evaluate', expression="document.querySelectorAll('.reveal').forEach(e=>e.classList.add('is-visible'));window.scrollTo(0,0)")
    time.sleep(2.5)
    # Hero auf Viewport-Höhe fixieren, sonst wächst 100svh mit der Aufnahmegröße
    call('Runtime.evaluate', expression=f"document.querySelector('.hero').style.minHeight='{vh}px'")
    h = call('Runtime.evaluate', expression='document.documentElement.scrollHeight', returnByValue=True)['result']['value']
    shot = call('Page.captureScreenshot', format='png', captureBeyondViewport=True,
                clip={'x': 0, 'y': 0, 'width': width, 'height': h, 'scale': 1})
    open(out, 'wb').write(base64.b64decode(shot['data']))
    print(out, width, h)
finally:
    p.kill()
