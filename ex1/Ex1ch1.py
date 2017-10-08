#!/usr/bin/python
# -*- coding: UTF-8 -*-

def hextobase64(decodedstr):
    rawstr = decodedstr.decode('hex')
    print rawstr.encode('base64')

decodedstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
hextobase64(decodedstr)

#the raw string is "I'm killing your brain like a poisonous mushroom"
#the result is "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"