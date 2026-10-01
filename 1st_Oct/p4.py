Str=input("Enter a string ")
count=0
vowels="AEIOUaeiou"
for char in Str:
    if char in vowels:
        count+=1
print("No. of vowels = ",count)