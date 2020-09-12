#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, 'D': 500, 'M': 1000}
        num = list(roman_string)
        add = []
        result = 0
        for idx, i in enumerate(num):
            if len(num) == 1:
                return(rom[i])
            if (idx + 1 <= len(num) - 1) and (rom[i]) >= (rom[num[idx + 1]]):
                add.append(rom[i])
                continue
            elif (idx + 1 <= len(num) - 1) and (rom[i] < rom[num[idx + 1]]):
                add.append(rom[num[idx + 1]] - rom[i])
                del num[idx]
                if idx + 1 <= len(num) - 1:
                    continue
                else:
                    break
            add.append(rom[i])
        for i in add:
            result = result + i
        return(result)
    else:
        return(0)
