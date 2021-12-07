import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

LANGS_URL = "https://www.science.co.il/language/Locale-codes.php"
URL = "https://google-translate1.p.rapidapi.com/language/translate/v2"
RAPID_API_KEY = "rapid-api-key"


def find_lang_code(lang):
    chrome_driver_path = "C:\Tools\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(LANGS_URL)

    all_langs = driver.find_elements_by_css_selector("tr")
    lang_list = [lang.text for lang in all_langs]
    lang_list = lang_list[1:]
    lang_dict = {lang.split(" ")[0]: lang.split(" ")[1] for lang in lang_list if lang.split(" ")[1] != '-'}
    second_dict = {lang.split(" ")[0]: lang.split(" ")[3] for lang in lang_list if (lang.split(" ")[1] == '-') and not lang.split(" ")[3].isnumeric()}
    final_dict = lang_dict | second_dict
    return final_dict[lang]


text_to_translate = input("What text do you want to translate? ")
target_language = input("What language do you want to translate the text to? ").capitalize()

payload = f"q={text_to_translate}&target={find_lang_code(target_language)}&source=en"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': RAPID_API_KEY
    }

response = requests.request("POST", URL, data=payload, headers=headers)
data = response.text
translation = data['data']['translations'][0]['translatedText']

print(translation)
