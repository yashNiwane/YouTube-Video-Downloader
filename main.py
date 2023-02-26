from flask import Flask, render_template, request
from pytube import YouTube


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
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

