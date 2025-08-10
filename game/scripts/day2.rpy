label day2Petr:
    stop music fadeout 1
    scene forest_day with slow_fade
    play music forest_ambience fadein 1

    # /Музика: Спокійна/
    # play music dialogue_music fadein 1

    show liza 6 at pos_liza

    "{italic}Сподіваюсь Поліанна прийде…{/italic}"
    "{italic}Може мені їй щось подарувати?{/italic}"

    scene ozero_day with dissolve
    show liza 6 at pos_liza
    with dissolve
    pause 1.5
    show poli 6 at pos_poli
    with dissolve

    poli "Ви тільки-но подивіться хто ж це прийшов!"
    poli "Невже це моє сонечко!"
    pause 1.0
    hide liza
    hide poli
    show liza 7 at pos_liza
    show poli 7 at pos_poli
    "{italic}Поліанна… назвала мене своєю? Сонечко? Це приємно, але якось дивно.{/italic}"
    poli "Хочеш я тобі дещо покажу? Але спочатку заплющ очі, не підглядай…"
    if not vorona1:
        call screen sc_vorona_ozero_day
    else:
        "Значить ворона 1 тру"
        jump day2Petr_2

label day2Petr_2:
    scene ozero_day
    show liza 8 at pos_liza
    show poli 7 at pos_poli
    liza "Так, хочу…"

    show black with fade
    "{italic}Тримай себе в руках, не витріщайся на неї… Не витріщайся!{/italic}"
    hide black with fade

    show poli 7 at pos_poli
    hide liza 8
    show liza 9 at pos_liza
    poli "І цееее… маленька квіточка! Гарна, правда ж?"
    liza "Так, дуже гарна..."
    liza "Це всього лиш квітка..."
    pause 1.5
    poli "Вона красивіша за мене?"
    show liza 9
    show liza 6 at pos_liza
    pause 1.5
    liza "Що? В сенсі?"
    poli "Ця квітка красивіша за мене?"
    liza "Ні-ні, я думаю ти красивіша!"
    poli "Не брешеш? Наскільки я красивіша за цю квітку?"
    pause 1.5
    liza "Я… я не знаю. На дуже?"
    poli "Ахахахаха. На дуже?"
    pause 1.0

    stop music fadeout 1

    poli "Ходи до мене, серденько…"
    hide poli 7
    show poli 8 at pos_poli
    liza "Навіщо?"
    pause 1.5
    poli "Невже ти боїшся мене? Нумо, ходи-но сюди."
    "{italic}Можливо зараз вона…{/italic}"

    scene holds_hands with fade
    play music romantic_keys

    poli "Ти вся зашарілася. Мені подобається, яка ти мила."
    "{italic}Щ-що?{/italic}"
    "{italic}Що вона має на увазі?{/italic}"
    "{italic}Я їй подобаюсь?{/italic}"
    pause 1.5
    liza "Ти мені також…"
    pause 1.5
    poli "Га?"
    liza "…"
    liza "А, ні, нічого. Я просто…"
    poli "Подумала, що ти мені подобаєшся?"
    pause 1.5
    poli "Ахахаха…"
    poli "Моя ти хороша."
    poli "Що ж, я зовсім не проти, якщо це стане правдою."

    scene hand with dissolve
    pause 1.5
    "{italic}Знову цей холод. Я відчуваю як від її дотику поколює шкіру, але… це приємно… Заспокоює…{/italic}"
    "{italic}Мене ніби знову сховали від усіх проблем, я більше не почуваюсь самотньою. Поліанна поруч... поруч зі мною…{/italic}"
    "{italic}І цей біль... він стає дедалі сильнішим...{/italic}"
    stop music
    liza "Ай!"

    scene ozero_day
    play music forest_ambience fadein 1
    show liza 10 at pos_liza
    show poli 9 at pos_poli_cen_to_right_move

    poli "Вибач, я зробила тобі боляче?"
    liza "Ні-ні, все добре, просто..."
    pause 1.5
    liza "Чи зустрінемось ми знову? Можливо завтра?"
    poli "Так, я чекатиму на тебе тут, сонечко."
    hide poli 9
    show poli 10 at pos_poli
    liza "Давай підемо кудись ще? Може погуляємо в місті? Або ж сходимо в парк, якщо ти любиш природу? А давай…."
    hide poli 10
    show poli 11 at pos_poli
    poli "Ні, моя хороша, я не можу йти так далеко."
    liza "Ну, добре тоді... Я обов’язково навідаю тебе завтра!"
    stop music

    #/Показуємо таймскіп/
    #/Сцена з календарем/
    scene calendar with fade
    play music clock_ticking volume 0.5
    # play music dialogue_music fadein 1

    "13 серпня"
    "{italic}Мені здається Поліанна хоче подружитись. Добре до мене ставиться й вислуховує.{/italic}"
    "{italic}Ще, розказала мені про свого птаха, що інколи приносить різні речі. Вона сказала, що птах завжди спостерігає за нами. Це трошки дивно, але доволі мило.{/italic}"
    "{italic}Ще, я їй розказала, що мої батьки часто сваряться, та мені здається, що вони хочуть розлучитися.{/italic}"
    "{italic}…{/italic}"
    "{italic}Мене це лякає.{/italic}"

    "14 серпня"
    "{italic}Поліанна здивувалась коли я розказала, що не вмію плавати. Це її занепокоїло, і вона сказала, що може мене навчити.{/italic}"
    "{italic}Я погодилась й мене повили одразу в озеро, я трошки хвилювалася, бо не хотіла мочити одяг, а ще я інколи заглядаюсь на її тіло... Дивне відчуття.{/italic}"
    "{italic}Під вечір, я подарувала їй маленький кулон в котрий вона може розмістити фотографію.{/italic}"
    "{italic}Було дуже ніяково від сорому, а ще більш ніяково коли Поліанна мене поцілувала в щічку... Гарний день.{/italic}"

    "15 серпня"
    "{italic}Поліанна мене налякала... коли вона продовжила вчити мене плавати, то несподівано почала лоскотати й я пішла під воду, а коли намагалась вибратись, то відчула, що її руки не дають мені виплисти.{/italic}"
    "{italic}Я... я думаю, що більше не хочу з нею дружити... В цей момент, я наче побачила її пташку під водою... Мені більше не хочеться приходити до неї. Поліанна мене лякає...{/italic}"

    # На порозі вибору до фіналу
    stop music
    jump pre_final
label day2Polyn:
    "Ця частина не закінчена"
    return
