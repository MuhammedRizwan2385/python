#Write a code segment that opens a file for input and prints the number of four letter words in the file (8)
f=open("fileprograms/input.txt",'r')
count=0
text=f.read()
words=text.split()
print(words)
for i in range(len(words)):
    if(len(words[i])==4):
        count=count+1
print(count)
