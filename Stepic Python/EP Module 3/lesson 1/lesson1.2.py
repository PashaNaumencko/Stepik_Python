def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        else:
            l.remove(l[i])
lst = [1, 2, 3, 5, 7]
modify_list(lst)
print(lst)