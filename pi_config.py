from argparse import ArgumentParser
import configparser
from colorama import just_fix_windows_console
from colorama import Fore
from colorama import Back
from colorama import Style

# ########################
# Farbige Terminalausgaben
# ########################

just_fix_windows_console()

# ##################
# Argumente einlesen
# ##################

parser = ArgumentParser(
            description="GPIO-Konfiguration für Raspberry")

parser.add_argument(
            "-f",
            "--file",
            default="pi.config",
            dest="CLI_PARAM_CONFIG_FILE",
            required=False,
            metavar="Dateiname",
            help="Andere Konfigurationsdatei verwenden anstelle von pi.config")

parser.add_argument(
            "-v",
            "--verbose",
            default=False,
            dest="CLI_PARAM_VERBOSE",
            required=False,
            action="store_true",
            help="Vollständige Ausgabe mit Raspberry-ASCII-Zeichen")
args = parser.parse_args()

# ############################
# Konfigurationsdatei einlesen
# ############################
config = configparser.ConfigParser()
CONFIG_FILE=args.CLI_PARAM_CONFIG_FILE
config.read(CONFIG_FILE)

def getGPIO(gpio_id):

    # GPIO-Modus (IN oder OUT)
    mode = config.get('GPIO_{0}'.format(gpio_id), 'MODE', fallback='IN')
    if(mode=="IN"):
        mode=f'{Fore.GREEN}I{Fore.RESET}'
    elif(mode=="OUT"):
        mode=f'{Fore.RED}O{Fore.RESET}'
    else:
        mode=f'{Fore.BLUE}?{Fore.RESET}'
    
    name=config.get('GPIO_{0}'.format(gpio_id), 'NAME', fallback='')
    if(len(name)>16):
        name=name[:14]+'..'
    
    # Linke Seite des GPIO-Boards
    text=f' {name: >16} {mode}'
    if(gpio_id in [14,15,18,23,24,25,8,7,1,12,16,20,21]):
        # Rechte Seite des GPIO-Boards
        text=f'{mode} {name: <16} '
    return text

def printRaspberry(model):
    if(model in ["Rasberry Pi Model 2B v1.1"]):
        print(f'{Fore.GREEN}')
        print(f' ┌────────────────────────────────────────┐  ')
        print(f' │ {Fore.WHITE}₂₄₆₈₀{Fore.YELLOW}₂₄₆₈₀{Fore.CYAN}₂₄₆₈₀{Fore.MAGENTA}₂₄₆₈₀{Fore.GREEN}                ╔══╧═ ')
        print(f' │ {Fore.WHITE}₁₃₅₇₉{Fore.YELLOW}₁₃₅₇₉{Fore.CYAN}₁₃₅₇₉{Fore.MAGENTA}₁₃₅₇₉{Fore.GREEN}                ║ {Fore.RESET}USB{Fore.GREEN} ')
        print(f' │                                     ╚══╤═ ')
        print(f' │                                        │  ')
        print(f' │  │{Fore.RESET}D{Fore.GREEN}         ┌───┐                   ╔══╧═ ')
        print(f' │  │{Fore.RESET}S{Fore.GREEN}         │{Fore.RESET}CPU{Fore.GREEN}│                   ║ {Fore.RESET}USB{Fore.GREEN} ')
        print(f' │  │{Fore.RESET}I{Fore.GREEN}         └───┘                   ╚══╤═ ')
        print(f' │  │{Fore.RESET}0{Fore.GREEN}               {Fore.RESET}C{Fore.GREEN}│                   │  ')
        print(f' │                   {Fore.RESET}S{Fore.GREEN}│              ╔════╧═ ')
        print(f' │                   {Fore.RESET}I{Fore.GREEN}│   │{Fore.RESET}A{Fore.GREEN}│        ║   {Fore.RESET}LAN{Fore.GREEN} ')
        print(f' │ {Fore.RESET}POWER{Fore.GREEN}     |{Fore.RESET}HDMI{Fore.GREEN}|  {Fore.RESET}0{Fore.GREEN}│   │{Fore.RESET}U{Fore.GREEN}│        ╚════╤═ ')
        print(f' └──┤ ├──────┤    ├───────┤{Fore.RESET}X{Fore.GREEN}├─────────────┘')
        print(f'{Fore.RESET}')
        print('')
    else:
        print('')

print('')
print(f'{Fore.GREEN}GPIO-KONFIGURATION{Fore.RESET}')
print('')
if(args.CLI_PARAM_VERBOSE):
    raspberry_model=config.get('RASPBERRY', 'MODEL', fallback='UNKOWN')

    config_sections=config.sections()
    config_sections.remove('RASPBERRY')

    print(f'{Fore.GREEN}Konfigurationsdatei:{Fore.RESET} {CONFIG_FILE}')
    print(f'{Fore.GREEN}Modell:{Fore.RESET} {raspberry_model}')
    print(f'{Fore.GREEN}GPIOs:{Fore.RESET}\n{config_sections}')
    printRaspberry(raspberry_model)
    print(f'           {Style.BRIGHT}{Fore.GREEN} ↻ Raspberry um 90° nach rechts gedreht ↻ {Style.RESET_ALL}')
    print('')

pi_box_end=f'{Fore.GREEN}│{Fore.RESET}'
print('{0} ──────────────────────────────────────────────────────────────┐{1}'.format(Fore.GREEN, Fore.RESET))
print('{0: >63}{1}│{2}'.format("", Fore.GREEN, Fore.RESET))
print('{0: >19}    {1}3V3{2}  {3}(1) (2){4}  {5}5V{6}     {7: <19}{8}'.format("", Back.RED, Back.RESET, Fore.WHITE, Fore.RESET, Back.RED, Back.RESET, "", pi_box_end))
print('{0: >19}  {1}GPIO2{2}  {3}(3) (4){4}  {5}5V{6}     {7: <19}{8}'.format(getGPIO(2), "", "", Fore.WHITE, Fore.RESET, Back.RED, Back.RESET, "", pi_box_end))
print('{0: >19}  {1}GPIO3{2}  {3}(5) (6){4}  {5}GND{6}    {7: <19}{8}'.format(getGPIO(3), "", "", Fore.WHITE, Fore.RESET, Style.DIM, Style.NORMAL, "", pi_box_end))
print('{0: >19}  {1}GPIO4{2}  {3}(7) (8){4}  {5}GPIO14{6} {7: <19}{8}'.format(getGPIO(4), "", "", Fore.WHITE, Fore.RESET, "", "", getGPIO(14), pi_box_end))
print('{0: >19}    {1}GND{2}  {3}(9) (10){4} {5}GPIO15{6} {7: <19}{8}'.format("", Style.DIM, Style.NORMAL, Fore.WHITE, Fore.RESET, "", "", getGPIO(15), pi_box_end))
print('{0: >19} {1}GPIO17{2} {3}(11) (12){4} {5}GPIO18{6} {7: <19}{8}'.format(getGPIO(17), "", "", Fore.YELLOW, Fore.RESET, "", "", getGPIO(18), pi_box_end))
print('{0: >19} {1}GPIO27{2} {3}(13) (14){4} {5}GND{6}    {7: <19}{8}'.format(getGPIO(27), "", "", Fore.YELLOW, Fore.RESET, Style.DIM, Style.NORMAL, "", pi_box_end))
print('{0: >19} {1}GPIO22{2} {3}(15) (16){4} {5}GPIO23{6} {7: <19}{8}'.format(getGPIO(22), "", "", Fore.YELLOW, Fore.RESET, "", "", getGPIO(23), pi_box_end))
print('{0: >19}    {1}3V3{2} {3}(17) (18){4} {5}GPIO24{6} {7: <19}{8}'.format("", Back.RED, Back.RESET, Fore.YELLOW, Fore.RESET, "", "", getGPIO(24), pi_box_end))
print('{0: >19} {1}GPIO10{2} {3}(19) (20){4} {5}GND{6}    {7: <19}{8}'.format(getGPIO(10), "", "", Fore.YELLOW, Fore.RESET, Style.DIM, Style.NORMAL, "", pi_box_end))
print('{0: >19}  {1}GPIO9{2} {3}(21) (22){4} {5}GPIO25{6} {7: <19}{8}'.format(getGPIO(9) , "", "", Fore.CYAN, Fore.RESET, "", "", getGPIO(25), pi_box_end))
print('{0: >19} {1}GPIO11{2} {3}(23) (24){4} {5}GPIO8{6}  {7: <19}{8}'.format(getGPIO(11), "", "", Fore.CYAN, Fore.RESET, "", "", getGPIO(8), pi_box_end))
print('{0: >19}    {1}GND{2} {3}(25) (26){4} {5}GPIO7{6}  {7: <19}{8}'.format("", Style.DIM, Style.NORMAL, Fore.CYAN, Fore.RESET, "", "", getGPIO(7), pi_box_end))
print('{0: >19}  {1}GPIO0{2} {3}(27) (28){4} {5}GPIO1{6}  {7: <19}{8}'.format(getGPIO(0) , "", "", Fore.CYAN, Fore.RESET, "", "", getGPIO(1), pi_box_end))
print('{0: >19}  {1}GPIO5{2} {3}(29) (30){4} {5}GND{6}    {7: <19}{8}'.format(getGPIO(5) , "", "", Fore.CYAN, Fore.RESET, Style.DIM, Style.NORMAL, "", pi_box_end))
print('{0: >19}  {1}GPIO6{2} {3}(31) (32){4} {5}GPIO12{6} {7: <19}{8}'.format(getGPIO(6) , "", "", Fore.MAGENTA, Fore.RESET, "", "", getGPIO(12), pi_box_end))
print('{0: >19} {1}GPIO13{2} {3}(33) (34){4} {5}GND{6}    {7: <19}{8}'.format(getGPIO(13), "", "", Fore.MAGENTA, Fore.RESET, Style.DIM, Style.NORMAL, "", pi_box_end))
print('{0: >19} {1}GPIO19{2} {3}(35) (36){4} {5}GPIO16{6} {7: <19}{8}'.format(getGPIO(19), "", "", Fore.MAGENTA, Fore.RESET, "", "", getGPIO(16), pi_box_end))
print('{0: >19} {1}GPIO26{2} {3}(37) (38){4} {5}GPIO20{6} {7: <19}{8}'.format(getGPIO(26), "", "", Fore.MAGENTA, Fore.RESET, "", "", getGPIO(20), pi_box_end))
print('{0: >19}    {1}GND{2} {3}(39) (40){4} {5}GPIO21{6} {7: <19}{8}'.format("", Style.DIM, Style.NORMAL, Fore.MAGENTA, Fore.RESET, "", "", getGPIO(21), pi_box_end))
print('{0: >63}{1}│{2}'.format("", Fore.GREEN, Fore.RESET))
print('')