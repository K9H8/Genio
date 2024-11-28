import google.generativeai as genai
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from flask import Flask, request, render_template, send_from_directory
from datetime import datetime
import json

# Initialize your OpenAI API key
api_key1="Enter-API-Key"
genai.configure(api_key = api_key1)

def ask_Gemini(question): 
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        return response.text
    
    except Exception as e:
        return f"An error occurred"
    

def image_url(word):
    modified_string = word.replace(" ", "+")
    url = "https://www.google.com/search?tbm=isch&q=" + modified_string
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(url, headers=headers)

    page = urlopen(req)

    bs = BeautifulSoup(page, 'html.parser')
    images = bs.find_all('img', {'src':re.compile('.*gstatic.com.*')})
    image_urls = []    
    for img in images:
        image_urls.append(img['src'])
        if len(image_urls) == 4:
            return (image_urls)

def vurl(topic):
    try:
        # Send a GET request to the URL
        response = requests.get(f"https://www.youtube.com/results?search_query={topic}")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            start_index = response.text.index('watch?v=')+len('watch?v=')
            new_str = response.text[start_index::]
            end_index = new_str.index('\\')
            new_str = new_str[:end_index]            
            return new_str  # Return the HTML content as a string
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    
def wrjson(topic):
        # Step 1: Read existing data
    with open("history.json", 'r') as file:
        try:
            existing_data = json.load(file)  # Load existing search history
        except json.JSONDecodeError:
            existing_data = []  # Start with an empty list if the file is malformed
 
    # Step 2: Append the new entry
    now = datetime.now()
    current_date = now.date().isoformat()
    current_time = now.time().strftime("%H:%M:%S")
    
    existing_data.append([topic,current_date,current_time])  # Add the new entry to the list

    # Step 3: Write the updated list back to the JSON file
    with open("history.json", 'w') as file:
        json.dump(existing_data, file, indent=4)  # Save with pretty formatting
    
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/history.json')
def send_json():
    return send_from_directory('','history.json')

@app.route('/submit', methods=['POST'])
def submit():
    country = request.form['country']
    wrjson(country)            
    answer = ask_Gemini(f"""im going to give you subject, give an introduction as a paragraph.
                        the subject is {country}""")
    url = image_url(country)
    video_url = "https://www.youtube.com/embed/" + vurl(country)
    print(video_url)
       
    return render_template('result.html', 
                               country_name=country.capitalize(), 
                               country_description=answer,
                               country_image= url,
                               country_video = video_url)




if __name__ == "__main__":
    app.run(debug=True)
    
    question = input("What would you like to ask Gemini? ")
    answer = ask_Gemini(f"""im going to give you a topic name, return a paragraph about it.
                        the topic is: f{question}. """)
    
    url = image_url((question))
    
    print(answer, url) 


    
    
   
    
    
