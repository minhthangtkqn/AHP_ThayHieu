import numpy
def abc(matrix):
    print matrix
    print '---------------'
    matrix = numpy.dot(matrix, matrix)
    print '---------------'
    print matrix
    return matrix

M = [
    [1.0, 4.0, 5.0, 0.0],
    [5.0, 1.0, 0.0, 5.0],
    [4.0, 1.0, 2.0, 5.0],
    [0.0, 3.0, 4.0, 0.0],
    ]
#dau` vao phai la so thuc de hien thi KET QUA chinh xac
M = numpy.array(M)

print 'Ma tran dau vao'
print M
print '---------------'

X = abc(M)

print 'Ma tran sau khi tinh toan' 
print X
print '---------------'
print 'Ma tran dau vao again'
print M