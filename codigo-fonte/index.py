print "Content-Type:text/html; charset=UTF-8\n"
print "<!doctype html>"
print "<html>"
print "<body>"
print "<body bgcolor=#DCDCDC>"


print "<font color=green><h3>EnergyCAD</h3></font>"
print "</form><hr>"


quantidade = 3010
potenciaEquipamentoEolica = 2.4
potenciaEquipamentoSolar = 2

print "<h2>Nome do Projeto: Teste</h2>"
print "<h2>Quantidade de energia: " + str(quantidade) +  " Kwh/mês</h2>"


velocidadeVentos = 38 #em Km/h
horasSol = 8 #quantidade de horas/dia de sol pleno

print "<img src=http://1.bp.blogspot.com/_8ooikrhoj48/TNrUSYeFqwI/AAAAAAAAAb8/0AiZg0tSguQ/s1600/llllll.png width=1000 height=450/><br><br>"

print "<font size = 6 face=Verdana><u>Características da região</u></font><br><br>"

print """
    <font size = 5 face=Arial>Velocidade dos ventos: """ + str(velocidadeVentos) +" Km/h</font><br>"

print """
    <font size = 5 face=Arial>Sol pleno: """ + str(horasSol) +" horas/dia</font><br>"

print "<br><br><br><br>"

from energyCalculation import *

numEolica, numSolar = calculatingEquipmentNumber(velocidadeVentos,horasSol,quantidade)

print "<font size = 8 face=Verdana>Para gerar a quantidade definida será preciso: </font><br>"
print "<font size = 6 face=Arial>- " +  str(numEolica) + " aerogeradores de " + str(potenciaEquipamentoEolica) + " kW de potência</font><br>"
print "<font size = 6 face=Arial>- " +  str(numSolar) + " painéis solares de " + str(potenciaEquipamentoSolar) + " kW de potência</font><br>"

print "<input type=button value='Ver Decisão do Sistema' onclick=\"location.href='detalhamento';\">"

print "</body>"
print "</html>"



