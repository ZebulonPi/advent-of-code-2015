import re


def main():
    with open('C:\\Users\\zebul\\AdventOfCode\\2015\\Day2Input.txt') as f:
        main_raw_input = [line.rstrip('\n') for line in f]

    # if you need the input broken up into constituent parts:
    # converted_input = main_raw_input[0].split(',')
    # converted input = [int(i) for i in main_raw_input] # for things like ints

    total_ribbon_length = 0
    bow_length = 1

    for row in main_raw_input:

        bow_length = 1

        converted_input = [int(i) for i in row.split('x')]

        for length in converted_input:
            bow_length *= length

        two_sides = sorted(converted_input)[:2]

        total_ribbon_length += 2 * sum(two_sides)
        total_ribbon_length += bow_length

    print(total_ribbon_length)


if __name__ == '__main__':
    main()
