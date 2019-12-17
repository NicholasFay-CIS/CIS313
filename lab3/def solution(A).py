def solution(A):
    # write your code in Python 3.6
    max = 0
    max2 = 0
    inc = 0
    arr_af = []
    arr_el = []
    for item in A:
        if(item > max):
            max = item
    while(inc != max):
        if(inc not in A):
            arr_af.append(inc)
            inc+= 1
    for item in arr_af:
        if item > max2:
            max2 = item
    return max2
    
solution([1,2,3])