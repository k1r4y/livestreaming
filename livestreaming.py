################################
# Original code by: ProxyES77  #
# Address: 127.0.0.1:5015/live #
################################

import os
import time
import threading
from flask import Flask, Response
from PIL import ImageGrab
import io

app = Flask(__name__)

def generate_frames():
    while True:
        img = ImageGrab.grab()
        img_io = io.BytesIO()
        img.save(img_io, format='JPEG')
        img_io.seek(0)
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + img_io.read() + b"\r\n")
        time.sleep(0.1)

@app.route('/live')
def live():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015, threaded=True)


