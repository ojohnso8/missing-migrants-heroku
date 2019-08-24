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

@app.route('/predictiveanalysis.html')
def render_predictiveanalysis():
    return render_template('predictiveanalysis.html')

@app.route('/temperature.html')
def render_temperature():
    return render_template('temperature.html')

@app.route('/totaldead.html')
def render_totaldead():
    return render_template('totaldead.html')

@app.route('/sourcequalitylinear.html')
def render_sourcequalitylinear():
    return render_template('sourcequalitylinear.html')

@app.route('/sourcequalitylogistic.html')
def render_sourcequalitylogistic():
    return render_template('sourcequalitylogistic.html')

@app.route('/data.html')
def render_data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run()