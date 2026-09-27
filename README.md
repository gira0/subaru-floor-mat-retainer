# Subaru Fußmatten-Halterung – OpenSCAD-Nachbau

Nachbau der Fußmatten-Halterung J501EAJ000 (EU) / J501SAJ300 (US) zum Selberdrucken.

| Datei | Wozu |
|---|---|
| `bracket.scad` | Das 3D-Modell. Alle Maße stehen ganz oben in der Datei. |
| `bracket.stl` | Fertige Druckdatei für den Slicer, schon richtig hingelegt |
| `masse.drawio` | **Maßzeichnung zum Ausfüllen.** Öffnen mit [app.diagrams.net](https://app.diagrams.net) oder der draw.io-App |
| `masse.svg` | Dieselbe Zeichnung als Bild, zum schnellen Anschauen |
| `preview/` | Ansichten des Modells zum Vergleich mit den Fotos |
| `tools/make_drawing.py` | Erzeugt die Zeichnung neu |

## Wie das Teil aufgebaut ist

Das Original ist ein **Kunststoff-Spritzgussteil aus einem Stück**. Es ist kein Blech.
Im Grunde ist es ein flaches Plastikband mit einer Stufe in der Mitte:

```
      Pin                                Clip
       ▄                                  ▼
       █                     ┌────────────┬─────┐
  ─────┴──────────┐         /              Haken│
  gerades Stück   └────────┘ ← Stufe            ▼
```

- **Pin**: der Pilzknopf. Auf ihn wird die Öse der Fußmatte gesteckt.
- **Stufe**: Hier knickt das Band schräg nach oben und läuft dann wieder gerade weiter.
- **Clip**: ein Stecker auf der Unterseite. Von unten gesehen ist er ein Plus, mit dünnen Lamellen-Platten an der Spitze. Er wird ins Loch im Fahrzeugboden gedrückt.
- **Haken**: das um 90° nach unten gebogene Ende. Es greift unter eine Kante.

Die beiden Teile auf `img4.jpg` sind identisch, also nicht spiegelverkehrt. Das Modell passt deshalb für links und rechts.

## Maße

Die Buchstaben sind in `masse.drawio`, hier und in `bracket.scad` dieselben.

| | Was | Wert | Status |
|---|---|---|---|
| A | Dicke des Bandes | 2,3 mm | gemessen |
| B | Breite des Bandes | 20 mm (19,93) | gemessen |
| C | Gesamtlänge, Teil flach hingelegt: Pin-Ende bis ganz außen am Haken (über die Rippe) | 147,9 mm | gemessen |
| D | Gerades Stück am Pin-Ende, bis die Stufe anfängt | 51 mm | angepasst nach Probedruck (gemessen: 56) |
| E | Wie viel höher der hintere Teil liegt | 30 mm | gemessen |
| F | Länge der Stufe, waagerecht | 50 mm | angepasst nach Probedruck (gemessen: 45) |
| G | Winkel der Stufe | 35,6° | angepasst: flacher, gleicher Biegeradius (gemessen: 40°) |
| H | Hakentiefe: Oberseite Band bis Hakenspitze | 14,9 mm | gemessen |
| I | Hakenwinkel | 90° | gemessen |
| J | Abstand Pin-Mitte bis Bandende | 10 mm | gemessen |
| K / L | Dicke Pin-Stiel / Pin-Kopf | 5 / 9 mm | gemessen |
| M / N | Oberseite Band bis Unterkante Kopf / Kopfhöhe | 15 / 4 mm | gemessen |
| O | Abstand Clip-Mitte bis Außenseite Haken | 20 mm | gemessen |
| P | Wie weit der Clip unten heraussteht | 17,5 mm | gemessen |
| Q | Clip: Lamellen-Größe (abgerundetes Quadrat) | 6,7 mm | gemessen |
| R / S | Clip: Breite eines Plus-Stegs / Größe des Plus | 2,2 / 7 mm | gemessen |
| T | Anzahl der Lamellen | 4 | gemessen |
| U | Rippe: Breite | 3 mm | gemessen |
| V | Rippe: Überstand an der Schräge | 4 mm | gemessen |
| W | Rippe: Überstand am oberen Teil (Clip-Seite) | 2 mm | gemessen |
| Z | Rippe auf dem geraden Stück am Pin: Gesamthöhe, mittig im Band | 5,5 mm | gemessen |
| a | Querstreben: Pin-Mitte bis Mitte der 2. Strebe | 24,6 mm | angepasst nach Probedruck (gemessen: 21,6) |
| b | Querstrebe: Dicke (längs gemessen) | 3 mm | gemessen |
| c | Querstrebe: Überstand auf der Rückseite | 2 mm | gemessen |
| d | Querstrebe: Länge quer zum Band | 20 mm (volle Breite) | gemessen |
| e | Clip: Abstand der Lamellen (Mitte zu Mitte) | 1,8 mm | gemessen |
| f | Clip: massiver Block direkt am Band | 1 mm | gemessen |
| g | Clip: Dicke einer Lamelle | 0,6 mm | gemessen |
| h | Clip: Eckenradius der Lamellen | 1,5 mm | *Schätzung* |
| i | Clip: Länge der stumpfen Spitze | 3 mm | gemessen |
| j | Clip: Breite des Plus ganz vorne an der Spitze | 1,5 mm | *Schätzung* |
| k | Kuppel (Pin-Seite, gegenüber vom Clip): Durchmesser | 15 mm | gemessen |
| l | Kuppel: Höhe in der Mitte | 2 mm | gemessen |
| m | Anschlagblock an der Hakenspitze: Länge | 3 mm | gemessen |

*Schätzung* bedeutet: noch nicht gemessen, sondern aus den Fotos abgeleitet.

**Den Biegeradius der Stufe muss man nicht messen.** Er ergibt sich aus E, F und G und liegt bei etwa 11,5 mm innen.

**Rundes Ende:** Das Pin-Ende ist ein Halbkreis mit dem Radius der halben Bandbreite, der Pin sitzt in seinem Mittelpunkt.
Deshalb ist J = B/2.

**Rippe:** Der Versteifungssteg (U, 3 mm breit) läuft mittig längs über das Band.
Auf dem geraden Stück am Pin sitzt er mittig im Band: 5,5 mm hoch (Z), steht also oben und unten je 1,6 mm über und geht in den Pin über.
Auf der Rückseite läuft er am Pin vorbei bis ganz ans runde Ende.
Die Rippe ist dabei ein durchgehender Steg mit gleichbleibender Höhe: In der Biegung am Fuß der Schräge wandert er nach oben und geht einfach durch das Band hindurch.
Unten taucht er dabei ins Band ein, oben wächst er auf die 4 mm der Schräge.
In der Biegung am Fuß der Schräge wandert die Rippe ganz auf die Pin-Seite: An der Schräge steht sie 4 mm über (V), auf dem oberen Teil 2 mm (W).
Ihre Oberkante geht dort in einem runden Bogen vom geraden Stück in die Schräge über (`rib_fillet1`, Radius 8,5 mm, geschätzt).
Dann läuft sie außen um den Haken bis zur Hakenspitze.
Dort endet sie in einem Anschlagblock (m, 3 mm lang). Er geht über die volle Bandbreite und ist außen bündig mit der Rippe.
In der Biegung zum oberen Teil geht die Oberkante der Rippe in einem runden Bogen von 4 auf 2 mm über (`rib_fillet`, Radius 15 mm, geschätzt).
Mit `rib_side = -1` wandert die Rippe auf die Clip-Seite.

**Clip:** Direkt am Band sitzt ein 1 mm dicker Block (f), danach folgen 4 dünne Lamellen (0,6 mm) im Abstand von 1,8 mm (e).
Dann kommt ein Plus aus zwei gekreuzten Stegen (R × S), dessen letzte 3 mm als stumpfe Spitze zusammenlaufen (i).
Die Clip-Länge P = 17,5 mm zählt ab der Bandunterseite.

**Kuppel:** Gegenüber vom Clip, auf der Pin-Seite des Bandes, sitzt eine flache runde Kuppel (15 mm Ø, in der Mitte 2 mm hoch).
Sie läuft zum Rand hin flach aus und geht in die Rippe über.

**Querstreben:** Auf der Rückseite des Pin-Endes sitzen zwei quer liegende Stege, einer direkt unter dem Pin und einer 24,6 mm weiter (a).
Ein- und ausschalten lassen sie sich mit `struts`.

### So trägst du neue Werte ein

1. `bracket.scad` in OpenSCAD öffnen.
2. Oben die Zeile mit dem passenden Buchstaben suchen, z. B. `hook_depth = 14.9; // H …`, und die Zahl ändern.
   Alternativ geht das über **Fenster → Customizer**, dort gibt es für jedes Maß ein Eingabefeld.
3. Mit F6 rendern, dann **Datei → Exportieren → STL**.

Über die Kommandozeile geht es auch:

```sh
openscad -o bracket.stl bracket.scad
openscad -D hook_depth=24 -o bracket.stl bracket.scad   # einzelnen Wert überschreiben
```

## Material und Druck

**Zu TPU:** Das Original ist ziemlich steif. Die Federwirkung kommt aus der Form, nicht aus weichem Material.
TPU 95A mit 2,3 mm Dicke wird merklich weicher: Der Haken hält weniger fest, und der Pin gibt nach.
Dagegen helfen zwei Einstellungen in `bracket.scad`:

- `t` (A) um 0,5–1 mm erhöhen. Das macht das Band dicker und deutlich steifer.
- Die Rippe verstärken: `rib_w` (U) auf 4–5 mm oder `rib_below` (V) auf 5–6 mm setzen.

Ist es dann immer noch zu weich, wäre PETG die steifere Alternative mit etwas Restflexibilität.
Die Lamellen am Clip sind sehr dünn. In TPU geben sie leicht nach, der Clip rastet zwar ein, lässt sich aber leichter herausziehen. Notfalls `clip_style = "hole"` einstellen und das Teil festschrauben.

### Druckausrichtung: auf der Seite (so ist das STL schon gespeichert)

Das Teil liegt mit der Seitenkante auf dem Druckbett, die Bandbreite (20 mm) ist dann die Druckhöhe.
Dadurch laufen die Druckbahnen durch alle Biegungen hindurch. Beim Biegen werden also nicht die Schichtgrenzen belastet, und das Band braucht keinen Support.
Nur Pin und Clip stehen dann waagerecht ab und brauchen etwas Support.

### OrcaSlicer-Hinweise (TPU 95A, Anycubic Kobra S1)

- Düse 0,4 mm, Schichthöhe 0,2 mm
- **Wände: 4–5.** Beim dünnen Band ist das praktisch massiv. Infill 100 %, Muster Konzentrisch
- Geschwindigkeit 20–30 mm/s, max. Volumenfluss ca. 3–4 mm³/s
- Retraction kurz (0,5–1 mm) und langsam
- Düse 220–230 °C, Bett 40–50 °C, Lüfter 30–50 %
- Filament vorher trocknen (TPU zieht Feuchtigkeit)
- Support: Tree, „nur auf Druckplatte“, Abstand oben 0,2–0,25 mm
- Brim 3–5 mm, weil die Auflagefläche schmal ist
- Clip-Lamellen (0,6 mm): Damit sie überhaupt gedruckt werden, in OrcaSlicer unter Qualität → „Detect thin wall“
  (Dünne Wände erkennen) einschalten. Sonst werden sie weggelassen. Wenn es nicht klappt, `clip_fin_t` auf 0,8 setzen.

## Annahmen im Modell

- Das Band ist überall gleich dick und gleich breit.
- Die Rippe steigt gleichmäßig an und läuft am Ende keilförmig aus.
- Beide Biegungen der Stufe haben denselben Radius.
- Der Pin-Kopf ist eine Scheibe, deren Rand oben und unten voll abgerundet ist (Radius = halbe Kopfhöhe).
- Die kleinen Noppen an den Kanten des Originals sind nicht nachgebaut. Das halte ich für Spuren aus dem Spritzguss.

## Technischer Hinweis: sauberes Netz

Band und Rippe werden als je ein geschlossenes Netz entlang des Pfads erzeugt (`sweep_mesh`), nicht aus vielen `hull()`-Stücken.
Die gestückelte Variante erzeugte in OpenSCAD 2021 an den Biegungen über 3000 non-manifold edges, die OrcaSlicer bemängelt.
Das aktuelle STL hat 0 non-manifold edges. Das gilt für alle Varianten von `clip_style` und `clip_at_tip`.
