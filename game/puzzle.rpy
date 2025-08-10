define grip_size = 75
define puzzle_field_size = 1100
define puzzle_field_offset = 150
define puzzle_piece_size = 450
define active_area_size = puzzle_piece_size - (grip_size * 2)

init python:

    def piece_dragged(drags, drop):
        if not drop:
            return

        p_x, p_y = drags[0].drag_name.split("-")[0], drags[0].drag_name.split("-")[1]
        t_x, t_y = drop.drag_name.split("-")[0], drop.drag_name.split("-")[1]

        # Додає шматочки головоломки до списку об'єднаних елементів
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)

        if p_x == t_x and p_y == t_y:

            # Обчислює правильну позицію для шматочка
            my_x = int(int(p_x) * active_area_size * x_scale_index) - int(grip_size * x_scale_index) + puzzle_field_offset
            my_y = int(int(p_y) * active_area_size * y_scale_index) - int(grip_size * y_scale_index) + puzzle_field_offset
            drags[0].snap(my_x, my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x), int(p_y)] = True

            # Перевіряє, чи всі шматочки на місці
            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if not placedlist[i, j]:
                        return
            return True
        return

screen jigsaw():
    key "rollback" action [[]]
    key "rollforward" action [[]]

    add im.Scale("puzzle_pieces/_puzzle_field.png", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset)

    draggroup:
        for i in range(grid_width):
            for j in range(grid_height):
                $ name = "%s-%s" % (i, j)
                $ my_x = i * int(active_area_size * x_scale_index) + puzzle_field_offset
                $ my_y = j * int(active_area_size * y_scale_index) + puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("puzzle_pieces/_blank_space.png", int(active_area_size * x_scale_index), int(active_area_size * y_scale_index))
                    draggable False
                    xpos my_x ypos my_y

        for i in range(grid_width):
            for j in range(grid_height):
                $ name = "%s-%s-piece" % (i, j)
                drag:
                    drag_name name
                    child imagelist[i, j]
                    dragged piece_dragged
                    xpos piecelist[i, j][0] ypos piecelist[i, j][1]



label puzzle:
    python:
        img_width, img_height = renpy.image_size(chosen_img)

        if img_width >= img_height and img_width > puzzle_field_size:
            img_scale_down_index = round((1.00 * puzzle_field_size / img_width), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        elif img_height >= img_width and img_height > puzzle_field_size:
            img_scale_down_index = round((1.00 * puzzle_field_size / img_height), 6)
            img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
            img_width = int(img_width * img_scale_down_index)
            img_height = int(img_height * img_scale_down_index)
        else:
            img_to_play = chosen_img

        x_scale_index = round((1.00 * (img_width / grid_width) / active_area_size), 6)
        y_scale_index = round((1.00 * (img_height / grid_height) / active_area_size), 6)

        mainimage = im.Composite(
            (int(img_width + (grip_size * 2) * x_scale_index), int(img_height + (grip_size * 2) * y_scale_index)),
            (int(grip_size * x_scale_index), int(grip_size * y_scale_index)), img_to_play
        )

        top_row = list(range(grid_width))
        bottom_row = list(range(grid_width * (grid_height - 1), grid_width * grid_height))
        left_column = [grid_width * i for i in range(grid_height)]
        right_column = [grid_width * i + (grid_width - 1) for i in range(grid_height)]

        jigsaw_grid = [[9, 9, 9, 9] for _ in range(grid_width * grid_height)]

        for i in range(grid_height):
            for j in range(grid_width):
                if grid_width * i + j not in top_row:
                    jigsaw_grid[grid_width * i + j][0] = 2 if jigsaw_grid[grid_width * (i - 1) + j][2] == 1 else 1
                else:
                    jigsaw_grid[grid_width * i + j][0] = 0

                jigsaw_grid[grid_width * i + j][1] = renpy.random.randint(1, 2) if grid_width * i + j not in right_column else 0
                jigsaw_grid[grid_width * i + j][2] = renpy.random.randint(1, 2) if grid_width * i + j not in bottom_row else 0

                if grid_width * i + j not in left_column:
                    jigsaw_grid[grid_width * i + j][3] = 2 if jigsaw_grid[grid_width * i + j - 1][1] == 1 else 1
                else:
                    jigsaw_grid[grid_width * i + j][3] = 0

        piecelist = {}
        imagelist = {}
        placedlist = {}

        for i in range(grid_width):
            for j in range(grid_height):
                piecelist[i, j] = [int(renpy.random.randint(0, int(config.screen_width * 0.9 - puzzle_field_size)) + puzzle_field_size), int(renpy.random.randint(0, int(config.screen_height * 0.8)))]

                temp_img = im.Crop(mainimage, int(i * active_area_size * x_scale_index), int(j * active_area_size * y_scale_index), int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index))

                imagelist[i, j] = im.Composite(
                    (int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index)),
                    (0, 0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzle_pieces/_00%s.png" % jigsaw_grid[grid_width * j + i][0], 0, 1.0), int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index))),
                    (0, 0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzle_pieces/_00%s.png" % jigsaw_grid[grid_width * j + i][1], 270, 1.0), int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index))),
                    (0, 0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzle_pieces/_00%s.png" % jigsaw_grid[grid_width * j + i][2], 180, 1.0), int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index))),
                    (0, 0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("puzzle_pieces/_00%s.png" % jigsaw_grid[grid_width * j + i][3], 90, 1.0), int(puzzle_piece_size * x_scale_index), int(puzzle_piece_size * y_scale_index)))
                )

                placedlist[i, j] = False

    call screen jigsaw
    jump win

label win:

    show puzzle2 with fade
    "Оуу... "
    pause 5.0
    hide black transperent
    hide puzzle2 with fade
    scene ozero_night
    show poli 2 at pos_poli 
    with dissolve
    show liza 2 at pos_liza
    with dissolve
    jump day1_2

screen control_scr():
    default current_file = 0
    if current_file != 0:
        $ img_width, img_height = renpy.image_size(current_file)
        $ preview_scale = 500.00 / max(img_width, img_height) if max(img_width, img_height) > 500 else 1
        $ preview = im.FactorScale(current_file, preview_scale)
        add preview pos (640, 100)

    python:
        extensions = [".jpg", ".jpeg", ".png"]
        image_files = [fn for fn in renpy.list_files() if not fn.startswith(("_", "gui", "puzzle_pieces")) and any(fn.lower().endswith(ext) for ext in extensions)]
        image_files.sort()

    frame:
        background Frame("puzzle_pieces/_puzzle_field.png", 0, 0)
        xpos 100 ypos 100
