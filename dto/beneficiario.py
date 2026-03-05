class Beneficiario:
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__cnpj_empresa = None
        self.__email = None


    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser Vazio!")
        self.__nome = valor


    @property
    def cpf(self):
        return self.__cpf
    

    @cpf.setter
    def cpf(self, valor):
        if not valor:
            raise ValueError("O CPF não pode ser vazio!")
        self.__cpf = valor

    
    @property
    def cnpj_empresa(self):
        return self.__cnpj_empresa
    

    @cnpj_empresa.setter
    def cnpj_empresa(self, valor):
        if not valor:
            raise ValueError("O CNPJ não pode ser vazio!")
        self.__cnpj_empresa = valor

    
    @property
    def email(self):
        return self.__email
    

    @email.setter
    def email(self, valor):
        if not valor:
            print("O EMAIL não pode ser vazio!")
        self.__email = valor