import os
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.exception import AuthenticationException

USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

device = {
    'ip': '192.168.154.129',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    c = ConnectHandler(**device)
except(AuthenticationException):
    print("An Authentication error occered while trying to connect to: " + device [ip])
    

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)
f.close()
