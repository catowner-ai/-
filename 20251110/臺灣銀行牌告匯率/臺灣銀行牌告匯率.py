import threading, csv, ast, requests, time
from bs4 import BeautifulSoup
def job(single_tr):
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]
    currency_name = currency_name.replace("\r\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0]
    if Mydict[currency_name] == currency_rate:
        return
    else:
        lock.acquire()
        print(currency_name, currency_rate, Mydict[currency_name])
        Mydict[currency_name] = currency_rate
        file = open('MyCurrDict.csv','w',encoding='utf8')
        file.write( str(Mydict) )
        file.close()
        lock.release()
file = open('MyCurrDict.csv','r',encoding='utf8')
contents = file.read()
Mydict = ast.literal_eval(contents)
file.close()
lock = threading.Lock()
while True:
    html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
    bsObj = BeautifulSoup(html.content, "lxml")
    All_tr = bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr")
    Th = []; i=0
    for single_tr in All_tr:
        Th.append(threading.Thread(target = job, args = (single_tr,)))
        Th[i].start()
        i+=1
    for j in range(i):
        Th[j].join()
    time.sleep(1)
    print(".",end='')
    
    
    
