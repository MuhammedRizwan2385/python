#Write a Python program to read a text file and store the count of occurrences of each character in a dictionary.

# Open the file in read mode
f = open("fileprograms/input.txt", 'r')
text = f.read()
linee=text.strip()
print(linee)

# Create an empty dictionary to store character counts
char_count = {}

# Loop through each character in the text
for i in range(len(linee)):
    if(linee[i]==" "or linee[i]=='\n'):
        continue
    count=linee.count(linee[i])
    char_count[linee[i]]=count
print(char_count)
