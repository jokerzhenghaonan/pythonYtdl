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
video_id = '_ZcmuKsyvzg'
API_KEY = 'AIzaSyBeLbXYguI1KK7xZtc03SBSz9zuj5-FiIA'


def get_audio_url1():
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

def get_video_info(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={API_KEY}&part=status,snippet'
    response = requests.get(url)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        return data['items'][0]  # 返回视频信息
    else:
        print("Error: Video not found or inaccessible.")
        return None

def get_audio_url(video_url):
    video_id = video_url.split("v=")[-1]  # 提取视频ID
    video_info = get_video_info(video_id)

    if video_info and video_info['status']['privacyStatus'] == 'public':
        ydl_opts = {
            'format': 'bestaudio/best',  # 获取最佳音频格式
            'noplaylist': True,  # 如果链接是一个播放列表，仅下载第一个视频
            'quiet': True,  # 禁止额外输出
            'extract_flat': True,  # 提取信息而不下载
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                audio_url = info_dict['url']
                print("Audio URL:", audio_url)
                return audio_url
        except Exception as e:
            print(f"Error occurred while extracting audio URL: {e}")
            return None
    else:
        print("Error: Video is private or cannot be accessed.")
        return None


@app.route('/',methods=["GET"])
def return_OneText():
    video_url = "https://www.youtube.com/watch?v=_ZcmuKsyvzg"
    audio_url = get_audio_url(video_url)
    if audio_url:
        print("Successfully retrieved audio URL.")
    else:
        print("Failed to retrieve audio URL.")