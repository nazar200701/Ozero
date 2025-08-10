# 1
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
    show "images/collectibles/ingame/coll5.png"
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide "images/collectibles/ingame/coll5.png"
    with dissolve
    jump day2Petr_2
# 2
screen sc_o_ptashka:
    button:
        style "empty"
        xfill True
        yfill True
        action Jump("no_water_ending_2")
    imagebutton:
        focus_mask True
        idle "images/vorona/o_ptashka.png"
        action [ToggleScreen("sc_o_ptashka"), Jump("L_sc_o_ptashka")]    
label L_sc_o_ptashka:
    scene eheeeee_dieeeeeee
    $ vorona2 = True
    $ persistent.coll1_unlocked = True
    show "images/collectibles/ingame/coll1.png"
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide "images/collectibles/ingame/coll1.png"
    with dissolve
    jump no_water_ending_2
# 3
screen sc_voron_ozero:
    button:
        style "empty"
        xfill True
        yfill True
        action Jump("no_water_ending_2")
    imagebutton:
        focus_mask True
        idle "images/vorona/voron_ozero.png"
        action [ToggleScreen("sc_voron_ozero"), Jump("L_sc_o_ptashka")]    
label L_sc_voron_ozero:
    scene eheeeee_dieeeeeee
    $ vorona3 = True
    $ persistent.coll9_unlocked = True
    show "images/collectibles/ingame/coll9.png"
    with dissolve
    "Річ додана до вашого альбому"
    pause 1.5
    hide "images/collectibles/ingame/coll9.png"
    with dissolve
    jump no_water_ending_2
# 4
