label polyn:
    play music dialogue_music fadein 1 volume 0.5

    "Молодець"
    "{b}Вибір \"Полин\" є недопрацьованим{/b}"
    menu:
        "Закохуємося, живемо довго":
            jump pol_live_long_life
        "Піду втоплюся...":
            jump pol_liza_want_to_die
        "Вона мені подобається, але...":
            jump pol_fear
        "Вибрати петрушку":
            jump Petrushka
# вибори полину
label pol_live_long_life:
    "І щасливо (?)"
    return
label pol_liza_want_to_die:
    "У річці..."
    "Глибокій..."
    "... Буль буль ..."
    return
# страх
label pol_fear:
    menu:
        "Я налякана":
            jump pol_fear_run
        "Я хоробра":
            jump pol_fear_kill
label pol_fear_run:
    "Ти втікла"
    return
label pol_fear_kill:
    "Ти вбила русалку"
    return
