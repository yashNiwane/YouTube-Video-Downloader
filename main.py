import re
from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    video_title = None



    if request.method == 'POST':
        url = request.form['url']
        youtube = YouTube(url)
        

        # Get the highest resolution video stream with audio
        video = youtube.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
        

        # Download the video with audio
        video_title = youtube.title
        download_path = os.path.join('static', 'downloads')
        video.download(download_path)
        


    return render_template('index.html', video_title=video_title)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
