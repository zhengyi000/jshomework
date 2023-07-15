import sys,os

with open("temp.html") as fp:
    fs=fp.read()

p165=list(range(1,20))
p183=list(range(1,6))
p197=list(range(1,6))

for x in p165:
    with open("P165T%d.html"%x,"w") as fp:
        fp.write(fs)

for x in p183:
    with open("P183T%d.html"%x,"w") as fp:
        fp.write(fs)

for x in p197:
    with open("P197T%d.html"%x,"w") as fp:
        fp.write(fs)