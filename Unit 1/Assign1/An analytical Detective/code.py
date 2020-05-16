import os

print("Kindly put this file in the folder where you have lastsave.txt/the file which has all the operations")

print("Press 1 if your filename is lastsave.txt. Else press any other key")
n = input()

if(n=='1'):
    fname = "lastsave.txt"
else:
    print("Enter your filename")
    fname = input()
    if('.txt' not in fname):
        fname = fname+ '.txt'

f= open(fname, "r")
opfile = 'Youroutput.txt'
fw = open(opfile, "w+")

Lines = f.readlines() 
for x in Lines:
    if('>' in x):
        x = x[2:]
        fw.write(x)
fw.close()

print("Do you want to change the extension from .txt to .r? Press 1 for Yes.")
n = input()
if n=='1':
    base = os.path.splitext(opfile)[0]
    os.rename(opfile, base + '.r')