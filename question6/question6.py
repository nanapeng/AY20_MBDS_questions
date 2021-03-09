# Use loop to treat every edge of the polygon as the same
# check whether there is an intersection with the horizontal ray of point p
# if there is an intersection, the flag is flipped once

def is_in_poly(p, poly):
    """
    check if point is inside polygon
    :param p: [x, y]
    :param poly: [[], [], [], [], ...]
    :return:
    """
    px, py = p
    is_in = False  # flag

    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (x2 - x1) * (py - y1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in


poly_file = "/Users/peng/Desktop/input_question_6_polygon"
point_file = "/Users/peng/Desktop/input_question_6_points"


def read_file_for_points(file_name):
    res = []
    with open(file_name) as f:
        for line in f.readlines():
            if len(line.strip().split(' ')) == 2:
                x, y = line.strip().split(' ')
            res.append([int(x), int(y)])
    return res



poly = read_file_for_points(poly_file)
points = read_file_for_points(point_file)

with open("output_question_6", "w") as f:
    for p in points:
        is_in = is_in_poly(p, poly)
        if is_in:
            result = "inside"
        else:
            result = "outside"
        f.write("%s %s %s\n" % (p[0], p[1], result))
