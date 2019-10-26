from flask import Flask, Response, session, render_template, request, redirect, g, url_for
import camera
import os


# start Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# init camera
camera_obj = camera.Camera(fps=5)
camera_obj.run()

################### Funcutions ###################
def img_gen():
    while True:
        frame_bytes = camera_obj.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/stream")
def stream_page():
    return render_template("stream.html")


@app.route("/video_feed")
def video_feed():
    return Response(img_gen(),
        mimetype="multipart/x-mixed-replace; boundary=frame")


###################### loop ######################
if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0', debug=False)
