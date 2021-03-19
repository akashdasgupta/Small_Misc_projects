// units in mm
// Tape holder for Emil
$fn = 40;

post_diameter_nominal = 22;
post_height = 150;

platexy = 50;
plate_diameter = 100;
plate_t = 8;

module body()
{
    union()
    {
        cylinder(d=post_diameter_nominal, h=post_height);
        cylinder(d=plate_diameter, h=plate_t);
    }
}

body();