Str=input("Enter a string: ")
count=0
ca=0
ce=0
ci=0
co=0
cu=0
vowels="AEIOUaeiou"
for char in Str:
    if char in vowels:
        count+=1
        if char.lower()=='a':
            ca+=1
        if char.lower()=='e':
            ce+=1
        if char.lower()=='i':
            ci+=1
        if char.lower()=='o':
            co+=1
        if char.lower()=='u':
            cu+=1
print("No. of vowels = ",count)
print("No. of 'a' = ",ca)
print("No. of 'e' = ",ce)
print("No. of 'i' = ",ci)
print("No. of 'o' = ",co)
print("No. of 'u' = ",cu)