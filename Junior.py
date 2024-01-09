class junior(object):

        
    def cadastro_J():
            Nome_J = (str(input("Insira o nome completo do Funcionário: ")))
            Endereco_J = (str(input("Insira o Endereco do Funcionário: ")))
            CPF_J_valido = False
            while not CPF_J_valido:
                 CPF_J = (input("Insira o CPF do Funcionário (Apenas Numeros): "))
                 if CPF_J.isdigit():
                     CPF_J_valido = True
                
            Data_J = (str(input("Insira a Data de Admissao do Funcionário (xx/xx/xx): ")))

            Horas_validas = False
            while not Horas_validas:
                 Horas_J = (input("Quantas horas extras foram trabalhadas: "))
                 if Horas_J.isdigit():
                     Horas_validas = True
                 else:
                    print("Insira apenas Numeros!")

            return Nome_J, Endereco_J, CPF_J, Data_J, Horas_J