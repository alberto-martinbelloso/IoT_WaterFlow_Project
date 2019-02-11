from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    return 'Ca dasa la javanta, que dese le jevente, qui disi li jivinti, co doso lo jovonto UUUUUU UUUUUUUU'


if __name__ == '__main__':
    app.run()
