#! /usr/bin/env python3

import numpy as np
import random
def makeBoard():
	arr=[] 
	arr = np.array(arr)
	for i in range(9): 
	    col = [] 
	    for j in range(1,10): 
	        col.append(j)
	    col = np.array(col)
	    col = np.roll(col,-i)
	    for r in range (5):
	    	n = random.randint(0,8)
	    	col[n] = 0
	    #print(col)
	    arr = np.concatenate((arr,col),axis=0) 
	arr = np.reshape(arr,(9,9))
	arr[[1, 3]] = arr[[3, 1]] # shorthand a[[1, 3], :]
	arr[[2, 6]] = arr[[6, 2]]
	arr[[5, 7]] = arr[[7, 5]]
	arr[arr==0] = None
	return arr

def sudokuSolver(arr):
	toFill = []
	for i in range(9):
		for j in range(9):
			if np.isnan(arr[i][j]):
				toFill.append([i,j])

	


def main():
	arr=makeBoard()
	print(arr) 
	sudokuSolver(arr)


if __name__ == "__main__":
	main()
