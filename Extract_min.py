import numpy as np

def extractMin(arr1, shape):
    '''
    This function is used to extract the minimum element at node [0,0] and replace
    it with infinity(100000 in this case). We call heapify to restore the matrix
    to its Young's tableau form
    '''

    min = arr1[0][0]
    arr1[0][0] = 100000
    print ("The minimum element is " + str((min)))
    heapify(arr1, shape)
    return min

def heapify(arr1, shape):
    '''
    This function takes matrix and converts it into Young's tableau. It compares
    element with its down and right neighbour to find lowest element.
    '''

    i = 0
    j = 0
    x = i
    y = j
    temp = 0


    while (x, y) != (shape[0] - 1, shape[1] - 1):
        if (j < shape[1] -1) and (arr1[i][j] > arr1[i][j + 1]):
            y = j + 1
            x = i

        if (i < shape[0] - 1) and (arr1[x][y] > arr1[i + 1][j]):
            x = i + 1
            y = j

        if arr1[x][y] == arr1[shape[0]- 1][shape[1]- 1]:
            x = shape[0] - 1
            y = shape[1] - 1

        temp = arr1[i][j]
        arr1[i][j] = arr1[x][y]
        arr1[x][y] = temp

        i = x
        j = y
    print ("Updated matrix is ")
    print arr1


def insertion(array, shape, ele):
    '''
    This function is used to insert element in Young's tableau.
    It finds the infinte element and then swaps it with element to be inserted.
    Then it compares new element with upper and left element to sort it back to
    Young's array
    '''

    arra1 = array
    temp = 0
    np.append(arra1, ele)
    index = np.where(arra1 == 100000)
    print "Insertion is possible at " + str(index[0][0]) + "," + str(index[1][0])
    arra1[index[0][0]][index[1][0]] = ele
    i = index[0][0]
    j = index[1][0]
    x = i
    y = j
    print ("Inserting new element " + str(ele))
    print ("New array is ")
    print arra1

    count = 1
    while (count > 0):
        count = 0
        if (j > 0) and (arra1[i][j] < arra1[i][j-1]):
            x = i
            y = j - 1
            count += 1

        if (i > 0) and (arra1[x][y] < arra1[i-1][j]):
            x = i - 1
            y = j
            count += 1

        if (x < i) or (y < j):
            temp = arra1[i][j]
            arra1[i][j] = arra1[x][y]
            arra1[x][y] = temp

        i = x
        j = y

    print "Updated array is "
    print arra1
    return arra1

def find(arr1, shape, ele):
    '''
    This function is used to find an element in Young's tableau.
    It starts with lower most left element and compares with element to find.
    If lower move up, if greater move right
    '''
    y = 0
    x = shape[0] - 1
    elefound = False
    while True:
        if ele == arr1[x][y]:
            elefound = True
            break
        elif ele < arr1[x][y]:
            x -= 1
        elif ele > arr1[x][y]:
            y += 1

        if x == 0 or y == shape[1] -1:
            break
        #print x, y, shape[1] -1
    if elefound == True:
        print ("Element found at position " +str(x) + "," + str(y))
    else:
        print ("Element not found ")


def arrayip():
    '''
    Main function to make a tableau and execute insertion, sorting, etc.
    '''

    arr1 = np.array([[0,3,4],[2,5,6],[10,11,15],[16,18,100000]])
    print ("Matrix is ")
    print arr1
    shape = np.shape(arr1)

    # Extract - min method
    print ("Executing Extract-min")
    min = extractMin(arr1, shape)
    print

    # Insertion of element
    print ("Executing insertion")
    ele = 1
    arr1 = insertion(arr1, shape, ele)
    print


    # Sorting
    print ("Executing Sorting")
    #total_el = shape[0] * shape[1]
    l = [3,0,4,5,6,10,11,15,2]
    arr2 = (np.ones((3,3),int)) * 100000
    shape2 = np.shape(arr2)
    temparr = arr2
    for x in l:
        print x
        temparr = insertion(arr2, shape2, x)
    arr2 = temparr

    minlist = []
    for x in l:
        temp = extractMin(arr2, shape2)
        minlist.append(temp)
    
    print "Array is "
    print arr2
    print "Sorted list is "
    print minlist
    print

    # Find
    print ("Executing Find")
    print ("Matrix is")
    print arr1
    ele = 18
    print ("Element to be found is " + str(ele))
    find(arr1, shape, ele)


arrayip()