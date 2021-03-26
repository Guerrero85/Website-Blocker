import time
from datetime import datetime as dt

# Hosts Files
# Windows c:\\windows\system32\drivers\etc
#  Mac & Linux /etc/hosts/

hosts_path_W = r"C:\windows\system32\drivers\etc\hosts" # Windows
hosts_path_U = "/etc/hosts" # Linux or MacOs
hosts_dir = "/home/user/Documentos/hosts" # Example

redirect = "127.0.0.1"
#website_list = ["www.facebook.com", "facebook.com", "mail.google.com", "www.youtube.com"]


str = "***** Bienvenido al Bloqueador de Sitios Web *****"
print(str.center(40, " "))
from_hour = int(input("Introduzca hora de trabajo: "))
to_hour = int(input("Introduzca hora de finalizacion de trabajo: "))


Numero_website = int(input("Numero de Pagina que desea Bloquear o Desbloquear: "))
website_list = []
for i in range(Numero_website):
    website_list.append(input("Ingresa su Sitio que deseas Bloquear o Desbloquear: "))


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,to_hour):
        print("Precione 'Ctrl + C' para continuar...")
        with open(hosts_dir, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Precione 'Ctrl + C' para continuar...")
        with open(hosts_dir, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


    time.sleep(1)