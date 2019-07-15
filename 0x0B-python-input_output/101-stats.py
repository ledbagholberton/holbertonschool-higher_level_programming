#!/usr/bin/python3
import sys
#import pdb; pdb.set_trace()
my_dict = {"200":0, "301":0, "400":0, "401":0, "403":0, "404":0, "405":0, "500":0}
for line in sys.stdin:
    a = line.split()
    init_all()
    while True:
        while cont < 10:
            my_size += int(a[9])
            print("Temporal size: {:d} and a[8]: {:s}".format(my_size, a[8]))
            if a[8] =="200":
                dic("200") 
            elif a[8] =="301":
                lis[0] += 1
            elif a[8] =="400":
                lis[0] += 1
                is400 += 1
            elif a[8] =="401":
                lis[0] += 1
                is401 += 1
            elif a[8] =="403":
                lis[0] += 1
                is403 += 1
            elif a[8] =="404":
                lis[0] += 1
                is404 += 1
            elif a[8] =="405":
                lis[0] += 1
                is405 += 15
            elif a[8] =="500":
                lis[0] += 1
                is500 += 1
            else:
                pass
                cont += 1

        print("File size: {:s}".format(my_size))
        if is200 is not 0:
            print("200: {:d}".format(is200))
        elif is301 is not 0:
            print("301: {:d}".format(is301))
        elif is400  is not 0:
            print("400: {:d}".format(is400))
        elif is401 is not 0:
            print("401: {:d}".format(is401))
        elif is403 is not 0:
            print("403: {:d}".format(is403))
        elif is404 is not 0:
            print("404: {:d}".format(is404))
        elif is405 is not 0:
            print("405: {:d}".format(is405))
        elif is500 is not 0:
            print("500: {:d}".format(is500))
        else:
            init_all()
