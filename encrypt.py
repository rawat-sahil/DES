from helper import *
from helper import _64bitArrayToString
from tables import *
from keyGeneration import *

def encrypt(filename="", key=""):
	text="abcdefghijklmnopqrstuvwxyz"
	key="abcdefgh"

	roundKeys=generateKey(key)
	bitArray=stringTo64BitArray(text)
	encryptedBitArray=[]

	for i in bitArray:
		encryptedBitArray.append(encryptString(i,roundKeys))

	return _64bitArrayToString(encryptedBitArray)



def encryptString(s64bits,roundKeys):
	s64bits=initialPermutaion(s64bits)
	left=s64bits[0:32]
	right=s64bits[32:]
	for i in range(16):
		tempRight=functionF(right,roundKeys[i])

		for i in range(len(tempRight)):#this for loop for xoring output of functionF with left
			tempRight[i]=tempRight[i]^left[i]
		left=right
		right=tempRight

	(left,right)=bitSwap32(left,right)
	s64bits.clear()
	s64bits.extend(left)
	s64bits.extend(right)
	s64bits=finalPermutation(s64bits)
	return s64bits

def bitSwap32(left,right):
	return (right,left)

def initialPermutaion(s64bits):
	tempS=[]
	for i in intialPermutationTable:
		tempS.append(s64bits[i-1])
	return tempS

def finalPermutation(s64bits):
	tempS = []
	for i in finalPermutationTable:
		tempS.append(s64bits[i - 1])
	return tempS

def functionF(right, key):
	right=expansionPbox(right)
	for i in range(len(right)):
		right[i]=right[i]^key[i]
	right=sBox(right)
	right=straightPBox(right)
	return right


def straightPBox(s32bits):
	tempS = []
	for i in straightPermutationTable:
		tempS.append(s32bits[i - 1])
	return tempS

def sBox(s48bits):
	tempS=[]
	for i in range(48//6):
		tempS.extend(sBoxLookup(s48bits[i*6:(i+1)*6],S_BOX[i]))
	return tempS

def sBoxLookup(s6bits,table):
	entry1_6=str(s6bits[0])+str(s6bits[5])
	entry2_3_4_5=str(s6bits[1])+str(s6bits[2])+str(s6bits[3])+str(s6bits[4])

	temp=table[int(entry1_6,2)][int(entry2_3_4_5,2)]

	base="0000"
	binTemp=bin(temp)[2:]
	binTemp=base[len(binTemp):]+binTemp
	return [int(i) for i in binTemp]

def expansionPbox(s32bit):
	tempS=[]
	for i in expansionPboxTable:
		tempS.append(s32bit[i-1])
	return tempS

if __name__=="__main__":
	print(encrypt())
	print(len(encrypt()))
