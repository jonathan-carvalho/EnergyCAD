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


def calculatingEquipmentNumber(local):

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

	quantidadeGerada = 0
	numeroEquipamentosEolica = 0
	numeroEquipamentosSolar = 0
	
	while (quantidadeGerada < quantidadePretendida):

                for i in range(2):
                        quantidadeGerada += energiaGeradaEolica
                        numeroEquipamentosEolica += 1
                        if quantidadeGerada >= quantidadePretendida:
                                break
                else:
			quantidadeGerada += energiaGeradaSolar
			numeroEquipamentosSolar += 1


	eolica = EnergiaLocal()
        eolica.setNumeroEquipamentos(numeroEquipamentosEolica)
        eolica.setPotencia(potenciaEolica)
        eolica.setEnergiaGeradaEquipamento(energiaGeradaEolica)
        eolica.setEnergiaGeradaTotal(numeroEquipamentosEolica*energiaGeradaEolica)
        
	solar = EnergiaLocal()
	solar.setNumeroEquipamentos(numeroEquipamentosSolar)
	solar.setPotencia(potenciaSolar)
        solar.setEnergiaGeradaEquipamento(energiaGeradaSolar)
        solar.setEnergiaGeradaTotal(numeroEquipamentosSolar*energiaGeradaSolar)

	return eolica, solar
