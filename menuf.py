#####################
# FUNÇÕES & MODULOS #
#####################


global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
import os, sys, pyfiglet
from time import sleep

def clear():
	os.system('clear')


##################
# MENU PRINCIPAL #
##################

print(f'{G}      --- FEITO POR {B} {G} LIPEZIN{B} </> {G}---')
result = pyfiglet.figlet_format("Home", font = "cosmic" )
print(f'''{C}{G}
{result}''')
print(f'    {C}======================================')
print(f'{C}    [{G} 1{C} ]{R} BAIXAR METASPLOIT( Gushmazuko) {G}')
print(f'{C}    [{G} 2{C} ]{R} NMAP')
print(f'{C}    [{G} 3{C} ]{R}THEHARVESTER')
print(f'{C}    [{G} 4{C} ]{R} CRIADOR')
print(f'{C}    [{G} 5{C} ]{R} MEU CHAT')
print(f'{C}    [{G} 6{C} ]{R} ROOT NO TERMUX')
print(f'    {C}======================================')
print(f'{C}   [{R} * {C}] DIGITE A OPCAO POR NUMERO')
opc = input(f'{G}\n\n   --> SELECIONE A OPÇÃO DESEJADA: ')



if opc == '1':
	os.system('''
	pkg install postgresql

pkg install openssh wget curl git -y

wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh

chmod +x metasploit.sh

./metasploit.sh''')


if opc == '4':
	os.system('termux-open-url https://WA.me/+553588317681')
	
	result = pyfiglet.figlet_format(" Menu", font = "cosmic" )



if opc == '3':
	os.system('git clone https://github.com/laramies/theHarvester')
	
	
	if opc == '2':
		os.system('git clone https://github.com/nmap/nmap')
		
result = pyfiglet.figlet_format(" BY LIPE", font = "cosmic" )
print(f'''{C}{G}
{result}''')

if opc == '5':
		os.system('termux-open-url https://chat.whatsapp.com/FCJM7bozPOMAJwwWzeAU5k')
		
		
if opc == '6':
	os.system('''
	apt update && apt -y upgrade

pkg install -y git

pkg install -y proot

termux-setup-storage

git clone https://github.com/Anonymous-Zpt/T-root

cd T-root

bash install.sh

./start ''')
