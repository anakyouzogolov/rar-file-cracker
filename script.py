import rarfile
from rarfile import RarWrongPassword
import random


rarfile.UNRAR_TOOL = "C:\\Program Files\\WinRAR\\UnRaR.exe"


rar_file = input("Enter your rar file name :")

r = rarfile.RarFile(f'{rar_file}.rar')

guess_password = ""


while(True):

    guess_password = str(random.randint(0, 999))

    print("*****", guess_password, "******")
    
    try:
        r.extractall(pwd=guess_password)
        print("RaR Password is : ", guess_password)
        break
    except RarWrongPassword as err:
        print("error", err)
        continue




    
   

       


