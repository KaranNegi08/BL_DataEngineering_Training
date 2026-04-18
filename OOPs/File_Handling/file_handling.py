
# f= open("sample.txt", "w")
# f.write("Hello world")
# f.close() 

# f=open("sample1.txt", "w")
# f.write("Hello world")
# f.write("\nHow  are you? ")
# f.close()

# f=open("sample.txt","w")
# f.write("My name is Salman khan")
# f.close()


# f=open("sample1.txt","a")
# f.write("\nI am appending this to file")
# f.close()

# L=["hello\n", "hi\n", "How are you\n", " i am tuple\n", "dict\n"]


# f= open("sample3.txt","w")
# f.writelines(L)


 




# f= open("sample.txt","r")
# print(f.readline())

# with open("sample.txt", "w") as f:
#     f.truncate(1)


with open("sample.txt", "w") as f:
    f.write("Virat Bhai\n")
    f.write("Rohit Bhai")
f.close()