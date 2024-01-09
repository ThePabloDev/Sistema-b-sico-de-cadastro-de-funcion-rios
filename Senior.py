class senior(object):

        def cadastro_S():
            Nome_S = (str(input("Insira o nome completo do Funcionário: ")))
            Endereco_S = (str(input("Insira o Endereco do Funcionário: ")))
            CPF_S_valido = False
            while not CPF_S_valido:
                 CPF_S = (input("Insira o CPF do Funcionário (Apenas Numeros): "))
                 if CPF_S.isdigit():
                     CPF_S_valido = True
                
            Data_S = (str(input("Insira a Data de Admissao do Funcionário (xx/xx/xx): ")))

            Horas_validas = False
            while not Horas_validas:
                 Horas_S = (input("Quantas horas extras foram trabalhadas: "))
                 if Horas_S.isdigit():
                     Horas_validas = True
                 else:
                    print("Insira apenas Numeros!")

            return Nome_S, Endereco_S, CPF_S, Data_S, Horas_S