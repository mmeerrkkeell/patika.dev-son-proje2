def reverse_list(a):
    a.reverse()
    result_list=[]
    for i in a:
        if type(i)==list:
            i.reverse()
            result_list.append(i)
        else:
            result_list.append(i)
        
    return result_list
    
print(reverse_list([[1, 2], [3, 4], [5, 6, 7]]))