import feira

def textovd():
    print('#########################################')
    print('########## Veja sua Dispensa ############')
    print('#########################################')
    print('\n\t 1 - Ver por ordem alfabetica ')
    print('\n\t 2 - Ver por data de validade \n\t "da mais recente a mais antiga" ')
    print('\n\t 3 - Ver por preço \n\t "do mais barato ao mais caro" ')
    print('\n\t 4 - Ver por categoria ')
    print('\n\t 0 - Sair ')
    try:
        opcao = int(input())
    except:
        print("Opção inválida! Tente novamente.")
        opcao = int(input())
    return opcao

def menu_vd():
    opcao = textovd()
    while opcao != 0:
        
        if opcao == 1:
            op = alfabeticav()
        elif opcao == 2:
            op = validadev()
        elif opcao == 3:
            op = precov()
        elif opcao == 4:
            op = categoriav
        
        opcao = textovd()
    return

def alfabeticav():
    
    for i in sorted(feira.feira, key = feira.feira.get):
        print('\n Nome:',feira.feira[i][0], '\n\t','Categoria:',  feira.feira[i][1],'Quantidade atual:', feira.feira[i][3],'Preço:', feira.feira[i][4],'\n')


    return

def validadev():
    for i in sorted(feira.feira, key = feira.feira.get):
        # aux = float(feira.feira[i][4])
        # print(aux)
         print(feira.feira[i][4])
    print()
    return

def precov():
    print()
    return

def categoriav():
    print()
    return