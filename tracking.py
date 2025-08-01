from flask import Flask, request

app = Flask(__name__)

@app.route('/location')
def handle_location():
    lat = request.args.get('lat')  
    lon = request.args.get('lon')
    print(f"Координаты: {lat}, {lon}")
    return "Данные получены!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)