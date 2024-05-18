from flask import Flask, render_template, Response, request
import test1
app = Flask(__name__)

def index():
    """Render the main HTML template"""
    return render_template('photo.html') 


@app.route('/photo/<item>')
def video_feed(item):
    return Response(test1.gen(item),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/photo/all')
def videofeed():
    return Response(test1.genall(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  