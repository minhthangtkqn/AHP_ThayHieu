import numpy

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    
    for step in xrange(steps):

        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    #Do lech
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    #cap nhat lai ma tran P va Q new
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        # ma tran R new sau khi cap nhat lai P va Q
        #eR = numpy.dot(P,Q)
        #----------------------------#
        # Do chinh xac - e
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    
                    # Ham muc tieu Omf
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    
                    # Kiem tra tranh' hoc vet
                    xP = 0
                    for m in xrange(len(R)):
                        for n in xrange(K):
                            xP = xP + pow(P[m][n], 2)
                    xQ = 0
                    for p in xrange(K):
                        for q in xrange(len(R[0])):
                            xQ = xQ + pow(Q[p][q], 2)
                    # tinh do chinh xac - cong thuc tranh' hoc vet
                    e = e + beta * (xP + xQ)
        # neu dat do chinh' xac' can thiet --> break
        if e < 0.001:
            break
    return P, Q
    
    # ---------------------------------- #
    # ----------MAIN PROGRAM--------- #
    # ---------------------------------- #

R = [
     [5,3,0,1],
     [4,0,0,1],
     [1,1,0,5],
     [1,0,0,4],
     [0,1,5,4],
    ]

R = numpy.array(R)
print "Ma tran goc"
print R
print "---------------"

N = len(R)
M = len(R[0])
K = 2

P = numpy.random.rand(N,K)
Q = numpy.random.rand(K,M)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = numpy.dot(nP, nQ)

print "Ma tran R"
print nR
print "---------------"
print "Ma tran P"
print nP
print "---------------"
print "Ma tran Q"
print nQ
