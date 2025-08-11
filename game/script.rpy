define liza = Character(_("Ліза"))
define poli = Character(_("Поліанна"))
define tele = Character(_("Телефон"))

define slow_dissolve = Dissolve(3)
define slow_fade = Fade(1, .5, 1)

image white = Solid("#ffff")
image disclaimoor = "images/Disclaimoor.png"
transform flash_white:
    matrixcolor TintMatrix("#FFFFFF")* BrightnessMatrix(0.0)
    linear 0 matrixcolor TintMatrix("#FFFFFF") * BrightnessMatrix(1.0)
    linear 0.1 matrixcolor TintMatrix("#FFFFFF") * BrightnessMatrix(0.0)

label start:
    show disclaimoor at pos (0.5, 0.5)
    pause 10.0
    hide disclaimoor
    stop music
    jump day1
# page down, page up
# Таємнича дівчина