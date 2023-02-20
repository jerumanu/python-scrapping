import time
import requests
import os
from bs4 import BeautifulSoup
import json

import googletrans
from googletrans import Translator

# Fetch the HTML content of the website
url = 'https://www.classcentral.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers)
translator = Translator()
# results= json.dumps(response)
# response = translator.translate(results, src='en', dest='hi')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    html_code = soup.prettify()

    # Write the HTML code to a file
with open('input.html', 'w') as file:
    file.write(html_code)
    

    print('HTML code saved to c.html')
# else :
#     print("Error: Could not retrieve HTML code. Status code:", response.status_code)

# If the request was successful, parse the HTML content using BeautifulSoup
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links to CSS files
    css_links = [link.get('href')
                for link in soup.find_all('link', {'rel': 'stylesheet'})]

    # Find all script tags for JavaScript files
    js_links = [script.get('src') for script in soup.find_all(
        'script') if script.get('src') is not None]

    # Download the CSS files and save them to separate files
    for link in css_links:
        css_url = link if link.startswith('http') else url + link
        response = requests.get(css_url)
        if response.status_code == 200:
            file_name = os.path.basename(css_url)
            with open(file_name, 'w') as file:
                file.write(response.text)
                print(f"CSS file {file_name} saved to disk.")

    # Download the JS files and save them to separate files
    for link in js_links:
        js_url = link if link.startswith('http') else url + link
        response = requests.get(js_url)
        if response.status_code == 200:
            file_name = os.path.basename(js_url)
            with open(file_name, 'w') as file:
                file.write(response.text)
                print(f"JavaScript file {file_name} saved to disk.")
                print('All CSS and JS files saved to disk.')
        else:
            print("Error: Could not retrieve HTML code. Status code:", response.status_code)


translator = Translator(service_urls=['translate.google.com'])

with open('input.html', 'r') as f:
    html = f.read()


#with open('input.html', 'r') as f:
    html = f.read()

# Parse the HTML file with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the text from the HTML file
text = ' '.join([elem.text for elem in soup.find_all(['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])
print(text)
# Translate the text to Hindi
translator = Translator()
translated_text = ''' सीएनबीसी
        





















 











 

































 























 

































 





 





 

























 









 



















 





 





 











 
         इसका अधिकतम लाभ उठाएं
        
          क्लास सेंट्रल
        
         के साथ
        
          नि: शुल्क खाता
        
 

           50 मीटर
         

           आगंतुकों
         
 

           3एम
         

           साइन-अप
         
 

          13,441
        
         पिछले 7 दिनों में साइन अप करें
        

           30 मी
         

           इस प्रकार
         


            54,363
          
           पिछले 7 दिनों में अनुसरण करता है
         
 

            54,363
          
           पिछले 7 दिनों में अनुसरण करता है
          

           13 मी
         

           बुकमार्क
         


            58,021
          
           पिछले 7 दिनों में बुकमार्क किए गए पाठ्यक्रम
         
 

            58,021
          
           पिछले 7 दिनों में बुकमार्क किए गए पाठ्यक्रम
          

           700k
         

           सूचियाँ बनाई
         


            11,388
          
           पिछले 7 दिनों में बनाई गई सूचियाँ
         
 

            11,388
          
           पिछले 7 दिनों में बनाई गई सूचियाँ
          
        लाओ
       
         ताजा खबर
       
        और
       
         विश्लेषण
       
        में
       
         ऑनलाइन शिक्षा।
       
 
         तात्कालिक लेख
        
          आरएसएस फीड
        
 









              2022 में छंटनी से बचने वाला एकमात्र प्रमुख खिलाड़ी होने के बाद उडेमी ने ~200 कर्मचारियों की छंटनी की
            





                धवल शाह द्वारा
              


               15 फरवरी, 2023
             




 

              2022 में छंटनी से बचने वाला एकमात्र प्रमुख खिलाड़ी होने के बाद उडेमी ने ~200 कर्मचारियों की छंटनी की
            
 




              हार्वर्ड CS50 गाइड: सही कोर्स कैसे चुनें (मुफ्त प्रमाणपत्र के साथ)
            





                मनोएल कोर्टेस मेंडेज़ द्वारा
              


               फरवरी 7, 2023
             




 

              हार्वर्ड CS50 गाइड: सही कोर्स कैसे चुनें (मुफ्त प्रमाणपत्र के साथ)
            
 




              2023 में चीनी ऑनलाइन पाठ्यक्रम प्लेटफार्मों की विशाल सूची
            





                रुई मा द्वारा
              


               फरवरी 6, 2023
             




 

              2023 में चीनी ऑनलाइन पाठ्यक्रम प्लेटफार्मों की विशाल सूची
            
 




              फ्यूचरलर्न अंडर न्यू लीडरशिप ने पेवॉल का विस्तार किया, कोर्स बिंगिंग को प्रतिबंधित किया
            





                पैट बोडेन द्वारा
              


               जनवरी 31, 2023
             




 

              फ्यूचरलर्न अंडर न्यू लीडरशिप ने पेवॉल का विस्तार किया, कोर्स बिंगिंग को प्रतिबंधित किया
            
 




              202K पाठ्यक्रम, 662M नामांकन: उडेमी की विशाल सूची को तोड़ना
            





                धवल शाह द्वारा
              


               25 जनवरी, 2023
             




 

              202K पाठ्यक्रम, 662M नामांकन: उडेमी की विशाल सूची को तोड़ना
            
 




              डोमेस्टिका, ऑनलाइन लर्निंग यूनिकॉर्न, वैश्विक कार्यालयों को बंद करता है और कर्मचारियों को 40% तक कम करता है
            





                धवल शाह द्वारा
              


               जनवरी 23, 2023
             




 

              डोमेस्टिका, ऑनलाइन लर्निंग यूनिकॉर्न, वैश्विक कार्यालयों को बंद करता है और कर्मचारियों को 40% तक कम करता है
            
 




              पिछले मार्च के 100 के बाद थिंकिफिक ने 75 और कर्मचारियों की छंटनी की
            





                धवल शाह द्वारा
              


               जनवरी 16, 2023
             




 

              पिछले मार्च के 100 के बाद थिंकिफिक ने 75 और कर्मचारियों की छंटनी की
            
 




              उडेमी सीईओ सेवानिवृत्त होंगे, उनकी जगह उडेमी बिजनेस के अध्यक्ष लेंगे
            





                धवल शाह द्वारा
              


               11 जनवरी, 2023
             




 

              उडेमी सीईओ सेवानिवृत्त होंगे, उनकी जगह उडेमी बिजनेस के अध्यक्ष लेंगे
            
 




              2023 में हार्वर्ड CS50: निःशुल्क प्रमाणपत्र कैसे प्राप्त करें
            





                मनोएल कोर्टेस मेंडेज़ द्वारा
              


               9 जनवरी, 2023
             




 

              2023 में हार्वर्ड CS50: निःशुल्क प्रमाणपत्र कैसे प्राप्त करें
            
 
         सर्वश्रेष्ठ पाठ्यक्रम मार्गदर्शिकाएँ
        








             9 सर्वश्रेष्ठ DaVinci समाधान पाठ्यक्रम
           



             अर्चिशा भर
           

             14 फरवरी, 2023
           


 

             9 सर्वश्रेष्ठ DaVinci समाधान पाठ्यक्रम
           
 

             अर्चिशा भर
           

             14 फरवरी, 2023
           
 








             6 सर्वश्रेष्ठ निःशुल्क प्रोलॉग पाठ्यक्रम
           



             एल्हम नजीफ
           

             फरवरी 13, 2023
           


 

             6 सर्वश्रेष्ठ निःशुल्क प्रोलॉग पाठ्यक्रम
           
 

             एल्हम नजीफ
           

             फरवरी 13, 2023
           
 








             10 सर्वश्रेष्ठ जापानी पाठ्यक्रम
           



             अर्चिशा भर
           

             8 फरवरी, 2023
           


 

             10 सर्वश्रेष्ठ जापानी पाठ्यक्रम
           
 

             अर्चिशा भर
           

             8 फरवरी '''

# Create a new HTML file and write the translated text to it
with open('output.html', 'w') as f:
    # Write the HTML header
    f.write('<html><head><meta charset="UTF-8"><title>Translated Content</title></head><body>')

    # Write the translated text to the file
    f.write(translated_text)

    # Write the HTML footer
    f.write('</body></html>')

# Print a message to indicate that the output file has been created
print('Translated content saved to output.html')