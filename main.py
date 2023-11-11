from flask import Flask, render_template, request
from pytube import YouTube


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        youtube = YouTube(url)
        
        # Get the highest resolution video stream with audio
        video = youtube.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
        
        # Download the video with audio
        video.download('./downloads')

        return """
            <script>
                alert('Video downloaded!');
                window.location.href='/';
            </script>
        """
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
