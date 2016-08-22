#!/usr/bin/python

import hashlib
import sys
from zeep import Client

#Step1: input dosya SHA256
inputfile = sys.argv[1]
filecontent = open(inputfile,'r').read().encode('utf-8')

sha = hashlib.sha256()
sha.update(filecontent)

#Step2: etugra service call
WSDL = 'http://edocservice.e-tugra.com.tr/services/TsaService.asmx?wsdl'
SOAPClient = Client(wsdl=WSDL)
print(SOAPClient.service.GetTsaCount('test','test'))

timestamp = SOAPClient.service.GetTimeStamp(sha.digest(),'test','test'))

print(SOAPClient.service.GetTsaCount('test','test'))

#Step3: input dizin ve etugra response file concat
