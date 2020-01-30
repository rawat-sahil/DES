from encrypt import encrypt as en
from decrypt import decrypt as de
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-f","--file",dest="filename",help="put the filename to get the text from")
parser.add_option("-e","--encrypt",dest="encrypt",default=False,action="store_true",help="use this option to encrypt")
parser.add_option("-d","--decrypt",dest="decrypt",default=False,action="store_true",help="use this option to decrypt")
(options,args)=parser.parse_args()
print(options)
print(args)
