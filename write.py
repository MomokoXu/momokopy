t = raw_input('Enter n:\n')
try:
	n = int(t)
	if n <= 0:
		print 'Non-positive input'
	else:
		for i in range(n):
			print '*' * (i+1)
except:
	print 'Invalid input'
