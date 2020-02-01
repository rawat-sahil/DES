from encrypt import encrypt as en
from decrypt import decrypt as de
from optparse import OptionParser

def main(options,args):
	if (options.filename == False) and (options.text ==False) :
		print("specify a file or give the text in the command line with -t option")
		return 
	if len(options.key)<8 or len(options.key)>8:
		print("key length should be 8")

	if options.encrypt:
		if(options.filename != False):
			en(filename=options.filename,key=options.key)
		else:
			en(text=options.text,key=options.key)
		return
	if options.decrypt:
		if(options.filename != False):
			de(filename=options.filename,key=options.key)
		else:
			de(text=options.text,key=options.key)
		return


parser=OptionParser()
parser.add_option("-f","--file",dest="filename",default=False,help="put the filename to get the text from")
parser.add_option("-e","--encrypt",dest="encrypt",default=False,action="store_true",help="use this option to encrypt")
parser.add_option("-d","--decrypt",dest="decrypt",default=False,action="store_true",help="use this option to decrypt")
parser.add_option("-k", "--key",dest="key",help="enter the key here")
parser.add_option("-t","--text",dest="text",default=False,help="this options is if you want to specify the text in the command line option itself")
(options,args)=parser.parse_args()
# print(options)
# print(args)
main(options,args)
# a=en(text="abcd",key="abcdefgh")
# de(text=a,key="abcdefgh")
