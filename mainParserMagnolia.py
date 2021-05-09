from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from Magnolia import dict_magnolia

def parserProductsMagnolia():
	global dict_magnolia

	TheAllMagnoliaProductsData = {"Category":[],
												"Name":[],
												"OldPrice":[],
												"NewPrice":[],
												"Measure":[]}

	
	for url in dict_magnolia['name-catS']['under-hrefs']:
		page = requests.get(url).text
		prSoup = BeautifulSoup(page, 'lxml')

		cat = prSoup.find_all(class_="breadcrumbs__item-name font_xs")

		names = prSoup.find_all("a", class_="dark_link option-font-bold font_sm")
		
		info_wrapp = prSoup.find_all("div", class_="cost prices clearfix")
		
		print("Category - ", len(TheAllMagnoliaProductsData['Category']))
		print("Name - ", len(TheAllMagnoliaProductsData['Name']))
		print("Old - ", len(TheAllMagnoliaProductsData['OldPrice']))
		print("New - ", len(TheAllMagnoliaProductsData['NewPrice']))
		print("Measure - ", len(TheAllMagnoliaProductsData['Measure']))

		for inf in info_wrapp:
			new_price_podvod = inf.find("div", class_="price_group min 1618b9f0-7969-11ea-9fc5-40167e7389e1")
			old_price_podvod = inf.find("div", class_="price_group acb496c6-9506-11ea-80bf-00505697dbd3")
			
			

			if new_price_podvod == None or old_price_podvod == None:
				
				simple_price = inf.find("span", class_="price_value")
				price_measure = inf.find("span", class_="price_measure")

				if simple_price != None or price_measure != None:

					TheAllMagnoliaProductsData['OldPrice'].append(simple_price.text)
					TheAllMagnoliaProductsData['NewPrice'].append("not/app")
					TheAllMagnoliaProductsData['Measure'].append(price_measure.text)
					TheAllMagnoliaProductsData['Category'].append(cat[-1].text)

			else:
				price_measure = inf.find("span", class_="price_measure")
				old = old_price_podvod.find("span", class_="price_value").text
				TheAllMagnoliaProductsData['Category'].append(cat[-1].text)
				new = new_price_podvod.find("span", class_="price_value").text
				#--------------------------------------------------	
				TheAllMagnoliaProductsData['OldPrice'].append(old)
				
				TheAllMagnoliaProductsData['NewPrice'].append(new)
				
				TheAllMagnoliaProductsData['Measure'].append(str(price_measure))


		for j in names:
			TheAllMagnoliaProductsData['Name'].append(j.text)

	return TheAllMagnoliaProductsData
	

parser = parserProductsMagnolia()