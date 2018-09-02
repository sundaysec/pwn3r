#!/usr/bin/env bash
# --n3x7--


# -----------
# Color Vars:
# ----------
red=`tput setaf 1`
green=`tput setaf 2`
normal=`tput sgr0`

cat <<EOF
                     _____
 _ ____      ___ __ |___ / _ __
| '_ \ \ /\ / / '_ \  |_ \| '__|
| |_) \ V  V /| | | |___) | |
| .__/ \_/\_/ |_| |_|____/|_|
|_| reverse shell creator

codename: Dande ☈ - The god of thunder ⛈
EOF
sleep 2


#Request root access/sudo
function check() {
  #$EUID = 0
  if [[ "$EUID" -ne 0 ]]; then
    echo "${red}[✘]Error!!! Not enough priviledge${normal}"
    sleep 3
    echo "${red}[✘]Requesting root${normal}"
    #Running the installer with sudo
    sudo ./install.sh
    # Prevent script from continue running
    exit 1
  fi
}

#-----------
#Check root:
#-----------
check

function wine() {
  # -----------------------------
  # Install Wine and Pyinstaller:
  # -----------------------------
  apt-get install wine
  wine msiexec /i python-2.7.10.msi /L*v log.txt
  cd ~/.wine/drive_c/Python27
  wine python.exe Scripts/pip.exe install pyinstaller
}


function access() {
  # -----------
  #Send to bin:
  # -----------
  echo "#!/bin/bash" > /usr/bin/pwn3r
  echo "cd /usr/share/pwn3r" >> /usr/bin/pwn3r
  echo "exec python2 pwn3r.py $@" >> /usr/bin/pwn3r
  chmod +x /usr/bin/pwn3r
}

# --------------------------
# Check Internet connection:
# --------------------------

wget -q --spider http://google.com
if [ $? -eq 0 ]; then
  echo "Installing Wine"; wine &
  PID=$!
  i=1
  sp="/-\|"
  echo -n ' '
  while [ -d /proc/$PID ]
  do
    printf "\b${sp:i++%${#sp}:1}"
  done
fi

access

echo "N⬠∫∫⎔"
