from flask import Flask, render_template, Response
import sys
import os
import base64
from Vision.Image import *
from Vision.ImagePreProcess import *
from Vision.camDisplay import *
from Vision.geo import *
from Vision.Async import *
import multiprocessing

app = Flask(__name__)
# print("h")
# op2 = Display(1)
# print('j')
# op3 = Operation(2)

def as_text(image):
    image = cv2.imencode('.jpg', image)[1]
    return image.tobytes()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    camera.start()
    while True:
        ret, frame = camera.read()
        if frame is not None:
            #print(frame)
            frame = as_text(frame)
            #print("here")
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen_front(camera):
    while True:
        n,t,sq,l,c,frame = camera.get()
        #print(frame)
        frame = as_text(frame)
        #print("here")
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'+n.encode())

@app.route('/video_feed')
def video_feed():
    return Response(gen(Async(0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
 
@app.route('/video_feed2')
def video_feed2():
    #global p 
    #p = Process(target=gen_front, args=(1))
    #p.start()
    return Response(gen_front(Display(1)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3')
def video_feed3():
    return Response(gen(Async(2)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)