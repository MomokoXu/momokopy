# open(), s.split()
f = open('grades.csv')
name = raw_input('Enter the person you want to check:\n').lower()

test = 0

for line in f:
	r = line.lower()
	t = r.split(',')
	n = t[0]
	if n == name:
		print t[1] + ':' + t[2]
		test = test + 1
	else:
		test = test

if test < 1:
	print 'No such person'

			
		
f.close()		
