import math

def main():
    n, w, h = [int(s) for s in raw_input().split()]
    d = math.sqrt(w**2 + h**2)
    for _ in range(n):
        l = input()
        print 'NE' if l > d else 'DA'

if '__main__' == __name__:
    main()
