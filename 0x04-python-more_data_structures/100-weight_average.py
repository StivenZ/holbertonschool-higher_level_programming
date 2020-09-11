#!/usr/bin/python3
def weight_average(my_list=[]):

    sum_pond = sum(map(lambda x: x[0] * x[1], my_list))
    den_sum = sum(map(lambda x: x[1], my_list))

    return(sum_pond / den_sum)
