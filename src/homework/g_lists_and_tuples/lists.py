#HW 7: Lists in math domain

def get_lowest_list_value(list):
    low = list[0]
    for item in list:
        if item < low:
            low = item
    return low

def get_highest_list_value(list):
    high = list[0]
    for item in list:
        if item > high:
            high = item
    return high
