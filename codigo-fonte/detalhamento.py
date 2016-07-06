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

print "<h2>Quantidade de energia: " + str(quantidade) +  " Kwh/mês</h2><br>"


print "<font size = 5 face=Verdana><u>1. Energia Eólica</u></font><br><br>"
print "<font size = 5 face='Times New Roman'>Aerogerador de " + str(potenciaEquipamentoEolica) + " kW de potência gera 844 Kwh/mês<br>"
print "<font size = 5 face= 'Times New Roman' color=green>3</font>"
print " X 844 = 2532 Kwh/mês</font><br>"

print "<br><br><br>"

print "<font size = 5 face=Verdana><u>2. Energia Solar</u></font><br><br>"
print "<font size = 5 face='Times New Roman'>Painél Solar de " + str(potenciaEquipamentoSolar) + " kW de potência gera 480 Kwh/mês<br>"
print "<font size = 5 face= 'Times New Roman' color=green>1</font>"
print " X 480 = 480 Kwh/mês</font><br>"

print "<br><br><br>"

print "<font size= 5 face=Verdana><b>Decisão do sistema: </b></font>"

print "<font size = 5 face= 'Times New Roman'> 2532 + 480 = </font>"
print "<font size = 5 face= 'Times New Roman' color=green>3012 Kwh/mês</font><br>"

print "</body>"
print "</html>"


