def to_jaden_case(string):
    result = ""
    new = []
    str_li = string.split(" ")

    for word in str_li:
        new.append(word.capitalize())

    result += new[0]

    for word in new[1:]:
        result += " " + word

    return result





