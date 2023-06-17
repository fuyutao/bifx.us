#!/usr/bin/python
import sys
import re

f = open(sys.argv[1],"r") #fasta input
nstart = 0
for line in f:
  if re.search(r'[^NATCGnatcg\W]',line[0])==None and nstart>0:
    sys.stdout.write(chr+":"+str(nstart)+"-"+str(length)+"\n")
    nstart = 0
  if line[0]==">":
    chr = line[1:-1]
    length = 0
  else:
    for m in re.finditer(r'[^NATCGnatcg\W]+',line):
      if nstart==0: nstart=length+m.start()+1
      if m.end()<len(line)-1:
        sys.stdout.write(chr+":"+str(nstart)+"-"+str(length+m.end())+"\n")
        nstart = 0
    length += len(line)-1
f.close()
if nstart>0: sys.stdout.write(chr+":"+str(nstart)+"-"+str(length)+"\n")

#def main():
#
#if __name__ == '__main__':
#    main()
