import numpy

def AHP_method(Rate, n):
    A = numpy.random.rand(n, n)
    #sao chep cac gia tri --> do chua biet truyen tham tri :v
    for i in xrange(n):
        for j in xrange(n):
            A[i][j] = Rate[i][j]
    
    


    #Tong cac cot
    sumCol = [0, 0, 0]
    for i in xrange(n):
        # lap theo cot
        
        for j in xrange(n):
            # lap theo hang
            sumCol[i] = sumCol[i] + A[j][i]
    print "sumCol[0] = ", sumCol[0]
    print "sumCol[1] = ", sumCol[1]
    print "sumCol[2] = ", sumCol[2]
    
    #chia ma tran
    for i in xrange(n):
        # lap theo hang
        
        for j in xrange(n):
            # lap theo cot
            A[i][j] = A[i][j]/sumCol[j]
            
    # In ma tran sau khi chia  
    print "Ma tran sau khi chia cho tong cua moi cot"
    print A
    
    #Tinh trung binh do quan trong cua moi phuong an
    important = [0,0,0]
    for i in xrange(n):
        #lap theo hang
        important[i] = numpy.sum(A[i][:])/3.0
    
    #Vecto trong so
    #weightedVector = numpy.dot(A,important)

    return important
    
    #----------------------------#
    # ------ MAIN PROGRAM ------ #
RI = [0,    0.58,   0.9,  1.12,    1.24,  1.32,    1.41]

# lua chon giua 3 he thong 
Rate = [
     [1,        3,      9],
     [1/3.0,    1,      6],
     [1/9.0,    1/6.0,  1],
    ]
    
n = 3

Rate = numpy.array(Rate)

important_methods = AHP_method(Rate, n)

# Tinh vecto trong so
weightedVector = numpy.dot(Rate, important_methods)

# Tinh vecto nhat quan
consistencyVector = numpy.random.rand(n)
for i in xrange(n):
    consistencyVector[i] = weightedVector[i]/important_methods[i]
    
#Tinh lamda
lamda = numpy.sum(consistencyVector[:])/3.0

#Chi so nhat quan
CI = (lamda - n)/(n - 1)

#Chi so thich hop
CR = CI/RI[n-2]

print "Ma tran danh gia"
print Rate
print "-------------------"
print "Ma tran so sanh"
print important_methods
print "-------------------"
print "Vector trong so"
print weightedVector
print "-------------------"
print "Vector nhat quan"
print consistencyVector
print "-------------------"
print "LAMDA"
print lamda
print "-------------------"
print "Chi so nhat quan CI"
print CI
print "-------------------"
print "Chi so thich hop CR"
print CR