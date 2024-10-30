
import requests
import json
import os
import sys
sys.path.append('python_modules')
import yt_dlp
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    print(111)

def download_video(url):
    # 配置下载参数
    ydl_opts = {
        'format': 'lowest',  # 下载最高质量的视频
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # 保存路径和文件名模板
    }
    # 使用 yt-dlp 进行下载
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def list_formats(url):
    ydl_opts = {
        'listformats': True,  # 列出视频所有可用格式
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=False)

API_KEY = 'AIzaSyBeLbXYguI1KK7xZtc03SBSz9zuj5-FiIA'

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
    logging.info("url:",url)

    if 'items' in data and len(data['items']) > 0:
        return data['items'][0]  # 返回视频信息
    else:
        logging.info("Error: Video not found or inaccessible.")

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
                logging.info("Audio URL:", audio_url)

                print("Audio URL:", audio_url)
                return audio_url
        except Exception as e:
            logging.info(f"Error occurred while extracting audio URL: {e}")

            print(f"Error occurred while extracting audio URL: {e}")
            return None
    else:
        print("Error: Video is private or cannot be accessed.")
        return None




if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=_ZcmuKsyvzg"
    audio_url = get_audio_url(video_url)
    logging.info("121132312312312")
    if audio_url:
        logging.info("Successfully retrieved audio URL.")

        print("Successfully retrieved audio URL.")
    else:
        logging.info("Failed to retrieve audio URL.")

        print("Failed to retrieve audio URL.")