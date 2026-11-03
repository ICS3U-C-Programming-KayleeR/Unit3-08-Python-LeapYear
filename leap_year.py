#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 11, 01, 2026
# This program calculate whether a given
# year is a leap year using a formula


def main():
    # get the user's year input
    year_str = input("Enter the year: ")

    # check if input is a valid data type
    try:
        year_int = int(year_str)
        if year_int % 4 == 0:
            if year_int % 100 == 0:
                if year_int % 400 == 0:
                    print("{} is a leap year.".format(year_int))
                else:
                    print("{} is not a leap year.".format(year_int))
            else:
                print("{} is a leap year.".format(year_int))
        else:
            print("{} is not a leap year.".format(year_int))
    except:
        print("{} is not a valid input.".format(year_str))


if __name__ == "__main__":
    main()
