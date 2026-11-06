
def counting(n, values):
    treestreak = 1
    values = [6,3,1,5]
    for i in values[:n]:
        if values[i] > 1:
            treestreak += 1
            print(treestreak)
        if i < values[i]:
            treestreak = 0
            print(treestreak)
            break
            
print(counting(4, [6, 3, 1, 5]))