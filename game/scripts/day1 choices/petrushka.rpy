label Petrushka:
    scene ozero_night

    show liza 4 at pos_liza
    show poli 3 at pos_poli_cen_to_right_move

    stop music

    liza "Гадаю… Петрушка?"
    pause 1.5

    # play music dialogue_music fadein 1
    play music lake_ambience
    if not persistent.vorona1:
        show voron_ozero with dissolve
        call screen sc_voron_ozero
    else:
        jump Petrushka_part2
label Petrushka_part2:
    hide voron_ozero with dissolve
    show liza 4 at pos_liza
    show poli 3 at pos_poli
    poli "То що в тебе сталося, серденько? Розповіси мені все, та, можливо, я тобі допоможу."
    liza "Хлопець, якого я, напевно, кохаю, зраджує мені з іншими дівчатами."
    pause 1.5
    liza "Спочатку він це приховував, але тепер, мабуть, зрозумів: я все одно не піду від нього, попри все…"
    pause 1.5
    poli "Чого ж ти тоді…"
    hide liza
    hide poli
    show liza 2 at pos_liza
    show poli 4 at pos_poli
    liza "Я старалася! Старалася з усіх сил!"
    liza "Робила все як він скаже! Поводила себе так, як він хотів."
    pause 1.5
    liza "Але мене ніколи не було достатньо..."
    liza "Недостатньо гарна, недостатньо кмітлива, недостатньо смішна, недостатньо…"
    pause 1.5
    liza "Я так втомилась…"
    poli "Ой лишенько… Йди до мене, я тебе обійму, тобі стане краще..."

    scene hug with fade
    play music romantic_keys

    "{italic}Вона така холодна… Цікаво як довго вона тут...{/italic}"
    pause 1.5
    "{italic}З нею так якось… спокійно? Вона неначе сховала мене від зовнішнього світу… Від всіх негараздів та тривожних думок.{/italic}"
    "{italic}Невже… Невже мені подобається? {/italic}"

    poli "Ну, що, стало краще?"

    scene ozero_night
    show liza 5 at pos_liza
    show poli 5 at pos_poli

    stop music fadeout 1
    play sound phone_vibrate
    tele "{cps=0}Брінь-дінь-дінь. Брінь-дінь-дінь.{/cps}"
    liza "…"
    show liza 5 at pos_liza

    play sound phone_vibrate
    tele "{cps=0}Брінь-дінь-дінь. Брінь-дінь-дінь.{/cps}"

    poli "Щось не так?"
    liza "Мені… Мені вже треба бігти додому... Бувай"
    liza "Давай... Давай зустрінемось тут завтра? І чи можу я дізнатись твоє ім'я?"
    poli "Поліанна. Моє ім'я Поліанна." #
    poli "Я чекатиму на тебе…"

    scene forest_night with dissolve
    play music night_ambience volume 7

    "{italic}Щось підказує мені, що я не маю повертатись до Поліанни. Але поряд з нею мені стало так добре… Вона була такою дивною, такою турботливою, такою красивою… {/italic}"
    "{italic}Її темно сині очі, неначе нічне небо. Мене охопило відчуття, що я потонула в них, як тільки вона мене відпустила.{/italic}"
    "{italic}А її волосся здалось мені таким неймовірно м’яким, як би мені хотілося зануритись в нього обличчям і заснути.{/italic}"
    "{italic}А обійми… Холодні, що пробирають до самих кісток, але такі спокійні…{/italic}"
    pause 1.5
    "{italic}Я хочу знову побачитись з нею. Можливо ми навіть станемо подругами…{/italic}"

    jump day2Petr
