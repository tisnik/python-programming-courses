fout = open("data.txt", "a")

for i in range(1, 11):
    fout.write(str(i) + "\n")

fout.close()
