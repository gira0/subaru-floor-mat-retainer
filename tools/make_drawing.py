#!/usr/bin/env python3
"""Erzeugt die Maßzeichnung masse.drawio (und masse.svg zur Kontrolle).

Buchstaben und Werte entsprechen den Parametern in bracket.scad.
Werte, die noch fehlen, stehen als "____" in der Zeichnung und können in
draw.io per Doppelklick überschrieben werden.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Buchstabe: (Wert oder None, Einheit, Kurzname, Wie messen)
DIMS = {
    "A": ("2,3", "mm", "Dicke Band", "Dicke des flachen Plastikbandes, an einer glatten Stelle"),
    "B": ("20", "mm", "Breite Band", "Breite des Bandes, quer gemessen"),
    "C": ("147,9", "mm", "Gesamtlänge", "Teil flach hinlegen: Ende am Pin bis ganz außen am Haken"),
    "D": ("51", "mm", "gerades Stück", "Pin-Ende bis dort, wo die schräge Stufe anfängt"),
    "E": ("30", "mm", "Höhe Stufe", "Wie viel höher der hintere Teil liegt (Unterseite zu Unterseite)"),
    "F": ("50", "mm", "Länge Stufe", "Waagerecht von Biegung zu Biegung"),
    "G": ("35,6", "°", "Winkel Stufe", "Wie steil die Stufe ansteigt"),
    "H": ("14,9", "mm", "Hakentiefe", "Oberseite Band bis Hakenspitze"),
    "I": ("90", "°", "Hakenwinkel", "90° = rechtwinklig; zeigt die Spitze etwas nach innen, ist es mehr"),
    "J": ("10", "mm", "Pin-Abstand", "Mitte Pin bis Bandende (Ende ist rund, Pin = Mittelpunkt)"),
    "K": ("5", "mm", "Pin Stiel", "Dicke des Stiels"),
    "L": ("9", "mm", "Pin Kopf", "Dicke des Kopfes"),
    "M": ("15", "mm", "Pin Hals", "Oberseite Band bis Unterkante Kopf"),
    "N": ("4", "mm", "Kopfhöhe", "Nur der Kopf (oben und unten voll abgerundet)"),
    "O": ("20", "mm", "Clip-Abstand", "Mitte Clip bis Außenseite Haken"),
    "P": ("17,5", "mm", "Clip-Länge", "Wie weit der Clip unten heraussteht"),
    "Q": ("6,7", "mm", "Lamellen-Größe", "Lamelle (abgerundetes Quadrat), Kante zu Kante"),
    "R": ("2,2", "mm", "Plus-Steg breit", "Breite eines Stegs vom Plus"),
    "S": ("7", "mm", "Plus-Größe", "Länge eines Stegs vom Plus, außen gemessen"),
    "T": ("4", "Stk", "Lamellen", "Anzahl der Lamellen am Clip"),
    "U": ("3", "mm", "Rippe Breite", "Wie dick der Versteifungssteg in der Mitte ist"),
    "V": ("4", "mm", "Rippe Schräge", "Wie weit die Rippe an der Schräge übersteht"),
    "W": ("2", "mm", "Rippe oben", "Wie weit sie am oberen Teil (Clip-Seite) übersteht"),
    "Z": ("5,5", "mm", "Rippe am Pin", "Gesamthöhe der Rippe auf dem geraden Stück am Pin (sitzt mittig im Band)"),
    "a": ("24,6", "mm", "Streben-Abstand", "Pin-Mitte bis Mitte der 2. Querstrebe"),
    "b": ("3", "mm", "Strebe dick", "Dicke einer Querstrebe, in Längsrichtung gemessen"),
    "c": ("2", "mm", "Strebe hoch", "Wie weit eine Querstrebe auf der Rückseite übersteht"),
    "d": ("20", "mm", "Strebe lang", "Länge einer Querstrebe, quer zum Band (= volle Breite)"),
    "e": ("1,8", "mm", "Lamellen-Abstand", "Abstand der Lamellen zueinander (Mitte zu Mitte)"),
    "f": ("1", "mm", "Clip-Block", "Massiver Block direkt am Band, Dicke"),
    "g": ("0,6", "mm", "Lamelle dick", "Dicke einer Lamelle"),
    "h": (None, "mm", "Lamelle Ecke", "Eckenradius der Lamellen (wie rund sind die Ecken?)"),
    "i": ("3", "mm", "Clip-Spitze", "Länge der stumpfen Spitze am Clip-Ende"),
    "j": (None, "mm", "Spitze vorne", "Wie breit das Plus ganz vorne an der Spitze noch ist"),
    "k": ("15", "mm", "Kuppel Ø", "Runde Erhebung auf der Pin-Seite, gegenüber vom Clip: Durchmesser"),
    "l": ("2", "mm", "Kuppel hoch", "Höhe der Kuppel in der Mitte (so hoch wie die Rippe W)"),
    "m": ("3", "mm", "Haken-Anschlag", "Block an der Hakenspitze: Länge (volle Breite, außen bündig mit der Rippe)"),
}

INK, DIM, OK, TODO, PART = "#333333", "#1f5fbf", "#1a7f37", "#c62828", "#9aa7b4"

cells = []   # drawio XML-Zellen
svg = []     # SVG-Elemente
_id = [1]


def nid():
    _id[0] += 1
    return f"c{_id[0]}"


def line(pts, width=1.0, color=INK, dash=False, arrows=False, rounded=False):
    style = (f"html=1;endArrow={'block' if arrows else 'none'};"
             f"startArrow={'block' if arrows else 'none'};startFill=1;endFill=1;"
             f"startSize=5;endSize=5;strokeWidth={width};strokeColor={color};"
             f"rounded={1 if rounded else 0};arcSize=40;"
             + ("dashed=1;dashPattern=4 3;" if dash else ""))
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    way = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    cells.append(
        f'<mxCell id="{nid()}" style="{style}" edge="1" parent="1">'
        f'<mxGeometry relative="1" as="geometry">'
        f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/><mxPoint x="{x2}" y="{y2}" as="targetPoint"/>'
        + (f'<Array as="points">{way}</Array>' if way else "")
        + '</mxGeometry></mxCell>')
    d = " ".join(f"{x},{y}" for x, y in pts)
    extra = ' stroke-dasharray="4 3"' if dash else ""
    extra += ' marker-start="url(#a)" marker-end="url(#a)"' if arrows else ""
    svg.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
               f'stroke-linejoin="round" stroke-linecap="butt"{extra}/>')


def shape(kind, x, y, w, h, fill=PART, stroke=INK, extra="", size=0.39, up=False):
    """up=True: Trapez schmal oben (Kuppel), sonst breit oben (Spitze)."""
    base = {"rect": "rounded=0;", "round": "rounded=1;arcSize=30;", "pill": "rounded=1;arcSize=50;", "ellipse": "ellipse;",
            "tri": "triangle;direction=south;",
            "trap": f"shape=trapezoid;perimeter=trapezoidPerimeter;flipV={0 if up else 1};size={size};fixedSize=0;"}[kind]
    cells.append(
        f'<mxCell id="{nid()}" value="" style="{base}html=1;fillColor={fill};strokeColor={stroke};{extra}" '
        f'vertex="1" parent="1"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    dash = ' stroke-dasharray="4 3"' if "dashed=1" in extra else ""
    if kind == "ellipse":
        svg.append(f'<ellipse cx="{x + w/2}" cy="{y + h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="{stroke}"{dash}/>')
    elif kind == "trap":
        d = w * size
        pts = (f"{x + d},{y} {x + w - d},{y} {x + w},{y + h} {x},{y + h}" if up
               else f"{x},{y} {x + w},{y} {x + w - d},{y + h} {x + d},{y + h}")
        svg.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}"/>')
    elif kind == "tri":
        svg.append(f'<polygon points="{x},{y} {x + w},{y} {x + w/2},{y + h}" fill="{fill}" stroke="{stroke}"/>')
    else:
        r = {"round": min(w, h) * 0.15, "pill": min(w, h) / 2}.get(kind, 0)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"{dash}/>')


def text(x, y, w, h, html, size=12, color=INK, align="center", bold=False, plain=None):
    style = (f"text;html=1;whiteSpace=wrap;align={align};verticalAlign=middle;fontSize={size};"
             f"fontColor={color};{'fontStyle=1;' if bold else ''}")
    cells.append(
        f'<mxCell id="{nid()}" value="{escape(html)}" style="{style}" vertex="1" parent="1">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    anchor = {"left": ("start", x), "center": ("middle", x + w/2), "right": ("end", x + w)}[align]
    svg.append(f'<text x="{anchor[1]}" y="{y + h/2 + size*0.35}" font-size="{size}" fill="{color}" '
               f'text-anchor="{anchor[0]}" font-family="sans-serif"{" font-weight=\"bold\"" if bold else ""}>'
               f'{escape(plain if plain is not None else html)}</text>')


def label(letter, x, y, w=90, align="center"):
    val, unit, _, _ = DIMS[letter]
    color = OK if val else TODO
    shown = val if val else "____"
    text(x, y, w, 18, f"<b>{letter}</b> = {shown} {unit}", size=12, color=color, align=align,
         plain=f"{letter} = {shown} {unit}")


def hdim(x1, x2, y, letter, ly=None, lw=90):
    line([(x1, y), (x2, y)], color=DIM, arrows=True)
    label(letter, (x1 + x2) / 2 - lw / 2, (ly if ly is not None else y - 20), w=lw)


def vdim(x, y1, y2, letter, side="right", lw=90):
    line([(x, y1), (x, y2)], color=DIM, arrows=True)
    lx = x + 6 if side == "right" else x - 6 - lw
    label(letter, lx, (y1 + y2) / 2 - 9, w=lw, align="left" if side == "right" else "right")


def ext(pts):
    line(pts, width=0.8, color=DIM, dash=True)


# ---------------------------------------------------------------------------
# 1) Seitenansicht (Maßstab 4 px/mm)
s = 4
X0, Y0 = 80, 360                 # Pin-Ende, Unterseite unterer Schenkel
xD = X0 + 51 * s                 # Beginn Stufe
xF = xD + 50 * s                 # Ende Stufe
yU = Y0 - 30 * s                 # Unterseite oberer Schenkel
xC = X0 + 147.9 * s              # Außenseite Haken
yH = yU + 22 * s                 # Hakenspitze
xPin, xClip = X0 + 10 * s, xC - 20 * s

text(40, 20, 700, 26, "Seitenansicht – Teil liegt auf der Seite, Pin zeigt nach oben", size=16, bold=True, align="left")
text(40, 46, 700, 20, "grün = schon gemessen · rot ____ = bitte messen und eintragen (Doppelklick auf den Text)",
     size=11, color="#555555", align="left")

# Rippe (dunkler): auf dem geraden Stück mittig im Band (oben und unten sichtbar),
# ab der Biegung auf der Pin-Seite, oben niedriger, außen um den Haken bis zur Spitze
line([(xPin, Y0 - 5), (xD - 6 * s, Y0 - 5)], width=22, color="#5b6673")
line([(X0 + 2, Y0 + 1), (xPin, Y0 + 1)], width=10, color="#5b6673")   # Rückseite bis ans runde Ende
line([(xD - 6 * s, Y0 - 11), (xD - 4, Y0 - 13), (xD + 10, Y0 - 21), (xF - 8, yU - 21), (xF + 20, yU - 13),
      (xC + 3, yU - 13), (xC + 3, yH)], width=5, color="#5b6673", rounded=True)
text(xD - 30, Y0 - 44, 60, 16, "Rippe", size=11, color="#555555", align="left")
# Band als dicke Linie (über der Rippe, damit sie oben und unten heraussteht)
line([(X0, Y0 - 5), (xD, Y0 - 5), (xF, yU - 5), (xC - 5, yU - 5), (xC - 5, yH)], width=10, color=PART, rounded=True)
# Anschlagblock an der Hakenspitze
shape("rect", xC - 10, yH - 12, 16, 12, fill="#5b6673")
label("m", xC - 104, yH + 12, w=90, align="right")
line([(xC - 12, yH - 12), (xC - 12, yH)], color=DIM, arrows=True)
# Querstreben auf der Rückseite
for xs in (xPin, xPin + 24.6 * s):
    shape("rect", xs - 4, Y0, 8, 6, fill="#5b6673")
# Pin
shape("rect", xPin - 10, Y0 - 10 - 60, 20, 60)
shape("pill", xPin - 18, Y0 - 10 - 76, 36, 16)
# Clip (Plus mit Lamellen)
shape("trap", xClip - 30, yU - 18, 60, 8, size=0.3, up=True)
shape("rect", xClip - 14, yU, 28, 58)
shape("rect", xClip - 13, yU, 26, 4)
for k in range(4):
    shape("rect", xClip - 13, yU + 8 + k * 7, 26, 3)
shape("trap", xClip - 14, yU + 58, 28, 12)
text(xPin + 20, Y0 - 10 - 80, 40, 16, "Pin", size=11, color="#555555")
text(xClip - 76, yU + 50, 60, 16, "Clip", size=11, color="#555555")
text(xC + 8, yH + 6, 60, 16, "Haken", size=11, color="#555555", align="left")
text(xD + 100, Y0 - 40, 100, 16, "Stufe", size=11, color="#555555")

# C, D unten
ext([(X0, Y0 + 4), (X0, Y0 + 70)])
ext([(xC, yH + 4), (xC, Y0 + 70)])
ext([(xD, Y0 + 4), (xD, Y0 + 56)])
hdim(X0, xD, Y0 + 32, "D", ly=Y0 + 36)
hdim(X0, xC, Y0 + 62, "C", ly=Y0 + 66)
# F, O oben
ext([(xD, Y0 - 12), (xD, yU - 70)])
ext([(xF, yU - 12), (xF, yU - 70)])
hdim(xD, xF, yU - 62, "F")
ext([(xClip, yU - 12), (xClip, yU - 40)])
ext([(xC, yU - 12), (xC, yU - 40)])
line([(xClip, yU - 32), (xC, yU - 32)], color=DIM, arrows=True)
label("O", xClip - 86, yU - 41, w=80, align="right")
# E zwischen den Unterseiten
xE = xF + 22
ext([(xD + 10, Y0), (xE + 6, Y0)])
ext([(xF + 6, yU), (xE + 6, yU)])
vdim(xE, yU, Y0, "E", side="left", lw=70)
# G Winkel
ext([(xD + 18, Y0 - 5), (xD + 80, Y0 - 5)])
label("G", xD + 60, Y0 - 34, w=70, align="left")
# H, I am Haken
ext([(xC + 4, yU - 10), (xC + 50, yU - 10)])
ext([(xC + 4, yH), (xC + 50, yH)])
vdim(xC + 42, yU - 10, yH, "H", side="right", lw=80)
label("I", xC - 90, yH - 9, w=80, align="right")
# J am Pin
ext([(X0, Y0 - 14), (X0, Y0 - 120)])
ext([(xPin, Y0 - 86), (xPin, Y0 - 120)])
line([(X0, Y0 - 112), (xPin, Y0 - 112)], color=DIM, arrows=True)
label("J", xPin + 6, Y0 - 121, w=80, align="left")

# ---------------------------------------------------------------------------
# 2) Draufsicht und Querschnitt
yT = 500
text(40, yT - 40, 700, 24, "Draufsicht (von oben auf den Pin geschaut)", size=16, bold=True, align="left")
shape("ellipse", X0, yT, 20 * s, 20 * s)
shape("rect", xPin, yT, xC - xPin, 20 * s, stroke="none")
line([(xPin, yT), (xC, yT), (xC, yT + 20 * s), (xPin, yT + 20 * s)])
shape("ellipse", xPin - 14, yT + 40 - 14, 28, 28, fill="#c9d1d9")
text(X0 - 30, yT + 84, 260, 16, "Ende halbrund, Pin sitzt im Mittelpunkt", size=11, color="#555555", align="left")
shape("round", xClip - 14, yT + 40 - 14, 28, 28, fill="none", extra="dashed=1;")
text(xClip - 170, yT + 30, 150, 20, "Clip (unten, verdeckt)", size=11, color="#333333", align="right")
vdim(xC + 16, yT, yT + 20 * s, "B", side="right", lw=70)

xq, yq, sq = 850, yT + 10, 10
text(xq - 20, yT - 40, 300, 24, "Querschnitt Band", size=16, bold=True, align="left")
shape("rect", xq, yq, 20 * sq, 2.3 * sq)
vdim(xq - 14, yq, yq + 23, "A", side="left", lw=80)
hdim(xq, xq + 200, yq + 50, "B", ly=yq + 54, lw=70)

# ---------------------------------------------------------------------------
# 3) Details Pin und Clip (Maßstab 8 px/mm)
yD = 690
text(40, yD - 40, 400, 24, "Detail Pin (vergrößert)", size=16, bold=True, align="left")
bx, by = 170, yD + 200              # Mitte Pin, Oberseite Band
shape("rect", bx - 110, by, 220, 18)
shape("rect", bx - 20, by - 124, 40, 124)
shape("pill", bx - 36, by - 152, 72, 32)
line([(bx - 20, by - 56), (bx + 20, by - 56)], color=DIM, arrows=True)
label("K", bx + 26, by - 65, w=70, align="left")
ext([(bx - 36, by - 156), (bx - 36, by - 172)])
ext([(bx + 36, by - 156), (bx + 36, by - 172)])
hdim(bx - 36, bx + 36, by - 166, "L", ly=by - 188, lw=70)
ext([(bx - 24, by - 120), (bx - 76, by - 120)])
vdim(bx - 68, by - 120, by, "M", side="left", lw=70)
ext([(bx + 40, by - 120), (bx + 76, by - 120)])
ext([(bx + 40, by - 152), (bx + 76, by - 152)])
vdim(bx + 68, by - 152, by - 120, "N", side="right", lw=70)

text(340, yD - 40, 400, 24, "Detail Clip", size=16, bold=True, align="left")
cs = 8
cx, cy = 470, yD + 40               # Mitte Clip, Unterseite Band
tip = cy + 17.5 * cs
shape("rect", cx - 90, cy - 18, 180, 18)
neck = tip - 3 * cs
boss = cy                                                        # Clip beginnt direkt am Band
shape("trap", cx - 60, cy - 18 - 2 * cs, 120, 2 * cs, size=0.3, up=True)  # Kuppel auf der Pin-Seite
shape("rect", cx - 28, boss, 56, neck - boss)                     # Plus-Steg, breite Seite
shape("rect", cx - 8.8, boss, 17.6, neck - boss, fill="#c9d1d9")  # quer liegender Steg
shape("trap", cx - 28, neck, 56, tip - neck)                      # stumpfe Spitze
shape("rect", cx - 27, boss, 54, 1 * cs, fill="#5b6673")          # Block
fins = [boss + 1 * cs + 1.5 * cs + k * 1.8 * cs for k in range(4)]   # Mitte der Lamellen
for fy in fins:
    shape("rect", cx - 27, fy - 2.4, 54, 4.8, fill="#5b6673")
ext([(cx - 60, cy - 22), (cx - 60, cy - 48)])
ext([(cx + 60, cy - 22), (cx + 60, cy - 48)])
line([(cx - 60, cy - 44), (cx + 60, cy - 44)], color=DIM, arrows=True)
label("k", cx + 66, cy - 53, w=80, align="left")
ext([(cx + 44, cy - 34), (cx + 98, cy - 34)])
ext([(cx + 90, cy - 18), (cx + 98, cy - 18)])
vdim(cx + 92, cy - 34, cy - 18, "l", side="right", lw=80)
ext([(cx - 32, cy + 0.5), (cx - 76, cy + 0.5)])
ext([(cx - 32, tip), (cx - 76, tip)])
vdim(cx - 68, cy, tip, "P", side="left", lw=70)
ext([(cx - 27, neck - 4), (cx - 27, tip + 30)])
ext([(cx + 27, neck - 4), (cx + 27, tip + 30)])
line([(cx - 27, tip + 24), (cx + 27, tip + 24)], color=DIM, arrows=True)
label("Q", cx + 34, tip + 15, w=70, align="left")
ext([(cx + 30, fins[2]), (cx + 64, fins[2])])
ext([(cx + 30, fins[3]), (cx + 64, fins[3])])
vdim(cx + 58, fins[2], fins[3], "e", side="right", lw=80)
ext([(cx + 30, boss + 1 * cs), (cx + 64, boss + 1 * cs)])
line([(cx + 58, boss), (cx + 58, boss + 1 * cs)], color=DIM, arrows=True)
label("f", cx + 64, boss + 2, w=80, align="left")
ext([(cx + 24, tip), (cx + 64, tip)])
line([(cx + 58, neck), (cx + 58, tip)], color=DIM, arrows=True)
label("i", cx + 64, tip - 5, w=80, align="left")
label("j", cx - 120, tip + 32, w=100)
text(cx - 130, tip + 48, 120, 14, "(Spitze vorne)", size=10, color="#555555")
label("g", cx + 34, fins[1] - 9, w=80, align="left")
label("T", cx + 34, tip + 36, w=90, align="left")
text(cx + 34, tip + 54, 130, 16, "(Anzahl Lamellen)", size=10, color="#555555", align="left")

# Clip von unten: Plus in abgerundetem Quadrat
qx, qy = 760, cy + 70
text(qx - 80, yD - 40, 300, 24, "Clip von unten", size=16, bold=True, align="left")
shape("round", qx - 27, qy - 27, 54, 54, fill="#c9d1d9")
shape("rect", qx - 28, qy - 8.8, 56, 17.6)
shape("rect", qx - 8.8, qy - 28, 17.6, 56)
ext([(qx - 28, qy - 32), (qx - 28, qy - 60)])
ext([(qx + 28, qy - 32), (qx + 28, qy - 60)])
line([(qx - 28, qy - 54), (qx + 28, qy - 54)], color=DIM, arrows=True)
label("S", qx + 34, qy - 63, w=70, align="left")
ext([(qx + 32, qy - 8.8), (qx + 64, qy - 8.8)])
ext([(qx + 32, qy + 8.8), (qx + 64, qy + 8.8)])
vdim(qx + 58, qy - 8.8, qy + 8.8, "R", side="right", lw=80)
label("h", qx - 120, qy + 18, w=90, align="right")
text(qx - 150, qy + 36, 170, 16, "(Ecke der Lamelle)", size=10, color="#555555", align="right")
text(qx - 100, qy + 60, 200, 16, "hell = Lamelle, dunkel = Plus", size=10, color="#555555")

# ---------------------------------------------------------------------------
# 4) Legende
lx, ly0 = 1080, 20
text(lx, ly0, 500, 26, "Was ist was?", size=16, bold=True, align="left")
rows = "".join(
    f'<tr><td style="padding:2px 6px;color:{OK if v else TODO}"><b>{k}</b></td>'
    f'<td style="padding:2px 6px"><b>{name}</b></td><td style="padding:2px 6px">{how}</td></tr>'
    for k, (v, unit, name, how) in DIMS.items())
table = f'<table style="border-collapse:collapse;font-size:11px">{rows}</table>'
cells.append(
    f'<mxCell id="{nid()}" value="{escape(table)}" style="text;html=1;whiteSpace=wrap;align=left;'
    f'verticalAlign=top;fontSize=11;" vertex="1" parent="1">'
    f'<mxGeometry x="{lx}" y="{ly0 + 34}" width="500" height="{len(DIMS) * 22}" as="geometry"/></mxCell>')
table_rows = len(DIMS)
for i, (k, (v, unit, name, how)) in enumerate(DIMS.items()):
    svg.append(f'<text x="{lx}" y="{ly0 + 60 + i * 22}" font-size="11" font-family="sans-serif" '
               f'fill="{OK if v else TODO}"><tspan font-weight="bold">{k}  {escape(name)}</tspan>'
               f'<tspan fill="{INK}" x="{lx + 110}">{escape(how)}</tspan></text>')
ly_end = ly0 + 60 + len(DIMS) * 22
text(lx, ly_end, 500, 18, "Den Biegeradius der Stufe muss man nicht messen, er ergibt sich aus E, F und G.",
     size=11, color="#555555", align="left")
text(lx, ly_end + 20, 500, 18, "Die Werte danach in bracket.scad beim gleichen Buchstaben eintragen.",
     size=11, color="#555555", align="left")

# ---------------------------------------------------------------------------
# 5) Detail Rippe: zwei Querschnitte (Maßstab 10 px/mm)
yr = ly_end + 160
text(lx, yr - 100, 520, 24, "Rippe im Querschnitt (vergrößert)", size=16, bold=True, align="left")
text(lx, yr - 60, 200, 18, "an der Schräge", size=12, bold=True, align="left")
shape("rect", lx, yr, 200, 23)
shape("rect", lx + 85, yr - 40, 30, 40, fill="#5b6673")
line([(lx + 85, yr + 50), (lx + 115, yr + 50)], color=DIM, arrows=True)
ext([(lx + 85, yr + 26), (lx + 85, yr + 56)])
ext([(lx + 115, yr + 26), (lx + 115, yr + 56)])
label("U", lx + 120, yr + 41, w=70, align="left")
ext([(lx + 119, yr - 40), (lx + 150, yr - 40)])
vdim(lx + 142, yr - 40, yr, "V", side="right", lw=70)

rx = lx + 270
text(rx, yr - 60, 240, 18, "am oberen Teil (Clip-Seite)", size=12, bold=True, align="left")
shape("rect", rx, yr, 200, 23)
shape("rect", rx + 85, yr - 20, 30, 20, fill="#5b6673")
ext([(rx + 119, yr - 20), (rx + 150, yr - 20)])
vdim(rx + 142, yr - 20, yr, "W", side="right", lw=70)
text(lx, yr + 80, 520, 18, "oben = Pin-Seite. Auf dem geraden Stück am Pin sitzt die Rippe mittig (unten links).",
     size=10, color="#555555", align="left")

# ---------------------------------------------------------------------------
# 6) Pin-Ende: Rippe und Querstreben auf der Rückseite (unten links)
y2 = 1050
text(40, y2 - 100, 900, 24, "Pin-Ende: Rippe und Querstreben (vergrößert)", size=16, bold=True, align="left")
text(60, y2 - 50, 260, 18, "gerades Stück am Pin, quer", size=12, bold=True, align="left")
shape("rect", 60, y2, 200, 23)
shape("rect", 145, y2 - 16, 30, 55, fill="#5b6673")
ext([(179, y2 - 16), (210, y2 - 16)])
ext([(179, y2 + 39), (210, y2 + 39)])
vdim(202, y2 - 16, y2 + 39, "Z", side="right", lw=80)
text(60, y2 + 50, 260, 16, "Rippe steckt mittig im Band und", size=10, color="#555555", align="left")
text(60, y2 + 66, 260, 16, "steht oben und unten gleich weit über", size=10, color="#555555", align="left")

text(360, y2 - 50, 260, 18, "Querstrebe, quer geschnitten", size=12, bold=True, align="left")
shape("rect", 360, y2, 200, 23)
shape("rect", 370, y2 + 23, 180, 15, fill="#5b6673")
ext([(554, y2 + 38), (584, y2 + 38)])
vdim(576, y2 + 23, y2 + 38, "c", side="right", lw=80)
ext([(370, y2 + 42), (370, y2 + 70)])
ext([(550, y2 + 42), (550, y2 + 70)])
hdim(370, 550, y2 + 64, "d", ly=y2 + 68, lw=80)

text(690, y2 - 50, 300, 18, "Pin-Ende von der Seite", size=12, bold=True, align="left")
ps = 8
px0, pp = 700, 700 + 10 * ps
shape("rect", pp, y2 + 9 - 22, 29 * ps, 44, fill="#5b6673")   # Rippe, mittig, 5,5 mm
shape("rect", px0, y2 + 9, pp - px0, 22, fill="#5b6673")      # Rückseite bis ans runde Ende
shape("rect", px0, y2, 40 * ps, 18)
shape("rect", pp - 20, y2 - 30, 40, 30)
for xs in (pp, pp + 24.6 * ps):
    shape("rect", xs - 8, y2 + 18, 16, 16, fill="#5b6673")   # c = 2 mm
text(pp + 24, y2 - 26, 40, 16, "Pin", size=11, color="#555555", align="left")
xs2 = pp + 24.6 * ps
ext([(xs2 - 8, y2 + 36), (xs2 - 8, y2 + 50)])
ext([(xs2 + 8, y2 + 36), (xs2 + 8, y2 + 50)])
line([(xs2 - 8, y2 + 46), (xs2 + 8, y2 + 46)], color=DIM, arrows=True)
label("b", xs2 + 14, y2 + 37, w=80, align="left")
ext([(pp, y2 + 34), (pp, y2 + 84)])
ext([(xs2, y2 + 54), (xs2, y2 + 84)])
hdim(pp, xs2, y2 + 78, "a", ly=y2 + 82, lw=90)

# ---------------------------------------------------------------------------
W, H = 1620, 1180
model = (f'<mxfile host="app.diagrams.net"><diagram id="masse" name="Maße">'
         f'<mxGraphModel dx="{W}" dy="{H}" grid="1" gridSize="10" guides="1" page="1" pageScale="1" '
         f'pageWidth="{W}" pageHeight="{H}" background="#ffffff" math="0" shadow="0"><root>'
         f'<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(cells) +
         '</root></mxGraphModel></diagram></mxfile>\n')
(ROOT / "masse.drawio").write_text(model, encoding="utf-8")

svg_doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
           f'<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" '
           f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker></defs>'
           f'<rect width="100%" height="100%" fill="#ffffff"/>' + "".join(svg) + "</svg>\n")
(ROOT / "masse.svg").write_text(svg_doc, encoding="utf-8")
print("masse.drawio und masse.svg geschrieben")
