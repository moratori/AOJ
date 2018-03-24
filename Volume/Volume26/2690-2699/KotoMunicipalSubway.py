#!/usr/bin/env python
#coding:utf-8

import math

def divide(integer):
    result = []
    limit = int(integer / 2)
    cnt = 0
    while (cnt <= limit):
        result.append((cnt, integer - cnt))
        cnt += 1
    return result

def distance_from_zero(point):
    (x, y) = point
    return math.sqrt(x ** 2 + y ** 2)


def solve(integer_distance, budget):

    differences_to_budget = []

    for (x_axis, y_axis) in divide(integer_distance):
        local_difference = abs(budget - distance_from_zero((x_axis, y_axis)))
        differences_to_budget.append(local_difference)

    return min(differences_to_budget)

def main():
    while True:
        line = input()
        integer_distance, budget= map(int, line.split(" "))
        if (integer_distance == 0) and (budget == 0):
            break
        print(solve(integer_distance, budget))


if __name__ == "__main__":
    main()
