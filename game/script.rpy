define grip_size = 75
define puzzle_field_size = 1100
define puzzle_field_offset = 60
define puzzle_piece_size = 450
define active_area_size = puzzle_piece_size - (grip_size * 2)

define liza = Character("Ліза")
define polianna = Character("Поліанна")



image bg_ozero_night = "BG/ozero_night.png"
image bg_ozero_day = "BG/ozero_day.png"
image bg_forest_day = "BG/forest_day.png"
image bg_forest_night = "BG/forest_night.png"
image bg_water_day = "BG/water_day.png"
image bg_water_night = "BG/water_night.png"



label start:

    scene bg2
    show bg2
    $ persistent.coll3_unlocked = True

    play music "1.mp3"

    show liza at left    
    liza "Яка ж він сволота. В мене вже немає сил терпіти ці знущання…"
    
    liza "Знову десь шляється з черговою шльондрою…
"
    
    liza "І цього разу навіть не приховує її! І жодного сорому, жодного… "
    #"(Пауза)"
    liza "А вона?!"
    show Liza_2
    liza "Як вона може гуляти з чужим хлопцем, ще й так його обіймати."

    
    show polianna at right
    liza "..."

    polianna "Нормально, не забилась!"
    polianna "Дякую за допомогу!"

    liza "Але я нічого не зробила..."

    polianna "Так це важко було не помітити"
    liza "..."
    polianna "Миленька, я бачу у тебе проблеми з кимось?"
    polianna "Через це забігла аж сюди?"
    #"пауза"
    polianna "До мене."
    polianna "На озеро."
    liza "Я... я не хотіла тебе турбувати"
    #"(пауза)"

    show polianna at center
    with moveinleft
    ## !!! РУХ ПЛАВНО, ДУЖЕ ПЛАВНО, МАЄ БУТИ ПЛАВНО!!! ПОТИПУ ПОВІЛЬНО
    ## о цей з низу те що нам треба КРИЛОКОТЕ КАЖУ ТЕ ЩО ЗНИЗУ В КОМЕНТАХ НАМ І ТРЕБА
    
    ##  MoveTransition(delay, *, enter=None, leave=None, old=False, layers=['master'], time_warp=_warper.linear, enter_time_warp=_warper.linear, leave_time_warp=_warper.linear)
    polianna "Така мила, беззахисна."
    #"(пауза)"
    polianna "Сумна й стурбована."
    liza "..."

    polianna "Не бійся."
    polianna "Тобі миленька, треба зробити  вибір"
    #"(пауза)"
    polianna "I все"
    liza "{font=Aptos-Italic.ttf}Вона мене лякає{/font}"
    liza "{font=Aptos-Italic.ttf}Не можу рухатись. Холод, що віє від неї не дає мені і кроку ступити.{/font}"
    liza "{font=Aptos-Italic.ttf}Ні, не підходь, будь ласка... {/font}"
    
    polianna "Полин чи петрушка?"
    
    liza "Щ... що?"
    #"(пауза)"
    polianna "ПОЛИН чи петрушка?!"

#    $ persistent.1_unlocked = True
#    $ persistent.2_unlocked = True
#    $ persistent.3_unlocked = True
#    $ persistent.4_unlocked = True
#    $ persistent.5_unlocked = True
#    $ persistent.6_unlocked = True
#    $ persistent.7_unlocked = True
#    $ persistent.8_unlocked = True
#    $ persistent.9_unlocked = True
    
    jump Petrushka
    
    menu:
        "Полин":
            jump pazzle1
        "Петрушка":
            jump Petrushka
        
label pazzle1:
    scene bg_water_day
    centered "Подивимося що тут...{nw}"
    $ grid_width = 8
    $ grid_height = 5
    $ chosen_img = "puzzle/puzzle1.png"
    call puzzle from _call_puzzle1
    scene bg_forest_day
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

