import requests
from bs4 import BeautifulSoup
import lxml

ZILLOW_SEARCH = "https://www.zillow.com/el-paso-tx/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A32.03742366637929%2C%22east%22%3A-105.63258268847656%2C%22south%22%3A31.479278565917745%2C%22west%22%3A-106.86717131152344%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22built%22%3A%7B%22min%22%3A1900%2C%22max%22%3A1981%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A17933%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"
PROPERTY_RESEARCH_FORM_URL = "https://forms.gle/Xk9RAMULh9EPP5ks5"
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

class Property_Scraper:
    def __init__(self):
        pass

    def get_zillow_data(self):
        zillow_response = requests.get(url=ZILLOW_SEARCH, headers=HEADERS)
        soup = BeautifulSoup(zillow_response.text, 'lxml')
        property_data_html = soup.find_all(class_="property-card")
        for property_data in property_data_html:
            # print(property_data)
            property_address = property_data.find(attrs={"data-test": "property-card-addr"}).text
            purchase_price = property_data.find(attrs={"data-test": "property-card-price"}).text
            property_link = property_data.find(attrs={"data-test": "property-card-link"})['href']
            description = ""
            print(f"address: {property_address}, price: {purchase_price}, link: {property_link}")
