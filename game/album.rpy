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
    gallery.button("godinik")
    gallery.image("images/collectibles/coll3_godinik.jpg") # Перейменовано з "coll3_" для ясності
    "ffd"
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


screen album():
    tag menu
    add "gui/game_menu.png"


    frame:

        background None
        grid 3 3:
            xalign 0.5
            yalign 0.5

            add gallery.make_button(name="tabletki",unlocked = "images/collectibles/small/Illustration106 (5).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="note",unlocked = "images/collectibles/small/Illustration106.png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="godinik",unlocked = "images/collectibles/small/Illustration106 (7).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="niz",unlocked = "images/collectibles/small/Illustration106 (8).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="kvitka",unlocked = "images/collectibles/small/Illustration106 (1).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="mirror",unlocked = "images/collectibles/small/Illustration106 (2).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="ochki",unlocked = "images/collectibles/small/Illustration106 (4).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="kartinka",unlocked = "images/collectibles/small/Illustration106 (8).png",locked="images/collectibles/locked.png")
            add gallery.make_button(name="telephon",unlocked = "images/collectibles/small/Illustration106 (6).png",locked="images/collectibles/locked.png")

            spacing 15
        textbutton _("Назад") action Return()
