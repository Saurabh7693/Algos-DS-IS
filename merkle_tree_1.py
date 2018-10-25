import hashlib
'''
Name: Saurabh Jaiswal
Id: 801082240

This is Merkle Tree implementation as part Mid term for Blockchain course.

'hashlib' library has been used to calculate for hash function implementation. 'SHA-256' hash function
is used for hashing values. 
The code has 2 main functions namely elemhash and merkle_impl. 
elemhash is used for hashing and merkle_impl is used for recursion over hashed elements till a merkle root is found.
List hashlist is used to store all the hashs and is implemented in tree form and a dictionary dic_store is used
store the element and their respective hashs.
input and print_op are used for taking input from user and printing the output respectively.
 
'''

class merkleTree():
    def __init__(self):
        self.dic_store = {}
        self.hash_list = []
        self.counter = 0
        self.input()

    def elem_hash(self, element):
        '''
        This function takes 1 input, converts it into string and calculates the SHA-256 hash of the element.
        It then stores the input in a list called hashlist and a dictionary dic_store and appends a counter used
        to calculate the number of new elements hashed.
        '''

        element = str(element)
        hash1 = hashlib.sha256(element).hexdigest()

        # store in dic and list
        self.hash_list.insert(0, hash1)
        self.dic_store[element] = str(hash1)
        self.counter += 1


    def merkle_impl(self, array1):
        '''
        merkle_impl takes the given user input as a list and passes to elem hash to calculate
        the hash of each input element.
        It then concatenated 2 inputs of hash_list at a time and recurssivly calls elemhash
        to produce hash and store them. If element has no adjacent element then it is hashed alone again.
        This is continued till we get a merkle root.
        '''

        #Getting hash of inputs
        for i in range(0, len(array1)):
            self.elem_hash(array1[i])

        #Recursion
        while self.counter != 1:
            combined = []
            for i in range(self.counter, 0, -2):
                if i != 0:
                    temp = self.hash_list[i - 1] + self.hash_list[i - 2]
                else:
                    temp = self.hash_list[i - 1]
                combined.append(temp)

            self.counter = 0
            for j in range(0, len(combined)):
                self.elem_hash(combined[j])
        self.print_op(array1)

    def print_op(self, array1):
        '''
        This function is used to produce proper output. It loops over the list hash_list to produce output.
        '''

        i = len(array1)
        r = ""
        root = self.hash_list[0]
        print ("Given inputs are")
        print array1
        print ("Respective hashs are")
        while i != 1:
            for k in range(0, i):
                r = r + " " + str(self.hash_list.pop(-1))
            print r
            r = ""
            i = float(i)
            i = int(round(i / 2))
        print ("Merkle root is ")
        print root

    def input(self):
        '''
        Used to get input from user and store them in a list.
        '''

        print ("Welcome to merkle tree implementation")
        array1 = [num for num in raw_input("Enter your inputs separated by a single space :").split()]
        #array1 = ["data_1", "data_2", 1, 5, "data_5"]
        self.merkle_impl(array1)

mt = merkleTree()
