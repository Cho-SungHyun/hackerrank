def print_formatted(number):
    # your code goes here
    l=len(bin(number)[2::])
    for i in range(1, number+1):
        print(str(i).rjust(l), str(oct(i).split('o')[1]).rjust(l), str(hex(i).split('x')[1].upper()).rjust(l), str(bin(i).split('b')[1]).rjust(l))

