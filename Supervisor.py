class supervisor(object):

        def cadastro_SV():
            Nome_SV = (str(input("Insira o nome completo do Funcionário: ")))
            Endereco_SV = (str(input("Insira o Endereco do Funcionário: ")))
            CPF_SV_valido = False
            while not CPF_SV_valido:
                 CPF_SV = (input("Insira o CPF do Funcionário (Apenas Numeros): "))
                 if CPF_SV.isdigit():
                     CPF_SV_valido = True
                
            Data_SV = (str(input("Insira a Data de Admissao do Funcionário (xx/xx/xx): ")))

            Horas_validas = False
            while not Horas_validas:
                 Horas_SV = (input("Quantas horas extras foram trabalhadas: "))
                 if Horas_SV.isdigit():
                     Horas_validas = True
                 else:
                    print("Insira apenas Numeros!")

            return Nome_SV, Endereco_SV, CPF_SV, Data_SV, Horas_SV