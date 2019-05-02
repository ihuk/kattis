#!/usr/bin/python
import math 

request_duration = 1000

def main():
    total_requests, max_requests_per_server = (int(s) for s in raw_input().split())
    max = 0
    inflight = []
    for _ in range(total_requests):
        timestamp = int(raw_input())
        while inflight:
            if inflight[0] > timestamp:
                break
            if inflight[0] <= timestamp:
                del inflight[0]
        inflight.append(timestamp + 1000)
        if len(inflight) > max:
            max = len(inflight)
    print int(math.ceil(max / float(max_requests_per_server)))

if '__main__' == __name__:
    main()

