class Cnpj:
    def __init__(self, cnpj : str):
        self.__cnpj = str(cnpj)
        self.__RG1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self.__RG2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        
    def _regra1(self) -> bool:
        resul = False if len(self.__cnpj) != 14 else True
        return resul
        
    def _regra2(self):
        try:
            
            sumValida = 0
            for i in range(0,12):
                sumValida += int(self.__cnpj[i]) * int(self.__RG1[i])
            # REGRA 1: Se o resto for 0 ou 1, então o segundo dígito verificador será igual a 0.
            rDivisao = int(sumValida % 11)
            
            if (True if rDivisao in [0,1] else False):
                regra1 = str(self.__cnpj[12]) == "0"
                return regra1
            #REGRA 2: Se o resto for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, então o primeiro dígito verificador é 
            #a diferença entre o número 11 e o resto da divisão por 11
                        
            elif (True if rDivisao in [2, 3, 4, 5, 6, 7, 8, 9, 10] else False):
                regra2 = (11 - rDivisao) == int(self.__cnpj[12])
                return regra2
            
            else:
                return False
                
        except:
            return False
        
    def _regra3(self):
        try:
            sumValida = 0
            for i in range(0,13):
                sumValida += int(self.__cnpj[i]) * int(self.__RG2[i])
                
            rDivisao = sumValida % 11
            #REGRA 1: Se o resto for 0 ou 1, então o segundo dígito verificador será igual a 0.
            if (True if rDivisao in [0,1] else False):
                regra1 = str(self.__cnpj[13]) == "0"
                return regra1
            
            #REGRA 2: Se  o resto for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, então o segundo dígito verificador é a diferença entre o número 11 e o resto da divisão por 11
            elif (True if rDivisao in [2, 3, 4, 5, 6, 7, 8, 9, 10] else False):
                regra2 = (11 - rDivisao) == int(self.__cnpj[13])
                return regra2     
            
            else:
                return False
        except:
            return False
            
class ValidarCnpj(Cnpj):
    def __init__(self, cnpj : str):
        super().__init__(cnpj)
        self.__valida = [super()._regra1(), super()._regra2(), super()._regra3()]
        
    def cnValidar(self) -> bool:
        resul = True if False not in self.__valida else False
        return resul
