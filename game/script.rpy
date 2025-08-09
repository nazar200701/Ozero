define liza = Character(_("Ліза"))
define poli = Character(_("Поліанна"))
define tele = Character("Телефон")
transform pos_liza:
    zoom 0.3
    ypos 150
    xalign 0.05

transform pos_poli:
    zoom 0.3
    ypos 25
    xalign 0.95

transform pos_poli_rig_to_centr_move:
    zoom 0.3
    ypos 25
    xalign 0.95
    ease 1.0 xalign 0.5
transform pos_poli_centr:
    zoom 0.3
    ypos 25
    xalign 0.5
transform pos_poli_cen_to_right_move:
    zoom 0.3
    ypos 25
    xalign 0.5
    ease 1.0 xalign 0.95
label start:
    jump day1
