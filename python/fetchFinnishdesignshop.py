from bs4 import BeautifulSoup
import asyncio
import uvloop
import aiohttp
from bs4 import BeautifulSoup
from model import Product
# pip3 install aiohttp cchardet aiodns
import ujson
from json2xls.json2xls import Json2Xls
import copy

def write_to_json(list):
    final_res_json = ujson.dumps(list, indent=4)
    write_to_json = "final_res.json"
    obj = open(write_to_json, 'w')
    obj.write(final_res_json)
    obj.close


def write_to_xls(list):
    final_res_excel_json = ujson.dumps(list, indent=4)
    file_name_xls = "final_res.xls"
    Json2Xls(file_name_xls, json_data=final_res_excel_json).make()


if __name__ == '__main__':
    # zhilian = Crawler_zhilian()
    # zhilian.url = Zl_url
    # zhilian.page_nums = 5
    # zhilian.encoding = "utf-8"
    # for zip_date in zhilian.run():
    #     for company, salary, address, date, name, url in zip_date:
    #         print(company, salary, address, date, name, url)
    #     break
    print(" START FETCH PAGE ")

    final_res = []
    final_res_excel = []


    # URL = 'http://httpbin.org/get?a={}'
    sema = asyncio.Semaphore(10)

    async def fetch_async(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.status)
                data = await resp.text()
                p    = Product()
                p.parse(data)
                print(p.__dict__)
                return p

    async def print_result(url):
        with (await sema):
            r = await fetch_async(url)
            print('fetch({}) = {}'.format(url, r))
            final_res.append(r.__dict__)

            r_excel = copy.deepcopy(r)
            r_excel.deal_for_excel()
            final_res_excel.append(r_excel.__dict__)


    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    # https://www.finnishdesignshop.com/outdoor-outdoor-furniture-c-896_779.html
    # var arr = jQuery.map( $('.thumbnail > a'), function(a)
    # {
    # return '"' + $(a).attr("href") + '"\n'
    # });
    # console.log(arr);
    # console.log(arr.join(","));

    URLS = [
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-mira-armchair-hunter-green-p-14127.html"
        , "https://www.finnishdesignshop.com/-mira-chair-anthracite-black-p-14126.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-mira-chair-hunter-green-p-14125.html"
        , "https://www.finnishdesignshop.com/-mira-table-160-anthracite-black-p-14132.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-mira-table-160-hunter-green-p-14131.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-mira-table-anthracite-black-p-14130.html"
        , "https://www.finnishdesignshop.com/-mira-table-hunter-green-p-14129.html"
        , "https://www.finnishdesignshop.com/-mira-armchair-anthracite-black-p-14128.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-cushion-for-dining-chair-outdoor-dark-grey-p-13836.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-cushion-for-dining-chair-outdoor-ivory-white-p-13835.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-cushion-for-lounge-chair-outdoor-dark-grey-p-13838.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-cushion-for-lounge-chair-outdoor-ivory-white-p-13837.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-dining-chair-black-p-9658.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-dining-chair-dusty-green-p-13827.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-dining-chair-white-p-9659.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-lounge-chair-black-p-9656.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-lounge-chair-dusty-green-p-13828.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-string-lounge-chair-white-p-9657.html"
        , "campaigns.php"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-anthracite-p-11621.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-aubergine-p-11611.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-carrot-p-11627.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-cedar-green-p-11623.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-chili-p-11612.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-cotton-white-p-11626.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-fuchsia-p-11614.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-honey-p-11616.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-lagoon-blue-p-11618.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-linen-p-11625.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-liquorice-p-11620.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-nutmeg-p-11629.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-paprika-p-11615.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-plum-p-11628.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-poppy-p-11613.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-russet-p-11610.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-steel-grey-p-11622.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-storm-grey-p-11630.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-turquoise-p-11619.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-verbena-green-p-11617.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-pcs-willow-green-p-11624.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-anthracite-p-9786.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-aubergine-p-7788.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-carrot-p-7790.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-cedar-green-p-6756.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-chili-p-6752.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-cotton-white-p-6755.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-fuchsia-p-7787.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-honey-p-7791.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-lagoon-blue-p-9787.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-linen-p-7777.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-liquorice-p-6751.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-nutmeg-p-7778.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-paprika-p-7780.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-plum-p-7789.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-poppy-p-7775.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-russet-p-7781.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-steel-grey-p-6753.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-storm-grey-p-7774.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-turquoise-p-7784.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-verbena-p-7786.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chair-willow-green-p-7783.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chaise-longue-cedar-green-p-6749.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chaise-longue-cotton-white-p-6750.html"
        ,
        "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-metal-chaise-longue-liquorice-p-13862.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-117-p-6745.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-117-cotton-white-p-12263.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-p-6748.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-cotton-white-p-12260.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-anthracite-p-13863.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-p-6746.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-cotton-white-p-12262.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-p-6747.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-bistro-table-cotton-white-p-12261.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-high-anthracite-black-p-12010.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-high-hunter-green-p-12009.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-high-silver-white-p-12007.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-high-slate-grey-p-12008.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-low-anthracite-black-p-12014.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-low-hunter-green-p-12013.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-low-silver-white-p-12011.html"
        , "https://www.finnishdesignshop.com/furniture-tables-skagerak-bow-bow-table-low-slate-grey-p-12012.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-breeze-dining-chair-black-p-7894.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-breeze-dining-chair-stackable-black-p-7893.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-breeze-footstool-black-p-7890.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-breeze-highback-chair-black-p-7891.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-breeze-lounge-chair-black-p-7892.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-black-p-2826.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-brown-p-3603.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-dark-blue-p-6617.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-light-grey-p-6619.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-lime-p-2828.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-orange-p-2823.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-petrol-p-6618.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-pink-p-6620.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-red-p-2824.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-sand-p-6616.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-taupe-p-3604.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-turquoise-p-2825.html"
        , "https://www.finnishdesignshop.com/outdoor-outdoor-furniture-buggle-bean-bag-white-p-2827.html"
        ,
        "https://www.finnishdesignshop.com/furniture-chairs-magis-chair-one-chair-one-black-painted-aluminium-legs-p-6077.html"
        ,
        "https://www.finnishdesignshop.com/furniture-chairs-magis-chair-one-chair-one-white-polished-aluminium-legs-p-6078.html"
    ]



    f = asyncio.wait([print_result(num) for num in URLS])
    loop.run_until_complete(f)
    loop.close()

    write_to_json(final_res)
    write_to_xls(final_res_excel)

    print(final_res)