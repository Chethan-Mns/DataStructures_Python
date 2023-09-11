def item_in_common(lst1, lst2):
    dict = {}
    for i in lst1:
        dict[i] = True
    for i in lst2:
        if i in dict:
            return True
    return False




list1 = [1,3,5]
list2 = [2,4,5]