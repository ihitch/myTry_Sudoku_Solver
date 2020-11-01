#! /usr/bin/env python3

import numpy as np
def makeBoard():
	arr=[] 
	arr = np.array(arr)
	for i in range(9): 
	    col = [] 
	    for j in range(1,10): 
	        col.append(j)
	    col = np.array(col)
	    col = np.roll(col,-i)
	    #print(col)
	    arr = np.concatenate((arr,col),axis=0) 
	arr = np.reshape(arr,(9,9))
	arr[[1, 3]] = arr[[3, 1]] # shorthand a[[1, 3], :]
	arr[[2, 6]] = arr[[6, 2]]
	arr[[5, 7]] = arr[[7, 5]]
	return arr


def main():
	arr=makeBoard()
	print(arr) 
	


if __name__ == "__main__":
	main()
