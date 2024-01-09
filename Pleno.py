class pleno(object):

        def cadastro_P():
            Nome_P = (str(input("Insira o nome completo do Funcionário: ")))
            Endereco_P = (str(input("Insira o Endereco do Funcionário: ")))
            CPF_P_valido = False
            while not CPF_P_valido:
                 CPF_P = (input("Insira o CPF do Funcionário (Apenas Numeros): "))
                 if CPF_P.isdigit():
                     CPF_P_valido = True
                
            Data_P = (str(input("Insira a Data de Admissao do Funcionário (xx/xx/xx): ")))

            Horas_validas = False
            while not Horas_validas:
                 Horas_P = (input("Quantas horas extras foram trabalhadas: "))
                 if Horas_P.isdigit():
                     Horas_validas = True
                 else:
                    print("Insira apenas Numeros!")

            return Nome_P, Endereco_P, CPF_P, Data_P, Horas_P