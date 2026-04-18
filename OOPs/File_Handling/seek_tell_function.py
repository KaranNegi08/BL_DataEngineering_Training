# with open("sample3.txt", "r") as f:
#     print(f.read(10))
#     print(f.tell())


# with open("sample.txt", "r") as f:
#     print(f.read(10))
#     f.seek(2)
#     print(f.read(10))


# seek during write
with open("sample4.txt", "w") as f:
    f.write("Hello")
    f.seek(11)
    f.write("Ka")