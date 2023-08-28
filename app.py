from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = nationality = probability = None

    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            nationalities = get_nationality(name)
            if nationalities:
                # Check if the 'country' field is present in the response
                if 'country' in nationalities:
                    # Assuming that the API returns nationality with the highest probability
                    top_nationality = max(nationalities['country'], key=lambda x: x['probability'])
                    nationality = top_nationality['country_id']
                    probability = top_nationality['probability']

    return render_template('index.html', name=name, nationality=nationality, probability=probability)

def get_nationality(name):
    url = f"https://api.nationalize.io/?name={name}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
