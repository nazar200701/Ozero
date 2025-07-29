default persistent.coll1_unlocked = False
default persistent.coll2_unlocked = False
default persistent.coll3_unlocked = False
default persistent.coll4_unlocked = False
default persistent.coll5_unlocked = False
default persistent.coll6_unlocked = False
default persistent.coll7_unlocked = False
default persistent.coll8_unlocked = False
default persistent.coll9_unlocked = False

image im_coll1_tablerki = im.zoom("coll1_tablerki.jpg", zoom 0.5)        
image im_coll2_note = im.zoom("coll2_note.jpg", zoom 0.5)

init python:
    

    gallery = Gallery()

    # --- Налаштування Зображення 1 ---
    gallery.button("tabletki")
    gallery.image("coll1_tablerki") # Зображення, яке буде показано
    gallery.condition("persistent.coll1_unlocked") # Змінна для перевірки
    

    # --- Налаштування Зображення 2 ---
    gallery.button("note")
    gallery.image("coll2_note")
    gallery.condition("persistent.coll2_unlocked")
    

    # --- Налаштування Зображення 3 ---
    gallery.button("godidnik")
    gallery.image("coll3_godidnik") # Перейменовано з "coll3_" для ясності
    gallery.condition("persistent.coll3_unlocked")

    # --- Налаштування Зображення 4 ---
    gallery.button("niz")
    gallery.image("coll4_niz")
    gallery.condition("persistent.coll4_unlocked")

    # --- Налаштування Зображення 5 ---
    gallery.button("kvitka")
    gallery.image("coll5_kvitka")

    gallery.condition("persistent.coll5_unlocked")

    # --- Налаштування Зображення 6 ---
    gallery.button("mirror")
    gallery.image("coll6_mirror")

    gallery.condition("persistent.coll6_unlocked")

    # --- Налаштування Зображення 7 ---
    gallery.button("ochki")
    gallery.image("coll7_ochki")

    gallery.condition("persistent.coll7_unlocked")

    # --- Налаштування Зображення 8 ---
    gallery.button("kartinka") # Використовуємо просту назву
    gallery.image("coll8_kartinka")
    gallery.condition("persistent.coll8_unlocked")

    # --- Налаштування Зображення 9 ---
    gallery.button("telephon")
    gallery.image("coll9_telephon")
    gallery.condition("persistent.coll9_unlocked")


screen album:
    tag menu
    add "p.png"
    
#    image im_coll3_ :
#        "coll3_.jpg"
#        zoom 0.1
#
#   image im_coll4_niz:
#        "coll4_niz.jpg"
#        zoom 0.1
#    image im_coll5_kvitka :
#        "coll5_kvitka.jpg"
#        zoom 0.1
#    image im_coll6_mirror :
#        "coll6_mirror.jpg"
#        zoom 0.1
#    image im_coll7_ochki:
#        "coll7_ochki.jpg"
#        zoom 0.1
#    image im_coll8_kartinka :
#        "coll8_картинка.jpg"
#        zoom 0.1
#    image im_coll9_telephon :
#        "coll9_telephon.jpg"
#        zoom 0.1
#    image im_locked1 :
#        "locked"
#        zoom 0.1

    frame:
        xalign 0.3
        yalign 0.5
        background None
        grid 3 3:

            add gallery.make_button(name="tabletki",image=im_coll1_tablerki, locked=im_locked1)
            add gallery.make_button(name="note",image=im_coll2_note, locked=im_locked1)
            #add gallery.make_button(name="godidnik",image=im_coll3_, locked=im_locked1)
            #add gallery.make_button(name="niz",image=im_coll4_niz, locked=im_locked1)
            #add gallery.make_button(name="kvitka",image=im_coll5_kvitka, locked=im_locked1)
            #add gallery.make_button(name="mirror",image=im_coll6_mirror, locked=im_locked1)
            #add gallery.make_button(name="ochki",image=im_coll7_ochki, locked=im_locked1)
            #add gallery.make_button(name="kartinka",image=im_coll8_kartinka,locked=im_locked1)
            #add gallery.make_button(name="telephon",image= im_coll9_telephon, locked=im_locked1)

            spacing 15
        textbutton "Return" action Return()