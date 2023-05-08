import random
from assign_location import random_locate
import numpy


# normal mountain
def mountain_rising(area, size, locx=random_locate()[0], locy=random_locate()[1]):
    # DEFINE REQUIRED VARIABLES
    # also side y determines how big the structure is and changeable
    side_y = 30  
    # max rise of mountain in every step, it is random and this is max
    limited_increase = 3
    # assign mountain area
    main_list = numpy.zeros((30,30))
    # assign the index which will be used in loop
    loop_index = 1
    # hold the index
    hold_loop_index = loop_index
    # determine if it is a sinkhole or mountain
    carry_mountain = 0
    carry_sinkhole = 0
    # a random variable to randomly decide if main mountain is mountain or a sinkhole
    random_is_it_mountain = random.randint(0, 9)
    # randomly decide if random var. is 2, make it a sinkhole. Unless make it a mountain
    if random_is_it_mountain == 2:
        main_list[loop_index][loop_index] = -1 * random.randint(0, limited_increase)
    else:
        main_list[loop_index][loop_index] = random.randint(0, limited_increase)
    
    # start main loop looping
    while loop_index < hold_loop_index + side_y/2:
        # assign x,y indexes
        x_number_index = loop_index
        y_number_index = loop_index
        # define max num for structure
        max_num_for_approach_in_loop = side_y - loop_index

        positive = 0
        # understand if it is a mountain or a sinkhole
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

        # assign corners of structure to be used further
        if loop_index != 1:
            if positive:
                main_list[loop_index][loop_index] = random.randint(main_list[loop_index - 1][loop_index - 1] - 1,
                                                                   main_list[loop_index - 1][
                                                                       loop_index - 1] + limited_increase)
            elif not positive:
                main_list[loop_index][loop_index] = random.randint(main_list
                                                                   [loop_index - 1][loop_index - 1] - limited_increase,
                                                                   main_list[loop_index - 1][loop_index - 1] + 1)
        # go up ^ while end point is not reached
        while y_number_index - 1 < max_num_for_approach_in_loop:
            # define random rise or decline of mountain by checking corners
            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)
            # check if a sinkhole or a mountain is being created
            if positive:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k
            # go up
            y_number_index += 1

        y_number_index -= 1  # can be complicated but it is the best way I thought
        
        # go right ---> while end point is not reached
        while x_number_index < max_num_for_approach_in_loop - 1:
            # define random rise or decline of mountain by checking corners
            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)
            # increase x index by one before starting to go right
            x_number_index += 1
            # action checking if a mountain or a sinkhole is created
            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k
                
        # go down v while end point is not reached
        while y_number_index > (side_y - max_num_for_approach_in_loop):
            # define random rise or decline of mountain by checking corners
            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)
            
            # go down by decreasing y
            y_number_index -= 1
            
            # action checking if a mountain or a sinkhole is created
            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k
        
        # go left < while end point is not reached
        while x_number_index - 1 > (side_y - max_num_for_approach_in_loop):
            # define random rise or decline of mountain by checking corners
            n = main_list[loop_index][loop_index]
            m = random.randint(n - 1, n + limited_increase)
            k = random.randint(n - limited_increase, n + 1)
            # go left
            x_number_index -= 1
            
            # action checking if a mountain or a sinkhole is created
            if positive == 1:
                main_list[x_number_index][y_number_index] = m
            else:
                main_list[x_number_index][y_number_index] = k

        # increase the index by one
        loop_index += 1
        
    # place the mountain on main area
    area[locx:locx+side_y, locy:locy+side_y] = main_list
    # return altered area
    return area

# Defined upcoming characters of mountains 
# rise and descend mountain
def mountain_balanced():
    # coming soon
    pass


# üstünde çukurlu dağ
def mountain_with_pit(area):
    # coming soon
    pass


def mountain_mess(area):
    # coming soon
    pass

