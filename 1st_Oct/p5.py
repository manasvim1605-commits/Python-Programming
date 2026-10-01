L=[1,2,2,3,4,5,5,6,7,8,9,9,9,0]
new=[] #made a new list to store
for i in L: #entering the list
    check=False #boolean variable used to check if numbers are foumd
    for j in new: #entering the new list 
        if i==j: #checking if the number found is already in thenew list
            check=True #yess if it is
            break #come out of the loop
    if check==False: #if didn't find any same number in iteration i.e the condition is false 
        new.append(i) #directly add the number in the new list
print(new)
