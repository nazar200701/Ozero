define grip_size = 75
define puzzle_field_size = 1100
define puzzle_field_offset = 60
define puzzle_piece_size = 450
define active_area_size = puzzle_piece_size - (grip_size * 2)

define liza = Character("Ліза")
define polianna = Character("Поліанна")



image bg_ozero_night = "ozero_night.png"
image bg_ozero_day = "ozero_day.png"
image bg_forest_day = "forest_day.png"
image bg_forest_night = "forest_night.png"
image bg_water_day = "BG/water_day.png"
image bg_water_night = "water_night.png"



label start:

    scene bg2
    show bg2
    $ persistent.coll3_unlocked = True

    play music "1.mp3"

    show gg at left    
    gg "Ох він й сволота."
    
    gg "Як я його терплю."
    
    gg "Знову з якоюсь хвойдою шляється й припинив це ховати від мене..."
    #"(Пауза)"
    gg "А вона?!"

    gg "Як вона може гуляти з чужим хлопцем, ще й так його обіймати."

    
    show Ukralke at right
    gg "..."

    Ukralke "Нормально, не забилась!"
    Ukralke "Дякую за допомогу!"

    gg "Але я нічого не зробила..."

    Ukralke "Так це важко було не помітити"
    gg "..."
    Ukralke "Миленька, я бачу у тебе проблеми з кимось?"
    Ukralke "Через це забігла аж сюди?"
    #"пауза"
    Ukralke "До мене."
    Ukralke "На озеро."
    gg "Я... я не хотіла тебе турбувати"
    #"(пауза)"

    show Ukralke at center
    with moveinleft
    ## !!! РУХ ПЛАВНО, ДУЖЕ ПЛАВНО, МАЄ БУТИ ПЛАВНО!!! ПОТИПУ ПОВІЛЬНО
    ## о цей з низу те що нам треба КРИЛОКОТЕ КАЖУ ТЕ ЩО ЗНИЗУ В КОМЕНТАХ НАМ І ТРЕБА
    
    ##  MoveTransition(delay, *, enter=None, leave=None, old=False, layers=['master'], time_warp=_warper.linear, enter_time_warp=_warper.linear, leave_time_warp=_warper.linear)
    Ukralke "Така мила, беззахисна."
    #"(пауза)"
    Ukralke "Сумна й стурбована."
    gg "..."

    Ukralke "Не бійся."
    Ukralke "Тобі миленька, треба зробити  вибір"
    #"(пауза)"
    Ukralke "I все"
    gg "{font=Aptos-Italic.ttf}Вона мене лякає{/font}"
    gg "{font=Aptos-Italic.ttf}Не можу рухатись. Холод, що віє від неї не дає мені і кроку ступити.{/font}"
    gg "{font=Aptos-Italic.ttf}Ні, не підходь, будь ласка... {/font}"
    
    Ukralke "Полин чи петрушка?"
    
    gg "Щ... що?"
    #"(пауза)"
    Ukralke "ПОЛИН чи петрушка?!"

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
            jump pol_gg_want_to_die
        "Закохуємося, але боїмося":
            jump pol_fear 
# вибори полину
label pol_live_long_life:
    "Закохуємося, живимо довго"
    return
label pol_gg_want_to_die:
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

label no_water_ending:
    gg "Ні... Я не хочу!"
    gg "Я не піду!"

label yes_water_ending:
    gg "Він ніколи мене не покине... Він залишиться зі мною назавжди..."
    gg "..."
    gg "Страшно..."
