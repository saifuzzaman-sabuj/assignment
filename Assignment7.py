inputs=str(input("Enter the inputs: "))
digits=["0","1","2","3","4","5","6","7","8","9"]
litters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
total_digits=0
total_litters=0
for i in inputs:
    if i in digits:
        total_digits+=1
    else:
        total_litters+=1
print(total_digits)
print(total_litters)