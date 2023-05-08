import random as rd
# creates main area, structures are built on them


def create_area(area):
    # for the number of nested lists in area
    for out in range(len(area)):
        # for number of elemnts in a list in the area
        for i in range(len(area[0])):
            # create a chaos, don't leave any flat area
            if area[out][i] == 0:
                area[out][i] = rd.randint(0, 2)

    return area
