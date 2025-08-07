label day1:
    scene water_night
    # $ persistent.coll3_unlocked = True
    # play music "1.mp3"

    show liza_1 at left
    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"
    liza "Знову десь шляється з черговою шльондрою…"
    liza "І цього разу навіть не приховує її! І жодного сорому, жодного… "
    #"(пауза)"
    liza "А вона?! Як у НЕЇ совісті вистачає гуляти з чужим хлопцем і так його обіймати!"
    #"(пауза)"
    show liza_2 at left

    liza "Як вона може гуляти з чужим хлопцем, ще й так його обіймати."

    show liza_3 at left
    show poli_1 at right

    poli "Ой блять!"
    liza "..."

    poli "Нормально, не забилась!"
    poli "Дякую за допомогу!"

    liza "Але я нічого не зробила..."

    poli "Так це важко було не помітити"
    liza "..."
    poli "Миленька, я бачу у тебе проблеми з кимось?"
    poli "Через це забігла аж сюди?"
    #(пауза)
    poli "До мене."
    poli "На озеро."
    liza "Я... я не хотіла тебе турбувати"
    #"(пауза)"

    show poli_1 at center
    with moveinleft
    ## !!! РУХ ПЛАВНО, ДУЖЕ ПЛАВНО, МАЄ БУТИ ПЛАВНО!!! ПОТИПУ ПОВІЛЬНО
    ## о цей з низу те що нам треба КРИЛОКОТЕ КАЖУ ТЕ ЩО ЗНИЗУ В КОМЕНТАХ НАМ І ТРЕБА

    ##  MoveTransition(delay, *, enter=None, leave=None, old=False, layers=['master'], time_warp=_warper.linear, enter_time_warp=_warper.linear, leave_time_warp=_warper.linear)
    poli "Така мила, беззахисна."
    #"(пауза)"
    poli "Сумна й стурбована."
    liza "..."

    poli "Не бійся."
    poli "Тобі миленька, треба зробити  вибір"
    #"(пауза)"
    poli "I все"
    liza "{font=Aptos-Italic.ttf}Вона мене лякає{/font}"
    liza "{font=Aptos-Italic.ttf}Не можу рухатись. Холод, що віє від неї не дає мені і кроку ступити.{/font}"
    liza "{font=Aptos-Italic.ttf}Ні, не підходь, будь ласка... {/font}"

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
            jump pazzle1
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

# перший вибір
label polyn:
    "Молодець"
    menu:
        "Закохуємося, живимо довго":
            jump pol_live_long_life
        "Я втоплюся":
            jump pol_liza_want_to_die
        "Закохуємося, але боїмося":
            jump pol_fear
# вибори полину
label pol_live_long_life:
    "Закохуємося, живимо довго"
    return
label pol_liza_want_to_die:
    "Я втоплюся"
    return
# страх
label pol_fear:
    menu:
        "Втікти":
            jump pol_fear_run
        "Вбити":
            jump pol_fear_kill
label pol_fear_run:
    "ти втікла"
    return
label pol_fear_kill:
    "ти вбила русалку"
    return

# вибори петрушки
label Petrushka:
    "Гам гам"
    menu:
        "Закохуємося, хочемо померти":
            jump pet_happy_die
        "Закохуємося, не хочемо померти":
            jump pet_sad_die

label pet_happy_die:
    "Закохуємося, хочемо померти"
    "Помираємо"
    return
label pet_sad_die:
    "Закохуємося, не хочемо померти"
    "Помираємо"
    return
