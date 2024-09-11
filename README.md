# My experiments on git and python
bla bla

## My env setup
Using VSCode 1.93+ and python 3.12.3+
```
gf@ant:~/Documents/github/test/test0$ pip freeze
WARNING: Skipping /usr/lib/python3.12/dist-packages/charset_normalizer-3.3.2.dist-info due to invalid metadata entry 'name'
acme-tiny==5.0.1
ajpy==0.0.5
apparmor==4.0.0b3
apturl==0.5.2
asgiref==3.7.2
Babel==2.10.3
bcrypt==3.2.2
beautifulsoup4==4.12.3
blinker==1.7.0
Brlapi==0.8.5
Brotli==1.1.0
certifi==2023.11.17
chardet==5.2.0
charset-normalizer==3.3.2
click==8.1.6
colorama==0.4.6
command-not-found==0.3
configobj==5.0.8
crudini==0.9.4
cryptography==41.0.7
cupshelpers==1.0
dbus-python==1.3.2
defer==1.0.6
deprecation==2.0.7
distro==1.9.0
dnspython==2.6.1
eyed3==0.9.7
fail2ban==1.0.2
feedparser==6.0.10
filelock==3.13.1
filetype==1.2.0
Flask==3.0.2
html2text==2024.2.26
httplib2==0.20.4
idna==3.6
ifaddr==0.2.0
IMDbPY==2021.4.18
impacket==0.11.0
indicator-cpufreq==0.2.2
iniparse==0.5
iotop==0.6
IPy==1.1
itsdangerous==2.1.2
Jinja2==3.1.2
kazam==1.4.5
launchpadlib==1.11.0
lazr.restfulclient==0.14.6
lazr.uri==1.0.6
ldap3==2.9.1
ldapdomaindump==0.9.4
LibAppArmor==4.0.0b3
libevdev==0.5
libvirt-python==10.0.0
louis==3.29.0
lxml==5.2.1
Mako==1.3.2.dev0
Markdown==3.5.2
markdown-it-py==3.0.0
MarkupSafe==2.1.5
mdurl==0.1.2
mutagen==1.46.0
mysqlclient==1.4.6
nemo-compare==6.2.0
nemo-terminal==6.2.0
netaddr==0.8.0
netifaces==0.11.0
numpy==1.26.4
oauthlib==3.2.2
onboard==1.4.1
packaging==24.0
PAM==0.4.2
paramiko==2.12.0
patator==1.0
pexpect==4.9.0
pillow==10.2.0
ply==3.11
psutil==5.9.8
psycopg2==2.9.9
ptyprocess==0.7.0
pyasn1==0.4.8
pyasyncore==1.0.2
pycairo==1.25.1
pycryptodomex==3.20.0
pycups==2.0.1
pycurl==7.45.3
pyelftools==0.30
Pygments==2.17.2
PyGObject==3.48.2
PyICU==2.12
pyinotify==0.9.6
PyJWT==2.7.0
PyNaCl==1.5.0
pyOpenSSL==23.2.0
pyparsing==3.1.1
pyparted==3.12.0
pypng==0.20231004.0
pysmi==0.3.4
pysnmp==4.4.12
python-apt==2.7.7+ubuntu3
python-debian==0.1.49+ubuntu2
python-gnupg==0.5.2
python-magic==0.4.27
python-xlib==0.33
pytz==2024.1
pyudev==0.24.0
pyxdg==0.28
PyYAML==6.0.1
qrcode==7.4.2
repolib==2.2.1
requests==2.31.0
requests-file==1.5.1
rich==13.7.1
s-tui==1.1.6
setproctitle==1.3.3
setuptools==68.1.2
sgmllib3k==1.0.0
simplejson==3.19.2
six==1.16.0
soupsieve==2.5
ssh-import-id==5.11
systemd-python==235
terminator==2.1.3
tinycss2==1.2.1
tldextract==3.1.2
typing_extensions==4.10.0
ubuntu-drivers-common==0.0.0
ufw==0.36.2
Unidecode==1.3.8
urllib3==2.0.7
urwid==2.6.10
usb-creator==0.3.16
vboxapi==1.0
wadllib==1.3.6
wcwidth==0.2.5
webencodings==0.5.1
websockets==10.4
websockify==0.10.0
Werkzeug==3.0.1
wheel==0.42.0
xdg==5
xkit==0.0.0
xlrd==2.0.1
yt-dlp==2024.4.9
zenmap==7.94+svn
```

### My runtime
```
gf@ant:~/Documents/github/test/test0$ env | sort
CHROME_DESKTOP=code-url-handler.desktop
CINNAMON_VERSION=6.2.9
COLORTERM=truecolor
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
DESKTOP_SESSION=cinnamon
DISPLAY=:0
GDK_BACKEND=x11
GDM_LANG=en_US
GDMSESSION=cinnamon
GIO_LAUNCHED_DESKTOP_FILE_PID=...
GIO_LAUNCHED_DESKTOP_FILE=/usr/share/applications/code.desktop
GIT_ASKPASS=/usr/share/code/resources/app/extensions/git/dist/askpass.sh
GJS_DEBUG_OUTPUT=stderr
GJS_DEBUG_TOPICS=JS ERROR;JS LOG
GNOME_DESKTOP_SESSION_ID=this-is-deprecated
GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
GTK3_MODULES=xapp-gtk3-module
GTK_MODULES=gail:atk-bridge
HOME=/home/gf
LANG=en_DK.UTF-8
LANGUAGE=en_DK
LC_ADDRESS=en_DK.UTF-8
LC_IDENTIFICATION=en_DK.UTF-8
LC_MEASUREMENT=en_DK.UTF-8
LC_MONETARY=en_DK.UTF-8
LC_NAME=en_DK.UTF-8
LC_NUMERIC=en_DK.UTF-8
LC_PAPER=en_DK.UTF-8
LC_TELEPHONE=en_DK.UTF-8
LC_TIME=en_DK.UTF-8
LESSCLOSE=/usr/bin/lesspipe %s %s
LESSOPEN=| /usr/bin/lesspipe %s
LIBVIRT_DEFAULT_URI=qemu:///system
LOGNAME=gf
LS_COLORS=...
ORIGINAL_XDG_CURRENT_DESKTOP=X-Cinnamon
PAPERSIZE=a4
PATH=/home/gf/bin:/home/gf/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
PWD=/home/gf/Documents/github/test/test0
PYTHONSTARTUP=/home/gf/.vscode/extensions/ms-python.python-2024.14.0-linux-x64/python_files/pythonrc.py
QT_ACCESSIBILITY=1
SESSION_MANAGER=...
SHELL=/bin/bash
SHLVL=1
TERM_PROGRAM_VERSION=1.93.0
TERM_PROGRAM=vscode
TERM=xterm-256color
USER=gf
_=/usr/bin/env
VSCODE_GIT_ASKPASS_EXTRA_ARGS=
VSCODE_GIT_ASKPASS_MAIN=/usr/share/code/resources/app/extensions/git/dist/askpass-main.js
VSCODE_GIT_ASKPASS_NODE=/usr/share/code/code
VSCODE_GIT_IPC_HANDLE=...
XAUTHORITY=/home/gf/.Xauthority
XDG_CONFIG_DIRS=/etc/xdg/xdg-cinnamon:/etc/xdg
XDG_CURRENT_DESKTOP=X-Cinnamon
XDG_DATA_DIRS=/usr/share/cinnamon:/usr/share/gnome:/home/gf/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share:/var/lib/snapd/desktop
XDG_GREETER_DATA_DIR=/var/lib/lightdm-data/gf
XDG_RUNTIME_DIR=/run/user/1000
XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
XDG_SEAT=seat0
XDG_SESSION_CLASS=user
XDG_SESSION_DESKTOP=cinnamon
XDG_SESSION_ID=c4
XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session1
XDG_SESSION_TYPE=x11
XDG_VTNR=7
```

My PC
=====
```
gf@ant:~$ neofetch --off ; date
gf@ant 
------ 
OS: Linux Mint 22 x86_64 
Host: 20JNS24C00 ThinkPad T470 W10DG 
Kernel: 6.8.0-44-generic 
Uptime: 13 hours, 43 mins 
Packages: 2800 (dpkg), 7 (flatpak), 12 (snap) 
Shell: bash 5.2.21 
Resolution: 1920x1080 
DE: Cinnamon 6.2.9 
WM: Mutter (Muffin) 
WM Theme: Mint-Y-Dark (Mint-Y) 
Theme: Mint-Y-Aqua [GTK2/3] 
Icons: Mint-Y-Sand [GTK2/3] 
Terminal: terminator 
CPU: Intel i5-6300U (4) @ 3.000GHz 
GPU: Intel Skylake GT2 [HD Graphics 520] 
Memory: 6202MiB / 31845MiB 

2024-09-11T08:35:51 CEST
```

How to format a README.md (syntax tips):
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
