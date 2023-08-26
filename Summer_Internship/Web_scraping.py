from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import re

# Globals
year_lst = []

sub_title_dict = {
    "Year": [],
    "^Toplam nüfus": [],
    "^Yayınevi sayısı": [],
    "^Bandrol alan kitap adedi": [],
    "^Ücretsiz dağıtılan ders kitabı adedi": [],
    "^Üretilen toplam kitap adedi": [],
    "^Dağıtım şirketi sayısı": [],
    "^Gayri safi yurtiçi": [],
    "^Kişi başına GSYH": []

}

sub_title_lst = [
    "^Toplam nüfus",
    "^Yayınevi sayısı",
    "^Bandrol alan kitap adedi",
    "^Ücretsiz dağıtılan ders kitabı adedi",
    "^Üretilen toplam kitap adedi",
    "^Dağıtım şirketi sayısı",
    "^Gayri safi yurtiçi",
    "^Kişi başına GSYH"]

num = 0

f = open("links_file.txt", 'r')
for link in f.readlines():
    page = urlopen(link)
    html_page = page.read()
    html = html_page.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    for i in sub_title_lst:
        for key in soup.find_all('td', string=re.compile(i)):
            if (year_lst and year_lst[-1] == 2008 and key.text == "Toplam nüfus"):
                temp_str = "72.561.312"
            else:    
                temp_str = str(key.find_next_sibling().string)

            if ('/' in temp_str):
                start = temp_str.find('/') + 1
                end = temp_str.find('Milyon $')
                temp_str = temp_str[start: end]
            if ('.' in temp_str):
                lst = temp_str.split('.')
                temp_str = "".join(lst)
            if (' ' in temp_str):
                lst = temp_str.split(' ')
                temp_str = "".join(lst)
            try:
                val = int(temp_str)
                sub_title_dict[i].append(val)
            except:
                sub_title_dict[i].append(temp_str)
        temp_str = ''

    year_lst.append(int("".join(((soup.title.string.split(' '))[0]))))

sub_title_dict["Year"] = year_lst

alter_lst = ["^Toplam nüfus", "^Kişi başına GSYH", ]

for j in alter_lst:
    del sub_title_dict[j][4]

del sub_title_dict["^Gayri safi yurtiçi"][3]
sub_title_dict["^Toplam nüfus"].append(77695904)
sub_title_dict["^Gayri safi yurtiçi"].insert(3, 957800)
sub_title_dict["^Kişi başına GSYH"].append(63)

# print(sub_title_dict)

df = pd.DataFrame(sub_title_dict)
df.to_csv("excel_table_partial.csv", encoding ='utf-8')
#print(df)


