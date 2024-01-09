# importanddo bibliotecas
import keyboard
import os

# importando classes
from Senior import senior as s
from Junior import junior as j
from Pleno import pleno as p
from Estagiario import estagiario as e
from Supervisor import supervisor as sv

# func_estagiario = []
# func_junior = []
# func_pleno = []
# func_senior = []
# func_supervisor = []


# definindo funcao para "continuar"
def continuar():
    print("Pressione qualquer botão para continuar...")
    keyboard.read_event()

# definindo funcao para limpar terminal
def limpar():
    os.system("cls")

def valida():
    print("Digite uma opção valida")

def obter_informacoes(nome, lista_nomes, lista_enderecos, lista_cpfs, lista_datas, lista_horas):
    if nome in lista_nomes:
        indice = lista_nomes.index(nome)
        print("\n")
        print(f"Informações para o funcionário {nome}:")
        print(f"Endereço: {lista_enderecos[indice]}")
        print(f"CPF: {lista_cpfs[indice]}")
        print(f"Data de contratação: {lista_datas[indice]}")
        print(f"Horas extras trabalhadas: {lista_horas[indice]}")
        print("\n")
        continuar()
    else:
        print("Não existe ninguém com esse nome.")
        continuar()


# definindo arquivo principal
def main():

    # lista de funcionarios
    func_estagiario = ['Fernando', 'Monica']
    func_junior = ['Kaio']
    func_pleno = ['João', 'Samuel']
    func_senior = ['Amanda']
    func_supervisor = ['Thais']

    # lista enderecos de funcionarios    
    endereco_estagiario = ['Prudentópolis', 'Guarapuava']
    endereco_junior = ['Brasília']
    endereco_pleno = ['Rio de Janeiro', 'São Paulo']
    endereco_senior = ['Guamiranga']
    endereco_supervisor = ['Prudentólis']

    # lista de CPF funcionarios
    cpf_estagiario = ['11829317237', '24628404518' ]
    cpf_junior = ['49150379674']
    cpf_pleno = ['11291272143', '43652144708']
    cpf_senior = ['65743645663']
    cpf_supervisor = ['95531238215']

    # lista de datas funcionarios
    data_estagiario = ['21/05/2020', '02/04/2021']
    data_junior = ['14/09/2020']
    data_pleno = ['23/06/2022', '12/03/2023']
    data_senior = ['02/04/2019']
    data_supervisor = ['07/09/2017']

    # lista de horas funcionarios
    hora_estagiario = ['5', '7']
    hora_junior = ['10']
    hora_pleno = ['6', '4']
    hora_senior = ['9']
    hora_supervisor = ['8']

    verificar = True

    while verificar:

        # definindo funcao menu
        def menu():
                print("""Olá, Bem Vindo ao sistema de cadastro de funcionarios, selecione uma das opçoes abaixo para prosseguir:
                
                    1 - Cadastramento de Novo Funcionário
                    2 - Funcionários Cadastrados
                    3 - Editar Funcionário
                    4 - Deletar Funcinário
                    5 - Sair do Sistema 
                    """)
                            
        menu()

        while verificar:
            try:
                MenuOption = int(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
                break
            except ValueError:
                print("Por favor, insira um número válido.")



        if MenuOption == 1:
                limpar()
                print("""Selecione o tipo de funcionário que deseja cadastrar:
                    
                    1 - Estagiário
                    2 - Junior
                    3 - Pleno
                    4 - Senior
                    5 - Supervisor""")
                
                
                while verificar:
                    try:
                        Nivel_Option_a = int(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
                        break
                    except ValueError:
                        print("Por favor, insira um número válido.")


                if Nivel_Option_a == 1:
                    limpar()
                    Nome_E, Endereco_E, CPF_E, Data_E, Horas_E = e.cadastro_E()
                    func_estagiario.append(Nome_E)
                    endereco_estagiario.append(Endereco_E)
                    cpf_estagiario.append(CPF_E)
                    data_estagiario.append(Data_E)
                    hora_estagiario.append(Horas_E)
                    limpar()

                if Nivel_Option_a == 2:
                    limpar()
                    Nome_J, Endereco_J, CPF_J, Data_J, Horas_J = j.cadastro_J()
                    func_junior.append(Nome_J)
                    endereco_junior.append(Endereco_J)
                    cpf_junior.append(CPF_J)
                    data_junior.append(Data_J)
                    hora_junior.append(Horas_J)
                    limpar()

                if Nivel_Option_a == 3:
                    limpar()
                    Nome_P, Endereco_P, CPF_P, Data_P, Horas_P = p.cadastro_P()
                    func_pleno.append(Nome_P)
                    endereco_pleno.append(Endereco_P)
                    cpf_pleno.append(CPF_P)
                    data_pleno.append(Data_P)
                    hora_pleno.append(Horas_P)
                    limpar()

                if Nivel_Option_a == 4:
                    limpar()
                    Nome_S, Endereco_S, CPF_S, Data_S, Horas_S = s.cadastro_S()
                    func_senior.append(Nome_S)
                    endereco_senior.append(Endereco_S)
                    cpf_senior.append(CPF_S)
                    data_senior.append(Data_S)
                    hora_senior.append(Horas_S)
                    limpar()

                if Nivel_Option_a == 5:
                    limpar()
                    Nome_SV, Endereco_SV, CPF_SV, Data_SV, Horas_SV = sv.cadastro_SV()
                    func_supervisor.append(Nome_SV)
                    endereco_supervisor.append(Endereco_SV)
                    cpf_supervisor.append(CPF_SV)
                    data_supervisor.append(Data_SV)
                    hora_supervisor.append(Horas_SV)
                    limpar()

        if MenuOption == 2:
            limpar()
            print("""Escolha o nivel que deseja verificar:
                    
                        1 - Estagiário
                        2 - Junior
                        3 - Pleno
                        4 - Senior
                        5 - Supervisor
                    """)
            
            while verificar:
                try:
                    Nivel_Option_b = int(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
                    break
                except ValueError:
                    print("Por favor, insira um número válido.")


            if Nivel_Option_b == 1:
                print(func_estagiario)
                nome = (str(input("Digite o nome do funcionário que deseja verificar informações: ")))
                obter_informacoes(nome, func_estagiario, endereco_estagiario, cpf_estagiario, data_estagiario, hora_estagiario)
                continuar()
                limpar()

            elif Nivel_Option_b == 2:
                print(func_junior)
                nome = (str(input("Digite o nome do funcionário que deseja verificar informações: ")))
                obter_informacoes(nome, func_junior, endereco_junior, cpf_junior, data_junior, hora_junior)
                continuar()
                limpar()

            elif Nivel_Option_b == 3:
                print(func_pleno)
                nome = (str(input("Digite o nome do funcionário que deseja verificar informações: ")))
                obter_informacoes(nome, func_pleno, endereco_pleno, cpf_pleno, data_pleno, hora_pleno)
                continuar()
                limpar()

            elif Nivel_Option_b == 4:
                print(func_senior)
                nome = (str(input("Digite o nome do funcionário que deseja verificar informações: ")))
                obter_informacoes(nome, func_senior, endereco_senior, cpf_senior, data_senior, hora_senior)
                continuar()
                limpar()

            elif Nivel_Option_b == 5:       
                print(func_supervisor)
                nome = (str(input("Digite o nome do funcionário que deseja verificar informações: ")))
                obter_informacoes(nome, func_supervisor, endereco_supervisor, cpf_supervisor, data_supervisor, hora_supervisor)
                continuar()
                limpar()

        if MenuOption == 3:
            limpar()
            print("""Selecione um dos niveis:
                
                    1 - Estagiário
                    2 - Junior
                    3 - Pleno
                    4 - Senior
                    5 - Supervisor
                
                """)
            
            while verificar:
                try:
                    Nivel_Option_c = int(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
                    break
                except ValueError:
                    print("Por favor, insira um número válido.")

        
            if Nivel_Option_c == 1:
                limpar()
                print(func_estagiario)
                nome = (str(input("Digite o nome do funcionário que deseja editar: ")))

                if nome in func_estagiario:
                    func_estagiario.remove(nome)
                    Nome_E, Endereco_E, CPF_E, Data_E, Horas_E = e.cadastro_E()
                    func_estagiario.append(Nome_E)
                    limpar()
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_c == 2:
                limpar()
                print(func_junior)
                nome = (str(input("Digite o nome do funcionário que deseja editar: ")))

                if nome in func_junior:
                    func_junior.remove(nome)
                    Nome_J, Endereco_J, CPF_J, Data_J, Horas_J = j.cadastro_J()
                    func_junior.append(Nome_J)
                    limpar()
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_c == 3:
                limpar()
                print(func_pleno)
                nome = (str(input("Digite o nome do funcionário que deseja editar: ")))
                if nome in func_pleno:
                    func_pleno.remove(nome)
                    Nome_P, Endereco_P, CPF_P, Data_P, Horas_P = p.cadastro_P()
                    func_pleno.append(Nome_P)
                    limpar()
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_c == 4:
                limpar()
                print(func_senior)
                nome = (str(input("Digite o nome do funcionário que deseja deletar: ")))
                if nome in func_senior:
                    func_senior.remove(nome)
                    Nome_S, Endereco_S, CPF_S, Data_S, Horas_S = s.cadastro_S()
                    func_senior.append(Nome_S)
                    limpar()

                else:
                    print("Não existe ninguem com esse nome")


            if Nivel_Option_c == 5:
                limpar()
                print(func_supervisor)
                nome = (str(input("Digite o nome do funcionário que deseja editar: ")))
                if nome in func_supervisor:
                    func_supervisor.remove(nome)
                    Nome_SV, Endereco_SV, CPF_SV, Data_SV, Horas_SV = sv.cadastro_SV()
                    func_supervisor.append(Nome_SV)
                    limpar()

                else:
                    print("Não existe ninguem com esse nome")

            else:       
                valida()
        

        
        if MenuOption == 4:
            limpar()
            print("""Selecione um dos niveis:
                   
                    1 - Estagiário
                    2 - Junior
                    3 - Pleno
                    4 - Senior
                    5 - Supervisor
                   
                  """)
             
            while verificar:
                try:
                    Nivel_Option_d = int(input("Insira o numero de acordo com a opcao que deseja selecionar: "))
                    break
                except ValueError:
                    print("Por favor, insira um número válido.")


            if Nivel_Option_d == 1:
                limpar()
                print(func_estagiario)
                nome = str(input("Digite o nome do funcionário que deseja remover: "))
                if nome in func_estagiario:
                    func_estagiario.remove(nome)
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_d == 2:
                limpar()
                print(func_junior)
                nome = str(input("Digite o nome do funcionário que deseja remover: "))
                if nome in func_junior:
                    func_junior.remove(nome)
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_d == 3:
                limpar()
                print(func_pleno)
                nome = str(input("Digite o nome do funcionário que deseja remover: "))
                if nome in func_pleno:
                    func_pleno.remove(nome)
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_d == 4:
                limpar()
                print(func_senior)
                nome = str(input("Digite o nome do funcionário que deseja remover: "))
                if nome in func_senior:
                    func_senior.remove(nome)
                else:
                    print("Não existe ninguem com esse nome")

            if Nivel_Option_d == 5:
                limpar()
                print(func_supervisor)
                nome = str(input("Digite o nome do funcionário que deseja remover: "))
                if nome in func_supervisor:
                    func_supervisor.remove(nome)
                else:
                    print("Não existe ninguem com esse nome")

            else:
                valida()

        if MenuOption == 5:
            break
        

if __name__ == '__main__':
    main()