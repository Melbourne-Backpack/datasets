from urllib import request

from flask import render_template, Flask, send_file
from geopy.geocoder import Nominatim
import pandas
import date_time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', method=['POST'])
def success():
    global filename
    if request.method == 'POST':
        file = request.files['file']
        try:
            df = pandas.read_csv(file)
            gc = Nominatim()
            df['longitude'] = df['address'].apply(lambda x: gc.geocode(x).longitude if gc.geocode(x) else None)
            df['latitude'] = df['address'].apply(lambda x: gc.geocode(x).latitude if gc.geocode(x) else None)

            filename = date_time.now().strftime("%Y-%m-%d-%H-%M-%S") + '.csv'
            df.to_csv(filename, index=False)
            return render_template('index.html', text=df.to_html(), btn='download.html')
        except:
            return render_template('index.html', text='Did you upload a CSV file with "address" column?')


@app.route('/download-file/')
def download():
    return send_file(filename, attachment_filename='filename.csv', as_attachment=True)
