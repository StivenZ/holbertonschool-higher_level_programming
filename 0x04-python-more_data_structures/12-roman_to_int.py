#!/usr/bin/python3
def roman_to_int(roman_string):
    ro_di = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, \
            'D': 500, 'M': 1000}
    num_list = []
    for i in roman_string:
        num_list.append(i)
    add_list = []
    result = 0

    for idx, i in enumerate(num_list):
        if (ro_di[num_list[idx + 1]]) and (ro_di[i]) >= (ro_di[num_list[idx + 1]]):
            add_list.append(ro_di[i])
            continue
        elif ro_di[i] <= ro_di[num_list[idx + 1]]:
            add_list.append(ro_di[num_list[idx + 1]] - ro_di[i])
            num_list.remove(i)
            continue

        for i in add_list:
            result = result + i
        return(result)
