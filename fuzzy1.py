import numpy as np
import random


def find_intersection(A, B, p, s, a, b):
    print ("Enter Intersection")
    r = random.randrange(p, s+1)
    print ("Random is " + str(r))
    temp1 = A[r]
    temp2 = B[r]
    A[r] = A[s]
    B[r] = B[s]
    A[s] = temp1
    B[s] = temp2
    a = A[s]
    b = B[s]
    print ("New array A is " + str(A))
    print ("New array B is " + str(B))
    for i in range(p, s):
        if A[i] < b and B[i] > a:
            print ("Intersction at " + str(i))
            if A[i] > a:
                a = A[i]
            if B[i] < b:
                b = B[i]
    print ("Intersection region is " + str(a) + " " + str(b))
    print
    return (a, b)

def partion_right(A, B, a, p, s):
    print ("Enter partion_right")
    i = p-1
    print a
    for j in range(p, s):
        if (A[j]) <= a:
            i += 1
            temp1 = A[i]
            temp2 = B[i]
            A[i] = A[j]
            B[i] = B[j]
            A[j] = temp1
            B[j] = temp2
    temp1 = A[i + 1]
    temp2 = B[i + 1]
    A[i + 1] = A[s]
    B[i + 1] = B[s]
    A[s] = temp1
    B[s] = temp2
    print ("Modified arrays are ")
    print A
    print B
    print ("i + 1 is " + str(i + 1))
    print
    return i + 1

def partion_left_middle(A, B, b, p, r):
    print ("Enter partion_left_middle")
    i = p - 1
    print b
    for j in range(p, r):
        if (B[j]) <= b:
            i += 1
            temp1 = A[i]
            temp2 = B[i]
            A[i] = A[j]
            B[i] = B[j]
            A[j] = temp1
            B[j] = temp2
    temp1 = A[i + 1]
    temp2 = B[i + 1]
    A[i + 1] = A[r]
    B[i + 1] = B[r]
    A[r] = temp1
    B[r] = temp2
    print ("Modified arrays are ")
    print A
    print B
    print ("i + 1 is " + str(i + 1))
    print
    return i + 1

def fuzzysort(A, B, p, s):
    if p < s:
        print ("Enter Fuzzy")
        a = b = 0
        region = find_intersection(A, B, p, s, a, b)
        a = region[0]
        b = region[1]
        r = partion_right(A, B, a, p, s)
        q = partion_left_middle(A, B, b, p, r)
        fuzzysort(A, B, p, q-1)
        fuzzysort(A, B, r+1, s)

#A = np.array([5,1,4,8])
#B = np.array([7,3,6,10])
A = np.array([6,9,13,3,11,13,12,14,9,5,7,1,1,6])
B = np.array([7,11,14,7,15,14,14,15,15,7,9,5,9,10])
print ("Array A is " + str(A))
print ("Array B is " + str(B))
fuzzysort(A, B, 0, len(A) -1)

