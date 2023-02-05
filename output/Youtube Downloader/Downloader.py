from pytube import YouTube 
import os

videos_path = f"C:/Users/{os.getlogin()}/Videos"

class StreamsMetaData:
    code = None
    videos = None
    quality = 360

    def __init__(self, code, videos = None, quality = None):
        self.code = code
        self.videos = videos
        self.quality = quality    

def InitailizeDownload(link:str, quality:int) -> StreamsMetaData:
    try:
        video_data = YouTube(link)
    except:
        if len(link) == 0:
            return StreamsMetaData(401)
        elif "youtube.com" not in link:
            return StreamsMetaData(402)
        else:
            return StreamsMetaData(400)

    try:
        mp4_videos = video_data.streams.filter(mime_type="video/mp4", progressive="True")
        return StreamsMetaData(200, mp4_videos, quality)
    except:
        return StreamsMetaData(502)

    return StreamsMetaData(500)
            
def DownloadInProgress(mp4_videos, quality):
    for video in mp4_videos:
        try:
            if int(video.resolution.replace("p", "")) >= quality:
                video.download(output_path=videos_path)
                return 200
        except:
            return 503