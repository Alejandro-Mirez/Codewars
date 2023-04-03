def find_odd(array):
    for i in array:
        if array.count(i)%2 != 0:
            return i
        else:
            continue

