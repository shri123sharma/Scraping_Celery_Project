def split_list(value):
    result=list(value)
    return result

def partheses_checker(str_x):
    l1=split_list(str_x)
    is_symmetric = True
    print(l1)
    for i in range(len(l1)//2):
        if l1[i]!=l1[-i-1]:
            is_symmetric=False
        # break
    if is_symmetric:
        print("this is symeetric")
    else:
        print("this is not symmetric")
        
value="{([])}"
print(partheses_checker(value))