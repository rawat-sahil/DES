def tobits(s):
    charArray=[]
    for i in s:
        b='00000000'
        binaryString=bin(int(ord(i)))[2:]
        binaryString=b[len(binaryString):]+binaryString
        charArray.extend([int(b)for b in binaryString])
    return charArray

def frombits(charArray):
    chars=[]
    for b in range(len(charArray)//8) :
        bytes=charArray[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in bytes]),2)))

    return ''.join(chars)

def stringTo64BitArray(s):
    array=[]
    for i in range(8-len(s)%8):
        s=s+' '
    for i in range(len(s)//8):
        array.append(tobits(s[i*8:(i+1)*8]))

    return array

def _64bitArrayToString(array):
    s=""
    for i in array:
        s=s+frombits(i)

    return s

if __name__=="__main__":
    stringTo64BitArray(" ")