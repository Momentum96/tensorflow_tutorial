
# coding: utf-8

# In[3]:


from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import csv

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(3)


# In[4]:


date = sys.argv[1]
h = 5
m = 0

bang = []
go = []
g = []
w = []

while(True):
    driver.get('https://astro.kasi.re.kr:444/life/pageView/10?useElevation=1&output_range=2&date=' + date + '&hour=' + str(h) + '&minute=' + str(m) + '&second=0&address=%EC%B6%A9%EB%82%A8+%EC%B2%9C%EC%95%88%EC%8B%9C+%EC%84%9C%EB%B6%81%EA%B5%AC+%EC%B2%9C%EC%95%88%EB%8C%80%EB%A1%9C+1223-24#')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('#sun-height-table > table > tbody > tr > td')

    undata = []

    for n in notices:
        undata.append(n.text.strip())

    bang.append(undata[0].split(' ')[0])
    go.append(undata[1].split(' ')[0])
    g.append(undata[2].split(' ')[0])
    w.append(undata[3].split(' ')[0])
    
    print(len(bang))
    print('--------------------------------------------------')
    
    m += 1
    
    if(m == 60):
        h += 1
        m = 0
    if(h == 20 and m == 1):
        break

f = open('./' + date + '_sun.csv', 'w')
csvWriter = csv.writer(f)

for i in range(len(bang)):
    csvWriter.writerow([bang[i], go[i], g[i], w[i]])

f.close()

