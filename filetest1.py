
while True:
	path = raw_input('Enter the path (Enter "done" to exit):  ')
	if path == 'done':
		print 'Thank you'
		break

	else:
		try:
			file = open (path)
			score = 0
			count = 0
			for line in file:
				a = line.split(',')
				t = int(a[2][:-1])
				score = score + t
				count = count + 1

			print 'The average score is: ' + str(score/count) + '. Thank you !'
			break

		except:
			print 'File open failed !'







