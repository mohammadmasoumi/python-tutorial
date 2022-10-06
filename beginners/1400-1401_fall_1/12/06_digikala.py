import http
import requests

headers = {
    "cookie": 'PHPSESSID=sg4bjml2s4pr5chdcf57cjgok52q1or4ortft043f3pbl9e16cc2kb78grlrgm1l; tracker_global=4E1MWJpQ; tracker_session=4E1MWJpR; sn_tracker_campaign={"u_medium":"SEO","u_source":"https://www.bing.com/","u_campaign":"Organic","u_term":"Organic","u_content":"Organic"}; __asc=6f0e89e217ce9d63824d836ba2d; __auc=6f0e89e217ce9d63824d836ba2d; _gid=GA1.2.1129139295.1636010705; _gat_UA-13212406-1=1; _conv_s=si:1*sh:1636010705224-0.18120652423787997*pv:1; _conv_r=s:www.bing.com*m:referral*t:*c:; _conv_v=vi:1*sc:1*cs:1636010705*fs:1636010705*pv:1*exp:{}; TS011a822c=0102310591f27eaaddb1f0c2dcea9488c8a6fd2592b61c86def4782b6a7699262029007f73f9823d91ba30c8438ca527fdbe7d9467e26ad3b49ed83bbc17eea9cf03700572032142e70ec18a5b68a2c35796271e4abc73aeb024440897053a9b69cf30eed10ce6c359c8581cbb898f792c4d3ef3f56caa38aa9f1700e89c51dc8c9c669675794590ef3f7de564164a65ca440c733f; _ga_4S04WR965Q=GS1.1.1636010703.1.1.1636010761.0; _ga_LR50FG4ELJ=GS1.1.1636010703.1.1.1636010761.2; _ga=GA1.2.1279875677.1636010705'
}
response = requests.get("https://www.digikala.com/recommendation/v1/", headers=headers)
with open("digikala.txt", "w") as file:
    file.write(response.text)

print(response.status_code)
print(response.text)
