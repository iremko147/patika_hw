"""
Bir listeyi düzleştiren (flatten) 
fonksiyon yazın. Elemanları birden 
çok katmanlı listtlerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar 
verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

totalElemansListe=[]

def toList(x):
    try:
        for i in x:
            if type(i)!=list:
                totalElemansListe.append(i)
                
            else:
                toList(i)
        return totalElemansListe
    except Exception:
        pass
    

print(toList([[1,'a',["irem",6],['cat'],2],[[[3]],'dog'],4,5]))


                    




