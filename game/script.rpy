define liza = Character(_("Ліза"))
define poli = Character(_("Поліанна"))
define tele = Character(_"Телефон")
transform pos_liza:
    zoom 0.3
    ypos 150
    xalign 0.05

transform pos_poli:
    zoom 0.3
    ypos 25
    xalign 0.95


label start:
    jump day1
