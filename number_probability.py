#!/usr/bin/env python3.7

def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
total_numbers=10
numbers = [0,1,2,3,4,5,6,7,8,9]


# Determine the probability of each number

for digit in numbers:

    probability_of_digit = event_probability(digit, total_numbers)
    print(str(probability_of_digit) + '%')

