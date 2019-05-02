#!/usr/bin/python

def main():
    lights, length = (int(s) for s in raw_input().split()) 
    duration = 0
    for l in range(lights):
        distance, red, green = (int(s) for s in raw_input().split())
        print 'l {}, r {}, g {}'.format(distance, red, green)
        duration += distance
        cycle_duration = red + green
        cycle = duration / cycle_duration
        print 'duration {}, red {}, green {}, cycle duration {}, cycle {}, position in cycle {}, exp {}'.format(duration, red, green, cycle_duration, cycle, duration % cycle_duration, (duration % cycle_duration) - red) 

    print duration

if '__main__' == __name__:
    main()
