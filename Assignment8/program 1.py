#program1
lines = 0
words = 0
chars = 0
fname = input("enter the name of file used:")
with open(fname, 'r') as f:
    data = f.read()
    lines = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
chars = (len(data) - len(spaces))
print("There are ", len(lines), "lines in the file.")
print("There are ", chars, "characters in the file.")
print("There are ", len(spaces), "spaces in the file.")
print("There are ", len(words), "words in the file.")

    
