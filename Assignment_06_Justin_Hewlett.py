# CS 3430
# Assignment 6
# Justin Hewlett

import Image
import ImageDraw

# Given an image path, image size, matrix of tuples in run-length encoding, and the length of a tile side in pixels,
# generates the image and saves it to the image path.
def draw_tile_ornament(imgpath='', imgsize=(0, 0), ornament=[], tileside=1):
    tile_image = draw_image(ornament, imgsize, tileside)
    tile_image.save(imgpath)

# Processes the matrix and draws the rectangles
def draw_image(ornament, imgsize, tileside):
    tile_image = Image.new('RGB', imgsize, (255, 255, 255))
    draw = ImageDraw.Draw(tile_image)
    
    for row_index, row in enumerate(ornament):
        for col_index, run in enumerate(row):
            for run_index in range(get_length(run)):
                x_pos = tileside * (get_col_pos(row, col_index) + run_index)
                y_pos = tileside * row_index

                upper_left = (x_pos, y_pos)
                lower_right = (x_pos + tileside - 1, y_pos + tileside - 1)

                draw.rectangle([upper_left, lower_right], fill=get_color(run), outline=get_outline(run))
                
    return tile_image

# Given a row and the column index, returns the absolute column position taking into account run length
def get_col_pos(row, col_index):
    total_length = 0
    for run in row[:col_index]:
        total_length += get_length(run)

    return total_length

def get_length(run):
    return run[0]

def get_color(run):
    return run[1]

def get_outline(run):
    return run[2]

r, w, o = (255, 0, 0), (255, 255, 255), (0, 0, 255)
ornament_01 = [
        [(1, r, o), (8, w, o), (1, r, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(4, w, o), (2, r, o), (4, w, o)],
        [(3, w, o), (1, r, o), (2, w, o), (1, r, o), (3, w, o)],
        [(2, w, o), (1, r, o), (4, w, o), (1, r, o), (2, w, o)],
        [(1, w, o), (1, r, o), (6, w, o), (1, r, o), (1, w, o)],
        [(1, r, o), (8, w, o), (1, r, o)],
        ]

