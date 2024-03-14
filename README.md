# crucify
---

Hello and Welcome!

Crucify is a package manager designed for any arch-based linux distro
It's simple and fast, and will make your life much faster and easier!

## Installation
---

To install crucify you don't have to do anything hard or complicated!
just download the source code and run `crucify` and it will download and install all neccessary packages.

## Usage
---

you can see all the help you need by using:
```bash
python crucify.py help
```

to install packages use:
```bash
python crucify.py i package_name
python crucify.py install package_name
```
both are correct!
you can also add `--aur` after the package name to use AUR repos
to remove:
```bash
python crucify.py r package_name
python crucify.py remove package_name
```

to syncronize databases:
```bash
python crucify.py s
python crucify.py sync
```

to change mirrors based on your country:
```bash
python crucify.py c country_name
python crucify.py country country_name
```

to backup original mirrorlist use:
```bash
python crucify.py backup
```
and to restore:
```bash
python crucify.py restore
```

and to do a full system upgrade:
```bash
python crucify.py u
python crucify.py update
```


