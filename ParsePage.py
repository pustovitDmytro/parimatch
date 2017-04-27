from bs4 import BeautifulSoup
import re

def getTable(page, descr):
    bs = BeautifulSoup(page, "html.parser")
    list = bs.find(id = "f1")
    for item in list.children:
        try:
            if(re.search(descr,item.h3.text)):
                print(item.h3.text)
                table  = item.find('table')
                for event in table.find_all("tbody",{"class": re.compile("row\d")}):
                    print(event.tr.td.text)
        except Exception:
            pass

testUrl = "site/Source.html"
testStr  = 'Футбол. Польша. Экстракласа'
f = open(testUrl,'r')

testHtml = f.read()
getTable(testHtml,testStr)