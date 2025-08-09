define liza = Character(_("Ліза"))
define poli = Character(_("Поліанна"))
define tele = Character(_("Телефон"))

define persitent.vorona1 = False
define persitent.vorona2 = False
define persitent.vorona3 = False
define persitent.vorona4 = False

define slow_dissolve = Dissolve(3)

label start:
    stop music
    jump day1
