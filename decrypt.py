from helper import *
from encrypt import *
from helper import _64bitArrayToString
from keyGeneration import *
def decrypt(filename="",key=""):
	text="$'3puf#(,o?y}~:147#`ev38}`5 `u`"
	key="abcdefgh"

	roundKeys=generateReverseKey(key)
	bitArray=stringTo64BitArray(text)
	decryptedBitArray=[]

	for i in bitArray:
		decryptedBitArray.append(encryptString(i,roundKeys))

	return _64bitArrayToString(decryptedBitArray)



if __name__=="__main__":
	print(decrypt())