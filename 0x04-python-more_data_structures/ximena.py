#!/usr/bin/python3
matrix = [[3, 4, 5, 3],
          [6, 8, 3, 2],
          [7, 0, 8, 1]]
for i in matrix:
    for j in i:
        print("{:}".format(j))
print()
print()

 for m in range(len(matrix)):
     for n in range(len(matrix[m])):
         print("{:}".format(matrix[m][n]), end=" ")
         print()
         print()
    
for o in matrix:
    print(list(map(lambda x: x, o)), end=" ")
    print()
    print()
        
for l, k, o, p in matrix:
    print("{:} {:} {:} {:}".format(l, k, o, p))
    print()
    print(list(map((lambda x: x), list(map(lambda y: y, matrix)))))
    print()

m = zip(matrix)
for q in m:
    print("{}".format(q[0]))
    print()
