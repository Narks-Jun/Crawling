
lst = []
lst_url_link = []
webtoon_lst = []

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.webtoons.com/en/dailySchedule'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

with open("Naver_Webtoon_Crawling_Home_Main.txt", "r", encoding="UTF8") as fh:
    for line in fh:
        line = line.rstrip()
        ls = line.split(',')
        webtoon_lst.append(ls)
print(webtoon_lst)

a_tag = soup.select('a')
for n in a_tag:
    link = n.attrs['href']
    if not 'list?title' in link:
        continue
    lst_url_link.append(link)

for m in range(0, len(lst_url_link)):
    #print(lst_url_link[m])
    url = lst_url_link[m]
    driver.get(url)
    time.sleep(1)

    title = soup.select('p.subj')[m]
    title_name = title.text
    view = driver.find_element(By.CSS_SELECTOR, '#_asideDetail > ul > li:nth-child(1) > em')
    view_num = view.text
    subscribers = driver.find_element(By.CSS_SELECTOR, '#_asideDetail > ul > li:nth-child(2) > em')
    subscribers_num = subscribers.text
    star_rate = driver.find_element(By.CSS_SELECTOR, '#_starScoreAverage')
    star_rate_num = star_rate.text
    updated_day = driver.find_element(By.XPATH, '//*[@id="_asideDetail"]/p[1]')
    updated_day_text = updated_day.text
    updated_day_text = updated_day_text.replace("UP\n", "")
    episode = driver.find_element(By.CLASS_NAME, 'tx')
    episode_num = episode.text

    for l in webtoon_lst:
        if len(l) == 11:
            continue
        if title_name == l[1]:
            #webtoon_lst[m]
            l.insert(4, updated_day_text)
            l.insert(5, episode_num)
            l.append(view_num)
            l.append(subscribers_num)
            l.append(star_rate_num)
            l.append(lst_url_link[m])
            lst.append(l)
            print(l)

fname = "Naver_Webtoon_Crawling_Episode_detail_page.txt"

with open(fname, "w", encoding="UTF8") as fh:
    fh.write("id,"+"title,"+"writer,"+"genre,"+"updated_day,"+"episode_num,"+"like,"+"view,"+"subscribers,"+"rate,"+"url"+"\n")
    for x in range(0, len(lst)):
        for y in range(0, len(lst[x])):
            if y == 11:
                fh.write(lst[x][y])
            else :
                fh.write(lst[x][y]+',')
        fh.write("\n")
