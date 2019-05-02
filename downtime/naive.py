#!/usr/bin/python
import math 

def main():
    requests, requests_per_server = (int(s) for s in raw_input().split())
    requests_per_second = {}
    for _ in range(requests):
        timestamp = int(raw_input())
        second = timestamp / 1000
        requests_per_second[second] = requests_per_second.get(second, 0) + 1
        if timestamp % 1000:
            requests_per_second[second + 1] = requests_per_second.get(second + 1, 0) + 1
    max = 0
    for k, v in requests_per_second.iteritems():
        required_servers = int(math.ceil(v / float(requests_per_server)))
        if required_servers > max:
            max = required_servers
    print max


if '__main__' == __name__:
    main()

