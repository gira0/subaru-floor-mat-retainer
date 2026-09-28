// Subaru floor mat retainer (OEM J501EAJ000 / J501SAJ300) – parametric replacement
// Test-fitted in a Subaru XV / Crosstrek (EU) 2014, 2.0D.
//
// The letters (A, B, C …) match the dimension drawing dimensions.drawio and the
// table in README.md.
//
//   measured = taken from the original part with calipers
//   adjusted = measured, then corrected after a test print
//   ESTIMATE = not measured, derived from photos / by eye
//
// Coordinates: X = length, Y = width, Z = height (pin points up).

/* [Strip: the flat, long plastic strip] */
t           = 2.3;    // A  measured    strip thickness
w           = 20;     // B  measured    strip width (19.93, rounded)
L_total     = 147.9;  // C  measured    overall length, part lying flat: pin end to the very outside of the hook (over the rib)
L_lower     = 51;     // D  adjusted    straight section at the pin end, up to where the slope starts
corner_r    = 1;      //    cosmetic    edge rounding
// The pin end is a half circle (radius = half the width); the pin sits at its centre.

/* [Step: the sloped offset in the middle] */
rise        = 30;     // E  measured    how much higher the upper section sits than the pin section
ramp_run    = 50;     // F  adjusted    length of the step (measured horizontally, bend to bend)
ramp_angle  = 35.6;   // G  adjusted    slope angle in degrees
// The bend radius of the step does not need measuring; it follows from E, F and G.

/* [Hook: the end bent downwards] */
hook_depth  = 14.9;   // H  measured    hook depth (top of strip to hook tip)
hook_angle  = 90;     // I  measured    hook angle: 90 = square, more than 90 = tip points slightly inwards
hook_stop   = 3;      // m  measured    stop block at the hook tip: length; full width, flush with the rib on the outside
hook_ri     = 1.5;    //    cosmetic    inner radius of the hook bend (small = sharp corner)

/* [Pin: the mushroom button the mat eyelet goes over] */
pin_x       = 10;     // J  measured    pin centre to strip end (= centre of the rounded end)
pin_d       = 5;      // K  measured    shaft diameter
pin_head_d  = 9;      // L  measured    head diameter
pin_neck    = 15;     // M  measured    top of strip to underside of head
pin_head_h  = 4;      // N  measured    head height (fully rounded top and bottom)

/* [Clip: the plug underneath that goes into the hole in the floor] */
// Seen from below it is a plus of two crossed webs. Right at the strip a 1 mm solid block,
// then thin lamella plates (rounded squares), then the plus-shaped neck down to a blunt tip.
// Opposite, on the pin side of the strip, sits a flat round dome.
clip_style  = "plus"; // [plus:plus clip with lamellae, hole:hole for a screw, none:nothing]
clip_x      = 20;     // O  measured    clip centre to the very outside of the hook
clip_len    = 17.5;   // P  measured    how far the clip sticks out below (from the strip)
clip_fin_sz = 6.7;    // Q  measured    lamella size (rounded square, edge to edge)
clip_arm    = 2.2;    // R  measured    width of one plus web
clip_plus   = 7;      // S  measured    plus size (length of one web)
clip_fins   = 4;      // T  measured    number of lamellae
clip_pitch  = 2.5;    // e  adjusted    lamella spacing (centre to centre; measured 1.8, 2.5 tested in the car)
clip_base   = 1;      // f  measured    solid block right at the strip
clip_fin_t  = 0.6;    // g  measured    lamella thickness (0.6 is tight for a 0.4 nozzle, see README)
clip_fin_r  = 1.5;    // h  ESTIMATE    lamella corner radius
clip_tip    = 3;      // i  measured    length of the blunt tip
clip_tip_w  = 1.5;    // j  ESTIMATE    width of the plus at the very tip (blunt end)
clip_at_tip = false;  //    false: block + lamellae right at the strip (like the original); true: at the tip
clip_boss_d = 15;     // k  measured    diameter of the round dome (pin side, opposite the clip)
clip_boss_h = 2;      // l  measured    dome height at the centre (same as rib W)
hole_d      = 5;      //    only for clip_style = "hole": hole diameter

/* [Rib: the stiffening web along the middle of the strip] */
// The rib runs lengthwise along the middle of the strip. On the straight pin section it sits
// centred in the strip and sticks out equally on both sides (total height Z). In the bend at
// the foot of the slope it moves to the pin side: on the slope it sticks out V, on the upper
// section only W, and it runs around the outside of the hook down to the hook tip.
rib         = true;   //    rib on/off
rib_side    = 1;      //    1 = pin side, -1 = clip side
rib_w       = 3;      // U  measured    rib width
rib_ramp    = 4;      // V  measured    how far the rib sticks out on the slope
rib_upper   = 2;      // W  measured    how far the rib sticks out on the upper (clip) section
rib_fillet  = 15;     //    ESTIMATE    radius of the rib edge transition from V to W at the 2nd bend
rib_fillet1 = 8.5;    //    ESTIMATE    radius of the rib edge transition at the 1st bend (foot of the slope)
rib_mid     = 5.5;    // Z  measured    total rib height on the straight pin section, centred in the strip

/* [Cross struts on the back, at the pin end] */
// Two transverse webs on the back: one directly under the pin, one further towards the slope.
struts      = true;   //    cross struts on/off
strut_gap   = 24.6;   // a  adjusted    pin centre to centre of the 2nd strut (measured 21.6, +3 after test print)
strut_t     = 3;      // b  measured    strut thickness (measured lengthwise)
strut_h     = 2;      // c  measured    how far a strut sticks out on the back
strut_len   = 20;     // d  measured    strut length (across the strip) = full strip width

/* [Output] */
print_on_side = true; // true: part lies on its side (recommended, see README)
$fn = 48;
arc_steps = 12;       // segments per bend

// ---------------------------------------------------------------------------
// Derived values (strip centre line)
a   = ramp_angle;
R1  = (ramp_run - rise / tan(a)) / (2 * tan(a/2));   // centre-line radius of the step, from E, F, G
R3  = hook_ri + t/2;               // centre-line radius of the hook
bend_ri = R1 - t/2;
L_ramp  = (rise - 2*R1*(1 - cos(a))) / sin(a);
hook_rib = (rib && rib_side > 0) ? rib_upper : 0;   // rib sits on the outside of the hook
L_band  = L_total - hook_rib;                        // outside of the strip at the hook
L_upper = L_band - L_lower - ramp_run - R3 - t/2;
L_hook  = hook_depth - t/2 - R3;

assert(bend_ri > 0, "F (ramp_run) too short for E (rise) and G (ramp_angle)");
assert(L_ramp  > 0, "F (ramp_run) too long for E (rise) and G (ramp_angle)");
assert(L_upper > 0, "C (L_total) too small for the other dimensions");
assert(L_hook  > 0, "H (hook_depth) too small");
assert(pin_head_d > pin_d, "L (head) must be larger than K (shaft)");
assert(rib_mid > t, "Z (rib_mid) must be larger than the strip thickness A");

// Path as turtle commands: ["line", length] | ["arc", radius, angle (+ = upwards)]
path = [
    ["line", L_lower - pin_x],
    ["arc",  R1,  a],
    ["line", L_ramp],
    ["arc",  R1, -a],
    ["line", L_upper],
    ["arc",  R3, -hook_angle],
    ["line", L_hook]
];

// Turtle -> list of [x, z, heading, segment index]; lines split into ~1 mm steps (for the rib)
function step_pts(p, c, i) =
    c[0] == "line"
      ? let(n = max(1, ceil(c[1] / 1)))
        [for (k = [1:n]) [p[0] + k*c[1]/n*cos(p[2]), p[1] + k*c[1]/n*sin(p[2]), p[2], i]]
      : [for (k = [1:arc_steps]) let(
            da = c[2]/arc_steps,
            pk = arc_pos(p, c[1], da, k))   // position after k chord steps
          [pk[0], pk[1], p[2] + k*da, i]];

function arc_pos(p, R, da, k) =
    k == 0 ? [p[0], p[1]]
           : let(q = arc_pos(p, R, da, k-1),
                 h = p[2] + (k-1)*da + da/2,
                 ch = 2*R*sin(abs(da)/2))
             [q[0] + ch*cos(h), q[1] + ch*sin(h)];

function walk(cmds, p, i = 0) =
    i >= len(cmds) ? []
    : let(s = step_pts(p, cmds[i], i), last = s[len(s)-1])
      concat(s, walk(cmds, last, i+1));

start = [pin_x, t/2, 0, 0];     // strip starts at the pin; the half-circle end sits before it
pts = concat([start], walk(path, start));

// arc length from the pin for each point, and x position -> arc length (before the hook)
function cum(i) = i == 0 ? 0 : cum(i-1) + norm([pts[i][0] - pts[i-1][0], pts[i][1] - pts[i-1][1]]);
S = [for (i = [0:len(pts)-1]) cum(i)];
x_to_s = [for (i = [0:len(pts)-1]) if (pts[i][3] <= 4) [pts[i][0], S[i]]];

// Rib: height above the strip surface per path point
// 1st bend (foot of the slope): here the rib moves from "centred" to the pin side
b1_s0 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 0) S[i]]);
b1_s1 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 1) S[i]]);
// At the 2nd bend: join the rib edge of the slope (V) and of the upper section (W) with an
// arc, so there is neither a bump nor a dent.
i_b2 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 2) i]);   // end of slope = start of 2nd bend
Q0  = [pts[i_b2][0], pts[i_b2][1]];
d1  = [cos(a), sin(a)];                    // slope direction
n1  = [-sin(a), cos(a)];                   // slope normal (pin side)
zc_up = rise + t/2;                        // centre line of upper section
Zh  = zc_up + t/2 + rib_upper;             // rib edge on upper section
P1  = Q0 + n1 * (t/2 + rib_ramp);          // point on the rib edge of the slope
u_c = (Zh - P1[1]) / sin(a);
K   = P1 + u_c * d1;                       // intersection of the two edges
tl  = rib_fillet * tan(a/2);
T1  = K - tl * d1;                         // arc starts
T2  = K + [tl, 0];                         // arc ends
Cf  = T2 - [0, rib_fillet];                // arc centre

function clamp01(v) = min(1, max(0, v));
function smooth(v) = let(x = clamp01(v)) x * x * (3 - 2 * x);   // smooth transition without a kink
function cross2(p, q) = p[0] * q[1] - p[1] * q[0];

// Distance from the centre line (point i, along the normal) to the rib edge:
// slope -> arc -> upper section. The ray hits exactly one of the three pieces.
function contour_dist(i) =
    let(P = [pts[i][0], pts[i][1]], n = [-sin(pts[i][2]), cos(pts[i][2])],
        D1 = P1 - P,
        l1 = cross2(D1, d1) / cross2(n, d1),
        u1 = cross2(D1, n) / cross2(n, d1),
        l2 = (Zh - P[1]) / n[1],
        Dc = P - Cf,
        nd = n * Dc,
        l3 = -nd + sqrt(max(0, nd * nd - Dc * Dc + rib_fillet * rib_fillet)),
        hit3 = P + l3 * n - Cf,
        th3 = atan2(hit3[1], hit3[0]))
    u1 <= u_c - tl ? l1
    : (P[0] + l2 * n[0] >= T2[0] ? l2
    : (th3 >= 90 && th3 <= 90 + a ? l3 : min(l1, l2)));

// Top/bottom edge relative to the strip centre line (+ = pin side)
// 1st bend (foot of the slope): join the rib edge of the straight section (centred, rib_mid/2 above
// the centre line) and of the slope (V) with a concave arc – like at the 2nd bend.
i_b1 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 1) i]);   // end of 1st bend = start of slope
Za   = t/2 + rib_mid/2;                                       // rib edge on straight section
P1b  = [pts[i_b1][0], pts[i_b1][1]] + n1 * (t/2 + rib_ramp);    // point on the rib edge of the slope
u_k1 = (Za - P1b[1]) / sin(a);
K1   = P1b + u_k1 * d1;                                       // corner between the two edges
tg   = rib_fillet1 * tan(a/2);
TA   = K1 - [tg, 0];                                          // arc starts (straight section)
TB   = K1 + tg * d1;                                          // arc ends (slope)
Cg   = TA + [0, rib_fillet1];                                 // arc centre (above)
function contour1_dist(i) =
    let(P = [pts[i][0], pts[i][1]], n = [-sin(pts[i][2]), cos(pts[i][2])],
        lA = (Za - P[1]) / n[1],
        D1 = P1b - P,
        lB = cross2(D1, d1) / cross2(n, d1),
        uB = cross2(D1, n) / cross2(n, d1),
        Dg = P - Cg,
        nd = n * Dg,
        disc = nd * nd - Dg * Dg + rib_fillet1 * rib_fillet1,
        lG = -nd - sqrt(max(0, disc)),
        hitG = P + lG * n - Cg,
        thG = atan2(hitG[1], hitG[0]))
    P[0] + lA * n[0] <= TA[0] ? lA
    : (uB >= u_k1 + tg ? lB
    : (disc >= 0 && thG >= -90 - 0.01 && thG <= -90 + a + 0.01 ? lG : max(lA, lB)));
i_ramp_mid = round((i_b1 + i_b2) / 2);

function rib_top(i) =
    pts[i][3] <= 1 || (pts[i][3] == 2 && i <= i_ramp_mid) ? contour1_dist(i)
    : pts[i][3] <= 4 ? contour_dist(i)
    : t/2 + rib_upper;
// Bottom edge: up to the middle of the slope the rib is one continuous web of constant height
// rib_mid. It moves up in the 1st bend and simply passes through the strip; on the slope its
// bottom edge lies inside the strip (invisible). After that it ends at the strip centre.
function rib_bot(i) =
    pts[i][3] <= 1 || (pts[i][3] == 2 && i <= i_ramp_mid) ? min(rib_top(i) - rib_mid, 0) : 0;
function rib_edges(i) =
    rib_side > 0 ? [rib_top(i), rib_bot(i)] : [-rib_bot(i), -rib_top(i)];

// ---------------------------------------------------------------------------
// Cross-section as a rounded rectangle in local coordinates [u = normal, v = width],
// counter-clockwise, always the same number of points (so the rings match up)
corner_steps = 4;
function rrect(sw, st, du = 0) =
    let(r = min(corner_r, st/2 - 0.01, sw/2 - 0.01),
        cu = st/2 - r, cv = sw/2 - r,
        c = [[cu, cv, 0], [-cu, cv, 90], [-cu, -cv, 180], [cu, -cv, 270]])
    [for (q = c) for (k = [0:corner_steps])
        let(th = q[2] + 90 * k / corner_steps) [du + q[0] + r * cos(th), q[1] + r * sin(th)]];

// cross-section at path point q in world coordinates
function ring(q, sec) = [for (p = sec) [q[0] - sin(q[2]) * p[0], p[1], q[1] + cos(q[2]) * p[0]]];

// One closed mesh along the path (instead of many hull() pieces -> clean manifold)
module sweep_mesh(secs, path = pts) {
    n = len(path); m = len(secs[0]);
    points = [for (i = [0:n-1]) each ring(path[i], secs[i])];
    sides = [for (i = [0:n-2]) for (j = [0:m-1])
                [i*m + j, i*m + (j+1) % m, (i+1)*m + (j+1) % m, (i+1)*m + j]];
    caps = [[for (j = [m-1:-1:0]) j], [for (j = [0:m-1]) (n-1)*m + j]];
    polyhedron(points, concat(sides, caps), convexity = 6);
}

module band() {
    sweep_mesh([for (i = [0:len(pts)-1]) rrect(w, t)]);
    // Half-circle end around the pin: exactly the same cross-section as the strip (half width as radius).
    // It reaches 5° into the strip on each side so the parts overlap instead of just touching.
    half = [for (p = rrect(w, t)) if (p[1] >= 0) [p[1], p[0]]];   // [radius, height]
    // 0.001 mm thinner than the strip so top/bottom faces do not coincide (otherwise non-manifold)
    translate([pin_x, 0, t/2]) scale([1, 1, 1 - 0.002 / t]) rotate([0, 0, 85]) rotate_extrude(angle = 190, $fn = 96)
        polygon(concat([[0, half[0][1]]], half, [[0, half[len(half)-1][1]]]));
    // Stop block at the hook tip: full width, as high as the rib on the outside.
    // Tiny gaps (0.001 mm) and 0.3 mm embedding prevent exactly coinciding faces.
    if (hook_stop > 0) {
        tip = pts[len(pts)-1];
        back = [tip[0] - hook_stop * cos(tip[2]), tip[1] - hook_stop * sin(tip[2]), tip[2]];
        end  = [tip[0] - 0.001 * cos(tip[2]), tip[1] - 0.001 * sin(tip[2]), tip[2]];
        outer = t/2 + ((rib && rib_side > 0) ? rib_upper : 0) + 0.001;
        inner = -t/2 + 0.3;
        sec = rrect(w - 0.002, outer - inner, (outer + inner) / 2);
        sweep_mesh([sec, sec], [back, end]);
    }
    // The rib on the back runs from the pin all the way to the rounded end. Same cross-section as
    // the rib (bottom at rib_mid/2), embedded 0.3 mm into the strip; 0.001 mm smaller so its faces
    // do not coincide with the main rib (otherwise non-manifold). Follows the rounded end.
    if (rib && rib_side > 0) {
        u_b = -rib_mid/2 + 0.001;
        u_t = -t/2 + 0.3;
        intersection() {
            sweep_mesh([for (k = [0:1]) rrect(rib_w - 0.002, u_t - u_b, (u_t + u_b) / 2)],
                       [[0, t/2, 0], [pin_x + 1, t/2, 0]]);
            translate([pin_x, 0, -rib_mid]) cylinder(r = w/2 - 0.01, h = 2 * rib_mid, $fn = 96);
        }
    }
    // rib ends inside the stop block
    rib_n = hook_stop > 0 ? max([for (i = [0:len(pts)-1]) if (S[i] <= S[len(S)-1] - hook_stop + 1) i]) : len(pts) - 1;
    if (rib)
        sweep_mesh([for (i = [0:rib_n]) let(e = rib_edges(i))
                        rrect(rib_w, e[0] - e[1], (e[0] + e[1]) / 2)], [for (i = [0:rib_n]) pts[i]]);
}

module back_struts() {
    // bottom of the strip at the pin end is at z = 0, top at z = t
    intersection() {
        for (x = [pin_x, pin_x + strut_gap])
            translate([x - strut_t/2, -strut_len/2, rib_side > 0 ? -strut_h : t/2])
                cube([strut_t, strut_len, t/2 + strut_h]);
        // do not stick out past the rounded pin end
        union() {
            translate([pin_x, 0, -50]) cylinder(r = w/2, h = 100);
            translate([pin_x, -w/2, -50]) cube([L_total, w, 100]);
        }
    }
}

module mushroom_pin() {
    rr = min(pin_head_h, pin_head_d) / 2;     // rim radius = half head height -> fully round top and bottom
    translate([pin_x, 0, t - 0.01]) {
        // shaft (reaches into the head centre so shaft and head overlap) with a fillet at the base
        cylinder(d = pin_d, h = pin_neck + pin_head_h / 2);
        cylinder(d1 = pin_d + 2, d2 = pin_d, h = 1);
        // head: disc with a fully rounded rim
        translate([0, 0, pin_neck])
            rotate_extrude($fn = 64)
                hull() {
                    square([0.01, pin_head_h]);
                    translate([pin_head_d/2 - rr, pin_head_h/2]) circle(r = rr, $fn = 32);
                }
    }
}

// upper section: bottom is at z = rise
upper_bottom_z = rise;
clip_cx = L_total - clip_x;
assert(clip_tip + clip_base + clip_fins * clip_pitch <= clip_len, "lamellae do not fit on clip length P");

module rounded_square_plate(h) {
    r = min(clip_fin_r, clip_fin_sz/2 - 0.01);
    linear_extrude(h) offset(r = r) square(clip_fin_sz - 2*r, center = true);
}

module plus_clip() {
    // local: z = 0 at the strip underside, +z points to the clip tip
    L      = clip_len;
    neck   = L - clip_tip;
    base_z = clip_at_tip ? neck - clip_base : 0;
    // same gap (clip_pitch - clip_fin_t) between block and 1st lamella as between lamellae
    fin_z  = [for (k = [1:clip_fins])
                 clip_at_tip ? base_z - k * clip_pitch
                             : clip_base + k * clip_pitch - clip_fin_t];
    translate([clip_cx, 0, upper_bottom_z + 0.01]) mirror([0, 0, 1]) {
        for (a = [0, 90]) rotate([0, 0, a])
            translate([-clip_plus/2, -clip_arm/2, 0]) cube([clip_plus, clip_arm, neck + 0.01]);
        // blunt tip: the plus webs taper to clip_tip_w
        for (a = [0, 90]) rotate([0, 0, a])
            translate([0, 0, neck])
                linear_extrude(clip_tip, scale = [clip_tip_w / clip_plus, 1])
                    square([clip_plus, clip_arm], center = true);
        translate([0, 0, base_z]) rounded_square_plate(clip_base);
        for (z = fin_z) translate([0, 0, z]) rounded_square_plate(clip_fin_t);
    }
}

module clip_boss() {
    // flat dome (spherical cap) on the pin side above the clip, fading out towards the rim
    rs = (pow(clip_boss_d/2, 2) + pow(clip_boss_h, 2)) / (2 * clip_boss_h);
    translate([clip_cx, 0, upper_bottom_z + t])
        intersection() {
            translate([0, 0, clip_boss_h - rs]) sphere(r = rs, $fn = 96);
            translate([0, 0, -0.3]) cylinder(d = clip_boss_d + 1, h = clip_boss_h + 0.3);   // 0.3 mm into the strip
        }
}

module bracket() {
    difference() {
        union() {
            band();
            if (struts) back_struts();
            mushroom_pin();
            if (clip_style == "plus") plus_clip();
            if (clip_style != "none") clip_boss();
        }
        if (clip_style == "hole")
            translate([clip_cx, 0, upper_bottom_z - 1]) cylinder(d = hole_d, h = t + 2);
    }
}

if (print_on_side)
    // side face on the bed: all bends lie within the layer plane
    translate([0, 0, w/2]) rotate([90, 0, 0]) bracket();
else
    bracket();

echo(str("step inner radius=", bend_ri, "  slope=", L_ramp, "  upper section=", L_upper, "  hook=", L_hook));
