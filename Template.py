import re


def main():
    with open('C:\\Users\\zebul\\AdventOfCode\\2015\\Dat1InputTest.txt') as f:
        main_raw_input = [line.rstrip('\n') for line in f]

    # if you need the input broken up into constituent parts:
    # converted_input = main_raw_input[0].split(',')
    # converted input = [int(i) for i in main_raw_input] # for things like ints

    for row in main_raw_input:
        print(row)

        # if you should need to break it into single units of the row, use this:
        # for single_unit in row:
        #     print(single_unit)


if __name__ == '__main__':
    main()
