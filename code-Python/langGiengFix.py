import numpy
import math

#langGiengUserPearson
def langGiengUserPearson(ma):
	#sao chep matrix (Ko biet truyen tham tri)
	matrix = numpy.random.rand(len(ma), len(ma[0]))
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			matrix[i][j] = ma[i][j]
	#end sao chep matrix

	# Tinh R(user)
	R = numpy.random.random(len(matrix))
	# reset ve gia tri 0
	for x in xrange(len(R)):
		R[x] = 0.0

	for i in xrange(len(matrix)):
		tuSo = 0.0
		mauSo = 0.0
		for j in xrange(len(matrix[i])):
			if matrix[i][j] != 0:
				tuSo += matrix[i][j]
				mauSo += 1.0
		R[i] = tuSo/mauSo;
		print 'R[ ', i + 1,' ] = ', R[i]

	#-------------------------------------#

	# Khoi tao mang sim ngau nhien
	sim = numpy.random.rand(len(matrix), len(matrix))
	
	# reset tat ca sim ve gia tri 0
	for i in xrange(len(sim)):
		for j in xrange(len(sim[i])):
			sim[i][j] = 0.0

	#Tinh sim giu~a user i va j
	for i in xrange(len(matrix) - 1):
		for j in xrange(i + 1, len(matrix)):
			tuSo = 0
			mauSo = 0
			mau1 = 0
			mau2 = 0
			#Tu so
			#xet tat ca item k
			for k in xrange(len(matrix[i])):
				if matrix[i][k] != 0 and matrix[j][k] != 0:
					tuSo += (matrix[i][k] - R[i]) * (matrix[j][k] - R[j])
				
			print 'Tu so \t[',i,'][',j,'] : \t', tuSo
			# end tu so 
			#------------------------------#
			#Mau so
			for k in xrange(len(matrix[i])):
				if matrix[i][k] != 0 and matrix[j][k] != 0:
					mau1 += pow(matrix[i][k] - R[i], 2)
					mau2 += pow(matrix[j][k] - R[j], 2)
			mauSo = math.sqrt(mau1) * math.sqrt(mau2)
			print 'Mau so \t[',i,'][',j,'] : \t', mauSo
			sim[i][j] = tuSo/(mauSo*1.0)
			# end mau so
	# end tinh sim 


	#-------------------------------------#


	#sao chep gia tri sim sang nua? ben kia ma tran
	for i in xrange(1, len(sim)):
		for j in xrange(i):
			sim[i][j] = sim[j][i]	
	#end sao chep

	print '---------------'
	print 'Sim'
	print sim
	print '---------------'

	# du doan 
	tuSo = 0
	mauSo = 0
	#chay ca? ma tran matrix --> gia tri nao = 0 thi` cap nhat
	for i in xrange(len(matrix)):					#user i can tinh'
		for j in xrange(len(matrix[i])):			#item j
			if matrix[i][j] == 0:
				#tinh lai gia tri cho matrix[i][j]
				for k in xrange(len(matrix)):		#user k so sanh voi' user i
					#tinh theo tung` hang` (k)
					if k != i and matrix[k][j] != 0:
						tuSo += sim[k][i] * (matrix[k][j] - R[k])*1.0
						mauSo += numpy.absolute(sim[k][i])*1.0
				matrix[i][j] = R[i]*1.0 + tuSo/(mauSo*1.0)
	# end du doan 
	print 'end pearson'
	return matrix
#end langGiengUserPearson
#------------------------------#
#------------------------------#
#------------------------------#
#langGiengUserCosine
def langGiengUserCosine(ma):
	
	#sao chep matrix (Ko biet truyen tham tri)
	matrix = numpy.random.rand(len(ma), len(ma[0]))
	for i in xrange(len(matrix)):
		for j in xrange(len(matrix[i])):
			matrix[i][j] = ma[i][j]
	#end sao chep matrix

	# Khoi tao mang sim ngau nhien
	sim = numpy.random.rand(len(matrix), len(matrix))
	
	# reset ve gia tri 0
	for i in xrange(len(sim)):
		for j in xrange(len(sim[i])):
			sim[i][j] = 0.0

	#Tinh sim giu~a user i va j
	for i in xrange(len(matrix) - 1):
		for j in xrange(i + 1, len(matrix)):
			tuSo = 0
			mauSo = 0
			mau1 = 0
			mau2 = 0
			#Tu so
			#xet tat ca item k
			for k in xrange(len(matrix[i])):
				if matrix[i][k] != 0 and matrix[j][k] != 0:
					tuSo += matrix[i][k] * matrix[j][k]
				
			print 'Tu so \t[',i,'][',j,'] : \t', tuSo
			# end tu so new
			#------------------------------#
			#Mau so
			for k in xrange(len(matrix[i])):
				if matrix[i][k] != 0 and matrix[j][k] != 0:
					mau1 += pow(matrix[i][k], 2)
					mau2 += pow(matrix[j][k], 2)
			mauSo = math.sqrt(mau1) * math.sqrt(mau2)
			print 'Mau so \t[',i,'][',j,'] : \t', mauSo
			sim[i][j] = tuSo/(mauSo*1.0)
			# end mau so
	# end tinh sim new

	#sao chep gia tri sim sang nua? ben kia ma tran
	for i in xrange(1, len(sim)):
		for j in xrange(i):
			sim[i][j] = sim[j][i]	
	#end sao chep

	print '---------------'
	print 'Sim'
	print sim
	print '---------------'


	# du doan 
	tuSo = 0
	mauSo = 0
	#chay ca? ma tran matrix --> gia tri nao = 0 thi` cap nhat
	for i in xrange(len(matrix)):					#user i can tinh'
		for j in xrange(len(matrix[i])):			#item j
			if matrix[i][j] == 0:
				#tinh lai gia tri cho matrix[i][j]
				for k in xrange(len(matrix)):		# user k so sanh voi' user i
					#tinh theo tung` hang` (k)
					if k != i and matrix[k][j] != 0:
						tuSo += sim[k][i] * matrix[k][j]*1.0
						mauSo += numpy.absolute(sim[k][i])*1.0
				matrix[i][j] = tuSo/(mauSo * 1.0)
	# end du doan
	print 'end cosine'
	return matrix
# end langGiengUserCosine

#--------------------#
#-------Main---------#

M = [
    [1.0, 4.0, 5.0, 0.0, 3.0],
    [5.0, 1.0, 0.0, 5.0, 2.0],
    [4.0, 1.0, 2.0, 5.0, 0.0],
    [0.0, 3.0, 4.0, 0.0, 4.0],
    ]
#dau` vao phai la so thuc de hien thi KET QUA chinh xac
M = numpy.array(M)



print 'Ma tran dau vao'
print M
print '---------------'

resultUserCosine = langGiengUserCosine(M)
resultUserPearson = langGiengUserPearson(M)


print 'Ket qua du doan (User) Cosine'
print resultUserCosine
print '---------------'
print 'Ket qua du doan (User) Pearson'
print resultUserPearson
