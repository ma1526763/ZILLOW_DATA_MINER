import json
import requests
import pandas
from bs4 import BeautifulSoup

# URL = "https://www.zillow.com/al/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22AL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-90.99774535587463%2C%22east%22%3A-82.36249144962463%2C%22south%22%3A29.8542035248672%2C%22north%22%3A35.285294025691336%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D"
# # for sale
# URL_1 = "https://www.zillow.com/al/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# URL_2 = "https://www.zillow.com/al/6_p/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%22currentPage%22%3A6%7D%7D"
# # rental url
# URL_3 = 'https://www.zillow.com/al/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.32776827097438%2C%22north%22%3A35.73083732410671%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'
# URL_4 = 'https://www.zillow.com/al/rentals/10_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A10%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.32776827097438%2C%22north%22%3A35.73083732410671%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'
# # sold url
# URL_5 = 'https://www.zillow.com/al/sold/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%7D%7D'
# URL_6 = 'https://www.zillow.com/al/sold/4_p/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%22currentPage%22%3A4%7D%7D'


class ZILLOW_DATA:
    def __init__(self, url):
        self.url = url
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 '
        self.accept_language = 'en-US,en;q=0.9'
        self.headers = {
            'User-Agent': self.user_agent,
            'Accept-Language': self.accept_language,
        }
        self.page_number = 1
        self.property_purpose = "sale"
        self.COLUMNS = ["street_address", "city", "state", "zipCode", "latitude", "longitude", "beds", "sale_price",
                        "listed_date", "property_link"]
        self.page_title = ""
        self.file_name = ""
        self.new_url = url
        self.property_street_address_list = []
        self.property_city_address_list = []
        self.property_state_address_list = []
        self.property_zipcode_address_list = []
        self.property_latitude_list = []
        self.property_longitude_list = []
        self.property_beds_list = []
        self.property_price_list = []
        self.property_time_info = []
        self.property_link_list = []
        self.get_property_purpose()
        # print(self.url)

    def get_property_purpose(self):
        if 'rentals' in self.url:
            self.COLUMNS[7] = "rent_price/month"
            self.property_purpose = "rentals"
        elif 'sold' in self.url:
            self.COLUMNS[7] = 'sold_price'
            self.COLUMNS[8] = "sold_date"
            self.property_purpose = 'sold'

    def validate_url(self):
        if not self.url.startswith("https://www.zillow.com/"):
            return False
        response = requests.get(url=self.new_url, headers=self.headers)
        if len(response.url) < 60:
            return False
        soup_data = BeautifulSoup(response.text, 'html.parser')
        return soup_data if soup_data.find(class_='result-count') or soup_data.find(class_='total-text') else False

    def extract_data(self, s):
        self.page_title = s.find(name='title').text
        print(f"EXTRACTING PAGE# {self.page_number}", end=" --- ")
        page_data = json.loads(
            s.find("script", attrs={"data-zrr-shared-data-key": "mobileSearchPageStore"}).text.strip('<!->'))
        # with open("zillow_data.json", "w") as file:
        #     json.dump(page_data, file, indent=4)
        page_data = page_data['cat1']['searchResults']['listResults']
        # print(page_data)
        for i, house_info in enumerate(page_data):
            # get property link
            link = house_info['detailUrl']
            self.property_link_list.append(f"https://www.zillow.com{link}") if not link.startswith(
                "https://") else self.property_link_list.append(link)

            # get property address
            if self.property_purpose == 'rentals':
                self.property_street_address_list.append(f"{house_info['statusText']} - {house_info['address']}")
            else:
                self.property_street_address_list.append(house_info['addressStreet'])
            self.property_city_address_list.append(house_info['addressCity'])
            self.property_state_address_list.append(house_info['addressState'])
            self.property_zipcode_address_list.append(house_info['addressZipcode'])

            # get price
            try:
                price = f"${house_info['hdpData']['homeInfo']['price']}"
            except KeyError:
                price = "/".join([p['price'] for p in house_info['units']])
            self.property_price_list.append(price)

            # get beds list
            try:
                beds = house_info['beds']
            except KeyError:
                beds = "/".join([b['beds'] for b in house_info['units']])
            self.property_beds_list.append(beds)

            # get longitude and latitude
            try:
                self.property_latitude_list.append(house_info['latLong']['latitude'])
            except KeyError:
                self.property_latitude_list.append(None)
            try:
                self.property_longitude_list.append(house_info['latLong']['longitude'])
            except KeyError:
                self.property_longitude_list.append(None)

            # get time info
            self.property_time_info.append(house_info['variableData']['text'])

    def update_url(self):
        self.page_number += 1
        if self.property_purpose == 'sale':
            print("updating sale url.")
            initial_part = f"https://www.zillow.com/{self.url.split('/')[3]}/"
            mid_part = "%7D%2C%22"
            add_length_part = '?searchQueryState=%7B%22'
            self.new_url = f"{self.url[:len(initial_part)]}{self.page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{self.page_number}{mid_part}{self.url[len(initial_part + add_length_part):]}"
        elif self.property_purpose == 'rentals':
            print("updating rentals url.")
            initial_part = f"https://www.zillow.com/{self.url.split('/')[3]}/rentals/"
            same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
            self.new_url = f"{self.url[:len(initial_part)]}{self.page_number}_p/{same_part}%22currentPage%22%3A{self.page_number}{self.url[len(initial_part + same_part):]}"
        else:
            print("updating sold url.")
            initial_part = f"https://www.zillow.com/{self.url.split('/')[3]}/sold/"
            same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
            self.new_url = f"{self.url[:len(initial_part)]}{self.page_number}_p/{same_part}%22currentPage%22%3A{self.page_number}{self.url[len(initial_part + same_part):]}"

    def upload_data_to_csv_sheet(self):
        if self.property_purpose == "rentals":
            extended_file_name = self.page_title.split('|')[0].split('-')[0]
        else:
            extended_file_name = self.page_title.split('|')[0]
        self.file_name = f"{self.property_purpose.upper()}_{extended_file_name}"[:-1]
        complete_data_list = []
        for i in range(len(self.property_city_address_list)):
            complete_data_list.append(self.get_new_house_info(i))
        # upload data to csv file
        dataframe = pandas.DataFrame(columns=self.COLUMNS, data=complete_data_list)
        dataframe.to_csv(f"csv_data_extracted/{self.file_name}.csv", index=False)

    def upload_data_to_json_file(self):
        json_data = {}
        with open(f"json_data_extracted/{self.file_name}.json", "w") as file:
            for i in range(len(self.property_city_address_list)):
                json_data[f"house_{i + 1}"] = self.get_new_house_info(i)
            json.dump(json_data, file, indent=4)

    def get_new_house_info(self, i):
        price_key = ""
        date_info = "listed_date"
        if self.property_purpose == 'sale':
            price_key = "sale_price"
        elif self.property_purpose == 'rentals':
            price_key = "rent_price/month"
        elif self.property_purpose == 'sold':
            price_key = "sold_price"
            date_info = "sold_date"

        return {"street_address": self.property_street_address_list[i],
                "city": self.property_city_address_list[i],
                "state": self.property_state_address_list[i],
                "zipCode": self.property_zipcode_address_list[i],
                "latitude": self.property_latitude_list[i],
                "longitude": self.property_longitude_list[i],
                "beds": self.property_beds_list[i],
                price_key: self.property_price_list[i],
                date_info: self.property_time_info[i],
                "property_link": self.property_link_list[i],
                }

    # def check_already_file(self):
    #     print(self.file_name)
    #     try:
    #         with open(self.file_name) as file:
    #             file.readline()
    #     except FileNotFoundError:
    #         print("EXCEPTION")
    #         return False
    #     else:
    #         ask_user = messagebox.askokcancel(title="Already Exist", message=f"\"{self.file_name}\" already exist Do you want to extract data again?")
    #         print("ASK USER", ask_user)
# URL = 'https://www.zillow.com/al/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# zillow = ZILLOW_DATA(URL)
# soup = zillow.validate_url()
# if soup:
#     zillow.extract_data(soup)
# print(zillow.property_street_address_list, zillow.property_city_address_list, zillow.property_state_address_list,
#       zillow.property_zipcode_address_list, zillow.property_latitude_list, zillow.property_longitude_list,
#       zillow.property_beds_list, zillow.property_price_list, zillow.property_link_list)
# zillow.upload_data_to_csv_sheet()

# zillow = ZILLOW_DATA(URL)

# while True:
#     soup = zillow.validate_url()
#     if soup:
#         zillow.extract_data(soup)
#         # print("Page#", zillow.page_number, len(zillow.property_street_address_list), len(zillow.property_time_info), len(zillow.property_price_list), len(zillow.property_beds_list), len(zillow.property_link_list), len(zillow.property_longitude_list))
#         zillow.url = zillow.update_url()
#     else:
#         print("INVALID")
#         break
# zillow.upload_data_to_csv_sheet()
