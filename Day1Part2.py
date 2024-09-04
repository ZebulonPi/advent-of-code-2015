import re


def main():
    with open('C:\\Users\\zebul\\AdventOfCode\\2015\\Day1Input.txt') as f:
        main_raw_input = [line.rstrip('\n') for line in f]

    # if you need the input broken up into constituent parts:
    # converted_input = main_raw_input[0].split(',')
    # converted input = [int(i) for i in main_raw_input] # for things like ints

    final_floor = 0

    for row in main_raw_input:
        single_unit_pos = 1
        for single_unit in row:
            if single_unit == '(':
                final_floor += 1
            else:
                final_floor -= 1
            if final_floor == -1:
                print(f"Answer is {single_unit_pos}")
                break
            else:
                single_unit_pos += 1


if __name__ == '__main__':
    main()
