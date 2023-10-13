import os
from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    resolution = request.form['resolution']

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(res=resolution).first()
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        stream.download(output_path=download_path)
        return "Download completed!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
