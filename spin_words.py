def spin_words(sentence):
    string_l = sentence.split(" ")
    new_string = ""
    for word in string_l:
        if len(word) >= 5:
            swapped = ""
            for j in range(len(word)):
                first = word[j]
                last = word[-(j+1)]
                first = last
                swapped += first
            new_string += swapped
            new_string += " "
        else:
            new_string += word
            new_string += " "

    return new_string.strip()


