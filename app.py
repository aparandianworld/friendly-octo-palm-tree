from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_population_data(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception (f"Error: Request failed with status code {response.status_code}")
        
        data = response.json()
        population_data = data[1]
        
        return population_data

    except Exception as e:
        print(str(e))
        return None

@app.route('/')
def home():
    WORLD_BANK_URL = "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json"
    population_data = fetch_population_data(WORLD_BANK_URL)
    
    return render_template('index.html', population_data=population_data)

if __name__ == '__main__':
    app.run(debug=True)