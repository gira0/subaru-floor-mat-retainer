# Subaru Floor Mat Retainer – Parametric OpenSCAD Replacement

Printable replacement for the Subaru floor mat retainer / hook, OEM part number **J501EAJ000** (EU) / **J501SAJ300** (US).
The original is hard to get and expensive to ship, so this is a parametric rebuild you can print yourself.

**Tested in:** Subaru XV (European Crosstrek), 2014, 2.0D 147 PS. It fits and holds the mat firmly.
The two originals (left/right) are identical, not mirrored, so one model covers both sides.

The model was measured from an original part with calipers and refined over two test prints.
It was designed with help from Claude (Anthropic's AI assistant) in Claude Code.

**Printables:** https://www.printables.com/model/1858866

| File | Purpose |
|---|---|
| `bracket.scad` | The OpenSCAD model. All dimensions are at the top of the file. |
| `bracket.stl` | Ready-to-print file, already oriented for printing |
| `dimensions.drawio` | Dimension drawing with all letters. Open with [app.diagrams.net](https://app.diagrams.net) or the draw.io app |
| `dimensions.svg` | The same drawing as an image |
| `preview/` | Renders of the model |
| `tools/make_drawing.py` | Regenerates the drawing |
| `printables/` | Listing text (`DESCRIPTION.md`) and render images for printables.com |

## What the part looks like

It is a **single injection-moulded plastic part** (not sheet metal): a flat strip with a step in the middle.

```
      Pin                                Clip
       ▄                                  ▼
       █                     ┌────────────┬─────┐
  ─────┴──────────┐         /              Hook │
  straight part   └────────┘ ← step             ▼
```

- **Pin**: mushroom button. The eyelet of the floor mat goes over it.
- **Step**: the strip bends up at an angle and then continues straight.
- **Clip**: a plug on the underside that is pushed into the hole in the car floor. Seen from below it is a plus shape with thin lamella plates.
- **Hook**: the end bent down by 90°. It grips under an edge.

## Dimensions

The letters are the same in `dimensions.drawio`, here and in `bracket.scad`.

| | What | Value | Status |
|---|---|---|---|
| A | Strip thickness | 2.3 mm | measured |
| B | Strip width | 20 mm (19.93) | measured |
| C | Overall length, part lying flat: pin end to the very outside of the hook (over the rib) | 147.9 mm | measured |
| D | Straight section at the pin end, up to where the step starts | 51 mm | adjusted after test print (measured: 56) |
| E | How much higher the upper section sits | 30 mm | measured |
| F | Length of the step, measured horizontally | 50 mm | adjusted after test print (measured: 45) |
| G | Slope angle | 35.6° | adjusted: flatter, same bend radius (measured: 40°) |
| H | Hook depth: top of strip to hook tip | 14.9 mm | measured |
| I | Hook angle | 90° | measured |
| J | Pin centre to strip end | 10 mm | measured |
| K / L | Pin shaft / pin head diameter | 5 / 9 mm | measured |
| M / N | Top of strip to underside of head / head height | 15 / 4 mm | measured |
| O | Clip centre to outside of hook | 20 mm | measured |
| P | How far the clip sticks out below | 17.5 mm | measured |
| Q | Clip: lamella size (rounded square) | 6.7 mm | measured |
| R / S | Clip: width of one plus web / size of the plus | 2.2 / 7 mm | measured |
| T | Number of lamellae | 4 | measured |
| U | Rib: width | 3 mm | measured |
| V | Rib: height above the strip on the slope | 4 mm | measured |
| W | Rib: height above the strip on the upper (clip) section | 2 mm | measured |
| Z | Rib on the straight pin section: total height, centred in the strip | 5.5 mm | measured |
| a | Cross struts: pin centre to centre of the 2nd strut | 24.6 mm | adjusted after test print (measured: 21.6) |
| b | Cross strut: thickness (lengthwise) | 3 mm | measured |
| c | Cross strut: height on the back | 2 mm | measured |
| d | Cross strut: length across the strip | 20 mm (full width) | measured |
| e | Clip: lamella spacing (centre to centre) | 2.5 mm | adjusted, tested in the car (measured: 1.8) |
| f | Clip: solid block right at the strip | 1 mm | measured |
| g | Clip: lamella thickness | 0.6 mm | measured |
| h | Clip: lamella corner radius | 1.5 mm | *estimate* |
| i | Clip: length of the blunt tip | 3 mm | measured |
| j | Clip: width of the plus at the very tip | 1.5 mm | *estimate* |
| k | Dome (pin side, opposite the clip): diameter | 15 mm | measured |
| l | Dome: height at the centre | 2 mm | measured |
| m | Stop block at the hook tip: length | 3 mm | measured |

*Estimate* means: not measured, derived from photos or by eye.

**The bend radius of the step does not need measuring.** It follows from E, F and G (about 11.5 mm inside).

**Rounded end:** the pin end is a half circle with a radius of half the strip width, and the pin sits at its centre, so J = B/2.

**Rib:** the stiffening rib (U, 3 mm wide) runs lengthwise along the middle of the strip.
- On the straight pin section it sits centred in the strip: 5.5 mm tall (Z), so it sticks out 1.6 mm on both sides and merges into the pin. On the back it runs past the pin all the way to the rounded end.
- It is one continuous web of constant height. In the bend at the foot of the slope it moves up and simply passes through the strip: on the back it dips into the strip, on top it grows to the 4 mm of the slope (V). Its top edge follows a round arc there (`rib_fillet1`, radius 8.5 mm, estimate).
- In the bend to the upper section its top edge goes from 4 to 2 mm (W) in a round arc (`rib_fillet`, radius 15 mm, estimate).
- It then runs around the outside of the hook to the tip, where it ends in a stop block (m, 3 mm long) that spans the full strip width and is flush with the rib.
- `rib_side = -1` moves the rib to the clip side.

**Clip:** right at the strip sits a 1 mm solid block (f), followed by 4 thin lamellae (0.6 mm, g) with equal gaps (spacing e).
Then comes a plus of two crossed webs (R × S) whose last 3 mm taper to a blunt tip (i).
The clip length P = 17.5 mm is measured from the underside of the strip.

**Dome:** opposite the clip, on the pin side of the strip, is a flat round dome (15 mm Ø, 2 mm high at the centre). It fades out towards its rim and merges with the rib.

**Cross struts:** on the back of the pin end there are two transverse webs, one directly under the pin and one 24.6 mm further (a). They can be switched off with `struts`.

### Changing dimensions

1. Open `bracket.scad` in OpenSCAD.
2. Find the line with the matching letter at the top, e.g. `hook_depth = 14.9; // H …`, and change the number.
   Or use **Window → Customizer**, which shows an input field for every dimension.
3. Render with F6, then **File → Export → STL**.

From the command line:

```sh
openscad -o bracket.stl bracket.scad
openscad -D hook_depth=16 -o bracket.stl bracket.scad   # override a single value
```

## Material and printing

**Material:**
- **Test fit:** PLA+ works well and is what the tested part was printed in. It is rigid, so the clip is tight going in (it needed a firm push with the foot) but then sits very securely.
- **Final part:** PLA+ softens at about 55–60 °C, which a car interior easily reaches in summer. Use **PETG**, **ASA** or **TPU** for a part that stays in the car.
- **TPU 95A** gives the flex of the original but is softer: the hook grips less and the clip lamellae give way more easily. If it is too soft, increase `t` (A) by 0.5–1 mm or make the rib stronger (`rib_w`, `rib_ramp`).
- For rigid materials (PETG, PLA+) you can make the clip easier to insert by reducing the lamella size `clip_fin_sz` (Q) from 6.7 to about 6.3 mm.
- If the clip does not hold in your car, `clip_style = "hole"` replaces it with a screw hole.

**Orientation: on its side** (the STL is already saved this way).
The strip width (20 mm) becomes the print height, so the extrusion lines run through all bends and the bends are not loaded across layer lines.
The strip needs no support; only the pin and the clip stick out sideways and need some.

**Slicer notes (OrcaSlicer, tested on an Anycubic Kobra S1):**
- 0.4 mm nozzle, 0.2 mm layers
- 4–5 walls (the thin strip is effectively solid), 100 % infill for TPU / 40 % is fine for PLA+ and PETG
- Tree support, "on build plate only", top Z distance 0.2–0.25 mm
- Brim 3–5 mm, because the contact area is narrow
- **Enable "Detect thin walls"** (Quality tab). Otherwise the 0.6 mm clip lamellae are left out. Check in the slice preview. If it still fails, set `clip_fin_t` to 0.8.
- TPU: 20–30 mm/s, max. volumetric flow about 3–4 mm³/s, short slow retraction, dry the filament first

## Modelling assumptions

- The strip has the same thickness and width everywhere.
- Both bends of the step have the same radius.
- The pin head is a disc whose rim is fully rounded top and bottom (radius = half the head height).
- The small nubs on the edges of the original are not modelled; they look like moulding marks.

## Technical note: clean mesh

The strip and the rib are each generated as one closed mesh along the path (`sweep_mesh`), not from many `hull()` pieces.
The piecewise version produced over 3000 non-manifold edges at the bends in OpenSCAD 2021, which OrcaSlicer complains about.
Where parts would otherwise touch exactly, they overlap slightly or are offset by 0.001 mm for the same reason.
The current STL has 0 non-manifold edges, for all variants of `clip_style` and `clip_at_tip`.

## License

This project is licensed under [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
You may print, share, modify and also sell it, as long as you give credit and share modified versions under the same license.
