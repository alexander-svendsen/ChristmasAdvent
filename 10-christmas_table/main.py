people = range(1,1501)

index = 0
while(len(people) > 1):
	index = (index + 1) % len(people)
	del people[index]

print people[0]