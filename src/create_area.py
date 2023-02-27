import random as rd
# creates main area, structures are built on them


def create_area(area):

    for out in range(len(area)):
        for i in range(len(area[0])):
            if area[out][i] == 0:
                area[out][i] = rd.randint(0, 2)

    return area
