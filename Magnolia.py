from bs4 import BeautifulSoup
import requests

def createDataBaseMagnolia():
	url = "https://shop.mgnl.ru"
	main_page = requests.get(url).text

	soup = BeautifulSoup(main_page, 'lxml')

	directoryNames = soup.find_all('a', {'class':'dark_link'}, href=True)
	directoryNames = directoryNames[3::]

	dictCategorys = {"name-catS":{"names":[], "categorys":[], "under-hrefs":[]}}

	allHrefs = []	
	for i in directoryNames:
		response1_help = requests.get(url+i['href']).text
		soup_help = BeautifulSoup(response1_help, 'lxml')
	
		under_hrefs = soup_help.find_all('a', class_="dark_link option-font-bold section-compact-list__item item bordered box-shadow flexbox flexbox--row", href=True)
		for hr in under_hrefs:
			response3 = requests.get(url+hr['href']).text
			soup3 = BeautifulSoup(response3, 'lxml')
			
			number = soup3.find("div", "nums")
			if number != None:
				num = soup3.find("span", "cur")
				numsber_nms = number.find_all("a", "dark_link")
				end_num = numsber_nms[-1].text
				allHrefs.append(url+hr['href'].replace("\n", ""))

				[allHrefs.append(url+hr['href']+f'?PAGEN_1={web}') for web in range(2, int(end_num)+1)]
					
			else:
				allHrefs.append(url+hr['href'].replace("\n", ""))


	dictCategorys['name-catS']['under-hrefs'] = allHrefs

	return dictCategorys

dict_magnolia = createDataBaseMagnolia()