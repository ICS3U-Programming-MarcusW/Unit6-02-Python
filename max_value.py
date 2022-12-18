#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Dec 13 2022
# This program uses a for loop to generate numbers and then find the
# maximum value within that set of numbers

import constants
import random


# Function to find max value within set of numbers
def find_max_value(random_nums):

    # Set max to the first number
    max = random_nums[0]

    # Find max value
    for counter in range(len(random_nums)):
        if max < random_nums[counter]:
            max = random_nums[counter]
    # Return the max value
    return max


def main():
    # Initialize the counter to 0
    counter = 0

    # Set empty string that will hold all values
    random_num_user = []

    # Display the random numbers being added to the list
    for counter in range(constants.MAX_ARRAY_SIZE):
        random_num_user.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        print(
            "{} added to the list at "
            "position {}".format(random_num_user[counter], counter)
        )

    # Call function that finds the max value
    user_max = find_max_value(random_num_user)
    print("")
    # Print the max value
    print("The max value is: {}".format(user_max))


if __name__ == "__main__":
    main()
