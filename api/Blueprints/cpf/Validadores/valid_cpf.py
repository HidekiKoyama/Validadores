class Cpf:
    def __init__(self, cpf : str) -> None:
        self.__cpf = str(cpf)
        self.__RG1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.__RG2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        
    def _regra1(self) -> bool:
        resul = False if len(self.__cpf) != 11 else True
        return resul
    
    # Validacao do primeiro digito validador
    def _regra2(self) -> bool:
        try:
            sumValida = 0
            for i in range(0, 9):
                sumValida += int(self.__cpf[i]) * int(self.__RG1[i])
            
            rDivisao = 0 if ((sumValida*10) % 11) == 10 else (sumValida*10) % 11
            
            if int(self.__cpf[9]) != rDivisao:
                return False
            else:
                return True
        except:
            return False
    #Validacao do segundo digito validador 
    def _regra2(self) -> bool:
        try:
            
            sumValida = 0
            for i in range(0, 10):
                sumValida += int(self.__cpf[i]) * int(self.__RG2[i])
            
            rDivisao = (sumValida * 10) % 11
            
            if int(self.__cpf[10]) != rDivisao:
                return False
            else:
                return True
            
        except:
            return False    
class ValidarCPF(Cpf):
    
    def __init__(self, cpf: str) -> None:
        super().__init__(cpf)
        self.__valido = [super()._regra1(), super()._regra2()]
        
    def cpValidar(self) -> bool:
        resul = False if False in self.__valido else True
        return resul
    
