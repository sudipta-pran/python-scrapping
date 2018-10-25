import requests
from bs4 import BeautifulSoup
from csv import writer

with open('companydetails.csv', 'w', newline='') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Name', 'Description', 'Address', 'WebUrl', 'Categories']
        csv_writer.writerow(headers)
csv_file.close()

with open('companies.csv', 'w', newline='') as csv_file2:
        csv_writer = writer(csv_file2)
        headers = ['Name', 'Url']
        csv_writer.writerow(headers)
csv_file2.close()

siteUrl = 'https://www.example.com/'
count = 0
page = 1

def mainscrap(url, name):
    categories = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rawDescription = soup.find(class_='entry__item__body__description')
    if not rawDescription:
        description = 'Description unavailable'
    else:
        description = rawDescription.get_text().strip()
    
    rawAddress = soup.find(class_='entry__item__body__contacts__address')
    if not rawAddress:
        address = 'Address unavailable'
    else:
        address= rawAddress.get_text().strip()

    web = soup.find(class_='entry__item__body__contacts__additional__website')
    if not web:
        webUrl = 'URL unavailable'
    else:
        webUrl = web.find('a')['href']
    categoriesAll = soup.find_all(class_='entry__body__categories__items__item')
    for category in categoriesAll:
        categories = categories + str(category.get_text().strip()) + '\n'
    
    with open('companydetails.csv', 'a', encoding='utf-8', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([name, description, address, webUrl, categories])
    csv_file.close()

def scrapAll(id):
    global count, page
    target = siteUrl + 'clients/?page=' + str(id)
    response = requests.get(target)
    soup = BeautifulSoup(response.text, 'html.parser')

    exhibitors = soup.find_all(class_='clients_list__items__item')

    if not exhibitors:
        print("End of pages")
        return
    with open('companies.csv', 'a', encoding='utf-8', newline='') as csv_file:
        csv_writer = writer(csv_file)
        for exhibitor in exhibitors:
            count+=1
            name = exhibitor.find(class_='clients_list__items__item__name__link').get_text().replace('\n', '').strip()
            link = exhibitor.find(class_='clients_list__items__item__name__link')['href']
            url = siteUrl + link
            mainscrap(url, name)
            csv_writer.writerow([name, url])
    csv_file.close()

    page += 1
    scrapAll(page)

if page == 1:
    scrapAll(page)

print(count)