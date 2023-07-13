#number 1 starts_with()
"""
def starts_with(x : str, y : str) :
    
    if len(x) > len(y) :
        i=0
        while i < len(y):
            if x[i] != y[i]:
                
                print("x does not start with y.")
                return 0
            
            else:
                i+=1
    
        print("x starts with y.")
        return 1
   

x = input("please enter first string(x).")
y= input("Please enter the second string(y).")
try :
    if len(x) < len(y):
        raise IndexError("x is shorter than y.")
    starts_with(x , y) 
except IndexError:
    print("Index error raised.")
    """    


#number 2 ends_with()
"""
def ends_with(x : str, y : str):
    i = 0
    while i < len(y):
        if y[i] != x[len(x) - len(y) + i]:
            print("x does not end with y.")
            return 0
        else:
            i+=1
    print("x ends with y.")
    return 1

x = input("Enter the first string(x).")
y = input("Enter the second string(y).")
try :
    if len(x) < len(y) :
        raise IndexError("x is shorter than y.")
    ends_with(x , y)
except IndexError :
    print("IndexError raised")
    """

#numer 3 swap_strings()
"""
def swap_strings(x : str , y : str ) :
    
    
        tmp = y[:]
        y = x[:]
        x = tmp
        return x , y

x = input("Please enter the first string(x).")
y = input("Please enter the second string(y).")

x , y = swap_strings(x , y)
print(x)
print(y)
"""
#number 4 last not of
"""
def find_last_not_of(str1 , seq):
    lstr1 = list(str1)
    seq1 = list(seq)
    i = len(lstr1) - 1
    j = len(seq1) - 1

    while i >= 0 :
        while j >= 0 :
            if lstr1[i] != seq1[j]:
                return lstr1[i]
                break
            else:
                i -= 1
                j -= 1
    return 0    
i = input("Type something!")
j = input("Type a sequence of characters!")
k = find_last_not_of(i , j)
print(k)
"""
# number 5 rotate by
"""
def rotate_by(arr : list, num : int) :
    arr2 = []
    for i in range(num , len(arr)):
        arr2.append(arr[i])
    for j in range(0, num ) :
       arr2.append(arr[j])
    return arr2
new_arr = [1, 2 , 3 , 4, 5]
num = 3
k = rotate_by(new_arr , num)
print(k)

"""









