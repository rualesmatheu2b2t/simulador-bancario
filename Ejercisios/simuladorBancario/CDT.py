class CDT:
    #aqui va el codigo

    '''----------------------------------------------------------------------------------------------------------------------------------------------------
     # Atributos 
    ----------------------------------------------------------------------------------------------------------------------------------------------------'''
    valorInvertido=0
    interesMensual=0
    mesApertura=0

    '''----------------------------------------------------------------------------------------------------------------------------------------------------
     # Metodo
    ----------------------------------------------------------------------------------------------------------------------------------------------------'''

    def ValorInvertido(self):
        #aqui va el codigo
        return "su Valor Invertido es de: "+ self.valorInvertido
        
    def InteresMensual(self):
        #aqui va el codigo
        interes = self.valorInvertido*self.interesMensual
        nValorInvertido = self.valorInvertido + interes
        self.valorInvertido = nValorInvertido
        return self.valorInvertido
    