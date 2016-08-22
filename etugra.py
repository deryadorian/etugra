#!/usr/bin/python

import hashlib
import sys
import getopt
from zeep import Client
import base64

#etugra service client definitions
WSDL = 'http://edocservice.e-tugra.com.tr/services/TsaService.asmx?wsdl'
SOAPClient = Client(wsdl=WSDL)

try:
    opts, args = getopt.getopt(sys.argv[1:],"tg:v:",["inputlogfile==","verifytimestamp"])
except getopt.GetoptError:
    print("etugra.py -t                         Show the number of tokens left")
    print("etugra.py -g <file>                  Get the timestamp token of the <file>")
    print("etugra.py -v <file> <timestamp>      Verify the timestamp of the file")
    sys.exit(2)
for opt, arg in opts:
    if opt == '-t':  #Check the current number of tokens left       
        print(SOAPClient.service.GetTsaCount('test','test'))
    elif opt  == '-g': #gettimestamp for a file
        filecontent = open(sys.argv[2],'r').read().encode('utf-8')
        sha = hashlib.sha256() 
        sha.update(filecontent) #SHA256 of the input file
        timestamp = SOAPClient.service.GetTimeStamp(sha.digest(),'test','test') #TODO: input the user and password from parameter/configfile
        file = open(sha.hexdigest(),'wb') #Open file in binary mode
        file.write(timestamp['TimeStampEncoded']) #write the binary timestamp to hex sha256 named file