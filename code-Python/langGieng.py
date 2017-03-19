import numpy
import math

#langGiengUserPearson
def langGiengUserPearson(matrix, purposeY, purposeX):
	purposeX -= 1
	purposeY -= 1

	# Tinh R(user)
	R = numpy.random.random(len(matrix))
	# reset ve gia tri 0
	for x in xrange(len(R)):
		R[x] = 0

	for i in xrange(len(matrix)):
		tuSo = 0
		mauSo = 0
		for j in xrange(len(matrix[i])):
			if matrix[i][j] != 0:
				tuSo += matrix[i][j]
				mauSo += 1.0
		R[i] = tuSo/mauSo;
		print 'R[ ', i + 1,' ] = ', R[i]

	# Khoi tao mang sim ngau nhien
	sim = numpy.random.random(len(matrix))
	
	# reset ve gia tri 0
	for x in xrange(len(sim)):
		sim[x] = 0

	#Tinh sim
	for i in xrange(len(matrix)):
		if i != purposeY:
			print 'hang` thu ', i
			tuSo = 0
			mauSo = 0
			mau1 = 0
			mau2 = 0
			#Tu so
			for j in xrange(len(matrix[i])):
				if matrix[purposeY][j] != 0 and matrix[i][j] != 0:
					tuSo += (matrix[purposeY][j] - R[purposeY]) * (matrix[i][j] - R[i])
				
			print 'Tu so ', i
			print tuSo
				
			#Mau so
			for k in xrange(len(matrix[i])):
				if matrix[purposeY][k] != 0 and matrix[i][k] != 0:
					mau1 += pow(matrix[purposeY][k] - R[purposeY], 2)
					mau2 += pow(matrix[i][k] - R[i], 2)
			mauSo = math.sqrt(mau1) * math.sqrt(mau2)
			print 'Mau so ', i
			print mauSo
			sim[i] = tuSo/mauSo
	# end tinh sim

	print '---------------'
	print 'Sim'
	print sim
	print '---------------'

	# du doan
	tuSo = 0
	mauSo = 0
	for i in xrange(len(matrix)):
		if matrix[i][purposeX] != 0:
			tuSo += sim[i] * (matrix[i][purposeX] - R[i])
			mauSo += numpy.absolute(sim[i])
	return R[purposeY] + tuSo / mauSo
	# end du doan

#end langGiengUserPearson

#langGiengUserCosine
def langGiengUserCosine(matrix, purposeY, purposeX):
	purposeX -= 1
	purposeY -= 1

	# Khoi tao mang sim ngau nhien
	sim = numpy.random.random(len(matrix))
	# reset ve gia tri 0
	for x in xrange(len(sim)):
		sim[x] = 0
	# Tinh sim(cos)
	for i in xrange(len(matrix)):
		if i != purposeY:
			print 'hang` thu ', i
			tuSo = 0
			mauSo = 0
			mau1 = 0
			mau2 = 0
			#Tu so
			for j in xrange(len(matrix[i])):
				tuSo += matrix[purposeY][j] * matrix[i][j]
				
			print 'Tu so ', i
			print tuSo
				
			#Mau so
			for k in xrange(len(matrix[i])):
				if matrix[purposeY][k] != 0 and matrix[i][k] != 0:
					mau1 += pow(matrix[purposeY][k], 2)
					mau2 += pow(matrix[i][k], 2)
			mauSo = math.sqrt(mau1) * math.sqrt(mau2)
			print 'Mau so ', i
			print mauSo
			sim[i] = tuSo/mauSo
	# end tinh Sim

	print '---------------'
	print 'Sim'
	print sim
	print '---------------'

	# du doan
	tuSo = 0
	mauSo = 0
	for i in xrange(len(matrix)):
		tuSo += sim[i] * matrix[i][purposeX]
		mauSo += numpy.absolute(sim[i])
	return tuSo / mauSo
	# end du doan
# end langGiengUserCosine

#--------------------#
#-------Main---------#

M = [
    [1, 4, 5, 0, 3],
    [5, 1, 0, 5, 2],
    [4, 1, 2, 5, 0],
    [0, 3, 4, 0, 4],
    ]
    
M = numpy.array(M)

print 'Ma tran dau vao'
print M
print '---------------'

resultUserCosine = langGiengUserCosine(M, 4, 1)
resultUserPearson = langGiengUserPearson(M, 4, 1)


print 'Ket qua du doan (User) Cosine'
print resultUserCosine
print '---------------'
print 'Ket qua du doan (User) Pearson'
print resultUserPearson