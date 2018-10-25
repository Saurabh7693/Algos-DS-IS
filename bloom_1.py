import xxhash
from fnvhash import fnv1a_32 as fnv

'''
Name: Saurabh Jaiswal
Id: 801082240

This is Bloom filter implementation as part Mid term for Blockchain course

The 'bloom_array' is a list of length 100 and is used as a bit array to be updated as per output
of hash functions
For implementation I have use 2 non-cryptographic hash functions 'xxhash' and 'fnv'
Output of both hash functions is % 100 to keep its value less than 100. This helps in updating
the bloom_array.

It has 3 main functions 'genfilter', 'lookup' and 'updatefilter'. These are used to create a generate a
bloom filter, do lookup of a string in filter and update the filter with a new value.
'''

class bloomFilterimpl():
    def __init__(self):
        self.str1 = ''
        self.dicstore = {}

    def hashfunc(self, str1):
        '''
        This function takes a string as input and hashes them using xxhash and fnv hash
        It returns 2 hash values for the input.
        '''

        hasher1 = ((xxhash.xxh32(str1)).intdigest()) % 100

        hasher2 = fnv(str1) % 100

        return [hasher1, hasher2]

    def genfilter(self):
        '''
        This function is used to generate a bloom filer. It initializes a 'bloom_array' with 100 values
        all of '0'.
        It has an list of string values and
        takes their hash using hashfunc. It then updates the bloom_array at the values of output.
        It also creates a dictionary of inputs and hashs to showcase the values currently in filter.
        '''

        print "Welcome to Bloom filter implementation"

        self.bloom_array = [0] * 100
        print  "Bloom bit array is"
        print self.bloom_array
        print
        str1 = ['man@mail.com', 'a123@mail.com', 'abc@mail.com', 'test@mail.com']
        self.str1 = str1
        print "Data in Bloom filter"
        print self.str1
        print

        for i in self.str1:
            #print i
            temp = self.hashfunc(i)
            self.bloom_array[temp[0]] = 1
            self.bloom_array[temp[1]] = 1
            self.dicstore[i] = [temp[0], temp[1]]
        print "Generated hashes are "
        print self.dicstore
        print "Updated Bloom filter "
        print self.bloom_array
        print

    def lookup(self, str2):
        '''
        This function is used to lookup if a string is present in bloom filter.
        It procures a hash of the string to compared. Then it compares if the bloom_array value
        at that hash position is 1. If both the values are 1 then the word is mostly present in the filter.
        (Due to certain chances of collusion we cannot say with certainity if the value is 100% present)
        '''

        self.str2 = str2
        print "Word to be searched is "
        print self.str2
        store = self.hashfunc(self.str2)
        print "Word hashs are"
        print store[0], store[1]
        counter = 0
        for i in range(0, 2):
            if self.bloom_array[store[i]] == 1:
                counter += 1
        if counter == 2:
            print "Word is probably there in bloom filter"
        else: print "Word does not exist in current Bloom filter"

    def updatefilter(self,str3):
        '''
        This function is used to add a new value to the filter.
        The new value(str3) is first hashed using function hashfunc.
        Then it appends the value of bloom_array as per value of hashs and adds the word to dictionay.
        :return:
        '''
        print "Updating the filter. New word to be added is "
        self.str3 = str3
        temp = self.hashfunc(self.str3)
        print self.str3
        print "Generated hash output bits are "
        print temp[0], temp[1]
        self.bloom_array[temp[0]] = 1
        self.bloom_array[temp[1]] = 1
        self.dicstore[self.str3] = [temp[0], temp[1]]
        print "Updated bloom filter is"
        print self.bloom_array
        print "Total list of elements are"

bm = bloomFilterimpl()
bm.genfilter()
bm.lookup('test@mail.com')
bm.updatefilter('kim@mail.com')
bm.lookup('kim@mail.com')


