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


print "<h2>Project Name: Test</h2>"


if pv('quantidade') and pv('velocidadeVentos') and pv('horasSol'):

    quantidade = int(pv('quantidade'))
    velocidadeVentos = int(pv('velocidadeVentos'))
    horasSol = int(pv('horasSol'))

    print "<h2>Amount of energy: " + str(quantidade) + " kWh/month</h2>"

    print "<h2>Characteristics of the region:</h2>"

    print "<font size = 5 face=Arial>Windspeed: " + str(velocidadeVentos) +" Km/h<br>"

    print "Sun full: " + str(horasSol) +" hours/day</font><br><br>"

    print "<hr><hr>"

    if velocidadeVentos==0 and horasSol==0:
        print "<div align=center><font size=6 face=Verdana color=green><b>Unable to generate the defined energy!</b></font></div>"
    else:

        local = Local()
        local.setQuantidade(quantidade)
        local.setVelocidadeVentos(velocidadeVentos)
        local.setHorasSolPleno(horasSol)

        eolica, solar = calculatesEnergy(local)
        
        print "<div align=center><font size = 6 face=Verdana color=green><b>Decision System</b></font></div><br>"
        
        print "<font size = 6 face=Arial><u>1. Wind Energy</u></font><br><br>"

        cadaEolica = eolica.getEnergiaGeradaEquipamento()
        quantidadeGeradaEolica = eolica.getEnergiaGeradaTotal()
        numEquipamentosEolica = eolica.getNumeroEquipamentos()
        
        print "<font size = 5 face=Arial>- " +  str(numEquipamentosEolica) + " Wind Turbines "
        if numEquipamentosEolica != 0:
            print "of " + str(eolica.getPotencia()) + " kW of power rating</font><br>"
            print "<font size = 5 face='Times New Roman'>Each Wind Turbine will generate " + str(cadaEolica) + " kWh/month<br>"
            print "<font size = 5 face= 'Times New Roman' color=green>"+str(numEquipamentosEolica)+"</font>"
            print " X "+ str(cadaEolica) +" = " + str(quantidadeGeradaEolica) +" kWh/month</font><br>"
        else:
            print "</font><br>"

        print "<br><br><br>"

        print "<font size = 6 face=Arial><u>2. Solar Energy</u></font><br><br>"

        cadaSolar = solar.getEnergiaGeradaEquipamento()
        quantidadeGeradaSolar = solar.getEnergiaGeradaTotal()
        numEquipamentosSolar = solar.getNumeroEquipamentos()

        print "<font size = 5 face=Arial>- " +  str(numEquipamentosSolar) + " Solar Panels "
        if numEquipamentosSolar != 0:
            print "of " + str(solar.getPotencia()) + " kW of power rating</font><br>"
            print "<font size = 5 face='Times New Roman'>Each Solar Panel will generate " + str(cadaSolar) + " kWh/month<br>"
            print "<font size = 5 face= 'Times New Roman' color=green>"+str(numEquipamentosSolar)+"</font>"
            print " X " + str(cadaSolar) + " = " + str(quantidadeGeradaSolar) +" kWh/month</font><br>"

        else:   
            print "</font><br>"

        print "<br><br><br>"


        print "<div align = center><font size= 6 face=Verdana><b>Amount Generated: </font>"
        
        quantidadeGeradaTotal = quantidadeGeradaEolica + quantidadeGeradaSolar
        print "<font size = 6 face= 'Times New Roman'>" + str(quantidadeGeradaEolica) + " + " + str(quantidadeGeradaSolar) + " = </font>"
        print "<font size = 6 face= 'Times New Roman' color=green>" + str(quantidadeGeradaTotal) + " kWh/month</font></b></div><br>"
        

else:
    
    print "<form method=post>"
    print """
    <font size = 4 face=Arial>Amount of energy (kWh/month):
    <input name=quantidade type=number min=0 required><br>
    
    Windspeed (Km/h):
    <input name=velocidadeVentos type=number min=0 required><br>
    
    Hours of Sun (per day): </font>
    <input name=horasSol type=number min=0 max=24 required>
    """
    print "<input type=submit value=Calculate><br><br>"

    
    data_uri = open('satelite.png', 'rb').read().encode('base64').replace('\n','')
    img_tag = '<img src="data:image/png;base64,{0}" width=1000 height=425>'.format(data_uri)
    print img_tag
    

print "</body>"
print "</html>"
