print "Content-Type:text/html; charset=UTF-8\n"
print "<!doctype html>"
print "<html>"
print "<body>"
print "<body bgcolor=#DCDCDC>"

from energyCalculation import *
import cgi


POST = cgi.FieldStorage()

def pv(x):
    if(POST.getvalue(x)):return POST.getvalue(x)
    return ''

print "<font color=green><h3>EnergyCAD</h3></font>"
print "</form><hr>"


velocidadeVentos = 38 #em Km/h
horasSol = 8 #quantidade de horas/dia de sol pleno

print "<h2>Nome do Projeto: Teste</h2>"


if pv('quantidade'):

    quantidadeString = pv('quantidade')

    print "<h2>Quantidade de energia: " + quantidadeString + " kWh/mês</h2>"

    print "<h2>Características da região:</h2>"

    print "<font size = 5 face=Arial>Velocidade dos ventos: " + str(velocidadeVentos) +" Km/h<br>"

    print "Sol pleno: " + str(horasSol) +" horas/dia</font><br><br>"

    print "<hr><hr>"

    if quantidadeString.isdigit():
        
        quantidade = int(pv('quantidade'))

        local = Local()
        local.setQuantidade(quantidade)
        local.setVelocidadeVentos(velocidadeVentos)
        local.setHorasSolPleno(horasSol)

        eolica, solar = calculatingEquipmentNumber(local)
        
        cadaEolica = eolica.getEnergiaGeradaEquipamento()
        cadaSolar = solar.getEnergiaGeradaEquipamento()

        print "<font size = 7 face=Verdana color=green>Para gerar a quantidade definida será preciso: </font><br><br>"
        
        print "<font size = 6 face=Arial><u>1. Energia Eólica</u></font><br><br>"

        quantidadeGeradaEolica = eolica.getEnergiaGeradaTotal()
        numEquipamentosEolica = eolica.getNumeroEquipamentos()
        
        print "<font size = 5 face=Arial>- " +  str(numEquipamentosEolica) + " Aerogeradores "
        if numEquipamentosEolica != 0:
            print "de " + str(eolica.getPotencia()) + " kW de potência</font><br>"
            print "<font size = 5 face='Times New Roman'>Cada Aerogerador vai gerar " + str(cadaEolica) + " kWh/mês<br>"
            print "<font size = 5 face= 'Times New Roman' color=green>"+str(numEquipamentosEolica)+"</font>"
            print " X "+ str(cadaEolica) +" = " + str(quantidadeGeradaEolica) +" kWh/mês</font><br>"
        else:
            print "</font><br>"

        print "<br><br><br>"

        print "<font size = 6 face=Arial><u>2. Energia Solar</u></font><br><br>"

        quantidadeGeradaSolar = solar.getEnergiaGeradaTotal()
        numEquipamentosSolar = solar.getNumeroEquipamentos()

        print "<font size = 5 face=Arial>- " +  str(numEquipamentosSolar) + " Paineis Solares "
        if numEquipamentosSolar != 0:
            print "de " + str(solar.getPotencia()) + " kW de potência</font><br>"
            print "<font size = 5 face='Times New Roman'>Cada Painel Solar vai gerar " + str(cadaSolar) + " kWh/mês<br>"
            print "<font size = 5 face= 'Times New Roman' color=green>"+str(numEquipamentosSolar)+"</font>"
            print " X " + str(cadaSolar) + " = " + str(quantidadeGeradaSolar) +" kWh/mês</font><br>"

        else:
            print "</font><br>"

        print "<br><br><br>"

        print "<div align = center><font size= 6 face=Verdana><b>Decisão do sistema:</font>"

        quantidadeGeradaTotal = quantidadeGeradaEolica + quantidadeGeradaSolar
        print "<font size = 6 face= 'Times New Roman'>" + str(quantidadeGeradaEolica) + " + " + str(quantidadeGeradaSolar) + " = </font>"
        print "<font size = 6 face= 'Times New Roman' color=green>" + str(quantidadeGeradaTotal) + " kWh/mês</font></b></div><br>"

    else:
        print "<div align = center><font size= 6 face=Verdana color=green>Entrada inválida!</font></div>"

else:   

    print "<form method=post>"
    print """
    <font size = 4 face=Arial>Quantidade de energia (kWh/mês): </font>
    <input name=quantidade>
    """
    print "<input type=submit value=Calcular><br><br>"
    
    print "<img src=http://1.bp.blogspot.com/_8ooikrhoj48/TNrUSYeFqwI/AAAAAAAAAb8/0AiZg0tSguQ/s1600/llllll.png width=1000 height=450/><br><br>"


print "</body>"
print "</html>"
