#write and read

f=open("file1.txt","w+")
print(f)
f.write("appu\n")
f.write("Appu")
f.read(1)
if f.readable():
    print("readable")
else:
    print("not readable")
if f.writable():
    print("writable")
else:
    print("not writable")
f.close()