image eheeeee_Dieeeeeee = "eheeeee_Dieeeeeee.png"
label day1:
    scene ozero_night
    with dissolve

    pause 1.5

    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"

    play music tense_music fadein 1

    show liza_1 at pos_liza
    liza "Знову десь шляється з черговою шльондрою…" with dissolve
    liza "І цього разу навіть не приховує її! І жодного сорому, жодного… "
    liza "..."
    liza "А вона?! Як у НЕЇ совісті вистачає гуляти з чужим хлопцем і так його обіймати!"
    pause 1.5
    hide liza_1
    show liza_2 at pos_liza

    scene ozero_night

    stop music

    show liza_3 at pos_liza

    play sound branch_creak
    poli "Ой блять!"
    play sound human_impact_on_ground
    liza "..."

    play music dialogue_music fadein 1

    show poli_1 at pos_poli
    with dissolve

    poli "*Хмпф* Вельми вдячна за допомогу!"
    liza "Але ж я нічого не зробила..."
    poli "А то я не помітила..."
    liza "..."
    hide poli_1
    show poli_2 at pos_poli
    poli "Ой, бачу на серці смуток? Невже коханий образив?"
    poli "Що ж скоїлось, що ти забігла так далеко від дому?"
    pause 1.5

    poli "{cps=20}Аж сюди... До мене... На моє озеро...{/cps}"

    liza "Я... Пробач мені, я не хотіла тебе турбувати."
    pause 1.5
    hide poli_2
    # +
    ## /Персонаж Поліанна наближається до ЛІЗА/

    show poli_2 at pos_poli_rig_to_centr_move

    poli "Така красива… Така беззахисна."
    pause 1.5
    poli "Така сумна… Така стурбована."

    liza "..."
    poli "Не бійся мене, мила дівчинко, я ж не така страшна..."
    poli "Відповіси на моє питання, любонько, та й дізнаємося доленьку твою..."

    stop music fadeout 1

    liza "{italic}Вона мене лякає.{/italic}"
    liza "{italic}Не можу рухатись... Чому раптом стало так холодно?.. Це… Це від неї віє холодом, що не дає мені й кроку ступити.{/italic}"
    liza "{italic}Ні… Ні, не підходь до мене! Ні! Ні, будь ласка…{/italic}"
    hide poli_2
    show poli_3 at pos_poli_centr
    poli "Полин чи петрушка?"

    liza "Щ... що?"
    #"(пауза)"
    poli "ПОЛИН чи петрушка?!"
    play music tense_music fadein 1

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
    scene water_day
    centered "Подивимося що тут...{nw}"
    $ grid_width = 8
    $ grid_height = 5
    $ chosen_img = "puzzle/puzzle1.png"
    call puzzle from _call_puzzle1
    scene forest_day
    jump polyn



