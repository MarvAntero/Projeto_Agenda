##############Projeto de uma agenda
AGENDA = {}  #Declarada como variavel global, não preciso passar ela como parametro para as funções




def buscar_contato(nome):
   a = 1
   for name in AGENDA:
       if nome == name: #testa se o contato está na agenda
           print("Dados de {}".format(name)) #Imprimindo nome do contato
           for dados in AGENDA[name]: #Imprimindo os dados do contato
               print(dados, ":", AGENDA[name][dados]) #Imprime os dados referentes a cada key
               # do nome contato
           break
       elif (nome !=name and a == len(AGENDA)): #Testa se o contato esta ou nao na agenda
           print("{} nao esta na agenda".format(nome))
       else:
           a += 1
#Fim do metodo

#Função para mostrar todos os contatos da agenda
def mostrar_agenda() :
   if AGENDA: ##Mesma coisa que if len(AGENDA) > 0:
       for contato in AGENDA:
           buscar_contato(contato)
           print("-------------------------------------------------")
   else:
       print(">>>>>>>>Agenda Vazia")
#Fim do metodo
#Uma função colocada dentro da outra

#Metodo para incluir/editar um contato

def incluir_editar_contato(nome, a):
   AGENDA[nome] = {}  #Estava dando erro pois nao tinha criado o dicionario
   tel = input("Insira o telefone do contato: ")
   email = input("Insira o email do contato: ")
   endereco = input("Insira o endereco do contato: ")
   AGENDA[nome]['telefone'] = tel
   AGENDA[nome]['email'] = email
   AGENDA[nome]['endereco'] = endereco
   save()
   print("-------------------------------")
   if a == True:
       print(">>>>>>> Contato {} editado com sucesso".format(nome))
   else:
       print(">>>>>>>> Contato {} adicionado com sucesso".format(nome))
   print("-------------------------------")
#Fim do metodo


#Metodo para remover um contato da agenda
def remover_contato(contato):
   try:
       AGENDA.pop(contato) #.pop é um metodo para excluir keys de um dicionario
       save()
       print("-------------------------------")
       print(">>>>>>>Contato {} excluido com sucesso".format(contato))
       print("-------------------------------")
   except KeyError: #Só existe esse erro possivel(keyerror, o que faria o programa crashar
       print(">>>>>>>>contato inexistente")
   except Exception as error: #Testar caso um erro aleatorio ocorra
       print(">>>>>>>>Um erro inesperado ocorreu")
       print(error)
#Fim do metodo

#MENU
def imprimir_menu():
   print("-------------------------------")
   print("1 - Mostrar todos os contatos da agenda")
   print("2 - Buscar Contato")
   print("3 - Incluir contato")
   print("4 - Editar contato")
   print("5 - Excluir contato")
   print("6 - Exportar contatos para CSV")
   print("7 - Importar contatos")
   print("8 - Fechar agenda")
   print("-------------------------------")

#Fim do metodo

#Exportar contatos
def exportar_contatos(name_file):

    try:
        with open(name_file, 'w') as file: #Criando arquivo
            #file.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write('{},{},{},{}\n'.format(contato,telefone,email,endereco)) #Escrevendo o nome do contato na agenda
                '''
                file.write(contato)
                for dados in AGENDA[contato]: ###jeito que achei mais bonito de se escrever
                    file.write('\n'+dados +':'+AGENDA[contato][dados])
                file.write("\n")'''

        print(">>>>>>>>Agenda exportada com sucesso")
    except Exception as error:
        print(">>>>>>>>Algum erro ocorreu")
        print(type(error))

#Fim do método

#Importar contatos
def importar_contatos(file_name):
    try:
        with open(file_name) as arquivo:
            conteudo = arquivo.readlines() #separa as linhas do arquivo em uma lista(Cada linha eh um indice)
            for linha in conteudo:
                detalhes = linha.strip().split(',') #Separa, por virgula, cada linha em uma lista de varios itens(cada string da linha eh um indice)
                AGENDA[detalhes[0]] = {}
                AGENDA[detalhes[0]]['telefone'] = detalhes[1]
                AGENDA[detalhes[0]]['endereco'] = detalhes[2]
                AGENDA[detalhes[0]]['email'] = detalhes[3]
               # print(">>>>>>>>Contato {} adicionado com sucesso".format(detalhes[0]))
        save()
    except FileNotFoundError:
        print(">>>>>>>>Arquivo nao encontrado")
    except Exception as error:
        print(">>>>>>>>Erro de abertura")
        print(error)

#Fim do metodo

def save():
    exportar_contatos('database.csv')

def load():
    importar_contatos('database.csv')