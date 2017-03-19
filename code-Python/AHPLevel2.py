import numpy

#AHP func
def AHP_method(X, X1, X2):
    
    M = X
    M1 = X1
    M2 = X2




# Tinh [C1, C2]
	# print '[C1, C2]'
    # khoi tao mang luu tong
    sumCol = numpy.random.rand(len(M))
    for x in xrange(len(sumCol)):
    	sumCol[x] = 0
    # end khoi tao mang
    #----------------------------#	
    # Tong cac cot	
    for i in xrange(len(M)):
        # lap theo cot
        for j in xrange(len(M[i])):
            # lap theo hang
            sumCol[i] = sumCol[i] + M[j][i]
    for x in xrange(len(M)):
    	print 'Tong cot ', x, ' = ', sumCol[x]
    # end tong cac cot
    #----------------------------#
    # chia ma tran
    for i in xrange(len(M)):
        # lap theo hang
        for j in xrange(len(M[i])):
            # lap theo cot
            M[i][j] = M[i][j]/sumCol[j]
    # end chia ma tran
    #----------------------------#
    # In ma tran sau khi chia  
    print "Ma tran sau khi chia cho tong cua moi cot"
    print M
    print '----------------------------'
    # end in ma tran sau khi chia
    #----------------------------#
    #Tinh trung binh do quan trong cua moi phuong an
	#+++++++++++++++++++
    # khoi tao mang 
    importantM = numpy.random.rand(len(M))
    for x in xrange(len(M)):
    	importantM[x] = 0
    # end khoi tao mang
    #----------------------------#
    for i in xrange(len(M)):
        # lap theo hang
        importantM[i] = numpy.sum(M[i][:])/(len(M)*1.0)
	#+++++++++++++++++++
	# end tinh do quan trong trung binh 
# end tinh [C1, C2]
	#----------------------------#
	#----------------------------#
	#----------------------------#




#Tinh [A1, A2, A3] cua C1
	#print '[A1, A2, A3] cua C1'
	# khoi tao mang luu tong
    sumCol = numpy.random.rand(len(M1))
    for x in xrange(len(sumCol)):
    	sumCol[x] = 0
    # end khoi tao mang
    #----------------------------#	
    # Tong cac cot	
    for i in xrange(len(M1)):
        # lap theo cot
        for j in xrange(len(M1[i])):
            # lap theo hang
            sumCol[i] = sumCol[i] + M1[j][i]
    for x in xrange(len(M1)):
    	print 'Tong cot ', x, ' = ', sumCol[x]
    # end tong cac cot
    #----------------------------#
    # chia ma tran
    for i in xrange(len(M1)):
        # lap theo hang
        for j in xrange(len(M1[i])):
            # lap theo cot
            M1[i][j] = M1[i][j]/sumCol[j]
    # end chia ma tran
    #----------------------------#
    # In ma tran sau khi chia  
    print "Ma tran sau khi chia cho tong cua moi cot"
    print M1
    print '----------------------------'
    # end in ma tran sau khi chia
    #----------------------------#
    #Tinh trung binh do quan trong cua moi phuong an
	#+++++++++++++++++++
    # khoi tao mang 
    importantM1 = numpy.random.rand(len(M1))
    for x in xrange(len(M1)):
    	importantM1[x] = 0
    # end khoi tao mang
    #----------------------------#
    for i in xrange(len(M1)):
        # lap theo hang
        importantM1[i] = numpy.sum(M1[i][:])/(len(M1)*1.0)
	#+++++++++++++++++++
	# end tinh do quan trong trung binh

#end tinh [A1, A2, A3] cua C1
	#----------------------------#
	#----------------------------#
	#----------------------------#






#Tinh [A1, A2, A3] cua C2
	#print '[A1, A2, A3] cua C2'
	# khoi tao mang luu tong
    sumCol = numpy.random.rand(len(M2))
    for x in xrange(len(sumCol)):
    	sumCol[x] = 0
    # end khoi tao mang
    #----------------------------#	
    # Tong cac cot	
    for i in xrange(len(M2)):
        # lap theo cot
        for j in xrange(len(M2[i])):
            # lap theo hang
            sumCol[i] = sumCol[i] + M2[j][i]
    for x in xrange(len(M2)):
    	print 'Tong cot ', x, ' = ', sumCol[x]
    # end tong cac cot
    #----------------------------#
    # chia ma tran
    for i in xrange(len(M2)):
        # lap theo hang
        for j in xrange(len(M2[i])):
            # lap theo cot
            M2[i][j] = M2[i][j]/sumCol[j]
    # end chia ma tran
    #----------------------------#
    # In ma tran sau khi chia  
    print 'Ma tran sau khi chia cho tong cua moi cot'
    print M2
    print '----------------------------'
    # end in ma tran sau khi chia
    #----------------------------#
    #Tinh trung binh do quan trong cua moi phuong an
	#+++++++++++++++++++
    # khoi tao mang 
    importantM2 = numpy.random.rand(len(M2))
    for x in xrange(len(M2)):
    	importantM2[x] = 0
    # end khoi tao mang
    #----------------------------#
    
    for i in xrange(len(M2)):
        # lap theo hang
        importantM2[i] = numpy.sum(M2[i][:])/(len(M2)*1.0)
	#+++++++++++++++++++
	# end tinh do quan trong trung binh 

#end tinh [A1, A2, A3] cua C2

 	#----------------------------#
	#----------------------------#
	#----------------------------#

    print "-------------------"
    print '[C1, C2]'
    print importantM
    print "-------------------"
    print '[A1, A2, A3] cua C1'
    print importantM1
    print "-------------------"
    print '[A1, A2, A3] cua C2'
    print importantM2
    print "-------------------"

	# khoi tao mang 
    A = numpy.random.rand(len(importantM1))
    for x in xrange(len(importantM1)):
        A[x] = 0
    # end khoi tao mang

    # ghep 2 mang important M1 va M2 lai voi nhau
    importantA = [importantM1, importantM2]
    importantA = numpy.array(importantA)
    print 'Sau khi ghep 2 mang A lai vs nhau'
    print importantA
    print '--------------------'
    # end ghep 2 mang
    for i in xrange(len(importantM)):
        for j in xrange(len(importantM1)):
            A[j] += importantM[i] * importantA[i][j]
		
    print 'So sanh do quan trong giua 3 lua chon'
    print A

	
# end AHP func 

    #----------------------------#
    # ------ MAIN PROGRAM ------ #
RI = [0,    0.58,   0.9,  1.12,    1.24,  1.32,    1.41]

# lua chon giua 3 he thong 
C = [
     [1,        3],
     [1/3.0,    1],
    ]
C1 = [
		[1,        2, 		4],
		[0.5,      1,	  	3],
		[0.25,     1/3.0,	1],
	]
C2 = [
		[1,        	3, 		5],
		[1/3.0,    	1,	  	2],
		[0.2,		0.5,	1],	
	]

C = numpy.array(C)
C1 = numpy.array(C1)
C2 = numpy.array(C2)

AHP_method(C, C1, C2)