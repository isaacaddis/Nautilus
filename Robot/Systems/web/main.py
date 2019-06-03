from flask import Flask, render_template, Response
import sys
import os
import base64

sys.path.insert(0,'/home/robotics45c/Desktop/rov2019/Robot/Systems/Vision')
from Image import *
from ImagePreProcess import *
from camDisplay import *
from geo import *


app = Flask(__name__)
#os.system("fuser -k /dev/video0")
op = Operation(0)
# print("h")
# op2 = Display(1)
# print('j')
# op3 = Operation(2)

def as_text(image):
	return base64.b64encode(cv2.imencode('.jpg', image))

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        ret, frame = op.get()
        print(frame)
        frame = as_text(frame)
        print("here")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)