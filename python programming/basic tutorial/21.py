#SEEK(),TELL()
f=open("mni.txt")
print(f.readline())
#print(f.tell())
print(f.readline())
#print(f.tell())
f.seek(11)
print(f.readline())
#print(f.tell())
f.close()