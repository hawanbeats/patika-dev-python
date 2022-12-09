#Soru 2
'''
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
'''
list1 = [[1, 2], [3, 4], [5, 6, 7]]  
def reverse_list(l):
    l.reverse()
    reverse = [reverse_list(sublist) for sublist in l if type(sublist) == list]
reverse_list(list1)
print(list1)
