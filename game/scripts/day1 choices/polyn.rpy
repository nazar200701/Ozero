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