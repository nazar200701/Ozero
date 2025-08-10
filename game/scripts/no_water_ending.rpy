label no_water_ending:
    scene water_night
    show liza 12 at pos_liza
    show poli 15 at pos_poli
    with dissolve

    # play music tense_music fadein 1

    liza "Ні... Я не хочу!"
    pause
    liza "Я не піду!"
    hide liza 12
    hide poli 15
    show poli 16 at pos_poli
    show liza 13 at pos_liza
    poli "Так, ти підеш зі мною!"
    poli "Ти МОЯ подруга! Ти маєш МЕНЕ слухати! Мене, мене... І тільки мене!"

    liza "Ти мене лякаєш... Я хочу додому, будь ласка..."

    poli "Стулися! Закрий рота!"
    poli "Ти маєш піти зі мною, зараз! Просто стулися — та йди!"

    liza "НІ! Ти мені не подруга! Ти лише хочеш..."

    # /звук ляпаса/
    show white:
        alpha 0
        ease 0 alpha 1
        ease 0.3 alpha 0
    play sound slap volume 0.8
    pause 0.3

    # /флеш білий, поступово переходить у прозорість/
    show liza_14 at pos_liza
    liza "Щ-що т-ти..."

    "{italic}Вона мене вдарила?..{/italic}"
    "{italic}Щока горить... Мене наче обпекло холодом. Це відчувається... Як вона.{/italic}"
    "{italic}Боляче... Я не хочу плакати перед нею...{/italic}"
    hide poli 12
    show poli 17 at pos_poli
    poli "Ти хочеш мене покинути?! Як всі інші?!"
    "..."
    liza "Я хочу додому... Мені страшно..."

    poli "Цього не буде! Ти нікуди не підеш! Не підеш! Не підеш!"

    # /сцена: Поліанна хапає дівчинку за волосся/
    scene took_by_the_hair

    # /тривожна музика/
    liza "Ай! Відпусти, благаю тебе! Не треба!"
    poli "Ніколи!.. Будеш зі мною... Завжди..."
    liza "Я не хочу! Відпусти мене!"
    liza "Не повернусь! Я тебе більше не потривожу... Просто дай мені піти! Будь ласка!"

    poli "Ти сама це вибрала! З самого початку не могло бути інакше!"
    poli "Ти залишишся тут!"

    # /Вмикаєм музику на фінал/
    play music final_music fadein 1

    "{italic}Що?.. Я не...{/italic}"
    # *тут було б гарно таким напівпрозорим показати фрейм, де гравець обирає петрушку*
    "{italic}Петрушка... Це все через це?.. Вона нічого не пояснила — як я могла зрозуміти?..{/italic}"

    play sound water_splash
    scene nooo_helpp

    poli "Не пручайся… Все буде добре. Ми будемо разом..."
    poli "Я тебе ніколи не покину."

    # /сцена: погляд від обличчя ЛІЗА/
    scene eheeeee_dieeeeeee
    if not vorona3:
        show o_ptashka with dissolve
        call screen sc_o_ptashka
    else:
        "Значить ворона 2 тру"
        jump no_water_ending_2
label no_water_ending_2:
    if not vorona3:
        hide o_ptashka with dissolve
        $ vorona3 = True     
    "{italic}Холодно...{/italic}"
    "{italic}Як я не помічала, до чого все йде?..{/italic}"
    "{italic}Поліанна просто маніпулювала мною, щоб... Щоб що?{/italic}"
    "{italic}Хотіла мене вбити?.. Так чому не зробила це одразу? Просто бавилась зі мною?..{/italic}"
    "{italic}Можливо… Можливо вона також просто не хотіла залишитись сама? Її теж покинули… Тепер вона просто мститься?.. Але чому я?..{/italic}"
    "..."

    # /сцена темряви, музика стихає/
    show black
    with dissolve

    # Зробити музику тихіше
    # play music final_music fadein 1 volume 0.5

    "{italic}Вона ж не людина, так?.. Від неї завжди віяло холодом, як від померлої..{/italic}"
    "{italic}Її довге волосся, що просто лежало на воді тепер тягнеться до мене… Воно огортає мої руки, мої ноги...{italic}"
    "{italic}Не можу... рухатись...{/italic}"
    "{italic}Я... не...{/italic}"

    poli "Ти... лиш... м... я... н... за... ди... на... з-вжд..."

    "{italic}Я так більше не можу...{/italic}"
    "{italic}Біль...{/italic}"
    "{italic}ше...{/italic}"

    window auto False
    window hide

    # /сцена з очима русалки через декілька секунд з прозорості/
    show eyea
    with slow_dissolve

    centered "{size=300}{shader=jitter:u__jitter=5.0, 10.0}Кінець{/shader}{/size}"(what_color=gui.accent_color)
    return
