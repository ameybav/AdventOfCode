file1 = open('day3_ip.txt')
content = [line.strip() for line in file1]

cont=[]
cont_new=[[0 for j in range(1000)] for i in range(1000)]
count=0
findThatOne=[]

for mark in content:
	cont = mark.split(' ')
	findThatOne.append(cont[0])

	#wide tall
	dim = cont[3].split('x')
	
	#left edge top edge
	limits = cont[2].replace(':','')
	limits = limits.split(',')	
	
	lower_limit = int(limits[0])+int(dim[0])
	high_limit = int(limits[1])+int(dim[1])

	''' PArt1
	for i in range(int(limits[0]), lower_limit):
		for j in range(int(limits[1]), high_limit):
			if cont_new[i][j] == 0:
				cont_new[i][j] +=1
			elif cont_new[i][j] == 1:
				count+=1
				cont_new[i][j] +=1
			else:
				cont_new[i][j] +=1
	'''

	''' Part2
	for i in range(int(limits[0]), lower_limit):
		for j in range(int(limits[1]), high_limit):
			if cont_new[i][j] == 0:
				cont_new[i][j] = cont[0]
			else:
				
				if cont[0] in findThatOne:
					findThatOne.remove(cont[0])
				if cont_new[i][j] in findThatOne:
					findThatOne.remove(cont_new[i][j])

				#findThatOne.pop()
	'''
print("lastone:",findThatOne)
