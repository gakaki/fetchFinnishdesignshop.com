from bs4 import BeautifulSoup
import pprint

class Product(object):
    """docstring for Model"""

    def __init__(self):
        super(Product, self).__init__()

        self.name = ""
        self.product_id = ""
        self.menu_text = ""
        self.menu_links = []

        self.desc = ""
        self.manufacturer = ""
        self.manufacturer_link = ""

        self.delivery = ""
        self.designer = ""
        self.designer_link = ""
        self.size = ""
        self.material = ""
        self.color = ""
        self.light_source = ""
        self.light_source = ""
        self.mounting = ""
        self.availability = ""
        self.price = ""
        self.img_main = ""
        self.img_extends = []

    def get_node_text_by_index(self, list, index):
        if index < len(list):
            return list[index].text
        else:
            return ""

    def deal_for_excel(self):
        self.img_extends = ",".join(self.img_extends)
        self.menu_links  = ",".join(self.menu_links)


    def parse(self, htm_str):
        soup = BeautifulSoup(htm_str, "html.parser")

        domain = "https://www.finnishdesignshop.com/"

        ol_menu = soup.find("", class_="breadcrumb")
        self.menu_text = (" > ").join([li.text for li in ol_menu.find_all("li", "")])
        self.menu_links = [a.attrs["href"] for a in ol_menu.find_all("a")]

        self.img_main = soup.select_one("#main_image_link img[src!='']").attrs["src"]

        img_extends = soup.select(".carousel-indicators img[src!='']")
        self.img_extends = [domain + img.attrs["src"] for img in img_extends]

        self.desc = soup.select_one("span[itemprop='description']").text

        dt_infos = soup.select("dl.dl-inline dt")
        dd_infos = soup.select("dl.dl-inline dd")

        manufacturer = dd_infos[0].find("a")
        self.manufacturer = manufacturer.text
        self.manufacturer_link = manufacturer.get("href")

        designer = dd_infos[1].find("a")
        self.designer = designer.text
        self.designer_link = designer.get("href")

        print(dt_infos);
        print(dd_infos);

        for i in range(2, 6 + 1):
            column_name     = self.get_node_text_by_index(dt_infos,i)
            column_value    = self.get_node_text_by_index(dd_infos,i)
            column_name     = column_name.lower().replace(" ", "_")
            setattr(self,column_name,column_value)

        # self.size = self.get_dd_text_by_index(dd_infos, 2)
        # self.material = self.get_dd_text_by_index(dd_infos, 3)
        # self.color = self.get_dd_text_by_index(dd_infos, 4)
        # self.light_source = self.get_dd_text_by_index(dd_infos, 5)
        # self.mounting = self.get_dd_text_by_index(dd_infos, 6)
        
        self.name = soup.select_one("span.custom-underline").text

        self.availability = soup.select_one("#delivery").text

        self.price = soup.select_one("#price [data-price_id='2/usd']").text

        self.delivery = soup.select_one("#mw-estimator-info").text

        self.product_id = soup.select_one("input[name=products_id]").get("value")

        self.product_url = soup.select_one("link[rel=canonical]").get("href")

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(self.__dict__)



if __name__ == '__main__':
    html_str = open("product_item.html")
    p = Product()
    p.parse(html_str)
    print(p.product_url)
			

			
			
			
			
			
			
			
			
			