def FindMax(x):
	try:
		t = x[0]
		for y in x:
			if t < y:
				t = y
		return t
	except:
		print 'Error'			

						

