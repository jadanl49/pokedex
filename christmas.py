
def counting(n, values):
    treestreak = 1
    current_dec = 1
    best_inc= 0 
    best_dec = 0
    for i in range(n-1):
        if h[i] > h[i+1]:
            current_dec += 1
            if current_dec > best_dec:
                best_dec = current_dec
        elif h[i] < h[i+1]:
            treestreak += 1
            if treestreak > best_inc:
                best_inc = treestreak
        else: 
            treestreak = 1
            current_dec = 1
h = [1,3,5,2]
            
