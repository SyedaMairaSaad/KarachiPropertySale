#!pip install beautifulsoup4
#!pip install lxml

quote = {};
import requests
from bs4 import BeautifulSoup
def innerScrap(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    row = soup.find('main')

    try:
        quote['Type'] = row.find('span',attrs={'aria-label':'Type'}).text.strip();
    except (AttributeError, NameError):
        quote['Type']='';
    try:
        quote['Purpose'] = row.find('span',attrs={'aria-label':'Purpose'}).text.strip();
    except (AttributeError, NameError):
        quote['Purpose']='';
    try:
        quote['near_by_schools'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#schools'}).text.strip();quote['near_by_schools']='Y';
    except (AttributeError, NameError):
    	quote['near_by_schools']='N';
    try:
        quote['near_by_hospitals'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#hospitals'}).text.strip();quote['near_by_hospitals'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_hospitals']='N';
    try:
        quote['near_by_restaurant'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#restaurants'}).text.strip();quote['near_by_restaurant'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_restaurant']='N';
    try:
        quote['near_by_airport'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#distance-from-airport-(kms)'}).text.strip();quote['near_by_airport'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_airport']='N';
    try:
        quote['near_by_public_transport'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#public-transport-service'}).text.strip();quote['near_by_public_transport'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_public_transport']='N';
    try:
        quote['parking_slot_available'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#parking-spaces'}).text.strip();quote['parking_slot_available'] ='Y';
    except (AttributeError, NameError):
    	quote['parking_slot_available']='N';
    try:
        quote['near_by_shopping_mall'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#shopping-malls'}).text.strip();quote['near_by_shopping_mall'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_shopping_mall']='N';
    try:
        quote['near_by_shopping_mall'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#shopping-malls'}).text.strip();quote['near_by_shopping_mall'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_shopping_mall']='N';
    try:
        quote['near_by_shopping_mall'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#shopping-malls'}).text.strip();quote['near_by_shopping_mall'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_shopping_mall']='N';
    try:
        quote['near_by_shopping_mall'] = row.find('use',attrs={'xlink:href':'/assets/iconAmenities_noinline.8dbde8780eff18a63210a01d691e1c6b.svg#shopping-malls'}).text.strip();quote['near_by_shopping_mall'] ='Y';
    except (AttributeError, NameError):
    	quote['near_by_shopping_mall']='N';
#**Below code fetch fetch parameter from zameen.com dataset page**</br>
#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
City='Islamabad';
quotes=[] # a list to store quotes
for i in range(1,460):
	print("page number"+str(i))
	URL = "https://www.zameen.com/Homes/"+City+"-2-"+str(i)+".html";

	r = requests.get(URL)

	soup = BeautifulSoup(r.content, 'lxml')



	table = soup.find('div', attrs = {'class':'_41cc3033 _7a3728c3'})
	i=0;
	for row in table.findAll('li', attrs = {'role':'article'}):
		i=i+1
		print('Record number'+str(i));

		quote['url'] = 'https://www.zameen.com/'+row.a['href'];
		quote['price'] = row.find('span',attrs={'aria-label':'Price'}).text.strip();
		quote['Title'] = row.find('h2',attrs={'aria-label':'Title'}).text.strip();
		quote['Location'] = row.find('div',attrs={'aria-label':'Location'}).text.strip();
		quote['City']=City;
		try:
			quote['Beds'] = row.find('span',attrs={'aria-label':'Beds'}).text.strip();
		except (AttributeError, NameError):
			quote['Beds']='';
		try:
			quote['Baths'] = row.find('span',attrs={'aria-label':'Baths'}).text.strip();
		except (AttributeError, NameError):
			quote['Baths']='';
		try:
			quote['Area'] = row.find('span',attrs={'aria-label':'Area'}).text.strip();
		except (AttributeError, NameError):
			quote['Area']='';
		quote['Upload_Date'] = row.find('span',attrs={'aria-label':'Listing creation date'}).text.strip();
		#print(quote['Upload_Date'])
		#print('hours' in str(quote['Upload_Date']))
		try:
			quote['Upload_Date'] = row.find('span',attrs={'aria-label':'Listing creation date'}).text.strip();
        except (AttributeError, NameError):
			quote['Upload_Date']='';

		innerScrap(quote['url'])
		quotes.append(quote);
		quote = {};
#writing data to csv file
from csv import writer
filename = '/content/drive/MyDrive/property_zammen_karachi_data1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url','price','Title','Location','City','Beds','Baths','Area','Upload_Date','Type','Purpose','near_by_schools','near_by_hospitals','near_by_airport','near_by_restaurant','near_by_public_transport','near_by_shopping_mall','parking_slot_available'])
    w.writeheader();
    for quote in quotes:
        w.writerow(quote)