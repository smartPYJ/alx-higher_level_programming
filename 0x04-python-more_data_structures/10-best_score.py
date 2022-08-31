#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
        values = list(a_dictionary.values())
        values.sort()
        for key, value in a_dictionary.items():
            if values[-1] == value:
                return key
