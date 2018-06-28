fout = open("data.txt", "w")

for i in range(1, 11):
    fout.write(str(i) + "\n")

fout.close()
