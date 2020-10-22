from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def Toggle_Box():
    return render_template('ToggleBox.html' , title = 'ToggleBox')
    
if __name__ ==  '__main__':
    app.run(debug = True)



