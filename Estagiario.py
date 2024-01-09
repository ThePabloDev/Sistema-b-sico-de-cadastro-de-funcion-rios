class estagiario(object):

        def cadastro_E():
            Nome_E = (str(input("Insira o nome completo do Funcionário: ")))
            Endereco_E = (str(input("Insira o Endereco do Funcionário: ")))
            CPF_E_valido = False
            while not CPF_E_valido:
                 CPF_E = (input("Insira o CPF do Funcionário (Apenas Numeros): "))
                 if CPF_E.isdigit():
                     CPF_E_valido = True
                
            Data_E = (str(input("Insira a Data de Admissao do Funcionário (xx/xx/xx): ")))

            Horas_validas = False
            while not Horas_validas:
                 Horas_E = (input("Quantas horas extras foram trabalhadas: "))
                 if Horas_E.isdigit():
                     Horas_validas = True
                 else:
                    print("Insira apenas Numeros!")

            return Nome_E, Endereco_E, CPF_E, Data_E, Horas_E
        



