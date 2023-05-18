
lst = []
lst_url_link = []

import requests
from bs4 import BeautifulSoup

url = 'https://www.webtoons.com/en/dailySchedule'
response = requests.get(url)
# print(response.status_code)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # info = soup.findAll('p')
    # print(info)
    # title = soup.findAll('p', attrs={"class": "subj"})
    title = soup.select('p.subj')
    author = soup.select('p.author')
    genre = soup.select('p.genre')
    like_grade = soup.select('em.grade_num')

    a_tag = soup.select('a')
    for n in a_tag:
        link = n.attrs['href']
        if not 'list?title' in link:
         continue
    lst_url_link.append(link)

    for n in range(0, len(title)):
        # print(title[n])
        title_name = title[n].text
        author_name = author[n].text
        genre_name = genre[n].text
        like_grade_num = like_grade[n].text
        episode_list = [title_name, author_name, genre_name, like_grade_num]
        if episode_list not in lst:
            lst.append(episode_list)

    for m in range(0, len(lst)):
        lst[m].insert(0, m)

else:
    print(response.status_code)

print(lst)


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "Naver_Webtoon_Crawling_Home_Main.txt"

with open(fname, "w", encoding="UTF8") as fh:
    for k in range(0, len(lst)):
        fh.write(str(lst[k][0])+","+lst[k][1]+","+lst[k][2]+","+lst[k][3]+","+lst[k][4]+"\n")

#<a class="_weekdaySelect NPI=a:mon,g:en_en" data-weekday="MONDAY" href="#">MON</a>

#dailyList > div.daily_section._list_MONDAY.on
#dailyList > div.daily_section._list_MONDAY.on > h2 > a
#dailyList > div.daily_section._list_MONDAY.on > ul
#dailyList > div.daily_section._list_MONDAY.on > ul > li:nth-child(1) > a
#dailyList > div.daily_section._list_MONDAY.on > ul > li:nth-child(1) > a > div
#dailyList > div.daily_section._list_MONDAY.on > ul > li:nth-child(1) > a > div > p.subj

#dailyList > div.daily_section._list_TUESDAY.on > ul > li:nth-child(1) > a > div > p.subj
#dailyList > div.daily_section._list_WEDNESDAY > ul > li:nth-child(1) > a > div > p.subj
#dailyList > div.daily_section._list_THURSDAY > ul > li:nth-child(1) > a > div
#dailyList > div.daily_section._list_FRIDAY > ul > li:nth-child(1) > a > div
#dailyList > div.daily_section._list_SATURDAY > ul > li:nth-child(1) > a > div > p.subj
#dailyList > div.daily_section._list_SUNDAY > ul > li:nth-child(1) > a > div
