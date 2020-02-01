from helper import *
from encrypt import *
from helper import _64bitArrayToString
from keyGeneration import *
def decrypt(text=None,filename=None,key=None):
	textfile=None

	if(filename!=None):
		try:
			textfile=open(filename,"r")
		except:
			print("file not found")
			return 
		text=textfile.readlines()
		text="".join(text)

	roundKeys=generateReverseKey(key)
	bitArray=stringTo64BitArray(text)
	decryptedBitArray=[]

	for i in bitArray:
		decryptedBitArray.append(encryptString(i,roundKeys))

	if(filename!=None):
		decryptedTextFile=open("decrypted.txt","w")
		decryptedTextFile.writelines(_64bitArrayToString(decryptedBitArray))
		return

	decryptedString= _64bitArrayToString(decryptedBitArray)

	print(decryptedString)
	return decryptedString



if __name__=="__main__":
	print(decrypt())
	print(len(decrypt()))