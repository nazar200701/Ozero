label day2Petr:
    scene forest_day
    # /Музика: Спокійна/
    show liza_6 at pos_liza
    
    liza "{italic}Сподіваюсь Поліанна прийде…{/italic}"
    liza "{italic}Може мені їй щось подарувати?{/italic}"

    scene ozero_day
    show liza_6 at pos_liza
    show Poli_6 at pos_poli
    

    menu:
        "Закохуємося, хочемо померти":
            jump pet_happy_die
        "Закохуємося, не хочемо померти":
            jump pet_sad_die

label day2Polyn:
    "Ця частина не закінчена"
    return