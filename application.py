from iotApp import create_app

app = create_app()
app.config.from_pyfile('../config.py')
app.run()

@app.route("/")
def hello():
    return "Hello World!"