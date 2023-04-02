from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('family_tree.html')

@app.route('/', methods=['POST'])
def submit():
    name = request.form.get('name')
    relationship = request.form.get('relationship')
    image = request.files.get('image')
    image.save(f'static/images/{name}.jpg')
    return render_template('family_tree.html', name=name, relationship=relationship)

if __name__ == '__main__':
    app.run(debug=True)
