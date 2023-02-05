from pytube import YouTube 
import os

videos_path = f"C:/Users/{os.getlogin()}/Videos"

def DownloadVideo(link:str, quality:int) -> int:
    
    try:
        video_data = YouTube(link)
    except:
        if len(link) == 0:
            return 401
        elif "youtube.com" not in link:
            return 402
        else:
            return 400

    try:
        mp4_videos = video_data.streams.filter(mime_type="video/mp4", progressive="True")
    except:
        return 500
    
    for video in mp4_videos:
        try:
            if int(video.resolution.replace("p", "")) >= quality:
                video.download(output_path=videos_path)
                return 200
        except:
            return 503

    return 502
            