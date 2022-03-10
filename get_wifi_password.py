import platform
import subprocess


os_platform = platform.system()
input_ssid = input("please enter the SSID:- ")

if os_platform == 'Windows':
    cmd = f'netsh wlan show profile name={input_ssid} key=clear | findstr Key'
    raw_paswd, error = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').communicate()
    if raw_paswd:
        paswd = raw_paswd.strip().split(':')[1].strip()
        print(f'Password for SSID {input_ssid} is {paswd}')
    else:
        print(f'No password found for {input_ssid} on Windows')

elif os_platform == 'Linux':
    cmd = f'sudo /usr/bin/cat /etc/NetworkManager/system-connections/{input_ssid}.nmconnection | grep psk='
    raw_passwd, error = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').communicate()
    if raw_passwd:
        passwd = raw_passwd.split('=')[1].strip()
        print(f'Password for SSID {input_ssid} is {passwd}')
    else:
        print(f'No password found for {input_ssid} on Linux Platform')

else:
    print(f'This tool only works for linux and Windows Platform')
