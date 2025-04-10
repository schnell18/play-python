#!/usr/bin/env python

rates = [
    [0, 4, 0.25],
    [4, 8, 0.20],
    [8, 16, 0.10],
    [16, 128, 0.06],
    [128, 999999, 0.02],
]


def cal_tax(initial, capacity):
    remaining = capacity
    tax = 0
    for rate in rates:
        if remaining > rate[1]:
            tax = tax + rate[1] * rate[2]
            remaining = remaining - rate[1]
        else:
            tax = tax + remaining * rate[2]
            break
    return 100 * (initial + tax) / capacity


if __name__ == "__main__":
    for i in range(1, 100):
        print("AKS reserved percent %dG=%.2f%%" % (i, cal_tax(0.75, i)))
