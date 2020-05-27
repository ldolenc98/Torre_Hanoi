def Menu():
    print("\n")
    print("***TORRE DE HANOI***")
    discos = int(input("Digite o número de discos: ")) 
    return discos

discos = Menu()
def Rodadas(discos):
    if discos == 0 or discos == 1:
        return 1
    else:
        return 2*Rodadas(discos-1)+1
     
movimentos = Rodadas(discos)
print("\n")
print("O número esperado de movimentos é: " + str(movimentos))
print("\n")

#A = Origem
#B = Destino
#C = Base

def movimento(discos,x,y):
    print("Movendo o disco " + str(discos) + " de " + x + " para " + y)
    
def Hanoi(discos, A, B, C):
    if discos == 1:
        movimento(discos, A, B)
    else:
        Hanoi(discos-1, A, C, B)
        movimento(discos,A, B)
        Hanoi(discos-1, C, B, A)


#Hanoi(discos,"A","B","C")
        
        
        
    
        
        
            
        
    
    
    


        





        
    



    


    
    