// Subaru Fußmatten-Halterung (OEM J501EAJ000 / J501SAJ300) – parametrischer Nachbau
//
// Die Buchstaben (A, B, C …) entsprechen der Zeichnung masse.drawio und der
// Tabelle in README.md.
//
//   gemessen  = vom Originalteil mit dem Messschieber abgenommen
//   SCHÄTZUNG = noch nicht gemessen, aus Fotoproportionen abgeleitet
//
// Koordinaten: X = Länge, Y = Breite, Z = Höhe (Pin zeigt nach oben).

/* [Band: das flache, längliche Kunststoffband] */
t           = 2.3;    // A  gemessen    Dicke des Bandes (wie dick das Plastik ist)
w           = 20;     // B  gemessen    Breite des Bandes (19,93 → gerundet)
L_total     = 147.9;  // C  gemessen    Gesamtlänge, Teil flach hingelegt: Ende am Pin bis ganz außen am Haken (über die Rippe)
L_lower     = 51;     // D  angepasst   gerades Stück am Pin-Ende, bis dort wo es anfängt hochzugehen
corner_r    = 1;      //    Formsache   Kantenrundung
// Das Pin-Ende ist ein Halbkreis (Radius = halbe Breite), der Pin sitzt in seinem Mittelpunkt.

/* [Kröpfung: die schräge Stufe in der Mitte] */
rise        = 30;     // E  gemessen    wie viel höher der hintere Teil liegt als der vordere
ramp_run    = 50;     // F  angepasst   wie lang die Stufe ist (waagerecht gemessen, von Biegung zu Biegung)
ramp_angle  = 35.6;   // G  angepasst   wie steil die Stufe ist, in Grad
// Den Biegeradius der Stufe muss man nicht messen, er ergibt sich aus E, F und G.

/* [Haken: das nach unten gebogene Ende] */
hook_depth  = 14.9;   // H  gemessen     wie weit der Haken nach unten reicht (Oberseite Band bis Hakenspitze)
hook_angle  = 90;     // I  gemessen     Winkel des Hakens: 90 = rechtwinklig, mehr als 90 = Spitze zeigt etwas nach innen
hook_stop   = 3;      //    gemessen    Anschlagblock an der Hakenspitze: Länge; volle Breite, außen bündig mit der Rippe
hook_ri     = 1.5;    //    Formsache   Innenradius der Hakenbiegung (klein = scharfe Ecke)

/* [Pin: der Pilzknopf, auf den die Fußmatte gesteckt wird] */
pin_x       = 10;     // J  gemessen    Abstand Pin-Mitte bis Bandende (= Mittelpunkt der Rundung)
pin_d       = 5;      // K  gemessen     Dicke des Stiels
pin_head_d  = 9;      // L  gemessen    Dicke des Kopfes
pin_neck    = 15;     // M  gemessen    Abstand Oberseite Band bis Unterkante Kopf
pin_head_h  = 4;      // N  gemessen    Höhe nur des Kopfes (oben und unten voll abgerundet)

/* [Clip: der Stecker unten, der ins Loch im Boden kommt] */
// Von unten gesehen ein Plus aus zwei gekreuzten Stegen. Direkt am Band ein 1 mm dicker
// Block, dann dünne Lamellen-Platten (abgerundete Quadrate), dann der Plus-Hals bis zur
// stumpfen Spitze. Gegenüber, auf der Pin-Seite des Bandes, sitzt eine flache runde Kuppel.
clip_style  = "plus"; // [plus:Plus-Clip mit Lamellen, hole:Loch für eine Schraube, none:nichts]
clip_x      = 20;     // O  gemessen    Abstand Clip-Mitte bis ganz außen am Haken
clip_len    = 17.5;   // P  gemessen    wie weit der Clip unten heraussteht (ab Band)
clip_fin_sz = 6.7;    // Q  gemessen    Größe der Lamellen (abgerundetes Quadrat, Kante zu Kante)
clip_arm    = 2.2;    // R  gemessen    Breite eines Plus-Stegs
clip_plus   = 7;      // S  gemessen    Größe des Plus (Länge eines Stegs)
clip_fins   = 4;      // T  gemessen    Anzahl der Lamellen
clip_pitch  = 2.5;    // e  gemessen    Abstand der Lamellen zueinander (Mitte zu Mitte)
clip_base   = 1;      // f  gemessen    massiver Block direkt am Band
clip_fin_t  = 0.6;    // g  gemessen    Dicke einer Lamelle (0,6 ist mit 0,4er Düse knapp, siehe README)
clip_fin_r  = 1.5;    // h  SCHÄTZUNG   Eckenradius der Lamellen
clip_tip    = 3;      // i  gemessen    Länge der stumpfen Spitze
clip_tip_w  = 1.5;    // j  SCHÄTZUNG   Breite des Plus ganz vorne an der Spitze (stumpfes Ende)
clip_at_tip = false;  //    false: Block + Lamellen direkt am Band (wie Original); true: an der Spitze
clip_boss_d = 15;     // k  gemessen    Durchmesser der runden Kuppel (Pin-Seite, gegenüber vom Clip)
clip_boss_h = 2;      // l  gemessen    Höhe der Kuppel in der Mitte (so hoch wie die Rippe W)
hole_d      = 5;      //    nur bei clip_style = "hole": Lochdurchmesser

/* [Rippe: der Versteifungssteg in der Mitte des Bandes] */
// Die Rippe läuft mittig längs übers Band. Auf dem geraden Stück am Pin steckt sie mittig
// im Band und steht oben und unten gleich weit über (Gesamthöhe Z). In der Biegung am
// Fuß der Schräge wandert sie auf die Pin-Seite: an der Schräge steht sie V über, auf dem
// oberen Teil nur noch W, und läuft außen um den Haken herum bis zur Hakenspitze.
rib         = true;   //    Rippe ein/aus
rib_side    = 1;      //    1 = Pin-Seite, -1 = Clip-Seite
rib_w       = 3;      // U  gemessen    Breite (Dicke) der Rippe
rib_ramp    = 4;      // V  gemessen    wie weit die Rippe an der Schräge übersteht
rib_upper   = 2;      // W  gemessen    wie weit die Rippe am oberen Teil (Clip-Seite) übersteht
rib_fillet  = 15;     //    SCHÄTZUNG   Radius, mit dem die Rippen-Oberkante an der 2. Biegung von V auf W übergeht
rib_fillet1 = 8.5;    //    SCHÄTZUNG   Radius, mit dem die Rippen-Oberkante an der 1. Biegung (Fuß der Schräge) übergeht
rib_mid     = 5.5;    // Z  gemessen    Gesamthöhe der Rippe auf dem geraden Stück am Pin, mittig im Band

/* [Querstreben auf der Rückseite, am Pin-Ende] */
// Zwei quer liegende Stege auf der Rückseite: einer direkt unter dem Pin, einer weiter Richtung Schräge.
struts      = true;   //    Querstreben ein/aus
strut_gap   = 24.6;   // a  angepasst   Abstand Pin-Mitte bis Mitte 2. Querstrebe (gemessen 21,6, nach Probedruck +3)
strut_t     = 3;      // b  gemessen    Dicke einer Querstrebe (in Längsrichtung gemessen)
strut_h     = 2;      // c  gemessen?   wie weit die Querstrebe auf der Rückseite übersteht
strut_len   = 20;     // d  gemessen    Länge der Querstrebe (quer zum Band) = volle Bandbreite

/* [Ausgabe] */
print_on_side = true; // true: Teil liegt auf der Seite (empfohlen, siehe README)
$fn = 48;
arc_steps = 12;       // Segmente pro Biegung

// ---------------------------------------------------------------------------
// Abgeleitete Größen (Mittellinie des Bandes)
a   = ramp_angle;
R1  = (ramp_run - rise / tan(a)) / (2 * tan(a/2));   // Mittellinienradius Kröpfung aus E, F, G
R3  = hook_ri + t/2;               // Mittellinienradius Haken
bend_ri = R1 - t/2;
L_ramp  = (rise - 2*R1*(1 - cos(a))) / sin(a);
hook_rib = (rib && rib_side > 0) ? rib_upper : 0;   // Rippe liegt außen am Haken
L_band  = L_total - hook_rib;                        // Außenseite Band am Haken
L_upper = L_band - L_lower - ramp_run - R3 - t/2;
L_hook  = hook_depth - t/2 - R3;

assert(bend_ri > 0, "F (ramp_run) zu kurz für E (rise) und G (ramp_angle)");
assert(L_ramp  > 0, "F (ramp_run) zu lang für E (rise) und G (ramp_angle)");
assert(L_upper > 0, "C (L_total) zu klein für die übrigen Maße");
assert(L_hook  > 0, "H (hook_depth) zu klein");
assert(pin_head_d > pin_d, "L (Kopf) muss dicker sein als K (Stiel)");
assert(rib_mid > t, "Z (rib_mid) muss größer als die Banddicke A sein");

// Pfad als Turtle-Befehle: ["line", Länge] | ["arc", Radius, Winkel(+ = nach oben)]
path = [
    ["line", L_lower - pin_x],
    ["arc",  R1,  a],
    ["line", L_ramp],
    ["arc",  R1, -a],
    ["line", L_upper],
    ["arc",  R3, -hook_angle],
    ["line", L_hook]
];

// Turtle -> Liste von [x, z, Richtung, Segmentindex]; Geraden in ~1-mm-Stücken (für die Rippe)
function step_pts(p, c, i) =
    c[0] == "line"
      ? let(n = max(1, ceil(c[1] / 1)))
        [for (k = [1:n]) [p[0] + k*c[1]/n*cos(p[2]), p[1] + k*c[1]/n*sin(p[2]), p[2], i]]
      : [for (k = [1:arc_steps]) let(
            da = c[2]/arc_steps,
            pk = arc_pos(p, c[1], da, k))   // Position nach k Sehnenschritten
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

start = [pin_x, t/2, 0, 0];     // Band beginnt am Pin; davor sitzt die Halbkreis-Rundung
pts = concat([start], walk(path, start));

// Bogenlänge ab Pin für jeden Punkt, und Umrechnung x-Position -> Bogenlänge (vor dem Haken)
function cum(i) = i == 0 ? 0 : cum(i-1) + norm([pts[i][0] - pts[i-1][0], pts[i][1] - pts[i-1][1]]);
S = [for (i = [0:len(pts)-1]) cum(i)];
x_to_s = [for (i = [0:len(pts)-1]) if (pts[i][3] <= 4) [pts[i][0], S[i]]];

// Rippe: Überstand über der Bandoberfläche je Pfadpunkt
// 1. Biegung (Fuß der Schräge): hier wandert die Rippe von "mittig" auf die Pin-Seite
b1_s0 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 0) S[i]]);
b1_s1 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 1) S[i]]);
// An der 2. Biegung: Rippen-Oberkante der Schräge (V) und des oberen Teils (W) mit einem
// Bogen verbinden, damit weder Buckel noch Delle entstehen.
i_b2 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 2) i]);   // Ende Schräge = Anfang 2. Biegung
Q0  = [pts[i_b2][0], pts[i_b2][1]];
d1  = [cos(a), sin(a)];                    // Richtung Schräge
n1  = [-sin(a), cos(a)];                   // Normale Schräge (Pin-Seite)
zc_up = rise + t/2;                        // Mittellinie oberer Teil
Zh  = zc_up + t/2 + rib_upper;             // Rippen-Oberkante oberer Teil
P1  = Q0 + n1 * (t/2 + rib_ramp);          // Punkt auf der Rippen-Oberkante der Schräge
u_c = (Zh - P1[1]) / sin(a);
K   = P1 + u_c * d1;                       // Schnittpunkt der beiden Oberkanten
tl  = rib_fillet * tan(a/2);
T1  = K - tl * d1;                         // Bogen beginnt
T2  = K + [tl, 0];                         // Bogen endet
Cf  = T2 - [0, rib_fillet];                // Bogenmittelpunkt

function clamp01(v) = min(1, max(0, v));
function smooth(v) = let(x = clamp01(v)) x * x * (3 - 2 * x);   // weicher Übergang ohne Knick
function cross2(p, q) = p[0] * q[1] - p[1] * q[0];

// Abstand von der Mittellinie (Punkt i, entlang der Normalen) bis zur Rippen-Oberkante
// Schräge -> Bogen -> oberer Teil. Der Strahl trifft genau eines der drei Stücke.
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

// Ober-/Unterkante relativ zur Band-Mittellinie (+ = Pin-Seite)
// 1. Biegung (Fuß der Schräge): Rippen-Oberkante des geraden Stücks (mittig, rib_mid/2 über der
// Mittellinie) und der Schräge (V) mit einem nach innen gewölbten Bogen verbinden – wie an der 2. Biegung.
i_b1 = max([for (i = [0:len(pts)-1]) if (pts[i][3] == 1) i]);   // Ende 1. Biegung = Anfang Schräge
Za   = t/2 + rib_mid/2;                                       // Rippen-Oberkante gerades Stück
P1b  = [pts[i_b1][0], pts[i_b1][1]] + n1 * (t/2 + rib_ramp);    // Punkt auf Rippen-Oberkante der Schräge
u_k1 = (Za - P1b[1]) / sin(a);
K1   = P1b + u_k1 * d1;                                       // Knick zwischen den beiden Oberkanten
tg   = rib_fillet1 * tan(a/2);
TA   = K1 - [tg, 0];                                          // Bogen beginnt (gerades Stück)
TB   = K1 + tg * d1;                                          // Bogen endet (Schräge)
Cg   = TA + [0, rib_fillet1];                                 // Bogenmittelpunkt (oberhalb)
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
// Unterseite: Die Rippe ist bis zur Mitte der Schräge ein durchgehender Steg mit konstanter Höhe
// rib_mid. Er wandert in der 1. Biegung nach oben und geht dabei einfach durchs Band hindurch;
// an der Schräge liegt seine Unterkante im Band (unsichtbar). Danach endet sie in der Mitte des Bandes.
function rib_bot(i) =
    pts[i][3] <= 1 || (pts[i][3] == 2 && i <= i_ramp_mid) ? min(rib_top(i) - rib_mid, 0) : 0;
function rib_edges(i) =
    rib_side > 0 ? [rib_top(i), rib_bot(i)] : [-rib_bot(i), -rib_top(i)];

// ---------------------------------------------------------------------------
// Querschnitt als abgerundetes Rechteck in lokalen Koordinaten [u = Normale, v = Breite],
// gegen den Uhrzeigersinn, immer gleich viele Punkte (damit die Ringe zusammenpassen)
corner_steps = 4;
function rrect(sw, st, du = 0) =
    let(r = min(corner_r, st/2 - 0.01, sw/2 - 0.01),
        cu = st/2 - r, cv = sw/2 - r,
        c = [[cu, cv, 0], [-cu, cv, 90], [-cu, -cv, 180], [cu, -cv, 270]])
    [for (q = c) for (k = [0:corner_steps])
        let(th = q[2] + 90 * k / corner_steps) [du + q[0] + r * cos(th), q[1] + r * sin(th)]];

// Querschnitt an Pfadpunkt q in Weltkoordinaten
function ring(q, sec) = [for (p = sec) [q[0] - sin(q[2]) * p[0], p[1], q[1] + cos(q[2]) * p[0]]];

// Ein geschlossenes Netz entlang des Pfads (statt vieler hull()-Stücke -> sauber manifold)
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
    // Halbkreis-Ende um den Pin: exakt derselbe Querschnitt wie das Band (halbe Breite als Radius).
    // Es greift je 5° ins Band hinein, damit sich beide Teile überlappen statt nur zu berühren.
    half = [for (p = rrect(w, t)) if (p[1] >= 0) [p[1], p[0]]];   // [Radius, Höhe]
    // 0,001 mm flacher als das Band, damit Ober-/Unterseite nicht exakt aufeinanderliegen (sonst non-manifold)
    translate([pin_x, 0, t/2]) scale([1, 1, 1 - 0.002 / t]) rotate([0, 0, 85]) rotate_extrude(angle = 190, $fn = 96)
        polygon(concat([[0, half[0][1]]], half, [[0, half[len(half)-1][1]]]));
    // Anschlagblock an der Hakenspitze: volle Breite, außen so hoch wie die Rippe.
    // Winzige Abstände (0,001 mm) bzw. 0,3 mm Einbettung verhindern exakt aufeinanderliegende Flächen.
    if (hook_stop > 0) {
        tip = pts[len(pts)-1];
        back = [tip[0] - hook_stop * cos(tip[2]), tip[1] - hook_stop * sin(tip[2]), tip[2]];
        end  = [tip[0] - 0.001 * cos(tip[2]), tip[1] - 0.001 * sin(tip[2]), tip[2]];
        outer = t/2 + ((rib && rib_side > 0) ? rib_upper : 0) + 0.001;
        inner = -t/2 + 0.3;
        sec = rrect(w - 0.002, outer - inner, (outer + inner) / 2);
        sweep_mesh([sec, sec], [back, end]);
    }
    // Rippe auf der Rückseite läuft vom Pin bis ganz ans runde Ende. Gleicher Querschnitt wie die
    // Rippe (unten rib_mid/2), oben 0,3 mm ins Band eingebettet; 0,001 mm kleiner, damit sich die
    // Flächen mit der Hauptrippe nicht exakt decken (sonst non-manifold). Folgt der Rundung am Ende.
    if (rib && rib_side > 0) {
        u_b = -rib_mid/2 + 0.001;
        u_t = -t/2 + 0.3;
        intersection() {
            sweep_mesh([for (k = [0:1]) rrect(rib_w - 0.002, u_t - u_b, (u_t + u_b) / 2)],
                       [[0, t/2, 0], [pin_x + 1, t/2, 0]]);
            translate([pin_x, 0, -rib_mid]) cylinder(r = w/2 - 0.01, h = 2 * rib_mid, $fn = 96);
        }
    }
    // Rippe endet innerhalb des Anschlagblocks
    rib_n = hook_stop > 0 ? max([for (i = [0:len(pts)-1]) if (S[i] <= S[len(S)-1] - hook_stop + 1) i]) : len(pts) - 1;
    if (rib)
        sweep_mesh([for (i = [0:rib_n]) let(e = rib_edges(i))
                        rrect(rib_w, e[0] - e[1], (e[0] + e[1]) / 2)], [for (i = [0:rib_n]) pts[i]]);
}

module back_struts() {
    // Unterkante des Bandes am Pin-Ende liegt auf z = 0, Oberseite auf z = t
    intersection() {
        for (x = [pin_x, pin_x + strut_gap])
            translate([x - strut_t/2, -strut_len/2, rib_side > 0 ? -strut_h : t/2])
                cube([strut_t, strut_len, t/2 + strut_h]);
        // nicht über die Rundung am Pin-Ende hinaus
        union() {
            translate([pin_x, 0, -50]) cylinder(r = w/2, h = 100);
            translate([pin_x, -w/2, -50]) cube([L_total, w, 100]);
        }
    }
}

module mushroom_pin() {
    rr = min(pin_head_h, pin_head_d) / 2;     // Randrundung = halbe Kopfhöhe -> oben und unten voll rund
    translate([pin_x, 0, t - 0.01]) {
        // Schaft (reicht bis in die Kopfmitte, damit sich Schaft und Kopf überlappen) mit Hohlkehle am Fuß
        cylinder(d = pin_d, h = pin_neck + pin_head_h / 2);
        cylinder(d1 = pin_d + 2, d2 = pin_d, h = 1);
        // Kopf: Scheibe mit voll abgerundetem Rand
        translate([0, 0, pin_neck])
            rotate_extrude($fn = 64)
                hull() {
                    square([0.01, pin_head_h]);
                    translate([pin_head_d/2 - rr, pin_head_h/2]) circle(r = rr, $fn = 32);
                }
    }
}

// oberer Schenkel: Unterseite liegt auf z = rise
upper_bottom_z = rise;
clip_cx = L_total - clip_x;
assert(clip_tip + clip_base + clip_fins * clip_pitch <= clip_len, "Lamellen passen nicht auf die Clip-Länge P");

module rounded_square_plate(h) {
    r = min(clip_fin_r, clip_fin_sz/2 - 0.01);
    linear_extrude(h) offset(r = r) square(clip_fin_sz - 2*r, center = true);
}

module plus_clip() {
    // lokal: z = 0 an der Band-Unterseite, +z zeigt zur Clip-Spitze
    L      = clip_len;
    neck   = L - clip_tip;
    base_z = clip_at_tip ? neck - clip_base : 0;
    // gleiche Luft (clip_pitch - clip_fin_t) zwischen Block und 1. Lamelle wie zwischen den Lamellen
    fin_z  = [for (k = [1:clip_fins])
                 clip_at_tip ? base_z - k * clip_pitch
                             : clip_base + k * clip_pitch - clip_fin_t];
    translate([clip_cx, 0, upper_bottom_z + 0.01]) mirror([0, 0, 1]) {
        for (a = [0, 90]) rotate([0, 0, a])
            translate([-clip_plus/2, -clip_arm/2, 0]) cube([clip_plus, clip_arm, neck + 0.01]);
        // stumpfe Spitze: die Plus-Stege laufen auf clip_tip_w zusammen
        for (a = [0, 90]) rotate([0, 0, a])
            translate([0, 0, neck])
                linear_extrude(clip_tip, scale = [clip_tip_w / clip_plus, 1])
                    square([clip_plus, clip_arm], center = true);
        translate([0, 0, base_z]) rounded_square_plate(clip_base);
        for (z = fin_z) translate([0, 0, z]) rounded_square_plate(clip_fin_t);
    }
}

module clip_boss() {
    // flache Kuppel (Kugelkappe) auf der Pin-Seite über dem Clip, läuft zum Rand hin aus
    rs = (pow(clip_boss_d/2, 2) + pow(clip_boss_h, 2)) / (2 * clip_boss_h);
    translate([clip_cx, 0, upper_bottom_z + t])
        intersection() {
            translate([0, 0, clip_boss_h - rs]) sphere(r = rs, $fn = 96);
            translate([0, 0, -0.3]) cylinder(d = clip_boss_d + 1, h = clip_boss_h + 0.3);   // 0,3 mm ins Band
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
    // Seitenfläche aufs Bett: Biegungen liegen in der Schichtebene
    translate([0, 0, w/2]) rotate([90, 0, 0]) bracket();
else
    bracket();

echo(str("Kröpfung Innenradius=", bend_ri, "  Rampe=", L_ramp, "  oberer Schenkel=", L_upper, "  Haken=", L_hook));
