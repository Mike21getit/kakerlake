#!/usr/bin/env python3
"""Erzeugt die selbst gezeichneten SVG-Illustrationen (keine Fremdbilder).
Aufruf: python3 tools/make_svgs.py  -> schreibt nach img/
Draufsicht auf die vier in Deutschland relevanten Schabenarten + Hero-Grafik."""
import os, math
OUT = os.path.join(os.path.dirname(__file__), '..', 'img')

SPECIES = {
    # key: (Titel, Körperfarbe, Rand/Schatten, Halsschild, Flügel, Beine, Muster, Länge-Faktor, Flügeltyp)
    'deutsche': dict(
        title='Deutsche Schabe (Blattella germanica), Illustration in Draufsicht',
        body='#9a6a35', dark='#5e3c1a', pron='#c09052', wing='#a9783f', leg='#8a5f30',
        pattern='stripes', length=1.0, width=1.0, wings='full'),
    'orientalische': dict(
        title='Orientalische Schabe (Blatta orientalis), Weibchen mit Stummelflügeln, Illustration in Draufsicht',
        body='#2e1d15', dark='#160d09', pron='#34221a', wing='#3f2a1e', leg='#5a3d2b',
        pattern='plain', length=1.0, width=1.12, wings='stub'),
    'amerikanische': dict(
        title='Amerikanische Schabe (Periplaneta americana), Illustration in Draufsicht',
        body='#8b3d1d', dark='#55220e', pron='#7a3214', wing='#9a4721', leg='#7a3a1c',
        pattern='rim', length=1.0, width=.92, wings='long'),
    'braunband': dict(
        title='Braunbandschabe (Supella longipalpa), Illustration in Draufsicht',
        body='#6e4224', dark='#40230f', pron='#5a3319', wing='#7b4a28', leg='#7a5230',
        pattern='bands', length=1.0, width=1.0, wings='full'),
}

def roach(key, inner=False):
    s = SPECIES[key]
    W = s['width']
    cx = 200
    p = []
    a = p.append
    if not inner:
        a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 560" role="img">')
        a(f'<title>{s["title"]}</title>')
    uid = key[:3]
    a('<defs>')
    a(f'<radialGradient id="sh-{uid}" cx=".38" cy=".3" r=".85"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".55" stop-color="#fff" stop-opacity=".04"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></radialGradient>')
    a('</defs>')
    # Fühler (sehr lang, geschwungen)
    ant_len = 1.25 if key == 'amerikanische' else 1.0
    for side in (1, -1):
        x1, y1 = cx + side * 10, 100
        c1 = (cx + side * 40, 60)
        c2 = (cx + side * 120 * ant_len, 40 - 10 * ant_len)
        e = (cx + side * min(190, 150 * ant_len), 6)
        a(f'<path d="M{x1} {y1} C {c1[0]} {c1[1]} {c2[0]:.0f} {c2[1]:.0f} {e[0]:.0f} {e[1]}" fill="none" stroke="{s["dark"]}" stroke-width="3" stroke-linecap="round"/>')
    # Beine: (Ansatz y, Gelenk, Fuß) rechts, links gespiegelt; Schienen mit Dornen
    legs = [
        (178, (262, 150), (300, 112)),
        (222, (286, 236), (346, 214)),
        (262, (284, 330), (338, 420)),
    ]
    for side in (1, -1):
        for y, knee, foot in legs:
            x0 = cx + side * 34 * W
            kx = cx + side * (knee[0] - 200) * W
            fx = cx + side * (foot[0] - 200) * W
            a(f'<path d="M{x0:.1f} {y} L{kx:.1f} {knee[1]} L{fx:.1f} {foot[1]}" fill="none" stroke="{s["leg"]}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
            # Dornen an der Schiene
            for t in (.3, .55, .8):
                px = kx + (fx - kx) * t
                py = knee[1] + (foot[1] - knee[1]) * t
                dx, dy = fx - kx, foot[1] - knee[1]
                L = math.hypot(dx, dy)
                nx, ny = -dy / L * 9, dx / L * 9
                a(f'<path d="M{px:.1f} {py:.1f} l{nx:.1f} {ny:.1f}" stroke="{s["leg"]}" stroke-width="2" stroke-linecap="round"/>')
    # Cerci (Hinterleibsanhänge)
    tail = 520 if s['wings'] != 'stub' else 500
    for side in (1, -1):
        a(f'<path d="M{cx + side * 14} {tail - 22} L{cx + side * 30} {tail + 18}" stroke="{s["dark"]}" stroke-width="5" stroke-linecap="round"/>')
    # Hinterleib (segmentiert, sichtbar bei Stummelflügeln)
    a(f'<path d="M{cx} 196 C {cx + 92 * W:.0f} 200 {cx + 96 * W:.0f} 330 {cx + 80 * W:.0f} 420 C {cx + 64 * W:.0f} 480 {cx + 30 * W:.0f} {tail - 10} {cx} {tail} C {cx - 30 * W:.0f} {tail - 10} {cx - 64 * W:.0f} 480 {cx - 80 * W:.0f} 420 C {cx - 96 * W:.0f} 330 {cx - 92 * W:.0f} 200 {cx} 196 Z" fill="{s["body"]}"/>')
    if s['wings'] == 'stub':
        for i, y in enumerate(range(300, 500, 26)):
            hw = 88 * W * (1 - ((y - 300) / 230) ** 2 * .75)
            a(f'<path d="M{cx - hw:.1f} {y} Q {cx} {y + 12} {cx + hw:.1f} {y}" fill="none" stroke="{s["dark"]}" stroke-width="2.4" opacity=".9"/>')
        # Stummelflügel
        for side in (1, -1):
            a(f'<path d="M{cx + side * 6} 206 C {cx + side * 60 * W:.0f} 206 {cx + side * 86 * W:.0f} 236 {cx + side * 82 * W:.0f} 270 C {cx + side * 60 * W:.0f} 290 {cx + side * 20} 284 {cx + side * 6} 272 Z" fill="{s["wing"]}" stroke="{s["dark"]}" stroke-width="1.5"/>')
    else:
        wing_end = {'full': 500, 'long': 540}[s['wings']]
        for side in (1, -1):
            a(f'<path d="M{cx + side * 2} 200 C {cx + side * 70 * W:.0f} 200 {cx + side * 98 * W:.0f} 300 {cx + side * 88 * W:.0f} 400 C {cx + side * 80 * W:.0f} 470 {cx + side * 40 * W:.0f} {wing_end - 6} {cx - side * 4} {wing_end} C {cx - side * 2} 420 {cx - side * 4} 300 {cx + side * 2} 200 Z" fill="{s["wing"]}" stroke="{s["dark"]}" stroke-width="1.6" opacity=".97"/>')
            # Flügeladern
            a(f'<path d="M{cx + side * 20} 214 C {cx + side * 60 * W:.0f} 280 {cx + side * 66 * W:.0f} 380 {cx + side * 40 * W:.0f} {wing_end - 60}" fill="none" stroke="{s["dark"]}" stroke-opacity=".45" stroke-width="1.3"/>')
            a(f'<path d="M{cx + side * 50 * W:.0f} 230 C {cx + side * 80 * W:.0f} 290 {cx + side * 82 * W:.0f} 360 {cx + side * 70 * W:.0f} 430" fill="none" stroke="{s["dark"]}" stroke-opacity=".35" stroke-width="1.2"/>')
        if s['pattern'] == 'bands':
            # zwei helle Querbänder über die Flügel
            for y0, h in ((262, 26), (352, 22)):
                a(f'<path d="M{cx - 92 * W:.0f} {y0} C {cx - 40} {y0 + 14} {cx + 40} {y0 + 14} {cx + 92 * W:.0f} {y0} L{cx + 90 * W:.0f} {y0 + h} C {cx + 40} {y0 + h + 14} {cx - 40} {y0 + h + 14} {cx - 90 * W:.0f} {y0 + h} Z" fill="#d9b27a" opacity=".78" clip-path="url(#wc-{uid})"/>')
            a(f'<clipPath id="wc-{uid}"><path d="M{cx} 196 C {cx + 100 * W:.0f} 200 {cx + 100 * W:.0f} 330 {cx + 88 * W:.0f} 420 C {cx + 70 * W:.0f} 490 {cx + 30} 506 {cx} 510 C {cx - 30} 506 {cx - 70 * W:.0f} 490 {cx - 88 * W:.0f} 420 C {cx - 100 * W:.0f} 330 {cx - 100 * W:.0f} 200 {cx} 196 Z"/></clipPath>')
    # Kopf (schaut unter dem Halsschild hervor)
    a(f'<ellipse cx="{cx}" cy="110" rx="21" ry="17" fill="{s["dark"]}"/>')
    for side in (1, -1):
        a(f'<ellipse cx="{cx + side * 13}" cy="106" rx="5" ry="7" fill="#0c0806"/>')
    # Halsschild (Pronotum), überdeckt den Kopf zum Teil
    a(f'<path d="M{cx} 118 C {cx + 58 * W:.0f} 118 {cx + 76 * W:.0f} 150 {cx + 72 * W:.0f} 184 C {cx + 66 * W:.0f} 210 {cx + 30} 214 {cx} 212 C {cx - 30} 214 {cx - 66 * W:.0f} 210 {cx - 72 * W:.0f} 184 C {cx - 76 * W:.0f} 150 {cx - 58 * W:.0f} 118 {cx} 118 Z" fill="{s["pron"]}" stroke="{s["dark"]}" stroke-width="1.6"/>')
    if s['pattern'] == 'stripes':
        for side in (1, -1):
            a(f'<path d="M{cx + side * 14} 128 C {cx + side * 22} 150 {cx + side * 24} 180 {cx + side * 18} 206" fill="none" stroke="#3a220e" stroke-width="10" stroke-linecap="round"/>')
    if s['pattern'] == 'rim':
        a(f'<path d="M{cx} 126 C {cx + 50 * W:.0f} 126 {cx + 66 * W:.0f} 154 {cx + 62 * W:.0f} 182 C {cx + 56 * W:.0f} 202 {cx + 26} 204 {cx} 203 C {cx - 26} 204 {cx - 56 * W:.0f} 202 {cx - 62 * W:.0f} 182 C {cx - 66 * W:.0f} 154 {cx - 50 * W:.0f} 126 {cx} 126 Z" fill="none" stroke="#e2b25c" stroke-width="7" opacity=".9"/>')
        a(f'<ellipse cx="{cx}" cy="166" rx="{36 * W:.0f}" ry="24" fill="#5a240d" opacity=".75"/>')
    if s['pattern'] == 'bands':
        a(f'<path d="M{cx - 64 * W:.0f} 172 C {cx - 30} 182 {cx + 30} 182 {cx + 64 * W:.0f} 172" fill="none" stroke="#d9b27a" stroke-width="6" opacity=".7"/>')
    # Glanz
    a(f'<path d="M{cx} 118 C {cx + 58 * W:.0f} 118 {cx + 76 * W:.0f} 150 {cx + 72 * W:.0f} 184 C {cx + 66 * W:.0f} 210 {cx + 30} 214 {cx} 212 C {cx - 30} 214 {cx - 66 * W:.0f} 210 {cx - 72 * W:.0f} 184 C {cx - 76 * W:.0f} 150 {cx - 58 * W:.0f} 118 {cx} 118 Z" fill="url(#sh-{uid})"/>')
    a(f'<path d="M{cx} 200 C {cx + 92 * W:.0f} 204 {cx + 96 * W:.0f} 330 {cx + 80 * W:.0f} 420 C {cx + 64 * W:.0f} 480 {cx + 30 * W:.0f} {tail - 10} {cx} {tail} C {cx - 30 * W:.0f} {tail - 10} {cx - 64 * W:.0f} 480 {cx - 80 * W:.0f} 420 C {cx - 96 * W:.0f} 330 {cx - 92 * W:.0f} 204 {cx} 200 Z" fill="url(#sh-{uid})" opacity=".7"/>')
    if not inner:
        a('</svg>')
    return '\n'.join(p)


def hero():
    # Fliesenraster (Küche) + Lichtkegel + Deutsche Schabe + Eipaket
    tiles = []
    for x in range(0, 901, 100):
        tiles.append(f'<path d="M{x} 0V1200"/>')
    for y in range(0, 1201, 100):
        tiles.append(f'<path d="M0 {y}H900"/>')
    rb = roach('deutsche', inner=True)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1200" role="img">
<title>Deutsche Schabe auf Küchenfliesen im Lichtkegel einer Taschenlampe, Illustration</title>
<defs>
<radialGradient id="glow" cx=".5" cy=".46" r=".55"><stop offset="0" stop-color="#e0a24a" stop-opacity=".30"/><stop offset=".55" stop-color="#e0a24a" stop-opacity=".06"/><stop offset="1" stop-color="#0b0b0c" stop-opacity="0"/></radialGradient>
<radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/></radialGradient>
</defs>
<rect width="900" height="1200" fill="#0f0e0d"/>
<g stroke="#e0a24a" stroke-opacity=".09" stroke-width="3">{''.join(tiles)}</g>
<rect width="900" height="1200" fill="url(#glow)"/>
<g transform="translate(450 560) rotate(-22) scale(1.35) translate(-200 -300)">{rb}</g>
<g transform="translate(700 930) rotate(18)">
  <rect x="-34" y="-15" width="68" height="30" rx="14" fill="#5a3a1c"/>
  <g stroke="#2e1d0c" stroke-width="2">{''.join(f'<path d="M{x} -13V13"/>' for x in range(-24, 30, 8))}</g>
  <path d="M-30 -15 H30" stroke="#8a6034" stroke-width="3"/>
</g>
<g fill="#2b1d12"><circle cx="210" cy="960" r="4"/><circle cx="228" cy="972" r="3"/><circle cx="196" cy="984" r="3.5"/><circle cx="240" cy="950" r="2.6"/><circle cx="222" cy="996" r="2.4"/></g>
<rect width="900" height="1200" fill="url(#vig)"/>
</svg>'''


files = {f'schabe-{k}.svg': roach(k) for k in SPECIES}
files['hero-schabe.svg'] = hero()
for name, svg in files.items():
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(svg + '\n')
print('ok', ', '.join(files))
