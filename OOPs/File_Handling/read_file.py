# f=open("sample.txt","r")
# print(f.read())


# f=open("sample.txt","r")
# print(f.read(5))


# f=open("sample.txt","r")
# print(f.readline(), end=" ")
# print(f.readline())

# READING ENTIRE FILE USING READLINE

f= open("sample.txt","r")
# while True:
#     data1 = f.readline()
#     if data1 == '':
#         break
#     else:
#         print(data1, end= " ")
        
print(f.readlines())
f.close()
