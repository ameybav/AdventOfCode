from collections import Counter

file = open('adventOfCode_2.txt','r')
twos_count=0
threes_count=0

for line in file:
	twos_count_flag = False
	threes_count_flag = False
	count = Counter(line)
	for td in count.items():
		if td[1] == 2 and twos_count_flag == False:
			twos_count+=1
			twos_count_flag = True
		if td[1] == 3 and threes_count_flag == False:
			threes_count_flag = True
			threes_count+=1
print(twos_count,threes_count)
print(twos_count*threes_count)