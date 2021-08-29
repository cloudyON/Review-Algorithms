def InsSort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

semp = [1,2,5,6,7,6,5]
InsSort(semp)
print(semp)
        
def MergeSort(a):
    n = len(a)
    if n <= 1:
        return
    
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    MergeSort(g1)
    MergeSort(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else :
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1


temp = [1,6,4,2,8,7,9,3]
MergeSort(temp)
print(temp)
