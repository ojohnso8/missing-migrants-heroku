from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_static():
    return render_template('index.html')

@app.route('/index.html')
def render_index():
    return render_template('index.html')

@app.route('/incidentmap.html')
def render_incidentmap():
    return render_template('incidentmap.html')

@app.route('/markermap.html')
def render_markermap():
    return render_template('markermap.html')

@app.route('/plots.html')
def render_plots():
    return render_template('plots.html')

@app.route('/data.html')
def render_data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run()