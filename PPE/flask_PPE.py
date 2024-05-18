from flask import Flask, render_template, Response, request
import PPE_rec
app = Flask(__name__)


def index():
    """Render the main HTML template"""
    return render_template('index.html')  


@app.route('/video_feed/<item>')
def video_feed(item):
    return Response(PPE_rec.gen(item),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed/all')
def videofeed():
    return Response(PPE_rec.genall(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)  
