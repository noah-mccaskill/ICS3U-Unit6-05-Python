#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program takes grades as input and calculates the average using lists


def find_average(grade_list):
    # this function calculates the average using a list

    total = 0

    for single_grade in grade_list:
        total += single_grade

    average = total / len(grade_list)

    return average


def main():
    # this function gets input, calls a function, then shows the average

    grade_list = []
    temp_mark = 0

    print("This program calculates your average mark. Enter -1 to stop.\n")

    # input
    try:
        temp_mark = int(input("Enter a mark (%): "))
        grade_list.append(temp_mark)
        while temp_mark != -1:
            if temp_mark < 0:
                0 / 0
            temp_mark = int(input("Enter a mark (%): "))
            grade_list.append(temp_mark)

        grade_list.pop()  # removes the -1 from being counted
        print("")

        average = find_average(grade_list)

        print("The average mark is {0:.2f}%.".format(average))

    except Exception:
        print("\nThat number is invalid, please restart the program.")

    print("\nDone.")


if __name__ == "__main__":
    main()
