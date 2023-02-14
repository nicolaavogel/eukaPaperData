

average = []
for i in range(30,150,5):
	t = open(f"/home/projects/animalia_mito/testGiraffe/mis{i}")
	y = []
	for j in t: 
		y.append(int(j))

	s = sum(y)
	l = len(y)

	av = s/l
	average.append(av)


a = sum(average)
h = len(average)

end = a/h
print(end)
