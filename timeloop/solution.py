import sys

def main():
    n = input()
    for incantation in ['{} Abracadabra'.format(i + 1) for i in range(n)]:
        print incantation

if __name__ == '__main__':
    main()

