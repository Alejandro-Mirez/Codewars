def century(year):

    if year < 101:
        return 1
    else:
        string_year = str(year)
        if year < 1001:
            first = string_year[0]
            last_two = string_year[-2] + string_year[-1]
            if last_two == "00":
                return int(first)
            else:
                return int(first) + 1
        else:
            first_two = string_year[0] + string_year[1]
            last_two = string_year[-2] + string_year[-1]
            if last_two == "00":
                return int(first_two)
            else:
                return int(first_two) + 1