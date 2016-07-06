def calculatingEquipmentNumber(velocidadeVentos, horasSol, quantidadePretendida):

	energiaGeradaEolica = (800.0/36)*velocidadeVentos
	energiaGeradaSolar = (300.0/5)*horasSol

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

	return numeroEquipamentosEolica, numeroEquipamentosSolar
