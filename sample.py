#!/usr/bin/env python3

def add(a , b):
		return a+ b

def subtract(a, b):
		return a -b
	# Comment here
	
def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		print("Cannot divide by zero.")
				return None
	else:
				return a / b
def main() :
		a = 10
		b = 5
		print("Add:", add(a, b))
		print("Subtract:", subtract(a, b))
			print("Multiply:", multiply(a, b))
		print("Divide:", divide(a, b))
	
if __name__ == "__main__":
		main(
			