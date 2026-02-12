
try:
    with open("sample.txt", 'rt') as fr:
        print(fr.read())
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found")
