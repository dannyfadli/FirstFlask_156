from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    if name.lower() == "veliona":
        return jsonify({
            "message": f"Hello, {name}!",
            "image": "https://example.com/veliona-image.jpg"  # Ganti URL gambar dengan link gambar Veliona
        })
    else:
        return jsonify({
            "message": f"Hello, {name}!",
            "image": None
        })

if __name__ == '__main__':
    app.run(debug=True)
