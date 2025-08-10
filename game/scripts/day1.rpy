image eheeeee_Dieeeeeee = "eheeeee_Dieeeeeee.png"


label day1:
    scene ozero_night
    with dissolve

    play music lake_ambience

    pause 1.5

    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"

    # play music tense_music fadein 1

    show liza 1 at pos_liza
    liza "Знову десь шляється з черговою шльондрою…" with dissolve
    liza "І цього разу навіть не приховує її! І жодного сорому, жодного… "
    "..."
    liza "А вона?! Як у НЕЇ совісті вистачає гуляти з чужим хлопцем і так його обіймати!"
    pause 1.5
    hide liza
    show liza 2 at pos_liza

    scene ozero_night

    # stop music

    show liza 3 at pos_liza

    play sound branch_creak
    poli "Ой блять!"
    play sound human_impact_on_ground
    "..."

    # play music dialogue_music fadein 1

    show poli 1 at pos_poli
    with dissolve

    poli "*Хмпф* Вельми вдячна за допомогу!"
    liza "Але ж я нічого не зробила..."
    poli "А то я не помітила..."
    "..."
    hide poli 1
    show poli 2 at pos_poli
    if persistent.collectibles_count == 4:
        call screen sc_pazzle
    else:
        jump day1_2
label day1_2:
    poli "Ой, бачу на серці смуток? Невже коханий образив?"
    poli "Що ж скоїлось, що ти забігла так далеко від дому?"
    pause 1.5
    poli "Аж сюди... "
    extend "До мене... "
    extend "На моє озеро..."

    liza "Я... Пробач мені, я не хотіла тебе турбувати."
    pause 1.5
    hide poli 2
    # +
    ## /Персонаж Поліанна наближається до ЛІЗА/

    show poli 2 at pos_poli_rig_to_centr_move
    play audio ["<silence .5>", dystort] volume 0.2


    poli "Така красива… Така беззахисна."
    pause 1.5
    poli "Така сумна… Така стурбована."

    "..."
    poli "Не бійся мене, мила дівчинко, я ж не така страшна..."
    poli "Відповіси на моє питання, любонько, та й дізнаємося доленьку твою..."

    stop music fadeout 1

    "{italic}Вона мене лякає.{/italic}"
    "{italic}Не можу рухатись... Чому раптом стало так холодно?.. Це… Це від неї віє холодом, що не дає мені й кроку ступити.{/italic}"
    "{italic}Ні… Ні, не підходь до мене! Ні! Ні, будь ласка…{/italic}"
    hide poli 2
    show poli 3 at pos_poli_centr
    poli "Полин чи петрушка?"

    liza "Щ... що?"
    #"(пауза)"
    poli "ПОЛИН чи петрушка?!"
    play music tense_music fadein 1 volume 0.5

#    $ persistent.1_unlocked = True
#    $ persistent.2_unlocked = True
#    $ persistent.3_unlocked = True
#    $ persistent.4_unlocked = True
#    $ persistent.5_unlocked = True
#    $ persistent.6_unlocked = True
#    $ persistent.7_unlocked = True
#    $ persistent.8_unlocked = True
#    $ persistent.9_unlocked = True
    menu:
        "Полин":
            jump polyn
        "Петрушка":
            jump Petrushka

label pazzle1:
    scene ozero_night
    show black transperent
    centered "Пазли в лісі?{nw}"
    $ grid_width = 8
    $ grid_height = 5
    $ chosen_img = "puzzle/puzzle1.png"
    call puzzle from _call_puzzle1
    scene ozero_night
    jump day1_2



