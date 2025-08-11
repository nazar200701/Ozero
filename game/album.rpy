init python:

    gallery = Gallery()
    # --- Налаштування Зображення 1 ---
    gallery.button("tabletki")
    gallery.image("images/collectibles/album/coll1.png")
    gallery.condition("persistent.coll1_unlocked")


    # --- Налаштування Зображення 2 ---
    gallery.button("note")
    gallery.image("images/collectibles/album/coll2.png")
    gallery.condition("persistent.coll2_unlocked")


    # --- Налаштування Зображення 3 ---
    gallery.button("godinik")
    gallery.image("images/collectibles/album/coll3.png")
    gallery.condition("persistent.coll3_unlocked")

    # --- Налаштування Зображення 4 ---
    gallery.button("niz")
    gallery.image("images/collectibles/album/coll4.png")
    gallery.condition("persistent.coll4_unlocked")
    # --- Налаштування Зображення 5 ---
    gallery.button("kvitka")
    gallery.image("images/collectibles/album/coll5.png")
    gallery.condition("persistent.coll5_unlocked")

    # --- Налаштування Зображення 6 ---
    gallery.button("mirror")
    gallery.image("images/collectibles/album/coll6.png")
    gallery.condition("persistent.coll6_unlocked")

    # --- Налаштування Зображення 7 ---
    gallery.button("ochki")
    gallery.image("images/collectibles/album/coll7.png")
    gallery.condition("persistent.coll7_unlocked")

    # --- Налаштування Зображення 8 ---
    gallery.button("kartinka") # Використовуємо просту назву
    gallery.image("images/collectibles/album/coll8.png")
    gallery.condition("persistent.coll8_unlocked")

    # --- Налаштування Зображення 9 ---
    gallery.button("telephon")
    gallery.image("images/collectibles/album/coll9.png")
    gallery.condition("persistent.coll9_unlocked")


screen album():
    tag menu
    add "gui/game_menu.png"


    frame:

        background None
        grid 3 3:
            xalign 0.5
            yalign 0.5

            add gallery.make_button(name="tabletki",unlocked = "images/collectibles/small/unlocked/unlocked1.png",locked="images/collectibles/small/locked/locked1.png")
            add gallery.make_button(name="note",unlocked = "images/collectibles/small/unlocked/unlocked2.png",locked="images/collectibles/small/locked/locked2.png")
            add gallery.make_button(name="godinik",unlocked = "images/collectibles/small/unlocked/unlocked3.png",locked="images/collectibles/small/locked/locked3.png")
            add gallery.make_button(name="niz",unlocked = "images/collectibles/small/unlocked/unlocked4.png",locked="images/collectibles/small/locked/locked4.png")
            add gallery.make_button(name="kvitka",unlocked = "images/collectibles/small/unlocked/unlocked5.png",locked="images/collectibles/small/locked/locked5.png")
            add gallery.make_button(name="mirror",unlocked = "images/collectibles/small/unlocked/unlocked6.png",locked="images/collectibles/small/locked/locked6.png")
            add gallery.make_button(name="ochki",unlocked = "images/collectibles/small/unlocked/unlocked7.png",locked="images/collectibles/small/locked/locked7.png")
            add gallery.make_button(name="kartinka",unlocked = "images/collectibles/small/unlocked/unlocked8.png",locked="images/collectibles/small/locked/locked8.png")
            add gallery.make_button(name="telephon",unlocked = "images/collectibles/small/unlocked/unlocked9.png",locked="images/collectibles/small/locked/locked9.png")

            spacing 15
        textbutton _("Повернутися") action Return() xalign 0.05 yalign 0.95
        textbutton _("Скинути") action [lambda: persistent._clear(), Return()] xalign 0.95 yalign 0.95
