import numpy
#Numpy module is needed as of version 1

def arrayStats(array):
    array.sort()
    length=len(array)
    
    mean=numpy.mean(array)
    median=numpy.median(array)
    standardDeviation=numpy.std(array)
    avg=numpy.average(array)

    print("ArrayStats of the array of integers ",array,"-")
    print("Mean=",mean)
    print("Median=",median)
    print("Standard deviation=",standardDeviation)
    print("Average=",avg)

    range=array[length-1]-array[0]

    print("Range=",range)
    
