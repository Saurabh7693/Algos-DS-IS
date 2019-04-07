import csv
import sys
import datetime

#This is implementation of FIFO Calculator for CoinFund technical test.
#Created by: Saurabh Jaiswal
class fifoCalculator():

    '''
    This function is takes file name as input.
    It then reads the csv file and processes it for various validation checks.
    Post that it maintains a dictionary of each asset to calculate its total value,
    remaining assets, current price and Profit and Loss on them.
    '''
    def traverse_txns(self,file):
        self.asset_dic1 = {}
        #print("Inside do operations")
        with open(file) as csvFile:
            reader = csv.reader(csvFile)
            tx_count = -1
            #Validation: Check input file is blank
            if not csvFile.read(1):
                self.error = "Error: Given input file is empty"
                print("Error: Given input file is empty")
            for row in reader:
                if tx_count ==-1:
                    tx_count +=1
                    prev_date = None
                    continue
                else:
                    try:
                        #Check for date format
                        curr_date = datetime.datetime.strptime(row[0], "%m/%d/%Y")
                        #print(prev_date)
                        if prev_date == None:
                            prev_date = datetime.datetime.strptime(row[0], "%m/%d/%Y")
                        elif (curr_date < prev_date):
                            print("Error:Given date is less than previous date.")
                            self.error = "Error:Given date is less than previous date."
                            return self.error
                        # Validations: Check asset length and 'USD' value.
                        elif len(row[1]) > 3:
                            print("Error:Length of asset name more than 3.")
                            self.error = "Error:Length of asset name more than 3."
                            return  self.error
                        elif row[1] == 'USD':
                            print("Error:Asset name 'USD' not allowed")
                            self.error = "Error:Asset name 'USD' not allowed"
                            return  self.error
                        else:
                            prev_date = datetime.datetime.strptime(row[0], "%m/%d/%Y")
                    except ValueError:
                        print("Error:Date format incorrect. "+ str(row[0]) + " Should be in MM/DD/YYYY")
                        self.error = "Error:Date format incorrect. "+ str(row[0]) + " Should be in MM/DD/YYYY"
                        return self.error

                    #For first new asset entry
                    if row[1] not in self.asset_dic1:
                        self.asset_dic1[row[1]] = {'current_price': int(row[2])}
                        self.asset_dic1[row[1]]['Error'] = False
                        self.asset_dic1[row[1]]['rem_asset'] = 0
                        self.asset_dic1[row[1]]['P&L'] = 0
                        tx_count += 1
                        if int(row[3]) < self.asset_dic1[row[1]]['rem_asset']:
                            self.asset_dic1[row[1]]['Error'] = "Error: detected sale before purchase (short selling is not supported)"
                        else:
                            self.asset_dic1[row[1]]['rem_asset'] = int(row[3])
                            self.asset_dic1[row[1]]['trnxs'] = [[int(row[2]), int(row[3])]]
                    else:
                        tx_count+=1
                        if not self.asset_dic1[row[1]]['Error']:
                            self.asset_dic1[row[1]]['trnxs'] += [[int(row[2]), int(row[3])]]
                            self.asset_dic1[row[1]]['current_price'] = int(row[2])

                            # Check for short selling if amount is negative (ie. sell).
                            if int(row[3]) < 0:
                                if (-int(row[3])) > self.asset_dic1[row[1]]['rem_asset']:
                                    #print("Error")
                                    #print((-int(row[3])), self.asset_dic1[row[1]]['rem_asset'])
                                    self.asset_dic1[row[1]]['Error'] = "Error: number of assets sold exceed purchases for asset " + str(row[1]) + " (short selling is not supported)"
                                else:
                                    tx_list = self.asset_dic1[row[1]]['trnxs']
                                    #tx_count = (len(self.asset_dic1[row[1]]['trnxs']))
                                    for j in range(len(tx_list)-1):
                                        #print(tx_list[j], (-int(tx_list[-1][1])))
                                        if tx_list[j][1] >= (-int(tx_list[-1][1])):
                                            #print((int(row[2]) - tx_list[j][0]) * (-int(row[3])))
                                            self.asset_dic1[row[1]]['P&L'] += (int(row[2]) - tx_list[j][0]) * (-int(tx_list[-1][1]))
                                            tx_list[j][1] += int(tx_list[-1][1])
                                            tx_list[-1][1] = 0
                                            break
                                        else:
                                            #print((int(row[2]) - tx_list[j][0]) * (tx_list[j][1]))
                                            self.asset_dic1[row[1]]['P&L'] += (int(row[2]) - tx_list[j][0]) * (tx_list[j][1])
                                            tx_list[-1][1] += tx_list[j][1]
                                            #print(tx_list[-1])
                                            tx_list[j][1] = 0
                                    self.asset_dic1[row[1]]['rem_asset'] += int(row[3])
                            else:
                                self.asset_dic1[row[1]]['rem_asset'] += int(row[3])
                    #print(self.asset_dic1[row[1]])
    '''
    This function creates a output file and writes the required Portfolio values in it.
    '''
    def write_output(self,file):
        name = file[:-4] + '.txt'
        totalportval = 0
        totalplval = 0
        f = open(name,'w')
        if self.error:
            f.write(self.error)
        else:
            keylen = len(self.asset_dic1.keys())
            f.write("Portfolio (" + str(keylen) + " assets)" + "\n")
            for key,val in self.asset_dic1.items():
                #print (key, self.asset_dic1[key]['Error'])
                if not self.asset_dic1[key]['Error']:
                    asset_value = self.asset_dic1[key]['rem_asset'] * self.asset_dic1[key]['current_price']
                    totalportval += asset_value
                    f.write(str(key) + ": " + str(self.asset_dic1[key]['rem_asset']) +" $"+ str(asset_value) +"\n")
                    totalplval += self.asset_dic1[key]['P&L']
                else:
                    #print(key + ":" + self.asset_dic1[key]['Error'])
                    f.write(str(key) + " :" + self.asset_dic1[key]['Error'] +"\n")
            f.write("Total portfolio value: $" + str(totalportval) + "\n")
            f.write("Portfolio P&L (" + str(keylen) + "assets): \n")
            for key, val in self.asset_dic1.items():
                if not self.asset_dic1[key]['Error']:
                    f.write(str(key) + ": $"+ str(self.asset_dic1[key]['P&L']) + "\n")
            f.write( "Total P&L: $" + str(totalplval) + "\n")
        f.close()

    def __init__(self):
        #initialize variables
        self.error = False
        self.statements = []
        self.asset_dic = {}

arguments = sys.argv
obj = fifoCalculator()
error = obj.traverse_txns(arguments[1])
obj.write_output(arguments[1])
print("Processing done. Kindly check the output file")
