#!/usr/bin/python

import hashlib
import sys
import getopt
from zeep import Client

#Step1: input dosya SHA256

    #Step2: etugra service client definition

WSDL = 'http://edocservice.e-tugra.com.tr/services/TsaService.asmx?wsdl'
SOAPClient = Client(wsdl=WSDL)

try:
    opts, args = getopt.getopt(sys.argv[1:],"tg:v:",["inputlogfile==","verifytimestamp"])
except getopt.GetoptError:
    print("etugra.py -t")
    sys.exit(2)
for opt, arg in opts:
    if opt == '-t':  #Check the current number of tokens left       
        print(SOAPClient.service.GetTsaCount('test','test'))
    elif opt  == '-g': #gettimestamp for a file
        inputfile = sys.argv[2]
        filecontent = open(inputfile,'r').read().encode('utf-8')
        sha = hashlib.sha256()
        sha.update(filecontent)
        timestamp = SOAPClient.service.GetTimeStamp(sha.digest(),'test','test')
        print(timestamp)
#Step3: input dizin ve etugra response file concat
