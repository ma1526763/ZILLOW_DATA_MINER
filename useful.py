####################### PRACTICE FILE #####################

# this url works for sale/rentals/sold when currentPage is inside
def sale_rental_sold_current_page_in(URL, url_c, p_num, purpose=""):
    page_number = p_num
    initial_part = f"https://www.zillow.com/{URL.split('/')[3]}/{purpose}"
    if URL[-6:] == "%7D%7D":
        different_part = "%22currentPage%22%3A7"
        update_url = f"{initial_part}{page_number}_p/{URL[len(initial_part):]}"[:-6] + different_part + "%7D%7D"
    else:
        print("IN")
        same_part = "?searchQueryState=%7B%22pagination%22%3A%7B"
        update_rl = f"{URL[:len(initial_part)]}{page_number}_p/{same_part}%22currentPage%22%3A{page_number}{URL[len(initial_part + same_part):]}"
        # print(update_rl)
        # print()
        # print(url_c)
        print("COMPARE: ", len(url_c))
        print("UPDATE: ", len(update_rl))
        if url_c == update_rl:
            print("SAME URL for current_page_in")

# when current page in for sale/rentals/sold
# u = 'https://www.zillow.com/ny/sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'
# c = 'https://www.zillow.com/ny/sold/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%7D'

# when current page is outside for sale/rentals/sold
# u = 'https://www.zillow.com/tx/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%7D%7D'
# c = 'https://www.zillow.com/tx/7_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%22currentPage%22%3A7%7D%7D'

u = 'https://www.zillow.com/ak/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-179.999%2C%22east%22%3A-110.91696875%2C%22south%22%3A48.7465939355191%2C%22north%22%3A72.60605437742127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D'
c = 'https://www.zillow.com/ak/rentals/5_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A5%7D%2C%22usersSearchTerm%22%3A%22AK%22%2C%22mapBounds%22%3A%7B%22west%22%3A-179.999%2C%22east%22%3A-110.91696875%2C%22south%22%3A48.7465939355191%2C%22north%22%3A72.60605437742127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%7D'
# sale_rental_sold_current_page_in(u, c,p_num=5, purpose="rentals/")


# checking
# u1 = 'https://www.zillow.com/ny/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A722north%22%3A45.10925919908303%2C%22south%22%3A40.3767460135696%2C%22east%22%3A-71.452413546875%2C%22west%22%3A-80.087667453125%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%2C%22category%22%3A%22cat1%22%7D'
# u2 = 'https://www.zillow.com/ny/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22mapBounds%22%3A%7B%22north%22%3A45.10925919908303%2C%22south%22%3A40.376746013569594%2C%22east%22%3A-71.452413546875%2C%22west%22%3A-80.087667453125%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'


# for other listing perfectly done
def update_url_for_other_listing(URL, url_c):
    page_number = 2
    initial_part = f"https://www.zillow.com/{URL.split('/')[3]}/"
    if URL[-6:] == "%7D%7D":
        different_part = f"%22currentPage%22%3A{page_number}%7D"
        update_url = f'{initial_part}{page_number}_p/{URL[len(initial_part):]}'[
                       :-6] + different_part + "%7D"
        print("COMPARE OTEHR LISTING %7D%7D: ", len(url_c))
        print("UPDATED OTHER LISTING %7D%7D", len(update_url))
        if url_c == update_url:
            print("OTHER LISTING SAME FOR %7D%7D")
    else:
        different_part = f"%2C%22pagination%22%3A%7B%22currentPage%22%3A{page_number}%7D"
        update_url = f'{initial_part}{page_number}_p/{URL[len(initial_part):]}'[
                       :-3] + different_part + "%7D"
        print("COMPARE OTEHR LISTING %7D: ", len(url_c))
        print("UPDATED OTHER LISTING %7D: ", len(update_url))
        if url_c == update_url:
            print("OTHER LISTING SAME FOR %7D")

# for other listing for % 7D
# u = 'https://www.zillow.com/ny/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%2C%22category%22%3A%22cat2%22%7D'
# c = 'https://www.zillow.com/ny/7_p/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-80.087667453125%2C%22east%22%3A-71.452413546875%2C%22south%22%3A40.3767460135696%2C%22north%22%3A45.10925919908303%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A43%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A7%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%22currentPage%22%3A7%7D%7D'
# for other listing for %7D%7D
# u = 'https://www.zillow.com/tx/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%7D%7D'
# c = 'https://www.zillow.com/tx/7_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22TX%22%2C%22mapBounds%22%3A%7B%22west%22%3A-108.71209640625%2C%22east%22%3A-91.44158859375%2C%22south%22%3A25.655180760546923%2C%22north%22%3A36.66294370573086%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A54%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A6%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%22currentPage%22%3A7%7D%7D'
# u = 'https://www.zillow.com/columbus-oh/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A40.29131407332305%2C%22south%22%3A39.67363767201555%2C%22east%22%3A-82.44842463085938%2C%22west%22%3A-83.52783136914063%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10920%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%7D'
# c = 'https://www.zillow.com/columbus-oh/2_p/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A40.29131407332305%2C%22south%22%3A39.67363767201555%2C%22east%22%3A-82.44842463085938%2C%22west%22%3A-83.52783136914063%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A10920%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D'

ux = 'https://www.zillow.com/la/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22LA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-95.71947702865661%2C%22east%22%3A-87.08422312240661%2C%22south%22%3A28.156311377951432%2C%22north%22%3A33.68506531672592%7D%2C%22mapZoom%22%3A7%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'
if 'cat2' in ux:
    print("YES")