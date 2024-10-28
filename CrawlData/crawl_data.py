
import requests
import json
import os
import sys
sys.path.append('python_modules')
import yt_dlp

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

def get_audio_url(video_url):
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




if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=_ZcmuKsyvzg'  # 替换为实际的视频链接
    get_audio_url(video_url)