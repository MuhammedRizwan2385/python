#Read a string and store each character and their occurrence in a dictionary with character as key and count as value
s=input("enter the string: ")
dict={}
for i in range(len(s)):
    count=s.count(s[i])
    dict[s[i]]=count
print(dict)
