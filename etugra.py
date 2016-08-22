#!/usr/bin/python

import hashlib
import sys
import base64
from zeep import Client

#Step1: input dosya SHA256 OK
#Step2: etugra service call
#Step3: input dizin ve etugra response file concat

inputfile = sys.argv[1]
filecontent = open(inputfile,'r').read().encode('utf-8')

sha = hashlib.sha256()
sha.update(filecontent)
print(sha.hexdigest())

WSDL = 'http://edocservice.e-tugra.com.tr/services/TsaService.asmx?wsdl'
SOAPClient = Client(wsdl=WSDL)
#print(SOAPClient.service.GetTsaCount('test','test'))

#hashbase64str = base64.b64encode(sha.hexdigest())

#print(hashbase64str)

#print(SOAPClient.service.GetTimeStamp(hashbase64str,'test','test'))

print(SOAPClient.service.GetTimeStamp1(sha.hexdigest(),'test','test'))
