# Schabenbekämpfung – Website der Falkner Schädlingsbekämpfung GmbH (Bonn/Köln/Rhein-Sieg · Mannheim/Rhein-Neckar)

Statische One-Page-Website (HTML/CSS/JS, kein Framework, kein Backend) zur Schabenbekämpfung („Kakerlaken bekämpfen“).
Layout, Typografie, CSS/JS und Komponenten sind 1:1 von der Hornissen-Seite (`hornisse-site`, https://www.vespa-velutina.com/)
übernommen – gleicher Header mit Logo, Navigation mit Scrollspy, Anrufen-Auswahl, Kontaktbereich, Impressum, Datenschutz,
Footer, Lightbox und Bernstein-Akzent `#e0a24a`.

Domain: https://www.kakerlake.net/ (Datei `CNAME` = `www.kakerlake.net`). **Noch nicht veröffentlicht** – lokales Git-Repo, kein Remote.

## Struktur

```
index.html              Alle Inhalte inkl. Impressum (#impressum) und Datenschutz (#datenschutz)
css/style.css           CSS der Hornissen-Seite + Ergänzungen am Ende („Ergänzungen für die Schaben-Seite“)
js/main.js              Navigation, Scrollspy, Einblend-Animationen, mailto-Anfrageformular, Lightbox, Anrufen-Auswahl
fonts/                  Cormorant Garamond (SIL Open Font License), lokal eingebunden
img/schabe-*.svg        Eigene Illustrationen der vier Arten (deutsche, orientalische, amerikanische, braunband)
img/hero-schabe.svg     Startbild (Illustration, kein Foto)
img/og-image.jpg        Vorschaubild für Social Media (1200×630, aus hero-schabe.svg + Schriftzug, per Headless Chrome gerendert)
img/qualifikation-zeugnis-schaedlingsbekaempfer(-800).webp  Sachkundenachweis (aus der Hornissen-Seite)
img/logo/               Firmenlogo (wie Hornissen-Seite)
favicon.ico, favicon-32.png, apple-touch-icon.png (Grasmarke aus dem Logo)
CNAME                   www.kakerlake.net
robots.txt, sitemap.xml, llms.txt
tools/make_svgs.py      Erzeugt die Schaben-Illustrationen und das Startbild neu (python3 tools/make_svgs.py)
tools/screenshot.py     Ganzseiten-Screenshot per Headless Chrome (benötigt websocket-client)
```

## Abschnitte

Hero · 01 Erkennen (4 Arten, Vergleichstabelle) · 02 Anzeichen · 03 Warum professionell (Risiken) · 04 Ablauf ·
05 Vorbeugung · 06 Gewerbe & Gastronomie (inkl. Quellen) · Über uns · 07 FAQ · Kontakt/Standorte · Impressum · Datenschutz.

## Firmendaten (übernommen von der Hornissen-Seite, Stand 02.11.2026)

| Feld | Wert | Wo |
|---|---|---|
| Firmenname / Rechtsform | Falkner Schädlingsbekämpfung GmbH | Header, Texte, Impressum, Datenschutz, Footer, `<title>`, Meta/OG, JSON-LD |
| Hauptsitz Bonn | Heinrich-Heine-Str. 41, 53225 Bonn · 0228 4336945 (`tel:+492284336945`) | Anrufen-Auswahl, Kontakt, Impressum, Datenschutz, JSON-LD |
| Standort Königswinter | Am Lindenbaum 14, 53639 Königswinter · 02244 8732038 (`tel:+4922448732038`) | dto. |
| Standort Mannheim | Neuhofer Straße 15, 68219 Mannheim · 0621 72492117 (`tel:+4962172492117`) | dto. |
| Standort Reilingen | Erich-Kästner-Ring 13, 68799 Reilingen · 06205 202135 (`tel:+496205202135`) | dto. – **bitte bestätigen** (auf falkner-sbk.de ist teils Hockenheim genannt) |
| E-Mail | mail@falkner-sbk.de | Kontakt, Formular (`data-mailto`/`action`), Impressum, Datenschutz, JSON-LD |
| Hauptwebsite | https://www.falkner-sbk.de | Menü, Über uns, Kontakt, Impressum, Footer, JSON-LD `sameAs` |
| Sitz / Register | Sitz Bonn · Amtsgericht Bonn, HRB 16142 | Impressum |
| Geschäftsführer | Dipl.-Wirtsch.-Ing. Michael Falkner | Impressum, Datenschutz, Über uns |
| USt-IdNr. | DE259876663 | Impressum, JSON-LD `vatID` |
| Erreichbarkeit | 08:30 – 18:00 Uhr | Kontakt, Anrufen-Auswahl, Gewerbe-Box |

## Platzhalter – noch offen

Alle Platzhalter stehen in **eckigen Klammern** und sind auf der Seite orange markiert (Klasse `ph`).
Suchen mit: `grep -n 'class="ph"' index.html`

| Platzhalter | Wo | Hinweis |
|---|---|---|
| `[FOTO DEUTSCHE SCHABE]`, `[FOTO ORIENTALISCHE SCHABE]`, `[FOTO WEITERE ART]` | Erkennen | eigene Fotos folgen |
| `[FOTO KOTSPUREN]`, `[FOTO OOTHEKEN]`, `[FOTO BEFALLSSTELLE]` | Anzeichen | eigene Fotos folgen |
| `[FOTO INSPEKTION]`, `[FOTO KLEBEFALLE]`, `[FOTO GELKÖDER]` | Ablauf | eigene Fotos folgen |
| `[FOTO GEWERBEKÜCHE]`, `[FOTO DOKUMENTATION]` | Gewerbe | eigene Fotos folgen |
| `[FOTO INHABER]` | Über uns | Porträt oder Teamfoto |
| `[Vertragsmodelle / Kontrollintervalle bitte ergänzen]` | Gewerbe → Monitoring | keine Intervalle/Preise erfunden |
| `[bitte bestätigen: neutrales Fahrzeug / Einsätze außerhalb der Öffnungszeiten]` | Gewerbe → Diskretion | |
| `November 2026` (Stand der Informationen) | Gewerbe → Hinweis | bei Änderungen aktualisieren |
| `[Weitere Qualifikationen, Mitgliedschaften oder Zertifizierungen …]` | Über uns | nur echte Angaben (z. B. Verbandsmitgliedschaft) |
| `[Name und Sitz des Versicherers …]` | Impressum (Berufshaftpflicht) | nur falls Pflicht/gewünscht |
| `[Liste nach Einsetzen der eigenen Fotos ergänzen]` | Impressum → Bildnachweise | |
| `[Hosting-Anbieter …]` | Datenschutz, Abschnitt 3 | sobald das Hosting feststeht (Strato, GitHub Pages o. a.) |
| `[Bitte an die tatsächliche Praxis anpassen]` | Datenschutz, Abschnitt 5 | |

Bewusst **nicht** angegeben (keine Quelle/Bestätigung): Preise, Garantien, Reaktionszeiten, Zertifizierungen, Kundenzahlen,
Bewertungen, Firmenjahre. Nach dem Ersetzen die Klasse `ph` am jeweiligen `<span>` entfernen.

## Logo

Identisch mit der Hornissen-Seite: `img/logo/falkner-logo-horizontal-light.(webp|png)` in Header und Footer,
`img/logo/falkner-logo-horizontal.png` im JSON-LD (`logo`). Favicons aus der Grasmarke.

## Eigene Fotos einsetzen

Fotoplätze sind `<figure class="photo-slot">…</figure>` mit dem Hinweis „Platz für ein eigenes Foto“ und `[FOTO …]`. Ersetzen durch z. B.:

```html
<figure class="photo reveal">
  <img src="img/eigen-klebefalle-800.webp?v=…" srcset="img/eigen-klebefalle-800.webp?v=… 800w, img/eigen-klebefalle.webp?v=… 2000w"
       sizes="(max-width: 900px) 100vw, 33vw" width="2000" height="1500" loading="lazy" decoding="async" alt="Kurze, sachliche Beschreibung">
  <figcaption><strong>Monitoring-Falle</strong> – …
    <span class="photo-credit">Foto: © Falkner Schädlingsbekämpfung GmbH / Michael Falkner</span></figcaption>
</figure>
```

Empfehlung wie bei der Hornissen-Seite: WebP, 2000 px lange Kante + `-800`-Variante, Exif/GPS entfernen, keine Kunden-/Ortsangaben
erkennbar (Diskretion!). **Startbild tauschen:** im Hero-`<img>` `src` (und ggf. `srcset`/`sizes="(min-width: 900px) 60vw, 220vw"`),
`width`/`height` und Alt-Text anpassen, `hero-credit` auf „Foto: © Falkner Schädlingsbekämpfung GmbH / Michael Falkner“ ändern;
`img/og-image.jpg` ggf. neu erzeugen. Danach Bildnachweise im Impressum und `sitemap.xml` (`image:image`) ergänzen.

Nur Fotos verwenden, an denen Sie die Rechte haben (am besten eigene). Keine Stockfotos mit unklarer Lizenz.

## Cache-Busting

Alle lokalen Assets werden mit `?v=20261102a` eingebunden. Nach jeder Änderung an CSS/JS/Bildern den Wert in `index.html`
erhöhen (z. B. `20261102b`).

## Eigene Domain

Die Seite ist für `https://www.kakerlake.net/` vorbereitet: `CNAME`, `canonical`, `og:url`, `og:image`, `twitter:image`,
`url`/`logo`/`image`/`@id` im JSON-LD, `robots.txt`, `sitemap.xml` und `llms.txt` zeigen auf diese Domain.

**Die Domain ist bei Strato registriert.** Sobald feststeht, wo die Seite gehostet wird, muss das DNS bei Strato darauf zeigen,
z. B. für GitHub Pages:

- `www` → CNAME auf `<benutzer>.github.io`
- Apex `kakerlake.net` → A-Records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 (bzw. Weiterleitung auf `www`)

Bei Hosting direkt bei Strato entfällt die `CNAME`-Datei (sie schadet aber nicht). HTTPS muss in jedem Fall aktiv sein
(Datenschutz Abschnitt 7). Danach Datenschutz Abschnitt 3 (Hosting) ausfüllen.

## SEO

- `robots.txt` (alles erlaubt, Verweis auf die Sitemap) und `sitemap.xml` (eine URL, `lastmod` bei größeren Änderungen anpassen).
- `<title>`, Meta-Description, H1 (inkl. Ortszeile „Schabenbekämpfung · Bonn · Köln · Rhein-Sieg · Mannheim · Rhein-Neckar“) und H2
  auf Schabenbekämpfung Bonn / Köln / Rhein-Sieg / Mannheim / Rhein-Neckar und „Kakerlaken bekämpfen“ ausgerichtet.
- JSON-LD als `@graph`: `PestControl` (Hauptsitz Bonn) mit drei `department`-Standorten (Königswinter, Mannheim, Reilingen),
  `WebSite` und `FAQPage`. **Die FAQPage-Texte müssen mit dem sichtbaren FAQ-Abschnitt (`#faq`) übereinstimmen** – bei Änderungen
  beide Stellen anpassen.
- `llms.txt`: Kurzfassung für KI-Assistenten.
- Kein `google-site-verification` (das Token der Hornissen-Seite gilt nur für vespa-velutina.com) – für die Search Console neu anlegen.

## Formular

Kein Server: Das Formular baut eine E-Mail (mailto:) im E-Mail-Programm des Besuchers zusammen (Felder: Anliegen, Name,
Telefon, Ort/Adresse, Art des Objekts, Wo gesehen, Beschreibung). Es werden keine Daten an die Website übertragen.

## Bildnachweis

Alle Illustrationen (vier Schabenarten, Startbild, Social-Media-Vorschau) und Icons sind eigens erstellte SVGs
(`tools/make_svgs.py`, Icons inline in `index.html`) – **Illustrationen, keine Fotos**; Merkmale vereinfacht dargestellt.
Sachkundenachweis: eigenes Dokument (wie Hornissen-Seite). Keine Fremd- oder Stockfotos. Schrift: Cormorant Garamond,
SIL Open Font License, lokal gehostet. Keine externen Ressourcen, keine Cookies.

## Quellen der Fachinhalte (abgerufen 02.11.2026)

- Umweltbundesamt – Schaben (Größen, Lebensweise, ca. 40 krankheitserregende Bakterienarten, Glukose-Aversion, Waldschaben, Reisegepäck): https://www.umweltbundesamt.de/schaben
- Umweltbundesamt / PAN Germany – Infoblatt „Schaben (Kakerlaken)“ (0,5-mm-Spalten, Geruch, Tagsichtungen, Ootheken, keine Laien-Insektizide, Hausverwaltung, nicht zertreten, Vorbeugung): https://www.umweltbundesamt.de/sites/default/files/medien/publikation/long/infoblatt_schaben_kakerlaken.pdf
- LAVES Niedersachsen – Infoblatt Schaben (Gesundheitsschädlinge, Keime bis 72 h, Entwicklung, IPM, Nachbehandlung 6–8 Wochen, Fachfirma): https://www.laves.niedersachsen.de/download/41516/Infoblatt_Schaben.pdf
- Institut für Schädlingskunde – Artsteckbriefe (Lebensräume, Ootheken geschützt): https://www.schaedlingskunde.de
- Infektionsschutzgesetz § 17 (und § 2 Nr. 12 Gesundheitsschädling): https://www.gesetze-im-internet.de/ifsg/__17.html
- VO (EG) Nr. 852/2004, Art. 5 (HACCP) und Anhang II Kap. IX Nr. 4 (Schädlingsbekämpfung): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02004R0852-20210324
- AVV Lebensmittelhygiene, Anlage 1: https://www.verwaltungsvorschriften-im-internet.de/BMELV-329-20091109-KF-005-A001.htm

Rechtliche Hinweise regelmäßig prüfen – sie können sich ändern (Stand im Text: November 2026). Die IFS-Erwähnung ist bewusst
allgemein gehalten („viele Standards erwarten ein dokumentiertes Monitoring“); keine Zertifizierung der Firma behauptet.

## Anrufen-Auswahl

Der Header-Link „Anrufen“, der Hero-Button und der Link in der Gewerbe-Box öffnen per JS eine Standortauswahl (`#call-chooser`)
mit allen vier Rufnummern (Desktop: Popover, Mobil ≤ 640 px: Bottom-Sheet; schließt bei Escape, Klick außerhalb oder ✕).
Ohne JavaScript führen sie zu `#standorte`. Telefonische Erreichbarkeit: 08:30 – 18:00 Uhr.
