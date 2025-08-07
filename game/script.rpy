define grip_size = 75
define puzzle_field_size = 1100
define puzzle_field_offset = 60
define puzzle_piece_size = 450
define active_area_size = puzzle_piece_size - (grip_size * 2)

define liza = Character(_("Ліза"))
define polianna = Character(_("Поліанна"))

image bg_ozero_night = "bg/ozero_night.png"
image bg_ozero_day = "bg/ozero_day.png"
image bg_forest_day = "bg/forest_day.png"
image bg_forest_night = "bg/forest_night.png"
image bg_water_day = "bg/water_day.png"
image bg_water_night = "bg/water_night.png"

label start:
    jump no_water_ending
