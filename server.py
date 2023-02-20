import requests
import os
from bs4 import BeautifulSoup
import json
import googletrans
from googletrans import Translator

# Fetch the HTML content of the website
url = 'https://www.classcentral.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Save the HTML content to a file
    soup = BeautifulSoup(response.content, 'html.parser')
    html_code = soup.prettify()
    with open('classcentral.html', 'w') as file:
        file.write(html_code)
    print('HTML code saved to classcentral.html')

    # Translate the HTML content to Hindi
    translator = Translator()
    translated_text = translator.translate(response.text, dest='hi').text

    
    output_html = soup.prettify().replace(response.text, translated_text)
    with open('output.html', 'w') as f:
        f.write(output_html)
   