
screen sc_vorona_ozero_day:
    button:
        style "empty"
        xfill True
        yfill True
        action Jump("day2Petr_2")
    imagebutton:
        focus_mask True
        idle "images/vorona/voron_ozero_day.png"
        action [ToggleScreen("sc_vorona_ozero_day"), Jump("L_vorona_ozero_day")]



label L_vorona_ozero_day:
    scene ozero_day
    $ vorona1 = True
    $ persistent.coll5_unlocked = True
    show coll5_kvitka
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide coll5_kvitka
    with dissolve
    jump day2Petr_2
