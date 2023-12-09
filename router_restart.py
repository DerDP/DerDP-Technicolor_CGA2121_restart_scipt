from http.cookiejar import MozillaCookieJar
from bs4 import BeautifulSoup as soup
import requests

cookies = MozillaCookieJar()

login_data = {
    'username_login': '<username>',
    'password_login': '<password>',
    'language_selector': 'en'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

#Create login session and set cookie

with requests.Session() as session:
    session.cookies = cookies
    response = session.post('http://192.168.1.1/goform/logon', data=login_data, cookies=cookies)

print(cookies)
# Using a cookie, load the restart page to obtain token

restart_page = requests.get('http://192.168.1.1/ad_restart_gateway.html', cookies=cookies)

token = soup(restart_page.text, 'html.parser').select_one('input')['value']
token = "csrftoken="+token



# Send data to a ad_restart_gateway form using the token generated before
git reset --hard
restart_data = token+"&tch_devicerestart=0x00"

restart = requests.post('http://192.168.1.1/goform/ad_restart_gateway', cookies=cookies, headers=headers, data=restart_data.encode())

print(restart.text)