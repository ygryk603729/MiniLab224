from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Вставь свой API-ключ NASA
NASA_API_KEY = 'kSutIKTTaXjjr40V4TIQss2X0LmxAOCNhUvOMKwu'

@app.route('/')
def home():
    return "NASA API Backend Application is running!"

# Новый эндпоинт для APOD
@app.route('/apod', methods=['GET'])
def get_apod():
    # Получаем параметр 'date' из запроса (если передан)
    date = request.args.get('date')

    # Формируем URL для NASA API
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': NASA_API_KEY,
        'date': date
    }

    # Запрос к NASA API
    response = requests.get(url, params=params)
    
    # Обработка ответа
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from NASA'}), response.status_code

#эндпоинт для фото с марсохода
@app.route('/mars-photos', methods=['GET'])
def get_mars_photos():
    # Получаем параметры из запроса: sol (солнечный день) и rover (название марсохода)
    sol = request.args.get('sol', default=1000)  # По умолчанию 1000
    rover = request.args.get('rover', default='curiosity')  # По умолчанию Curiosity

    # Формируем URL для NASA API
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
    params = {
        'sol': sol,
        'api_key': NASA_API_KEY
    }

    # Запрос к NASA API
    response = requests.get(url, params=params)

    # Обработка ответа
    if response.status_code == 200:
        photos = response.json().get('photos', [])
        if not photos:
            return jsonify({'message': 'No photos available for the given parameters.'})
        return jsonify(photos)
    else:
        return jsonify({'error': 'Failed to fetch data from NASA'}), response.status_code
    
@app.route('/neo', methods=['GET'])
def get_neo():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({'error': 'Both start_date and end_date are required'}), 400

    # Формируем URL для NASA API
    url = 'https://api.nasa.gov/neo/rest/v1/feed'
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': NASA_API_KEY
    }

    # Запрос к NASA API
    response = requests.get(url, params=params)

    # Обработка ответа
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from NASA'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
