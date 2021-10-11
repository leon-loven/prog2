#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	timep = []
	timec = []
	nlist = [n for n in range(30, 46)]
	for n in range(30, 46):
		start = pc()
		fib_py(n)
		end = pc()
		timep.append(end-start)
		start2 = pc()
		f = Integer(n)
		f.fib()
		end2 = pc()
		timec.append(end2-start2)
	plt.plot(nlist, timep)
	plt.plot(nlist, timec)
	plt.xlabel('Fibonacci number n')
	plt.ylabel('Time (s)')
	plt.savefig('timeplot.png')
	
	time = []
	for n in range(1,31):
		start3 = pc()
		fib_py(n)
		end3 = pc()
		time.append(round(end3-start3, 8))
	print(time)

	f.set(47)
	print(f.fib())

if __name__ == '__main__':
	main()