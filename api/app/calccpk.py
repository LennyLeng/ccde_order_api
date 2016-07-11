#encoding=utf8
#! /bin/python

import numpy as np


def cp(mylist, usl, lsl):
    arr = np.array(mylist)
    arr = arr.ravel()
    sigma = np.std(arr)
    Cp = float(usl - lsl) / (6*sigma)
    return Cp


def cpk(mylist, usl, lsl):
    arr = np.array(mylist)
    arr = arr.ravel()
    sigma = np.std(arr)
    m = np.mean(arr)

    Cpu = float(usl - m) / (3*sigma)
    Cpl = float(m - lsl) / (3*sigma)
    Cpk = np.min([Cpu, Cpl])
    return Cpk


if __name__ == "__main__":
    #a1 = np.random.randn(10)
    #print a1
    #print Cp(a1, 1, -1)
    #print Cpk(a1, 1, -1)

    a1 = np.arange(0, 10)
    print a1
    print cp(a1, 10, 0)
    print cpk(a1, 10, 0)
