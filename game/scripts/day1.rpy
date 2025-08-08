image eheeeee_Dieeeeeee = "eheeeee_Dieeeeeee.png"
label day1:
    scene water_night
    # $ persistent.coll3_unlocked = True
    # play music "1.mp3"
    scene eheeeee_Dieeeeeee
    show o_ptashka
    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"

    show liza_1 at pos_liza
        
    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"
    liza "Знову десь шляється з черговою шльондрою…"
    liza "І цього разу навіть не приховує її! І жодного сорому, жодного… "
    #"(пауза)"
    liza "А вона?! Як у НЕЇ совісті вистачає гуляти з чужим хлопцем і так його обіймати!"
    #"(пауза)"
    show liza_2 at pos_liza

    liza "Як вона може гуляти з чужим хлопцем, ще й так його обіймати."

    show liza_3 at pos_liza
    show poli_1 at pos_poli

    poli "Ой блять!"
    liza "..."
    poli "*Хмпф* Вельми вдячна за допомогу!"
    liza "Але x я нічого не зробила..."
    poli "А то я не помітила..."
    liza "..."
    show poli_2 at pos_poli
    poli "Ой, бачу на серці смуток? Невже коханий образив?"
    poli "Що ж скоїлось, що ти забігла так далеко від дому?"
    pause 1.5
    poli "Аж сюди... До мене... На моє озеро"
    pause 1.5
    liza "Я... Пробач мені, я не хотіла тебе турбувати."
    pause 1.5
    hide poli_2
    # /Персонаж Поліанна наближається до ЛІЗА/
    
    show poli_2 at pos_poli
    with moveinleft

    poli "Така красива… Така беззахисна."
    pause 1.5
    poli "Така сумна… Така стурбована."
    
    liza "..."
    poli "Не бійся мене, мила дівчинко, я ж не така страшна..."
    poli "Відповіси на моє питання, любонько, та й дізнаємося доленьку твою..."

    liza "{italic}Вона мене лякає.{/italic}"
    liza "{italic}Не можу рухатись... Чому раптом стало так холодно?.. Це… Це від неї віє холодом, що не дає мені й кроку ступити.{/italic}"
    liza "{italic}Ні… Ні, не підходь до мене! Ні! Ні, будь ласка…{/italic}"
    hide poli_2
    show poli_3
    poli "Полин чи петрушка?"

    liza "Щ... що?"
    #"(пауза)"
    poli "ПОЛИН чи петрушка?!"

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


