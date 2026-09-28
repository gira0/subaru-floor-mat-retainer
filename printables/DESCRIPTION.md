# Printables listing – copy & paste

Everything below is meant to be copied into the matching fields on printables.com.
Fields in [square brackets] still need your input.

---

## Name

Subaru Floor Mat Retainer Hook – J501EAJ000 / J501SAJ300 (parametric)

## Summary (short text under the title)

Printable replacement for the Subaru floor mat retainer clip (J501EAJ000 / J501SAJ300). Tested in a Subaru XV / Crosstrek 2014. Parametric OpenSCAD source included.

## Description

A printable replacement for the Subaru floor mat retainer: the hook that holds the floor mat in place, with a pin for the mat's eyelet and a clip that pushes into the hole in the car floor.

**OEM part numbers:** J501EAJ000 (EU) / J501SAJ300 (US)

**Tested in:** Subaru XV (European Crosstrek), 2014, 2.0D 147 PS. The printed part fits, clips in and holds the mat firmly.
The left and right originals are identical (not mirrored), so one model covers both sides.
Other Subaru models that use the same part number should fit too, but I have only tested the XV. Please post a make or a comment if it fits your car.

The original was hard to get and shipping it in was expensive, so I measured an original with calipers and rebuilt it as a parametric OpenSCAD model. It went through two test prints before it was "barely distinguishable" from the original.

### Printing

- **Orientation:** print it **on its side**, exactly as the STL is saved. That way all bends lie within the layers and do not break along layer lines.
- **Supports:** tree supports, "on build plate only", only needed for the pin and the clip.
- **Enable "Detect thin walls"** in your slicer (OrcaSlicer/PrusaSlicer: Quality tab). The clip lamellae are only 0.6 mm thick and are otherwise left out. Check the slice preview.
- Brim 3–5 mm helps, because the part stands on a narrow edge.
- 0.4 mm nozzle, 0.2 mm layers, 4–5 walls. 40 % infill is enough for PLA/PETG, 100 % for TPU.

### Material

- **PLA+** works well for a test fit (that is what the tested part is made of). It is rigid, so the clip is tight going in: it needed a firm push with the foot, then sits very securely.
- **For permanent use, print PETG, ASA or TPU.** PLA softens at 55–60 °C, which a parked car easily reaches in summer.
- **TPU 95A** gives the flexibility of the original but grips a bit less firmly.

### Customising (OpenSCAD)

`bracket.scad` is fully parametric. Every dimension is a named variable at the top of the file with a letter that matches the included dimension drawing (`dimensions.svg`). Open it in OpenSCAD and use **Window → Customizer**. Useful tweaks:
- Clip too tight in a rigid material: reduce `clip_fin_sz` (lamella size) from 6.7 to about 6.3 mm.
- Clip does not hold in your car: set `clip_style = "hole"` to get a screw hole instead.
- Too soft in TPU: increase the strip thickness `t` by 0.5–1 mm.

The exported STL is clean (0 non-manifold edges).

### Transparency

I designed this with help from Claude (Anthropic's AI assistant) in Claude Code. I took all the measurements from the original part and checked every step against it and against test prints. Claude wrote and refined the OpenSCAD model from those measurements.

## Files to upload

- `bracket.stl` – ready to print, already oriented
- `bracket.scad` – parametric source
- `dimensions.svg` – dimension drawing (optional; nice as an extra image or file)
- `README.md` – full dimension table and notes (optional)

## Images

- **Your own photos first** (Printables shows the first image as the cover): the print next to the original, and the part installed in the car.
- Then the renders from this folder: `01-overview.png`, `02-side.png`, `03-below.png`, `04-clip-hook.png`, `05-pin-end.png`,
  and the dimension drawing `06-dimensions.png`.
- **Do not use the photos in `img/`**; they look like shop product photos and are probably someone else's copyright.

## Print settings (the form fields)

- Printer: Anycubic Kobra S1
- Rafts: No
- Supports: Yes (tree, build plate only – pin and clip)
- Resolution: 0.2 mm
- Infill: 40 % (PLA+/PETG), 100 % (TPU)
- Filament: PLA+ (test fit); PETG / ASA / TPU recommended for permanent use

## Category

Hobby & Makers → Automotive  *(or: Household → Replacement Parts, whichever fits better)*

## Tags

subaru, xv, crosstrek, floor mat, floormat, retainer, clip, hook, car, automotive, replacement, spare part, J501EAJ000, J501SAJ300, openscad, parametric

## License

[choose: CC BY / CC BY-NC / CC BY-SA – see chat]
