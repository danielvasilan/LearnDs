#from sklearn.datasets import load_iris
    
# Load the Iris dataset
#data = load_iris()

# pGet feature values
#print('The feature values for Obs 0 are: ', data.data[0])



""" from unicodedata import name
ret = {chr(i) : name(chr(i), '') for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(ret)
 """


import sys
import math

message = input()

message_bits = ""
for c in message:
    message_bits += str(bin(ord(c)))[2:].zfill(7)

unary_message = ""
crt_bit = "x"
for bit in message_bits:
    if crt_bit != bit:
        crt_bit = bit
        if unary_message != "":
            unary_message += " "
        if bit == "1":
            unary_message += "0"
        else:
            unary_message += "00"
        unary_message += " 0"
    else:
        unary_message += "0"


print (message_bits)
print(unary_message)

print(bin(ord("%")))