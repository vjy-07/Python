list1 = [1,2,3,4,5,6]

idx=0
x=4
for num in list1:
    if num==x:
        print(f"value found at index: {idx}")
        break
    else:
        idx+=1