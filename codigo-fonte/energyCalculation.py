class Local():

        quantidadePretendida = 0
        velocidadeVentos = 0 
        horasSolPleno = 0

        def getQuantidade(self):
                return self.quantidadePretendida

        def setQuantidade(self, novaQuantidade):
                self.quantidadePretendida = novaQuantidade
                
        def getVelocidadeVentos(self):
                return self.velocidadeVentos

        def setVelocidadeVentos(self, novaVelocidade):
                self.velocidadeVentos = novaVelocidade


        def getHorasSolPleno(self):
                return self.horasSolPleno

        def setHorasSolPleno(self, novaHoras):
                self.horasSolPleno = novaHoras

class EnergiaLocal():

        numeroEquipamentos = 0
        potencia = 0
        energiaGeradaEquipamento = 0
        energiaGeradaTotal = 0

        def getNumeroEquipamentos(self):
                return self.numeroEquipamentos

        def setNumeroEquipamentos(self, novoNumeroEquipamentos):
                self.numeroEquipamentos = novoNumeroEquipamentos

        def getPotencia(self):
                return self.potencia

        def setPotencia(self, novaPotencia):
                self.potencia = novaPotencia

        def getEnergiaGeradaEquipamento(self):
                return self.energiaGeradaEquipamento

        def setEnergiaGeradaEquipamento(self, novaEnergiaGeradaEquipamento):
                self.energiaGeradaEquipamento = novaEnergiaGeradaEquipamento

        def getEnergiaGeradaTotal(self):
                return self.energiaGeradaTotal

        def setEnergiaGeradaTotal(self, novaEnergiaGeradaTotal):
                self.energiaGeradaTotal = novaEnergiaGeradaTotal
                          

                

def quantidadeEnergiaEolicaMes(potenciaEquipamento, velocidadeVentos):
        
        if potenciaEquipamento == 2.4:
                energiaGerada = 800
        elif potenciaEquipamento == 10:
                energiaGerada = 2800

        energiaGeradaEolica = (energiaGerada/36)*velocidadeVentos

        return energiaGeradaEolica



def quantidadeEnergiaSolarMes(potenciaEquipamento, horasSol):

        if potenciaEquipamento == 2:
                energiaGerada = 300
        elif potenciaEquipamento == 7:
                energiaGerada = 1000

        energiaGeradaSolar = (energiaGerada/5)*horasSol

        return energiaGeradaSolar


def calculatesEnergy(local):

        velocidadeVentos = local.getVelocidadeVentos()
        horasSol = local.getHorasSolPleno()
        quantidadePretendida = local.getQuantidade()


        if quantidadePretendida >= 5600:
                potenciaEolica = 10
        else:
                potenciaEolica = 2.4

        if quantidadePretendida >= 3000:
                potenciaSolar = 7
        else:
                potenciaSolar = 2


        energiaGeradaEolica = quantidadeEnergiaEolicaMes(potenciaEolica, velocidadeVentos)
	energiaGeradaSolar = quantidadeEnergiaSolarMes(potenciaSolar, horasSol)

	eolica = EnergiaLocal()
	eolica.setPotencia(potenciaEolica)
	eolica.setEnergiaGeradaEquipamento(energiaGeradaEolica)

        solar = EnergiaLocal()
        solar.setPotencia(potenciaSolar)
        solar.setEnergiaGeradaEquipamento(energiaGeradaSolar)


        if energiaGeradaEolica >= energiaGeradaSolar:
                maior = eolica
                menor = solar
        else:
                maior = solar
                menor = eolica

        energiaGeradaMenor = menor.getEnergiaGeradaEquipamento()
        energiaGeradaMaior = maior.getEnergiaGeradaEquipamento()

        porcentagem = energiaGeradaMenor*1.0/energiaGeradaMaior


        quantidadeGerada = 0
        numeroEquipamentosMaior = 0
	numeroEquipamentosMenor = 0
	
	
        while (quantidadeGerada < quantidadePretendida/(1+porcentagem)):

                quantidadeGerada += energiaGeradaMaior
                numeroEquipamentosMaior += 1

        while (quantidadeGerada < quantidadePretendida):

                quantidadeGerada += energiaGeradaMenor
                numeroEquipamentosMenor += 1

        maior.setNumeroEquipamentos(numeroEquipamentosMaior)
        maior.setEnergiaGeradaTotal(numeroEquipamentosMaior*energiaGeradaMaior)

        menor.setNumeroEquipamentos(numeroEquipamentosMenor)
        menor.setEnergiaGeradaTotal(numeroEquipamentosMenor*energiaGeradaMenor)


        return eolica, solar
