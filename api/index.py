from flask import Flask , request
import requests , json , random
import sys
sys.path.append('python_modules')
import yt_dlp
app = Flask(__name__)
def select(a):
    dict ={'Anime':'a','Comic':'b','Game':'c','Literature':'d','Original':'e','Internet':'f','Other':'g','Video':'h','Poem':'i','NCM':'j','Philosophy':'k','Funny':'l'}
    if str(a) in dict.keys() :
        return dict[str(a)]
    else :
        return dict[str(random.choice(list(dict.keys())))]

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/search/',methods=["GET"])
def search():
    url = get_audio_url()

    print("is in search function  url :"+url)
    return url


def get_audio_url():
    video_url = 'https://www.youtube.com/watch?v=_ZcmuKsyvzg&key=AIzaSyBeLbXYguI1KK7xZtc03SBSz9zuj5'  # 替换为实际的视频链接
    ydl_opts = {
        'format': 'bestaudio/best',  # 获取最佳音频格式
        'noplaylist': True,  # 如果链接是一个播放列表，仅下载第一个视频
        'quiet': True,  # 禁止额外输出
        'extract_flat': True,  # 提取信息而不下载
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        audio_url = info_dict['url']
        print("Audio URL:", audio_url)
        return audio_url



@app.route('/',methods=["GET"])
def return_OneText():
    url = get_audio_url()
    print("is in return_OneText:" + url)
    return url