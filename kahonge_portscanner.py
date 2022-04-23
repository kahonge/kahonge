"""
Program: portscanner
Language: Python
IDE: Pycharm Community Edition
Developer: Kahonge_jr
facebook:kahonge njuguna
twitter:@kahongenjuguna
linkedin:kahonge njuguna
Email: kahongenjuguna@gmail.com
Developer Comment: It's never too late,
                   always try harder,
                   what would happen if you never stopped
Last Edited: 23rd,04, 2022
NOTE: The project is open-source,
"""
import pyfiglet
import subprocess
import time
import socket
import sys
from termcolor import colored
import platform
import datetime

# start program with clear terminal
if platform.system() == 'Linux':
    print("Checking Host Operating System")
    print("Host Operating System is LINUX")
    time.sleep(5)
    subprocess.call('clear', shell=True)
elif platform.system() == 'Windows':
    print("Checking Host Operating System")
    print('Host Operating System is WINDOWS')
    time.sleep(5)
    subprocess.call('cls', shell=True)
else:
    #here one can add other operating system
    sys.exit("UNKNOWN OPERATING SYSTEM")

# program banner
banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

host = input("Enter host to scan: \n")
target_ip = socket.gethostbyname(host)
target_name = socket.gethostbyaddr(host)
print('*' * 30)
print('*' * 30)
print("Target IP: {}".format(target_ip))
print("Target Host Name: {}".format(target_name[0]))
print('*' * 30)
print('*' * 30)


def main():
    try:
        for ports in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, ports))
            if result == 0:
                # print("Scanner started at {} ".format(str(datetime.time())))
                print("scanning {} ".format(host))
                print(colored("port {}/tcp is open".format(ports), 'green'))
                pass
            sock.close()
    except socket.gaierror:
        print("Unable to resolve host")
        #sys.exit()
        main()
        pass
    except KeyboardInterrupt:
        print("you killed the program {CTRL +c}")
        sys.exit('bye')
        pass
    except socket.error:
        print("server not responding")
        main()


if __name__ == "__main__":
    main()
