#!/usr/bin/python3
def roman_to_int(roman_string):
    decode = []
    roman = {"X": 10, "L": 50, "V": 5, "I": 1, "C": 100, "D": 500, "M": 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    else:
        for j in roman_string:
            decode.append(roman.get(j))
        decode.append(0)
        i = 0
        sumup = 0
        while i < len(decode)-1:
            if decode[i] < decode[i+1]:
                sumup += (decode[i+1] - decode[i])
                i += 1
            else:
                sumup += decode[i]
            i += 1
        return sumup
