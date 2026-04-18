# USING CONTEXT MANAGER (WITH)
# with open("sample.txt","a") as f:
#     f.write("\nRohit Bhai")

# with open("sample.txt", "r") as f:
#     print(f.read(10))
#     print(f.read(10))


# big_L= ["Virat Negi\n" for _ in range(100)]
# with open("virat.txt", "w") as f:
#     f.writelines(big_L)


with open("boss.txt", "r") as f:
    chunk_size=8
    
    while len(f.readline(chunk_size)) > 0:
        print(f.read(chunk_size), end= " | ")
        f.read(chunk_size)

 