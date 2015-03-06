def numlist():

    largest = None
    smallest = None
    while True:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        try:    
    	   n = float(num)
        except:
            print 'Invalid input'
    #print num
    
    #for y in n:
        if largest is None:
            largest = n
        elif n > largest:
            largest = n            
	#print "Maximum is ", largest
	#for x in n:
        if smallest is None:
            smallest = n
        elif n < smallest:
            smallest = n
    print "Maximum is", largest
    print "Minimum is", smallest
