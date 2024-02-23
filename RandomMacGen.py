#!/usr/bin/env python

import random

def MacGen():
	
	prefix = "02468"
	values = "ABCDEF1234567890"
	loop = 0

	MAC = ''
	MAC += random.choice(prefix)
	MAC += random.choice(prefix)
	MAC += ":"

	while loop < 5:

		password = ''

		for i in range(2):
			password += random.choice(values)

		MAC += password

		if loop != 4:

			MAC += ":"

		loop += 1

	print(f"Your random MAC: {MAC}")

def main():
	MacGen()

main()
