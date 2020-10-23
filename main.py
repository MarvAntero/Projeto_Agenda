from Agenda import *
p = 0

#Inicio do programa
load()

while p != 1:
   imprimir_menu()
   try:
       opcao = int(input("Escolha uma opcao: "))
       if opcao == 1:
           mostrar_agenda()
       elif opcao == 2:
           nome = input("Insira o nome do contato a ser buscado: ")
           buscar_contato(nome)
       elif opcao == 3 :
           nome = input("Insira o nome do contato: ")
           try:
               AGENDA[nome]
               print(">>>>>>>>Contato já existe: ")
               continue
           except KeyError:
               print(">>>>>>>>Incluindo contato", nome)
               a = False
               incluir_editar_contato(nome, a)
       elif opcao == 4:
           nome = input("Insira o nome do contato: ")
           try:
               AGENDA[nome]
               print(">>>>>>>>Editando contato: ", nome)
               a = True
               incluir_editar_contato(nome, a)

           except KeyError:
               print(">>>>>>>>Contato inexistente")
       elif opcao == 5:
           nome = input("Insira o nome do contato a ser removido: ")
           remover_contato(nome)
       elif opcao == 6:
           name_file = input("Insira o nome/caminho do arquivo:")
           exportar_contatos(name_file)
       elif opcao == 7:
           name_file = input("Insira o nome/caminho do arquivo:")
           importar_contatos(name_file)
       elif opcao == 8:
           print(">>>>>>>>Agenda fechada")
           p += 1
       else:
           print("Escolha uma opcao valida")
   except ValueError as error:
       print("Input inválido, insira apenas numeros")
       print(error)