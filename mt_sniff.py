from paramiko.client import SSHClient
import paramiko
import time

#Użycie:
# Do działania trzeba python3 i bibliotekę paramiko
# Na mt ustawiamy parametry sniffera, nazwa pliku musi być 'siema' :D
# W skrpycie ustawiamy dostęp do mt, rozmiar jaki ma osiągnąć plik

host = ""
port = 22
username = "admin"
password = ""
file_size = 100000 #rozmiar musi być w bajtach
file_counter = 0

def download(file_nr):
    transport = paramiko.Transport((host, port))
    transport.connect(username = username, password = password)

    sftp = paramiko.SFTPClient.from_transport(transport)

    filepath = '/siema'
    localpath = '/%s' %(file_nr,) #ścieżka lokalna
    sftp.get(filepath, localpath)

    sftp.close()
    transport.close()

if __name__ == '__main__':

    client = SSHClient()
    client.load_system_host_keys()
    client.connect(hostname=host, port=port, username=username, password=password)
    client.exec_command('tool sniffer start')

    while file_counter < 3:  # ilosc plikow do sciagnięcia
        time.sleep(10)
        stdin, stdout, stderr = client.exec_command('file print where name=siema size>=%s' %(file_size,))
        for i in stdout:
            print(i)
            if 'siema' in i:
                client.exec_command('tool sniffer stop')
                download(file_counter)
                client.exec_command('file remove siema')
                file_counter+=1
                client.exec_command('tool sniffer start')

    client.exec_command('tool sniffer stop')
    client.exec_command('file remove siema')
        
