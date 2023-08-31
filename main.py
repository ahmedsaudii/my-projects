# from bs4 import BeautifulSoup
# import requests
# import numpy as np
# import pandas as pd
# import urllib.parse
# import xlsxwriter
#
# productname = []
# productprice = []
# productinfos = []
# producturl = []
# compinedurls = []
#
# for i in range(1, 400):
#     website = 'https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops?pageNumber=' + str(i)
#
#     response = requests.get(website)
#
#     assert response.status_code == 200
#
#     contents = BeautifulSoup(response.content, ('html.parser'))
#
#     laptop = contents.find('div', id='products')
#
#     rooturl='https://www.laptopsdirect.co.uk'
#
#     url = laptop.find_all('a', class_='offerboxtitle')
#
#     names = laptop.find_all('a', class_='offerboxtitle')
#
#     prices = laptop.find_all('span', class_='offerprice')
#
#     detail = laptop.find_all('ul')
#
#     for n in names:
#
#         try:
#             productname.append(n.text.strip())
#         except:
#             productname.append('n/a')
#     for p in prices:
#         try:
#             productprice.append(p.text.strip())
#         except:
#             productprice.append('n/a')
#     for r in url:
#         try:
#             producturl.append(r.get('href'))
#         except:
#             producturl.append('n/a')
#     for d in detail:
#         try:
#             productinfos.append(d.text.strip().replace("\n", " "))
#         except:
#             productinfos.append('n/a')
#
# for link in producturl:
#         compinedurls.append(urllib.parse.urljoin(rooturl,link))
#
# productover_view = pd.DataFrame({'name': productname, 'detail': productinfos, 'price': productprice,'url':compinedurls})
#
# productover_view.to_csv('laptops.csv',index=False)
#
