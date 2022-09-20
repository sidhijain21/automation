from bs4 import BeautifulSoup
import requests
from csv import writer


url="https://www.reliancedigital.in/lifelong-llpcm05-men-s-beard-trimmer/p/491903023?gclid"
page = requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('div',class_="Grid_StyledGrid-sc-syw1oe-0 jyUYRF")
with open('housing.csv','w',encoding='utf8',newline='')as f:
    thewriter=writer(f)
    header=['customer1','customer2','customer3','customer4','customer5']
    thewriter.writerow(header)
    for list in lists:
        customer1=lists.find('div',class_="TextWeb__Text-sc-jRS1jv Flex-sc-1suf6mt-0 fecBFE").text.replace('\n','5star')
        customer2=lists.find('div',class_="TextWeb__Text-sc-jRS1jv Flex-sc-1suf6mt-0 fecBFE").text.replace('\n','4star')
        customer3=lists.find('div',class_="TextWeb__Text-sc-jRS1jv Flex-sc-1suf6mt-0 fecBFE").text.replace('\n','3star')
        customer4=lists.find('div',class_="TextWeb__Text-sc-jRS1jv Flex-sc-1suf6mt-0 fecBFE").text.replace('\n','2star')
        customer5=lists.find('div',class_="TextWeb__Text-sc-jRS1jv Flex-sc-1suf6mt-0 fecBFE").text.replace('\n','1star')
        info=[customer1,customer2,customer3,customer4,customer5]
        thewriter.writerow(info)



