from modules import libraries

# Initializing neccessary stuff
term = libraries.system
color = libraries.Fore
print (color.GREEN, 'Crucify!', color.RESET, 'Simple and fast package manager.')
# configurating docopt
usage = '''
Usage:
    crucify i <package_name> [--aur]
    crucify install <package_name> [--aur]
    crucify r <package_name>
    crucify remove <package_name>
    crucify u 
    crucify update
    crucify s
    crucify sync
    crucify backup
    crucify restore
    crucify c <country_name>
    crucify country <country_name>
    crucify h
    crucify help

Options:
    --aur
'''
print (f'use {color.GREEN}crucify {color.LIGHTMAGENTA_EX}help{color.RESET} for help!')
parser = libraries.docopt(usage)
pacm = 'sudo pacman'
if '--aur' in parser:
    pacm = 'yay'
if parser['i'] or parser['install']:
    package = parser['<package_name>']
    term(f'{pacm} -S {package}')

elif parser['r'] or parser['remove']:
    package = parser['<package_name>']
    term(f'sudo pacman -R {package}')

elif parser['u'] or parser['update']:
    term('sudo pacman -Syyu')

elif parser['s'] or parser['sync']:
    term('sudo pacman -Syy')

elif parser['backup']:
    term('sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak')
    print(color.GREEN, 'Backup created.', color. RESET)

elif parser['restore']:
    term('sudo cp /etc/pacman.d/mirrorlist.bak /etc/pacman.d/mirrorlist')
    print(color.GREEN, 'Backup restored.', color. RESET)

elif parser['c'] or parser['country']:
    country = parser['<country_name>']
    term(f'sudo reflector -c {country} --save /etc/pacman.d/mirrorlist')
    print(color.GREEN, 'mirrorlist updated.', color. RESET)

elif parser['h'] or parser['help']:
    print(f'''
    {color.RESET}
    Hello and welcome to {color.LIGHTGREEN_EX}Crucify{color.RESET}!
    I\'m here to help you manage your applications:)
    ==> use {color.LIGHTMAGENTA_EX}i{color.RESET} or {color.LIGHTMAGENTA_EX}install{color.RESET} to install a package
    {color.BLUE}you can also use {color.LIGHTMAGENTA_EX}--aur{color.BLUE} after the package name to install package from AUR Repositories{color.RESET}
    ==> if you feel like you don\'t need a package anymore, you can always remove it by using {color.LIGHTMAGENTA_EX}r{color.RESET} or {color.LIGHTMAGENTA_EX}remove{color.RESET}.
    ==> use {color.LIGHTMAGENTA_EX}u{color.RESET} or {color.LIGHTMAGENTA_EX}update{color.RESET} to do a full system upgrade.
    ==> to check if you\'re getting the latest packages, use {color.LIGHTMAGENTA_EX}s{color.RESET}  ot {color.LIGHTMAGENTA_EX}sync{color.RESET} to syncronize databases.
    ==> use {color.LIGHTMAGENTA_EX}backup{color.RESET} to backup your mirrorlist.
    ==> use {color.LIGHTMAGENTA_EX}restore{color.RESET} to restore your original mirrorlist.
    ==> you can use {color.LIGHTMAGENTA_EX}c{color.RESET} or {color.LIGHTMAGENTA_EX}country{color.RESET} to modify mirrorlist based on your country.
    {color.LIGHTRED_EX}remember to do a {color.LIGHTMAGENTA_EX}backup{color.LIGHTRED_EX} from the original mirrorlist before modifying!{color.RESET}

    ''')

