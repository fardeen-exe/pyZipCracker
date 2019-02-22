import zipfile
import argparse


def main(zipfilename,dictionary):  
 password=None
 zip_file=zipfile.ZipFile(zipfilename)
 with open (dictionary,'r') as f:
  for line in f.readlines():
   password=line.strip('\n')
   try:
    zip_file.extractall(pwd=password)
   except:
    pass 
	
 print password 
 
 
if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument("-z",'--z',action='store',dest="zipfilename",help="zip file name")
 parser.add_argument("-d",'--dict',action='store',dest="dictionary",help="password file with location")
 args=parser.parse_args()
 main(args.zipfilename,args.dictionary)
 
