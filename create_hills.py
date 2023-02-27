from create_area import create_area
import random
import numpy
from assign_location import random_locate


def hill_type_1(area,locx=random_locate()[0], locy=random_locate()[1]):
    # DEFINE REQUIRED VARIABLES
    side_y = 10  # also side y determines how big the structure is and changeable
    limited_increase = 3
    main_list = numpy.zeros((side_y, side_y))
    loop_index = 1
    hold_loop_index = loop_index
    carry_mountain = 0
    carry_sinkhole = 0
    random_is_it_mountain = random.randint(0, 9)

    if random_is_it_mountain == 2:
        main_list[loop_index][loop_index] += -1 * random.randint(0, limited_increase)
    else:
        main_list[loop_index][loop_index] += random.randint(0, limited_increase)

    while loop_index < hold_loop_index + side_y / 2:

        x_number_index = loop_index
        y_number_index = loop_index

        max_num_for_approach_in_loop = side_y - loop_index

        positive = 0
        if loop_index == 1:
            if main_list[loop_index][loop_index] > 0:
                positive = 1
                carry_mountain += 1
        else:
            if main_list[loop_index - 1][loop_index - 1] > 0:
                positive = 1
                carry_mountain += 1
            else:
                carry_sinkhole += 1

        # 4 while loops is a loop index
        if loop_index != 1:
            if positive:
                main_list[loop_index][loop_index] = random.randint(main_list[loop_index - 1][loop_index - 1] - 1,
                                                                   main_list[loop_index - 1][
                                                                       loop_index - 1] + limited_increase)
            elif not positive:
                main_list[loop_index][loop_index] = random.randint(main_list
                                                                   [loop_index - 1][loop_index - 1] - limited_increase,
                                                                   main_list[loop_index - 1][loop_index - 1] + 1)

        while y_number_index - 1 < max_num_for_approach_in_loop:

            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)

            if positive:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k

            y_number_index += 1

        y_number_index -= 1  # can be complicated but it is the best way I thought
        while x_number_index < max_num_for_approach_in_loop - 1:

            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)

            x_number_index += 1

            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k

        while y_number_index > (side_y - max_num_for_approach_in_loop):

            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)

            y_number_index -= 1

            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k

        while x_number_index - 1 > (side_y - max_num_for_approach_in_loop):

            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)

            x_number_index -= 1

            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k

        loop_index += 1

    area[locx:locx + side_y, locy:locy + side_y] += main_list
    print(main_list)
    return area


def hill_type_2(area):

    pass
