import re


def main():
    with open('C:\\Users\\zebul\\AdventOfCode\\2015\\Day2Input.txt') as f:
        main_raw_input = [line.rstrip('\n') for line in f]

    # if you need the input broken up into constituent parts:
    # converted_input = main_raw_input[0].split(',')
    # converted input = [int(i) for i in main_raw_input] # for things like ints

    total_wrapping_paper = 0

    for row in main_raw_input:

        converted_input = [int(i) for i in row.split('x')]

        side_list = []

        l, w, h = converted_input
        side_list.append(l * w)
        side_list.append(w * h)
        side_list.append(h * l)

        min_side = min(side_list)

        total_wrapping_paper += sum(side_list * 2)
        total_wrapping_paper += min_side

    print(total_wrapping_paper)


if __name__ == '__main__':
    main()
