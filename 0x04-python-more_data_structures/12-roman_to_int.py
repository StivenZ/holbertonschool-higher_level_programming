#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):

        ro_di = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, \
                'D': 500, 'M': 1000}
        num_list = list(roman_string)
        add_list = []
        result = 0

        for idx, i in enumerate(num_list):
            if len(num_list) == 1:
                return(ro_di[i])
            if (idx + 1 <= len(num_list) - 1) and (ro_di[i]) >= (ro_di[num_list[idx + 1]]):
                add_list.append(ro_di[i])
                continue
            elif (idx + 1 <= len(num_list) - 1) and (ro_di[i] < ro_di[num_list[idx + 1]]):
                add_list.append(ro_di[num_list[idx + 1]] - ro_di[i])
                del num_list[idx]
                if idx + 1 <= len(num_list) - 1:
                    continue
                else:
                    break
            add_list.append(ro_di[i])
        for i in add_list:
            result = result + i
        return(result)
    else:
        return(0)
