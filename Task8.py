
with open("output.txt", 'wt') as fw:
        fw.write(input("Enter text to Write to the file :")+"\n")
        print("Data successfully written to output.txt")

with open("output.txt", 'at') as fa:
        fa.write(input("Enter text to append to the file :")+"\n")
        print("Data successfully appended")

with open("output.txt", 'rt') as fr:
    print(fr.read())
