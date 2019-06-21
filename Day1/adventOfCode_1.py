import os

'''
# Part 1
calc=0
file = open('adventOfCode_ip.txt','r')
for number in file:
	calc+=int(number)
print(calc)'''


'''
# Part 2

import os

file = open('adventOfCode_ip.txt','r')

calc=0
list_in=set()
list_in.add(0)
ip = file.readlines()
print(len(ip))
idx=0
loop = True

while loop:
	number = ip[idx]

	calc+=int(number)
	if calc in list_in:
		loop = False
		print(calc)
		break
	else:
		list_in.add(calc)
	idx = (idx+1) % len(ip)
	print(idx)

	
'''