define collectibles_count = 0
# 1 працює справно

screen sc_voron_ozero:
    button:
        style "empty"
        xfill True
        yfill True
        action [ToggleScreen("sc_voron_ozero"),Jump("Petrushka_part2")]
    imagebutton:
        focus_mask True
        idle "images/vorona/voron_ozero.png"
        action [ToggleScreen("sc_voron_ozero"), Jump("L_sc_voron_ozero")]    
label L_sc_voron_ozero:
    scene ozero_night
    
    $ persistent.coll9_unlocked = True
    show in_coll9
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide in_coll9
    with dissolve
    jump Petrushka_part2
# 2
screen sc_vorona_ozero_day:
    button:
        style "empty"
        xfill True
        yfill True
        action [ToggleScreen("sc_vorona_ozero_day"),Jump("day2Petr_2")]
    imagebutton:
        focus_mask True
        idle "images/vorona/voron_ozero_day.png"
        action [ToggleScreen("sc_vorona_ozero_day"), Jump("L_vorona_ozero_day")]
label L_vorona_ozero_day:
    scene ozero_day
    $ persistent.coll5_unlocked = True
    show in_coll5
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide in_coll5
    with dissolve
    jump day2Petr_2
# 3
screen sc_o_ptashka:
    button:
        style "empty"
        xfill True
        yfill True
        action [ToggleScreen("sc_o_ptashka"), Jump("no_water_ending_2")]
    imagebutton:
        focus_mask True
        idle "images/vorona/o_ptashka.png"
        action [ToggleScreen("sc_o_ptashka"), Jump("L_sc_o_ptashka")]    
label L_sc_o_ptashka:
    scene eheeeee_dieeeeeee
    $ persistent.coll1_unlocked = True
    show in_coll1
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide in_coll1
    with dissolve
    jump no_water_ending_2

# 4
screen sc_voron_nad_ozerom:
    button:
        style "empty"
        xfill True
        yfill True
        action [ToggleScreen("sc_voron_nad_ozerom"),Jump("yes_water_ending2")]
    imagebutton:
        focus_mask True
        idle "/images/vorona/voron_nad_ozerom.png"
        action [ToggleScreen("sc_voron_nad_ozerom"), Jump("L_sc_voron_nad_ozerom")]    
label L_sc_voron_nad_ozerom:
    scene water_night_silhouettes
    $ persistent.coll7_unlocked = True
    show in_coll7
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide in_coll7
    with dissolve
    jump yes_water_ending2

screen sc_pazzle:   
    imagebutton:
        focus_mask True
        idle "/images/puzzle/puzzle_button.png"
        action [ToggleScreen("sc_pazzle"), Jump("prePazzle")]
    timer 5.0 action [ToggleScreen("sc_pazzle"),Jump("day1_2")]
label prePazzle:
    poli "Ой, бачу всі колектібелси у тебе є?"
    poli "На пазл!"
    jump pazzle1