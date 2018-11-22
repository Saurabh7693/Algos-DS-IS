'''
Id: 801082240
Code for Coin changes assignment
'''

# Function for part 'a'
def coin_changes_a(n):
    changes = [25, 10, 5, 1]
    coins = []
    print "Change is required for " + str(n) + " cents"
    print "Coins available are"
    print changes
    print "Coins required are"
    remaining = n
    i = 0
    while i != len(changes):
#        print i
        if (changes[i] <= remaining):
            remaining = remaining - changes[i]
#            print remaining
            coins.append(changes[i])
        else:
            i += 1
    return coins;
	
# Function for part 'b'
def coin_changes_b(n,c,k):
    changes = []
    for i in range(0, k):
        changes.append(c**i)
    coins = []
    print "Given value of c is " + str(c)
    print "Given value of k is " + str(k)
    print "So, the coins available are"
    print changes
    print "Coins required for " + str(n) + " cents are"
    remaining = n
    i = len(changes)
    while i != 0:
#        print i
        if (changes[i-1] <= remaining):
            remaining = remaining - changes[i-1]
#            print remaining
            coins.append(changes[i-1])
        else:
            i -= 1
    return coins;

a = coin_changes_a(217)
print a
b = coin_changes_b(50,6,3)
print b    



    
    
    
    
    
