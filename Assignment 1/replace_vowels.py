Str="Manasvi"
vowels="AEIOUaeiou"
for char in Str:
    if char in vowels:
        Str=Str.replace(char,"z")
print("My new name is ",Str)