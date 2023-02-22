from tkinter import messagebox
################### PRACTICE FILE ################
# var = {"countryCurrency": "$",
#        "price": "$1,700/mo",
#        "unformattedPrice": 1700,
#        "beds": 3,
#        "baths": 2.0,
#        "area": 1435,
#        "latLong": {
#            "latitude": 34.75276,
#            "longitude": -86.88313
#        },
#        "variableData": {
#            "type": "TIME_ON_INFO",
#            "text": "12 days ago",
#        },
#        "hdpData": {
#            "homeInfo": {
#                "latitude": 34.75276,
#                "longitude": -86.88313,
#                "price": 1700.0,
#                "bathrooms": 2.0,
#                "bedrooms": 3.0,
#                "livingArea": 1435.0,
#                "homeType": "SINGLE_FAMILY",
#
#            }
#        },
#        }
#
# x = {
#         "latLong": {
#             "latitude": 32.571724,
#             "longitude": -85.506004
#         },
#         "units": [
#             {
#                 "price": "$950+",
#                 "beds": "1"
#             },
#             {
#                 "price": "$1,200+",
#                 "beds": "2"
#             }
#         ],
#         "variableData": {
#             "type": "TIME_ON_INFO",
#             "text": "16 days ago"
#         },
#     },
#
# URL_4 = "https://www.zillow.com/al/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
#

# based on zipcode
# page_number = 3
# x = f"https://www.zillow.com/{URL_5.split('/')[3]}"
# a = f"{x}/{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page_number}"
# print(a)
# print('https://www.zillow.com/prattville-al-36067/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A3')


# initial_part = f"https://www.zillow.com/{URL_3.split('/')[3]}/"
# add_page_number = f"{initial_part}{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B"
# add_current_page = f"{add_page_number}%22currentPage%22%3A{page_number}"
# initial_length = len(f'{initial_part}?searchQueryState=%7B%22pagination%22%3A%7B')

# based on city
# URL_3 = 'https://www.zillow.com/prattville-al/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A32.85384068136581%2C%22south%22%3A32.17407719848951%2C%22east%22%3A-86.02688113085938%2C%22west%22%3A-87.10628786914063%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54001%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URL_4 = 'https://www.zillow.com/prattville-al/4_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A4%7D%2C%22mapBounds%22%3A%7B%22north%22%3A32.85384068136581%2C%22south%22%3A32.17407719848951%2C%22east%22%3A-86.02688113085938%2C%22west%22%3A-87.10628786914063%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54001%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'

# page_number = 4
# x = f"https://www.zillow.com/{URL_3.split('/')[3]}/"
# mid_part = ""
# add_length_part = '?searchQueryState=%7B%22pagination%22%3A%7B'
# updated_url = f"{URL_3[:len(x)]}{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page_number}{mid_part}{URL_3[len(x + add_length_part):]}"
# print(len(updated_url), len(URL_4))
# if updated_url == URL_4:
#     print('HI')
#
# # sale
# URL_1 = "https://www.zillow.com/al/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-91.679515796875%2C%22east%22%3A-83.044261890625%2C%22south%22%3A29.84942514663804%2C%22north%22%3A35.28079666545284%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# URL_Y = 'https://www.zillow.com/al/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-91.679515796875%2C%22east%22%3A-83.044261890625%2C%22south%22%3A29.84942514663804%2C%22north%22%3A35.28079666545284%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URL_X = "https://www.zillow.com/al/10_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A10%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-92.272777515625%2C%22east%22%3A-83.637523609375%2C%22south%22%3A30.327768270974378%2C%22north%22%3A35.73083732410671%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"

#
# page_number = 10
# initial_part = f"https://www.zillow.com/{URL_1.split('/')[3]}/"
# mid_part = "%7D%2C%22"
# add_length_part = '?searchQueryState=%7B%22'
# updated_url = f"{URL_1[:len(initial_part)]}{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page_number}{mid_part}{URL_1[len(initial_part + add_length_part):]}"
# print(len(updated_url), len(URL_Y))
# if updated_url == URL_Y:
#     print("HO")


# property_purpose = "sale"
# street = ['23962 Fifith Ave', '404 5th St', '107 Parker St', '29791 Low Dr', '117 55th St', '1307 Keith Rd', '119 Normandy Dr', '104 Pine Hill Ln', '3087 Cottage Hill Rd', '23883 Kilkenny Ln', '412 Holly Ridge Dr', '715 Kornegay Loop', '520 Hardwood Ln', '3403 Tall Timbers Cir NW', '256 Westchester Dr', '203 Alice Ln', '1304 Barker Dr E', '1,453 Square Feet Plan, Ingersoll Drive-Starter Houses', '1116 Dixie Ave', '2010 E Lake Blvd', '725 Mimosa Dr', '31705 Wildflower Trl', '102 Jewell St', '607 Euclid Ave', '111 Joiner Rd', '3154 S Holley St', '263 D Thomas Rd', '25957 Canal Rd #303', '12740 Mill Creek Dr', '32167 Terranova Loop', '3066 County Road 503', '9755 Potomac Ridge Dr', '5386 Florida Ave', '305 Wickerberry Way', '2673 County Road 29', '15451 Broad Branch Rd', '2104 Short 14th St', '553 Creekview Dr', '4371 McLain St N', '351 Edgil Rd']
# city = ['Florala', 'Pleasant Grove', 'East Brewton', 'Orange Beach', 'Fairfield', 'Pelham', 'Florence', 'Hayneville', 'Mobile', 'Daphne', 'Montgomery', 'Altoona', 'Birmingham', 'Huntsville', 'Birmingham', 'Prattville', 'Mobile', 'Phenix City', 'Florence', 'Birmingham', 'Anniston', 'Spanish Fort', 'Opp', 'Mobile', 'Hayden', 'Loxley', 'Ozark', 'Orange Beach', 'Northport', 'Lillian', 'Verbena', 'Mobile', 'Orange Beach', 'Athens', 'Abbeville', 'Chunchula', 'Bessemer', 'Pelham', 'Gadsden', 'Jasper']
# state = ['AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL', 'AL']
# zip_code = ['36442', '35127', '36426', '36561', '35064', '35124', '35630', '36040', '36606', '36526', '36109', '35952', '35215', '35810', '35215', '36066', '36608', '36867', '35630', '35217', '36206', '36527', '36467', '36606', '35079', '36551', '36360', '36561', '35473', '36549', '36091', '36695', '36561', '35611', '36310', '36521', '35020', '35124', '35903', '35503']
# latitude = [None, 33.49671, 31.08206, 30.30815, 33.482983, 33.30352, 34.81778, 32.24436, 30.667107, 30.572721, 32.3746, 34.09041, 33.672886, 34.770023, 33.662006, 32.433464, 30.715014, 32.47055, 34.81545, 33.578182, 33.71234, 30.692179, 31.269724, 30.669546, 33.840694, 30.619707, 31.545824, 30.292648, 33.287323, 30.41259, 32.725018, 30.615553, 30.304102, 34.792076, 31.639927, 31.013512, 33.409733, 33.30783, 33.97983, 33.902096]
# longitude = [None, -86.966324, -87.06138, -87.51807, -86.9172, -86.816444, -87.64086, -86.74768, -88.11911, -87.850235, -86.23702, -86.3127, -86.67215, -86.61108, -86.692116, -86.40794, -88.19172, -85.02248, -87.68743, -86.75663, -85.82194, -87.816124, -86.25782, -88.091324, -86.912155, -87.751, -85.564514, -87.58231, -87.637726, -87.47862, -86.48204, -88.271225, -87.52012, -86.96657, -85.31123, -88.10724, -86.981636, -86.81145, -85.89034, -87.36387]
# beds = [5, 3, 3, 3, 2, 3, 3, 4, 4, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 4, 2, 1, 3, 3, 3, 2, 4, 4, 3, 4, 3, 3, 4, 5, 3, 4, 3, 4]
# price = ['$280000.0', '$180000.0', '$99000.0', '$665000.0', '$87900.0', '$225000.0', '$184900.0', '$60000.0', '$177700.0', '$585000.0', '$219900.0', '$157900.0', '$225900.0', '$249900.0', '$114400.0', '$109900.0', '$139900.0', '$199900.0', '$169900.0', '$95999.0', '$59900.0', '$615000.0', '$38500.0', '$45000.0', '$175000.0', '$215000.0', '$37000.0', '$239000.0', '$334900.0', '$296900.0', '$69900.0', '$299330.0', '$450000.0', '$337000.0', '$57000.0', '$224900.0', '$82500.0', '$245000.0', '$189900.0', '$69900.0']
# links = ['https://www.zillow.com/homedetails/23962-Fifith-Ave-Florala-AL-36442/2059105054_zpid/', 'https://www.zillow.com/homedetails/404-5th-St-Pleasant-Grove-AL-35127/1019709_zpid/', 'https://www.zillow.com/homedetails/107-Parker-St-East-Brewton-AL-36426/110287921_zpid/', 'https://www.zillow.com/homedetails/29791-Low-Dr-Orange-Beach-AL-36561/2060399422_zpid/', 'https://www.zillow.com/homedetails/117-55th-St-Fairfield-AL-35064/1023290_zpid/', 'https://www.zillow.com/homedetails/1307-Keith-Rd-Pelham-AL-35124/196339_zpid/', 'https://www.zillow.com/homedetails/119-Normandy-Dr-Florence-AL-35630/67122515_zpid/', 'https://www.zillow.com/homedetails/104-Pine-Hill-Ln-Hayneville-AL-36040/2106829550_zpid/', 'https://www.zillow.com/homedetails/3087-Cottage-Hill-Rd-Mobile-AL-36606/51020575_zpid/', 'https://www.zillow.com/homedetails/23883-Kilkenny-Ln-Daphne-AL-36526/196072144_zpid/', 'https://www.zillow.com/homedetails/412-Holly-Ridge-Dr-Montgomery-AL-36109/72787041_zpid/', 'https://www.zillow.com/homedetails/715-Kornegay-Loop-Altoona-AL-35952/88005_zpid/', 'https://www.zillow.com/homedetails/520-Hardwood-Ln-Birmingham-AL-35215/67747452_zpid/', 'https://www.zillow.com/homedetails/3403-Tall-Timbers-Cir-NW-Huntsville-AL-35810/92080648_zpid/', 'https://www.zillow.com/homedetails/256-Westchester-Dr-Birmingham-AL-35215/900936_zpid/', 'https://www.zillow.com/homedetails/203-Alice-Ln-Prattville-AL-36066/135027_zpid/', 'https://www.zillow.com/homedetails/1304-Barker-Dr-E-Mobile-AL-36608/50986932_zpid/', 'https://www.zillow.com/community/ingersoll-drive-starter-houses/2059096733_zpid/', 'https://www.zillow.com/homedetails/1116-Dixie-Ave-Florence-AL-35630/67126041_zpid/', 'https://www.zillow.com/homedetails/2010-E-Lake-Blvd-Birmingham-AL-35217/945235_zpid/', 'https://www.zillow.com/homedetails/725-Mimosa-Dr-Anniston-AL-36206/109448886_zpid/', 'https://www.zillow.com/homedetails/31705-Wildflower-Trl-Spanish-Fort-AL-36527/120115332_zpid/', 'https://www.zillow.com/homedetails/102-Jewell-St-Opp-AL-36467/248135943_zpid/', 'https://www.zillow.com/homedetails/607-Euclid-Ave-Mobile-AL-36606/51019753_zpid/', 'https://www.zillow.com/homedetails/111-Joiner-Rd-Hayden-AL-35079/297106359_zpid/', 'https://www.zillow.com/homedetails/3154-S-Holley-St-Loxley-AL-36551/196138987_zpid/', 'https://www.zillow.com/homedetails/263-D-Thomas-Rd-Ozark-AL-36360/110287150_zpid/', 'https://www.zillow.com/homedetails/25957-Canal-Rd-303-Orange-Beach-AL-36561/72771793_zpid/', 'https://www.zillow.com/homedetails/12740-Mill-Creek-Dr-Northport-AL-35473/109543269_zpid/', 'https://www.zillow.com/homedetails/32167-Terranova-Loop-Lillian-AL-36549/2060714888_zpid/', 'https://www.zillow.com/homedetails/3066-County-Road-503-Verbena-AL-36091/112768709_zpid/', 'https://www.zillow.com/homedetails/9755-Potomac-Ridge-Dr-Mobile-AL-36695/51049927_zpid/', 'https://www.zillow.com/homedetails/5386-Florida-Ave-Orange-Beach-AL-36561/72766421_zpid/', 'https://www.zillow.com/homedetails/305-Wickerberry-Way-Athens-AL-35611/249167530_zpid/', 'https://www.zillow.com/homedetails/2673-County-Road-29-Abbeville-AL-36310/96817518_zpid/', 'https://www.zillow.com/homedetails/15451-Broad-Branch-Rd-Chunchula-AL-36521/50950585_zpid/', 'https://www.zillow.com/homedetails/2104-Short-14th-St-Bessemer-AL-35020/1044726_zpid/', 'https://www.zillow.com/homedetails/553-Creekview-Dr-Pelham-AL-35124/196670_zpid/', 'https://www.zillow.com/homedetails/4371-McLain-St-N-Gadsden-AL-35903/2062729662_zpid/', 'https://www.zillow.com/homedetails/351-Edgil-Rd-Jasper-AL-35503/2060141379_zpid/']
# file_name = f"{property_purpose}_al.csv"
# for state rental
# URL_ = 'https://www.zillow.com/ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.79006003125%2C%22east%22%3A-66.51955221875%2C%22south%22%3A37.20239954718533%2C%22north%22%3A46.76099642392218%7D%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URD = 'https://www.zillow.com/ny/rentals/6_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A6%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.79006003125%2C%22east%22%3A-66.51955221875%2C%22south%22%3A37.20239954718533%2C%22north%22%3A46.76099642392218%7D%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URLX = 'https://www.zillow.com/ny/rentals/9_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A9%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-83.79006003125%2C%22east%22%3A-66.51955221875%2C%22south%22%3A37.20239954718533%2C%22north%22%3A46.76099642392218%7D%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URL = 'https://www.zillow.com/ny/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A2%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'
# URL_2 = 'https://www.zillow.com/ny/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22usersSearchTerm%22%3A%22NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A2%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'

# URL = 'https://www.zillow.com/new-york-ny/sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51938436914062%2C%22east%22%3A-73.43997763085937%2C%22south%22%3A40.39156689207835%2C%22north%22%3A41.00273448429281%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# URB = 'https://www.zillow.com/new-york-ny/sold/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51938436914062%2C%22east%22%3A-73.43997763085937%2C%22south%22%3A40.39156689207835%2C%22north%22%3A41.00273448429281%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# page_number = 2
# initial_part = f"https://www.zillow.com/{URL.split('/')[3]}/sold/"
# same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
# updated_url = f"{URL[:len(initial_part)]}{page_number}_p/{same_part}%22currentPage%22%3A{page_number}{URL[len(initial_part + same_part):]}"
# print(len(updated_url), len(URB))
# if updated_url == URB:
#     print("HO")


# page_number = 10
# initial_part = f"https://www.zillow.com/{URL.split('/')[3]}/"
# mid_part = "%7D%2C%22"
# add_length_part = '?searchQueryState=%7B%22'
# updated_url = f"{URL[:len(initial_part)]}{page_number}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page_number}{mid_part}{URL[len(initial_part + add_length_part):]}"
# print(len(updated_url), len(URL_2))
# if updated_url == URL_2:
#     print("HO")
# other listing for sale only
# URL_1 = 'https://www.zillow.com/ak/?searchQueryState=%7B%22usersSearchTerm%22%3A%22AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-179.999%2C%22east%22%3A-110.91696875%2C%22south%22%3A48.7465939355191%2C%22north%22%3A72.60605437742127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22category%22%3A%22cat2%22%7D'
# URL_Y = 'https://www.zillow.com/anchorage-ak/2_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Anchorage%2C%20AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-150.52645173828125%2C%22east%22%3A-148.36763826171875%2C%22south%22%3A60.6389082360858%2C%22north%22%3A61.41977180275254%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A23482%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D'
# page_number = 2
# print()
# if URL_1[-6:] == "%7D%7D":
#
# initial_part = f"https://www.zillow.com/{URL_1.split('/')[3]}/"
# different_part = f"%2C%22pagination%22%3A%7B%22currentPage%22%3A{page_number}%7D"
# updated_url = f'{initial_part}{page_number}_p/{URL_1[len(initial_part):]}'[:-3] + different_part + "%7D"
# different_part_2 = f"%22currentPage%22%3A{page_number}%7D"
# updated_url_2 = f'{initial_part}{page_number}_p/{URL_1[len(initial_part):]}'[:-6] + different_part_2 + "%7D"
# print(len(updated_url_2), len(URL_Y))
# if updated_url_2 == URL_Y:
#     print("SAME 2")
# print(len(updated_url), len(URL_Y))
# if updated_url == URL_Y:
#     print("SAMe 1")

# home for sale/ rent/ sold
URL_1 = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.61582637451369%2C%22north%22%3A37.934413316145616%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
URL_Y = 'https://www.zillow.com/homes/for_rent/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.61582637451369%2C%22north%22%3A37.934413316145616%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'


# for sold/ rentals/ sale
# URL_1 = "https://www.zillow.com/homes/recently_sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.61582637451369%2C%22north%22%3A37.934413316145616%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# URL_Y = 'https://www.zillow.com/homes/recently_sold/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.61582637451369%2C%22north%22%3A37.934413316145616%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# page_number = 7
# initial_part = f"https://www.zillow.com/{URL_1.split('/')[3]}/"
# same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
# updated_url = f"{URL_1[:len(initial_part)]}{page_number}_p/{same_part}%22currentPage%22%3A{page_number}{URL_1[len(initial_part + same_part):]}"
# print(len(updated_url), len(URL_Y))
# if updated_url == URL_Y:
#     print("HO")

a = "https://www.zillow.com/ak/?searchQueryState=%7B%22usersSearchTerm%22%3A%22AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-179.999%2C%22east%22%3A-110.91696875%2C%22south%22%3A48.7465939355191%2C%22north%22%3A72.60605437742127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%7D%7D"
b = 'https://www.zillow.com/ak/?searchQueryState=%7B%22usersSearchTerm%22%3A%22AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-179.999%2C%22east%22%3A-110.91696875%2C%22south%22%3A48.7465939355191%2C%22north%22%3A72.60605437742127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22category%22%3A%22cat2%22%7D'

a_1 = 'https://www.zillow.com/tx/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%7D%7D'
a_x = 'https://www.zillow.com/tx/7_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%22currentPage%22%3A7%7D%7D'

page_number = 7
initial_part = f"https://www.zillow.com/{a_1.split('/')[3]}/"
same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
update_rl = f"{a_1[:len(initial_part)]}{page_number}_p/{same_part}%22currentPage%22%3A{page_number}{a_1[len(initial_part + same_part):]}"
print("COMPARE: ", len(a_x))
print("UPDATE: ", len(update_rl))
if a_x == update_rl:
    print("SAME URL")




