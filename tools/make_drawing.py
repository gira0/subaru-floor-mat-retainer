#!/usr/bin/env python3
"""Generates the dimension drawing dimensions.drawio (and dimensions.svg as an image).

Letters and values match the parameters in bracket.scad.
Values not measured yet are shown as "____" and can be filled in by
double-clicking the text in draw.io.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# letter: (value or None, unit, short name, how to measure)
DIMS = {
    "A": ("2.3", "mm", "Strip thickness", "Thickness of the flat plastic strip, at a smooth spot"),
    "B": ("20", "mm", "Strip width", "Width of the strip, measured across"),
    "C": ("147.9", "mm", "Overall length", "Part lying flat: pin end to the very outside of the hook"),
    "D": ("51", "mm", "Straight section", "Pin end up to where the step starts"),
    "E": ("30", "mm", "Step height", "How much higher the upper section sits (underside to underside)"),
    "F": ("50", "mm", "Step length", "Measured horizontally, bend to bend"),
    "G": ("35.6", "°", "Step angle", "How steep the step rises"),
    "H": ("14.9", "mm", "Hook depth", "Top of strip to hook tip"),
    "I": ("90", "°", "Hook angle", "90° = square; more if the tip points slightly inwards"),
    "J": ("10", "mm", "Pin position", "Pin centre to strip end (end is round, pin = centre)"),
    "K": ("5", "mm", "Pin shaft", "Shaft diameter"),
    "L": ("9", "mm", "Pin head", "Head diameter"),
    "M": ("15", "mm", "Pin neck", "Top of strip to underside of head"),
    "N": ("4", "mm", "Head height", "Head only (fully rounded top and bottom)"),
    "O": ("20", "mm", "Clip position", "Clip centre to outside of hook"),
    "P": ("17.5", "mm", "Clip length", "How far the clip sticks out below"),
    "Q": ("6.7", "mm", "Lamella size", "Lamella (rounded square), edge to edge"),
    "R": ("2.2", "mm", "Plus web width", "Width of one web of the plus"),
    "S": ("7", "mm", "Plus size", "Length of one web of the plus, outside"),
    "T": ("4", "pcs", "Lamellae", "Number of lamellae on the clip"),
    "U": ("3", "mm", "Rib width", "Width of the stiffening rib"),
    "V": ("4", "mm", "Rib on slope", "How far the rib sticks out on the slope"),
    "W": ("2", "mm", "Rib upper", "How far it sticks out on the upper (clip) section"),
    "Z": ("5.5", "mm", "Rib at pin", "Total rib height on the straight pin section (centred in the strip)"),
    "a": ("24.6", "mm", "Strut spacing", "Pin centre to centre of the 2nd cross strut"),
    "b": ("3", "mm", "Strut thickness", "Thickness of a cross strut, measured lengthwise"),
    "c": ("2", "mm", "Strut height", "How far a cross strut sticks out on the back"),
    "d": ("20", "mm", "Strut length", "Length of a cross strut, across the strip (= full width)"),
    "e": ("2.5", "mm", "Lamella spacing", "Spacing of the lamellae (centre to centre)"),
    "f": ("1", "mm", "Clip block", "Solid block right at the strip, thickness"),
    "g": ("0.6", "mm", "Lamella thickness", "Thickness of one lamella"),
    "h": (None, "mm", "Lamella corner", "Corner radius of the lamellae"),
    "i": ("3", "mm", "Clip tip", "Length of the blunt tip at the clip end"),
    "j": (None, "mm", "Tip width", "Width of the plus at the very tip"),
    "k": ("15", "mm", "Dome Ø", "Round dome on the pin side, opposite the clip: diameter"),
    "l": ("2", "mm", "Dome height", "Dome height at the centre (same as rib W)"),
    "m": ("3", "mm", "Hook stop", "Block at the hook tip: length (full width, flush with the rib)"),
}
PITCH = 2.5   # lamella spacing e in mm, used for the clip detail

INK, DIM, OK, TODO, PART = "#333333", "#1f5fbf", "#1a7f37", "#c62828", "#9aa7b4"

cells = []   # drawio XML cells
svg = []     # SVG elements
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
    """up=True: trapezoid narrow at the top (dome), otherwise wide at the top (tip)."""
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
# 1) Side view (scale 4 px/mm)
s = 4
X0, Y0 = 80, 360                 # pin end, underside of lower section
xD = X0 + 51 * s                 # start of step
xF = xD + 50 * s                 # end of step
yU = Y0 - 30 * s                 # underside of upper section
xC = X0 + 147.9 * s              # outside of hook
yH = yU + 22 * s                 # hook tip
xPin, xClip = X0 + 10 * s, xC - 20 * s

text(40, 20, 700, 26, "Side view – part lying on its side, pin pointing up", size=16, bold=True, align="left")
text(40, 46, 700, 20, "green = measured · red ____ = not measured (estimated in the model; double-click to fill in)",
     size=11, color="#555555", align="left")

# Rib (darker): centred in the strip on the straight section (visible on both sides),
# on the pin side from the bend on, lower on the upper section, around the hook to the tip
line([(xPin, Y0 - 5), (xD - 6 * s, Y0 - 5)], width=22, color="#5b6673")
line([(X0 + 2, Y0 + 1), (xPin, Y0 + 1)], width=10, color="#5b6673")   # back side up to the rounded end
line([(xD - 6 * s, Y0 - 11), (xD - 4, Y0 - 13), (xD + 10, Y0 - 21), (xF - 8, yU - 21), (xF + 20, yU - 13),
      (xC + 3, yU - 13), (xC + 3, yH)], width=5, color="#5b6673", rounded=True)
text(xD - 30, Y0 - 44, 60, 16, "Rib", size=11, color="#555555", align="left")
# strip as a thick line (on top of the rib, so the rib sticks out on both sides)
line([(X0, Y0 - 5), (xD, Y0 - 5), (xF, yU - 5), (xC - 5, yU - 5), (xC - 5, yH)], width=10, color=PART, rounded=True)
# stop block at the hook tip
shape("rect", xC - 10, yH - 12, 16, 12, fill="#5b6673")
label("m", xC - 104, yH + 12, w=90, align="right")
line([(xC - 12, yH - 12), (xC - 12, yH)], color=DIM, arrows=True)
# cross struts on the back
for xs in (xPin, xPin + 24.6 * s):
    shape("rect", xs - 4, Y0, 8, 6, fill="#5b6673")
# pin
shape("rect", xPin - 10, Y0 - 10 - 60, 20, 60)
shape("pill", xPin - 18, Y0 - 10 - 76, 36, 16)
# clip (plus with lamellae)
shape("trap", xClip - 30, yU - 18, 60, 8, size=0.3, up=True)
shape("rect", xClip - 14, yU, 28, 58)
shape("rect", xClip - 13, yU, 26, 4)
for k in range(4):
    shape("rect", xClip - 13, yU + 8 + k * 9, 26, 3)
shape("trap", xClip - 14, yU + 58, 28, 12)
text(xPin + 20, Y0 - 10 - 80, 40, 16, "Pin", size=11, color="#555555")
text(xClip - 76, yU + 50, 60, 16, "Clip", size=11, color="#555555")
text(xC + 8, yH + 6, 60, 16, "Hook", size=11, color="#555555", align="left")
text(xD + 100, Y0 - 40, 100, 16, "Step", size=11, color="#555555")

# C, D below
ext([(X0, Y0 + 4), (X0, Y0 + 70)])
ext([(xC, yH + 4), (xC, Y0 + 70)])
ext([(xD, Y0 + 4), (xD, Y0 + 56)])
hdim(X0, xD, Y0 + 32, "D", ly=Y0 + 36)
hdim(X0, xC, Y0 + 62, "C", ly=Y0 + 66)
# F, O above
ext([(xD, Y0 - 12), (xD, yU - 70)])
ext([(xF, yU - 12), (xF, yU - 70)])
hdim(xD, xF, yU - 62, "F")
ext([(xClip, yU - 12), (xClip, yU - 40)])
ext([(xC, yU - 12), (xC, yU - 40)])
line([(xClip, yU - 32), (xC, yU - 32)], color=DIM, arrows=True)
label("O", xClip - 86, yU - 41, w=80, align="right")
# E between the undersides
xE = xF + 22
ext([(xD + 10, Y0), (xE + 6, Y0)])
ext([(xF + 6, yU), (xE + 6, yU)])
vdim(xE, yU, Y0, "E", side="left", lw=70)
# G angle
ext([(xD + 18, Y0 - 5), (xD + 80, Y0 - 5)])
label("G", xD + 60, Y0 - 34, w=70, align="left")
# H, I at the hook
ext([(xC + 4, yU - 10), (xC + 50, yU - 10)])
ext([(xC + 4, yH), (xC + 50, yH)])
vdim(xC + 42, yU - 10, yH, "H", side="right", lw=80)
label("I", xC - 90, yH - 9, w=80, align="right")
# J at the pin
ext([(X0, Y0 - 14), (X0, Y0 - 120)])
ext([(xPin, Y0 - 86), (xPin, Y0 - 120)])
line([(X0, Y0 - 112), (xPin, Y0 - 112)], color=DIM, arrows=True)
label("J", xPin + 6, Y0 - 121, w=80, align="left")

# ---------------------------------------------------------------------------
# 2) Top view and cross-section
yT = 500
text(40, yT - 40, 700, 24, "Top view (looking down onto the pin)", size=16, bold=True, align="left")
shape("ellipse", X0, yT, 20 * s, 20 * s)
shape("rect", xPin, yT, xC - xPin, 20 * s, stroke="none")
line([(xPin, yT), (xC, yT), (xC, yT + 20 * s), (xPin, yT + 20 * s)])
shape("ellipse", xPin - 14, yT + 40 - 14, 28, 28, fill="#c9d1d9")
text(X0 - 30, yT + 84, 260, 16, "Half-round end, pin at its centre", size=11, color="#555555", align="left")
shape("round", xClip - 14, yT + 40 - 14, 28, 28, fill="none", extra="dashed=1;")
text(xClip - 170, yT + 30, 150, 20, "Clip (underneath, hidden)", size=11, color="#333333", align="right")
vdim(xC + 16, yT, yT + 20 * s, "B", side="right", lw=70)

xq, yq, sq = 850, yT + 10, 10
text(xq - 20, yT - 40, 300, 24, "Strip cross-section", size=16, bold=True, align="left")
shape("rect", xq, yq, 20 * sq, 2.3 * sq)
vdim(xq - 14, yq, yq + 23, "A", side="left", lw=80)
hdim(xq, xq + 200, yq + 50, "B", ly=yq + 54, lw=70)

# ---------------------------------------------------------------------------
# 3) Pin and clip details (scale 8 px/mm)
yD = 690
text(40, yD - 40, 400, 24, "Pin detail (enlarged)", size=16, bold=True, align="left")
bx, by = 170, yD + 200              # pin centre, top of strip
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

text(340, yD - 40, 400, 24, "Clip detail", size=16, bold=True, align="left")
cs = 8
cx, cy = 470, yD + 40               # clip centre, underside of strip
tip = cy + 17.5 * cs
shape("rect", cx - 90, cy - 18, 180, 18)
neck = tip - 3 * cs
boss = cy                                                        # clip starts right at the strip
shape("trap", cx - 60, cy - 18 - 2 * cs, 120, 2 * cs, size=0.3, up=True)  # dome on the pin side
shape("rect", cx - 28, boss, 56, neck - boss)                     # plus web, wide side
shape("rect", cx - 8.8, boss, 17.6, neck - boss, fill="#c9d1d9")  # crossing web
shape("trap", cx - 28, neck, 56, tip - neck)                      # blunt tip
shape("rect", cx - 27, boss, 54, 1 * cs, fill="#5b6673")          # block
fins = [boss + 1 * cs + (PITCH - 0.3) * cs + k * PITCH * cs for k in range(4)]   # lamella centres, equal gaps
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
text(cx - 130, tip + 48, 120, 14, "(tip width)", size=10, color="#555555")
label("g", cx + 34, fins[1] - 9, w=80, align="left")
label("T", cx + 34, tip + 36, w=90, align="left")
text(cx + 34, tip + 54, 130, 16, "(number of lamellae)", size=10, color="#555555", align="left")

# clip from below: plus inside a rounded square
qx, qy = 760, cy + 70
text(qx - 80, yD - 40, 300, 24, "Clip from below", size=16, bold=True, align="left")
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
text(qx - 150, qy + 36, 170, 16, "(lamella corner)", size=10, color="#555555", align="right")
text(qx - 100, qy + 60, 200, 16, "light = lamella, dark = plus", size=10, color="#555555")

# ---------------------------------------------------------------------------
# 4) Legend
lx, ly0 = 1080, 20
text(lx, ly0, 500, 26, "What is what?", size=16, bold=True, align="left")
rows = "".join(
    f'<tr><td style="padding:2px 6px;color:{OK if v else TODO}"><b>{k}</b></td>'
    f'<td style="padding:2px 6px"><b>{name}</b></td><td style="padding:2px 6px">{how}</td></tr>'
    for k, (v, unit, name, how) in DIMS.items())
table = f'<table style="border-collapse:collapse;font-size:11px">{rows}</table>'
cells.append(
    f'<mxCell id="{nid()}" value="{escape(table)}" style="text;html=1;whiteSpace=wrap;align=left;'
    f'verticalAlign=top;fontSize=11;" vertex="1" parent="1">'
    f'<mxGeometry x="{lx}" y="{ly0 + 34}" width="500" height="{len(DIMS) * 22}" as="geometry"/></mxCell>')
for i, (k, (v, unit, name, how)) in enumerate(DIMS.items()):
    svg.append(f'<text x="{lx}" y="{ly0 + 60 + i * 22}" font-size="11" font-family="sans-serif" '
               f'fill="{OK if v else TODO}"><tspan font-weight="bold">{k}  {escape(name)}</tspan>'
               f'<tspan fill="{INK}" x="{lx + 120}">{escape(how)}</tspan></text>')
ly_end = ly0 + 60 + len(DIMS) * 22
text(lx, ly_end, 500, 18, "The bend radius of the step follows from E, F and G and does not need measuring.",
     size=11, color="#555555", align="left")
text(lx, ly_end + 20, 500, 18, "The same letters are used for the parameters in bracket.scad.",
     size=11, color="#555555", align="left")

# ---------------------------------------------------------------------------
# 5) Rib detail: two cross-sections (scale 10 px/mm)
yr = ly_end + 160
text(lx, yr - 100, 520, 24, "Rib cross-section (enlarged)", size=16, bold=True, align="left")
text(lx, yr - 60, 200, 18, "on the slope", size=12, bold=True, align="left")
shape("rect", lx, yr, 200, 23)
shape("rect", lx + 85, yr - 40, 30, 40, fill="#5b6673")
line([(lx + 85, yr + 50), (lx + 115, yr + 50)], color=DIM, arrows=True)
ext([(lx + 85, yr + 26), (lx + 85, yr + 56)])
ext([(lx + 115, yr + 26), (lx + 115, yr + 56)])
label("U", lx + 120, yr + 41, w=70, align="left")
ext([(lx + 119, yr - 40), (lx + 150, yr - 40)])
vdim(lx + 142, yr - 40, yr, "V", side="right", lw=70)

rx = lx + 270
text(rx, yr - 60, 240, 18, "on the upper (clip) section", size=12, bold=True, align="left")
shape("rect", rx, yr, 200, 23)
shape("rect", rx + 85, yr - 20, 30, 20, fill="#5b6673")
ext([(rx + 119, yr - 20), (rx + 150, yr - 20)])
vdim(rx + 142, yr - 20, yr, "W", side="right", lw=70)
text(lx, yr + 80, 520, 18, "top = pin side. On the straight pin section the rib sits centred (bottom left).",
     size=10, color="#555555", align="left")

# ---------------------------------------------------------------------------
# 6) Pin end: rib and cross struts on the back (bottom left)
y2 = 1050
text(40, y2 - 100, 900, 24, "Pin end: rib and cross struts (enlarged)", size=16, bold=True, align="left")
text(60, y2 - 50, 260, 18, "straight pin section, cross-section", size=12, bold=True, align="left")
shape("rect", 60, y2, 200, 23)
shape("rect", 145, y2 - 16, 30, 55, fill="#5b6673")
ext([(179, y2 - 16), (210, y2 - 16)])
ext([(179, y2 + 39), (210, y2 + 39)])
vdim(202, y2 - 16, y2 + 39, "Z", side="right", lw=80)
text(60, y2 + 50, 260, 16, "The rib sits centred in the strip and", size=10, color="#555555", align="left")
text(60, y2 + 66, 260, 16, "sticks out equally on both sides", size=10, color="#555555", align="left")

text(360, y2 - 50, 260, 18, "cross strut, cross-section", size=12, bold=True, align="left")
shape("rect", 360, y2, 200, 23)
shape("rect", 370, y2 + 23, 180, 15, fill="#5b6673")
ext([(554, y2 + 38), (584, y2 + 38)])
vdim(576, y2 + 23, y2 + 38, "c", side="right", lw=80)
ext([(370, y2 + 42), (370, y2 + 70)])
ext([(550, y2 + 42), (550, y2 + 70)])
hdim(370, 550, y2 + 64, "d", ly=y2 + 68, lw=80)

text(690, y2 - 50, 300, 18, "pin end from the side", size=12, bold=True, align="left")
ps = 8
px0, pp = 700, 700 + 10 * ps
shape("rect", pp, y2 + 9 - 22, 29 * ps, 44, fill="#5b6673")   # rib, centred, 5.5 mm
shape("rect", px0, y2 + 9, pp - px0, 22, fill="#5b6673")      # back side up to the rounded end
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
model = (f'<mxfile host="app.diagrams.net"><diagram id="dimensions" name="Dimensions">'
         f'<mxGraphModel dx="{W}" dy="{H}" grid="1" gridSize="10" guides="1" page="1" pageScale="1" '
         f'pageWidth="{W}" pageHeight="{H}" background="#ffffff" math="0" shadow="0"><root>'
         f'<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(cells) +
         '</root></mxGraphModel></diagram></mxfile>\n')
(ROOT / "dimensions.drawio").write_text(model, encoding="utf-8")

svg_doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
           f'<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" '
           f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker></defs>'
           f'<rect width="100%" height="100%" fill="#ffffff"/>' + "".join(svg) + "</svg>\n")
(ROOT / "dimensions.svg").write_text(svg_doc, encoding="utf-8")
print("wrote dimensions.drawio and dimensions.svg")
