from time import sleep

def Formatacao(LA, LB, LC, i, discos):
    tamanho1 = float((len(LA[i])/2))
    tamanho2 = float((len(LB[i])/2))
    tamanho3 = float((len(LC[i])/2))
    
    #space1
    if LA[i] == " ":
        space1 = " "* discos
    else:
        tamanho1 = int((len(LA[i])/2))
        space1 = " " *(discos - tamanho1)
        
    #space2   
    if LB[i] == " " and LA[i] == " ":
        space2 = " "* 12     
        
    elif LB[i] == " " and LA[i] != " ":
        tamanho1 = int((len(LA[i])/2))
        space2 = " " * (12 - (tamanho1 - 1))
        
    elif LB[i] != " " and LA[i] ==  " ":
        tamanho2 = int((len(LB[i])/2))
        space2 = " " * (12 - (tamanho2 - 1))
    
    else:
        tamanho1 = int((len(LA[i])/2))
        tamanho2 = int((len(LB[i])/2))
        if tamanho1 > tamanho2:
            space2 = " " * (12 - (tamanho1 - tamanho2))
        else:
            space2 = " " * (12 - (tamanho2 - tamanho1))
            
    #space3
    if LC[i] == " " and LB[i] == " ":
        space3 = " "* 13     
        
    elif LC[i] == " " and LB[i] != " ":
        tamanho2 = int((len(LB[i])/2))
        space3 = " " * (12 - (tamanho2-1))
        
    elif LC[i] != " " and LB[i] ==  " ":
        tamanho3 = int((len(LC[i])/2))
        space3 = " " * (12 - (tamanho3 - 1))
    
    else:
        tamanho3 = int((len(LC[i])/2))
        tamanho2 = int((len(LB[i])/2))
        if tamanho2 > tamanho3:
            space3 = " " * (12 - (tamanho2 - tamanho3 + 3))
        else:
            space3 = " " * (12 - (tamanho3 - tamanho2))  
            
    print(space1 + "[" + LA[i] + "]"  + space2+ "[" + LB[i] + "]" + space3 + "[" + LC[i] + "]" )
    """print(str(tamanho1) + str(LA[i]))
    print(str(tamanho2) + str(LB[i]))
    print(str(tamanho3) + str(LC[i]))"""

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
arquivo = open('passos.txt', 'w')
def movimento(discos,x,y):
    a = "Movendo o disco " + str(discos) + " de " + x + " para " + y + "\n"
    return a
    
def Hanoi(discos, A, B, C, arquivo):
    if discos == 1:
        print(movimento(discos,A,B))
        arquivo.write((movimento(discos, A, B)))
    else:
        Hanoi(discos-1, A, C, B, arquivo)
        print(movimento(discos,A,B))
        arquivo.write((movimento(discos, A, B)))
        Hanoi(discos-1, C, B, A, arquivo)
            
Hanoi(discos,"A","B","C", arquivo)
arquivo = open('passos.txt', 'r')
LA = []
LB = []
LC = []
i = 1
while i < discos + 1:
    LA.append("xx" * i)
    LB.append(" ")
    LC.append(" ")   
    i = i + 1
LA.append("erro")
LB.append("erro")
LC.append("erro")
i = 0
j = discos - 1
while i < discos:
    print(" "*j + "[" + LA[i] + "]"  + " "*j + "         " + "[" + LB[i] + "]" + "         "  + "[" + LC[i] + "]" )
    i = i + 1
    j = j - 1      
print("-" * (discos * 2 + 28))
print(" " *(discos + 1) + "A" + " " *(discos + 1) + " "*9 + "B" + " "*12 + "C")
escolha = input(str("Você deseja ver gráficamente o passo a passo?[S/N]: "))
print("\n")

if escolha == "N":
    ""
elif escolha == "S":
    for linha in arquivo:
        sleep(3)
        print(linha)
        a = linha
        disco = a[16]
        origem = a[21]
        destino = a[28]
        i = 0
        j = 0
        if origem == "A":
            while LA[i] == " ":
                i = i + 1
            if destino == "B":
                while LB[j+1] == " " and j != discos - 1:
                    j = j + 1
                LB[j] = LA[i]
                LA[i] = " "  
            else:
                while LC[j+1] == " " and j != discos - 1:
                    j = j + 1
                LC[j] = LA[i]
                LA[i] = " " 
            i = 0
            j = discos-1
            while i < discos:
                Formatacao(LA, LB, LC, i, discos)
                i = i + 1
                j = j - 1 
                
            print("-" * (discos * 2 + 32))
            print(" " *(discos + 1) + "A" + " " *(discos + 1) + " "*9 + "B" + " " *(discos + 1) + " "*11 + "C")
            print("\n")
            
        elif origem == "B":
            while LB[i] == " ":
                i = i + 1
            if destino == "A":
                while LA[j+1] == " " and j != discos - 1:
                    j = j + 1
                LA[j] = LB[i]
                LB[i] = " "    
            else:
                while LC[j+1] == " " and j != discos - 1:
                    j = j + 1
                LC[j] = LB[i]
                LB[i] = " "    
            i = 0
            j = discos-1
            while i < discos:
                Formatacao(LA, LB, LC, i, discos)
                i = i + 1
                j = j - 1 
                
            print("-" * (discos * 2 + 32))
            print(" " *(discos + 1) + "A" + " " *(discos + 1) + " "*9 + "B" + " " *(discos + 1) + " "*11 + "C")
            print("\n")
            
        else:
            while LC[i] == " ":
                i = i + 1
            if destino == "A":
                while LA[j+1] == " " and j != discos - 1:
                    j = j + 1
                LA[j] = LC[i]
                LC[i] = " "    
            else:
                while LB[j+1] == " " and j != discos - 1:
                    j = j + 1
                LB[j] = LC[i]
                LC[i] = " "    
            i = 0
            j = discos-1
            while i < discos:
                Formatacao(LA, LB, LC, i, discos)
                i = i + 1
                j = j - 1  
                
            print("-" * (discos * 2 + 32))
            print(" " *(discos + 1) + "A" + " " *(discos + 1) + " "*9 + "B" + " " *(discos + 1) + " "*11 + "C")
            print("\n")
            
        
else:
    print("Você deve digitar S ou N")
            
            
            
                
                
                
            
                
            
                
                
            
                                    
            
            


    