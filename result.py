#Programmas autors - Gints Jankovskis 221RMB019
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

print("Ievadiet Lietotājvārdu")
Login=input()
print("Ievadiet Paroli")
Parole=input()

url = "https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv"
driver.get(url)
find=driver.find_element(By.ID, "cn-notice-button-aggree")
find.click()
find=driver.find_element(By.ID, "IDToken1")
find.send_keys(Login)

find=driver.find_element(By.ID, "IDToken2")
find.send_keys(Parole)
find=driver.find_element(By.NAME, "Login.Submit")
find.click()

while True:

    print("Ko jūs gribat atvērt?")
    print("1-Grafiki 2-Atzīmes par studiju programmām 3-Uzdoto uzdevumu grafiku 4-Konkrētu studijas kursu 5-Atvērt E-pastu")
    atvert=input()

    if atvert==("1"):
        url2 = "https://ortus.rtu.lv/f/u108l1s5/normal/render.uP"
        driver.get(url2)
        find=driver.find_element(By.ID, "tabLink_u108l1s329")
        find.click()
        print("Vai jūs vēlaties turpināt?")
        print("1-Jā 2-Nē")
        end=input()
        if end=="2":
            sys.exit(0)
            close
        elif end=="1":
            continue
    elif atvert==("2"):
        url2 = "https://ortus.rtu.lv/f/u108l1s5/normal/render.uP"
        driver.get(url2)
        find=driver.find_element(By.ID, "tabLink_u108l1s22")
        find.click()
        url3 = "https://ortus.rtu.lv/f/u108l1s22/p/rtu-eusso-studijas-info.u108l1n151/normal/action.uP?pP_action=info&pP_page=6"
        driver.get(url3)
        print("Vai jūs vēlaties turpināt?")
        print("1-Jā 2-Nē")
        end=input()
        if end=="2":
            sys.exit(0)
            close
        elif end=="1":
            continue
    elif atvert==("3"):
        url2 = "https://estudijas.rtu.lv/my/index.php"
        driver.get(url2)
        print("Vai jūs vēlaties turpināt?")
        print("1-Jā 2-Nē")
        end=input()
        if end=="2":
            sys.exit(0)
            close
        elif end=="1":
            continue
    elif atvert==("5"):
        url2 = "https://outlook.office.com/mail/"
        driver.get(url2)
        time.sleep(2)
        find=driver.find_element(By.ID, "i0116")
        find.send_keys(Login+"@edu.rtu.lv")
        find=driver.find_element(By.ID, "idSIButton9")
        find.click()
        time.sleep(2)
        find=driver.find_element(By.ID, "i0118")
        find.send_keys(Parole)
        find=driver.find_element(By.ID, "idSIButton9")
        find.click()
        print("Vai jūs vēlaties turpināt?")
        print("1-Jā 2-Nē")
        end=input()
        if end=="2":
            sys.exit(0)
            close
        elif end=="1":
            continue
    elif atvert ==("4"):
        print("Kādu studiju kursu jūs vēlaties apmeklēt?")
        print("1-Civilā aizsardzība")
        print("2-Datorgrafikas un attēlu apstrādes pamati")
        print("3-Ievads datoru arhitektūrā")
        print("4-Ievads studiju nozarē")
        print("5-Lietojumprogrammatūras automatizēšanas rīki")
        print("6-Matemātika")
        print("7-Risinājumu algoritmizēšana un programmēšana")
        print("8-Terminoloģijas minimums (angļu valodā)")
        kurss=input()
        if kurss ==("1"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348632"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("2"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348197"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("3"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348367"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("4"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348334"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("5"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348235"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("6"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348222"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("7"):
            url2="https://estudijas.rtu.lv/course/view.php?id=348229"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue
        elif kurss==("8"):
            url2="https://estudijas.rtu.lv/course/view.php?id=362863"
            driver.get(url2)
            print("Vai jūs vēlaties turpināt?")
            print("1-Jā 2-Nē")
            end=input()
            if end=="2":
                sys.exit(0)
                close
            elif end=="1":
                continue