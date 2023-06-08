def print_rangoli(size):
    # your code goes here
    hyphen_width = 1 + (4 * (size - 1))
    num_levels = 2 * size - 1
    levels = []

    for l in range(num_levels // 2 + 1):
        right_string = ""
        left_string = ""
        for c in range(97 + size - 1, 97 + size - 1 - l, -1):
            left_string += chr(c) + "-"
            right_string = "-" + chr(c) + right_string
        levels.append("".join([
            (hyphen_width // 2 * "-"),
            left_string,
            chr(97 + size - 1 - l),
            right_string,
            (hyphen_width // 2 * "-")
        ]))
        hyphen_width -= 4

    for l in levels:
        print(l)

    for i in range(len(levels) - 2, -1, -1):
        print(levels[i])
    
    


