from os import system as term


print('Checking Dependencies, Please Wait.\n')
term('pacman -Q > .dep.tmp')
f = open('.dep.tmp', 'r')
installed = f.read()
f.close()
term('rm .dep.tmp')
if 'python-docopt' not in installed:
    term('sudo pacman -S python-docopt')
if 'reflector' not in installed:
    term('sudo pacman -S reflector')
if 'python-colorama' not in installed:
    term('sudo pacman -S python-colorama')
if 'yay' not in installed:
    term('pacman -S --needed git base-devel')
    term('git clone https://aur.archlinux.org/yay.git /tmp/yay')
    term('cd /tmp/yay')
    term('makepkg -si')
    term('yay -Y --gendb')

term('clear')