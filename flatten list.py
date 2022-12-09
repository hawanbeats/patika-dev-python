#Soru 1
'''
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
'''
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []
def flatten(l):
    isFlatting = [flatten(sublist) if type(sublist) == list else flatten_list.append(sublist) for sublist in l]

flatten(list1)
print(flatten_list)
