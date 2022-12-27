import time,pyautogui,json
#print(pyautogui.displayMousePosition())
f = open("acc.json")
data = json.load(f)
#coordinates
giris_bos_alan=(1080,790)
trendyol_giris_yap =(1080,451)
e_posta=(420,359)
sifre=(450,458)
giris_yap=(1080,567)
arama=(1040,96)
oneri=(960,130)
sirala=(1155,358)
en_yeniler=(865,851)
sol_orta =(960,500)
sag_orta= (1220,500)
kalp =(1320,92)
geri =(831,92)
hesabim=(1310,996)
cikis_yap=(990,784)
evet =(1170,601)

def girisyap(mail,password):
    pyautogui.click(giris_bos_alan)
    time.sleep(0.5)
    pyautogui.click(trendyol_giris_yap)
    time.sleep(2.5)
    pyautogui.click(e_posta)
    time.sleep(0.5)
    pyautogui.typewrite(mail)
    time.sleep(0.5)
    pyautogui.hotkey('altright','q')
    time.sleep(0.5)
    pyautogui.typewrite("hotmail.com")
    time.sleep(0.5)
    pyautogui.click(giris_bos_alan)
    time.sleep(0.5)
    pyautogui.click(sifre)
    time.sleep(0.5)
    pyautogui.typewrite(password)
    time.sleep(0.5)
    pyautogui.click(giris_yap)
def go_to_target(targ):
    pyautogui.click(arama)
    time.sleep(1)
    pyautogui.hotkey('altright','q')
    time.sleep(0.5)
    pyautogui.typewrite(targ)
    time.sleep(1.5)
    pyautogui.click(oneri)
def siralama():
    pyautogui.click(sirala)
    time.sleep(1)
    pyautogui.click(en_yeniler)
    time.sleep(2)
    for x in range(25):
       pyautogui.scroll(360)
    time.sleep(1)
def begen(sayi):
    for x in range(sayi):
        pyautogui.click(sol_orta)
        time.sleep(1.5)
        pyautogui.click(kalp)
        time.sleep(0.5)
        pyautogui.click(geri)
        time.sleep(0.5)
        pyautogui.click(sag_orta)
        time.sleep(1.5)
        pyautogui.click(kalp)
        time.sleep(0.5)
        pyautogui.click(geri)
        time.sleep(0.5)
        pyautogui.scroll(-90)
        time.sleep(0.8)
def cikisyap():
    pyautogui.click(geri)
    time.sleep(1)
    pyautogui.click(geri)
    time.sleep(1)
    pyautogui.click(hesabim)
    time.sleep(1)
    pyautogui.click(cikis_yap)
    time.sleep(0.5)
    pyautogui.click(evet)
    time.sleep(1)

time.sleep(2)


def yap(targ,sayi):
    for x in range(5):
        mail= data[x][0]
        password= data[x][1]
        time.sleep(2)
        girisyap(mail=mail,password=password)
        time.sleep(2)
        go_to_target(targ=targ)
        time.sleep(1)
        siralama()
        time.sleep(1)
        begen(sayi=sayi)
        time.sleep(1)
        cikisyap()
        time.sleep(1)
        data.append(data[0])
        data.pop(0)
        with open("acc.json", "w") as outfile:
            json.dump(data, outfile)
        
    
    


yap(targ="",sayi=5)


    





