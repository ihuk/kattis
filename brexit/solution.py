#!/usr/bin/python
import math


def main():
    countries, number_of_partnerships, home_country, first_to_leave_country = [int(s) for s in raw_input().split()]
    if home_country == first_to_leave_country:
        print 'leave'
        return
    partnerships = {}
    trading_partners = {}
    for p in range(number_of_partnerships):
        c0, c1 = [int(s) for s in raw_input().split()]
        trading_partners[c0] = trading_partners.get(c0, 0) + 1
        if c0 in partnerships:
            partnerships[c0].add(c1)
        else:
            partnerships[c0] = set()
            partnerships[c0].add(c1)
        trading_partners[c1] = trading_partners.get(c1, 0) + 1
        if c1 in partnerships:
            partnerships[c1].add(c0)
        else:
            partnerships[c1] = set()
            partnerships[c1].add(c0)
    test(partnerships, home_country, first_to_leave_country)
    to_leave = [first_to_leave_country]
    while to_leave:
        l = to_leave.pop()
        for c in partnerships[l]:
            partnerships[c].remove(l)
            if len(partnerships[c]) <= (trading_partners[c] / 2.0):
                if c == home_country:
                    print 'leave'
                    return
                if c in partnerships[home_country]:
                    if len(partnerships[home_country]) - 1 <= (trading_partners[home_country] / 2.0):
                        print 'leave'
                        return
                to_leave.append(c)
    print 'leave' if len(partnerships[home_country]) <= (trading_partners[home_country] / 2.0) else 'stay'


if '__main__' == __name__:
    main()

