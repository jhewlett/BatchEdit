# Justin Hewlett
# CS 3430
# Assignment 7
#
# Uses zone matching to determine the similarity of two images
# Assumes that both images are 20x20 black and white bitmaps

import math
import os
import string
import Image

def cosine_similarity(zv1, zv2):
    """
    cosine_similarity(zv1, zv2) -> float
    this function computes the cosine similarity between two vectors zv1 and zv2.
    """
    dotp = sum(map(lambda x, y: x * y, zv1, zv2))
    zmagn1 = math.sqrt(sum([v1*v1 for v1 in zv1]))
    zmagn2 = math.sqrt(sum([v2*v2 for v2 in zv2]))

    return float(dotp)/(zmagn1 * zmagn2)

def zone_vector(imgpath, zone_coords):
    """
    Given the path to a 20x20 image and a tuple of zone coordinates, returns the number of black pixels in each zone
    """
    BLACK = (0, 0, 0)
    image = Image.open(imgpath)
    black_count_list = []

    for zone in zone_coords:
        black_count = 0
        for x in range(get_lower_x(zone), get_upper_x(zone) + 1):
            for y in range(get_lower_y(zone), get_upper_y(zone) + 1):
                if image.getpixel((x, y)) == BLACK:
                    black_count += 1
        black_count_list.append(black_count)

    return black_count_list

def get_lower_x(zone):
    return zone[0]

def get_upper_x(zone):
    return zone[2]

def get_lower_y(zone):
    return zone[1]

def get_upper_y(zone):
    return zone[3]

def build_zone_vector_map(dir, zone_coords):
    """
    Given a directory with 20x20 images named 'A.bmp', 'B.bmp', ... 'Z.bmp' and zone coordinates,
    builds a dictionary mapping the letter to its zone vector
    """
    dict = {}
    for letter in string.uppercase:
        file_name = os.path.join(dir, letter) + ".bmp"
        if os.path.isfile(file_name):
            dict[letter] = zone_vector(file_name, zone_coords)

    return dict

def find_best_zv_char_match(char_zv, zv_map, similarity = cosine_similarity):
    """
    Given a single zone mapping, a zone vector map, and a similarity function (optional), returns the character in the map
    that is most similar to the character in the single zone mapping. The default similarity function is cosine similarity.
    """
    if len(zv_map.items()) == 0:
        return None

    all_matches = find_all_zv_char_matches(char_zv, zv_map, similarity)

    return all_matches[0]

def find_all_zv_char_matches(char_zv, zv_map, similarity = cosine_similarity):
    """
    Given a single zone mapping, a zone vector map, and a similarity function (optional), returns a list of 2-tuples comparing
    that single zone mapping to every zone mapping in the zone mapping vector. The returned list is sorted by similarity in descending
    order. The default similarity function is cosine similarity
    """
    tuple_list = []
    for key, value in zv_map.iteritems():
        sim = similarity(char_zv, value)
        tuple_list.append((key, sim))

    return sorted(tuple_list, key = lambda a: a[1], reverse = True)

zone_coords = ((0, 0, 4, 4),   (5, 0, 9, 4),   (10, 0, 14, 4),   (15, 0, 19, 4),
               (0, 5, 4, 9),   (5, 5, 9, 9),   (10, 5, 14, 9),   (15, 5, 19, 9),
               (0, 10, 4, 14), (5, 10, 9, 14), (10, 10, 14, 14), (15, 10, 19, 14),
               (0, 15, 4, 19), (5, 15, 9, 19), (10, 15, 14, 19), (15, 15, 19, 19))

map1 = build_zone_vector_map('C:\\Users\\Justin\\Desktop\\courR18\\letter_images_courR18', zone_coords)
map2 = build_zone_vector_map('C:\\Users\\Justin\\Desktop\\helvR18\\letter_images_helvR18', zone_coords)

print find_best_zv_char_match(map1['L'], map2)

