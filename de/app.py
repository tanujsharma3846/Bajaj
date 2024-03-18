from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your actual user ID (full_name_ddmmyyyy format)
user_id = "tanujsharma"
email = "tanujsharma3846@gmail.com"
roll_number = "2110993846"

@app.route('/bfhl', methods=['POST'])
def process_array():
  try:
    data = request.get_json()['data']

    if not data or not isinstance(data, list):
      return jsonify({'is_success': False, 'error': 'Invalid request: data must be an array'}), 400

    even_numbers = []
    odd_numbers = []
    alphabets = []

    for item in data:
      if isinstance(item, str):
        alphabets.append(item.upper())
      elif isinstance(item, int):
        if item % 2 == 0:
          even_numbers.append(item)
        else:
          odd_numbers.append(item)
      else:
        return jsonify({'is_success': False, 'error': 'Invalid data type in array'}), 400

    response = {
        'is_success': True,
        'user_id': user_id,
        'email': email,
        'roll_number': roll_number,
        'odd_numbers': odd_numbers,
        'even_numbers': even_numbers,
        'alphabets': alphabets,
    }

    return jsonify(response)
  except Exception as e:
    print(f"Error processing request: {e}")
    return jsonify({'is_success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
  app.run(debug=False)