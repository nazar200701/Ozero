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
    "Твір «Під впливом» є незавершеним.
    Текст містить теми самогубства та аб’юзивних стосунків.
    «Під впливом» є художньою вигадкою і не має на меті пропагувати чи романтизувати завдання моральної або фізичної шкоди собі чи іншим людям.

    Якщо ви переживаєте емоційну кризу, будь ласка, зверніться по допомогу до близьких або спеціалізованих служб.

    Ваше життя має цінність. Ви не самі. Якщо ви переживаєте емоційну кризу, будь ласка, зверніться по допомогу до близьких або спеціалізованих служб.

    Маніпулювати людьми — погано.

    Топити людей — погано.

    Спілкуватися з людьми, які можуть вас утопити — шкідливо для вашого здоров’я.

    Дівчата, які кохають дівчат — добре.{w=10.0}"
    stop music
    jump day1
# page down, page up
# Таємнича дівчина