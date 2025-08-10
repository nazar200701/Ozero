define liza = Character(_("Ліза"))
define poli = Character(_("Поліанна"))
define tele = Character(_("Телефон"))

default persistent.vorona1 = False
default persistent.vorona2 = False
default persistent.vorona3 = False
default persistent.vorona4 = False

define slow_dissolve = Dissolve(3)
define slow_fade = Fade(1, .5, 1)

image white = Solid("#ffff")

transform flash_white:
    matrixcolor TintMatrix("#FFFFFF")* BrightnessMatrix(0.0)
    linear 0 matrixcolor TintMatrix("#FFFFFF") * BrightnessMatrix(1.0)
    linear 0.1 matrixcolor TintMatrix("#FFFFFF") * BrightnessMatrix(0.0)

label start:
    stop music
    jump day1
