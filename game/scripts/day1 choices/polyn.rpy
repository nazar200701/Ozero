label polyn:
    "Молодець"
    menu:
        "Закохуємося, живимо довго":
            jump pol_live_long_life
        "Іду втоплюся...":
            jump pol_liza_want_to_die
        "Вона мені подобається, але...":
            jump pol_fear
# вибори полину
label pol_live_long_life:
    "Закохуємося, живимо довго"
    return
label pol_liza_want_to_die:
    "У річці..."
    "Глибокій.."
    "... Буль буль ..."
    
    return
# страх
label pol_fear:
    menu:
        "i am scared":
            return
            jump pol_fear_run
        "i am brave":
            return
            jump pol_fear_kill
label pol_fear_run:
    "ти втікла"
    return
label pol_fear_kill:
    "ти вбила русалку"
    return