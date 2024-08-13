
import random;

def ordenados():
    data = [1, 2, 3, 4, 6, 5]
    for j in range(1, len(data)): 
        temp = data[j]
        i = j - 1
        
        
        while i >= 0 and temp < data[i]:
            data[i + 1] = data[i]
            i = i - 1
            
       
        data[i + 1] = temp
        
    return data
        
        
        
        
        
def ordenados_inversa():
    data = [1, 2, 3, 4, 5]
    for x in range(len(data)):
        lista_rev = data[::-1]
    return lista_rev
    
    
def elemetno_dup():
    data = [1,2,1,3,4,5]
    for j in range(1, len(data)): 
        temp = data[j]
        i = j - 1
        
        
        while i >= 0 and temp < data[i]:
            data[i + 1] = data[i]
            i = i - 1
            
       
        data[i + 1] = temp
        
    return data
        
def random_aa():
    lista = []
    
 
    for i in range(0, 6):
        a = random.randint(0, 6)
        
        if a in lista:
            lista.remove(a)
        else:
            lista.append(a)
    
   
    for j in range(1, len(lista)): 
        temp = lista[j]
        i = j - 1
        
        while i >= 0 and temp < lista[i]:
            lista[i + 1] = lista[i]
            i = i - 1
            
        lista[i + 1] = temp
        
    return lista
    
    
    
print(ordenados())
print(ordenados_inversa())
print(elemetno_dup())
print(random_aa())
      
