from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Path to your Excel file
EXCEL_FILE_PATH = 'numbers.xlsx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    number = data.get('number')
    if number is not None and search_in_excel(number):
        return jsonify({'message': 'Pass'})
    else:
        return jsonify({'message': '404 Not Found'})

def search_in_excel(number):
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, header=None)
        return number in df[0].astype(str).values
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True, port=5002)

#EXCEL_FILE_PATH = r'https://docs.google.com/spreadsheets/d/1Nwu1AUsjklIQ59MX6f0IvSupNC94I7hWAyMYOl4zdkI/edit?usp=sharing'
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     data = request.get_json()
#     number = data.get('number')
#     if number is not None and search_in_excel(number):
#         return jsonify({'message': 'Number found'})
#     else:
#         return jsonify({'message': 'Number not found'})

# def search_in_excel(number):
#     try:
#         # Try reading with 'openpyxl' engine first (for .xlsx files)
#         df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl', header=None)
#         if number in df[0].astype(str).values:
#             return True

#         # If not found, try reading with 'xlrd' engine (for .xls files)
#         df = pd.read_excel(EXCEL_FILE_PATH, engine='xlrd', header=None)
#         return number in df[0].astype(str).values

#     except Exception as e:
#         print(f"Error reading Excel file: {e}")
#         return False

# if __name__ == '__main__':
#     app.run(debug=True, port=5002)


























