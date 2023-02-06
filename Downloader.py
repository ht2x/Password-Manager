from pytube import YouTube #import the YouTube object from the pytube library
import os #import the system library

videos_path = f"C:/Users/{os.getlogin()}/Videos" #decide the video download path

class StreamsMetaData: # create a metadata object
    code = None # error/success code
    videos = None # list of streams, streams being the same video in different resolutions 
    quality = 360 # desired resolution

    def __init__(self, code, videos = None, quality = None): # initialization function, taking same arguments as above variables
        self.code = code        #assignment
        self.videos = videos    #//
        self.quality = quality  #//

def InitailizeDownload(link:str, quality:int) -> StreamsMetaData: # a function to start the download process, returns an object of type StreamsMetaData
    try: #error handling
        video_data = YouTube(link) #get the video data using the link
    except: # in case of an error
        if len(link) == 0: #if the field is empty
            return StreamsMetaData(401) # return only code, which is an erro
        elif "youtube.com" not in link: #if the link isn't from youtube
            return StreamsMetaData(402) #//
        else:
            return StreamsMetaData(400) #//

    try: #error handling
        mp4_videos = video_data.streams.filter(mime_type="video/mp4", progressive="True") #filter unwanted data and assign the list of videos(streams) to 'mp4_videos'
        return StreamsMetaData(200, mp4_videos, quality) #return code 200 which indicate success and return other necessary data
    except: # in case of an error
        return StreamsMetaData(502) # return only code, which is an erro

    return StreamsMetaData(500) # return only code, which is an erro
            
def DownloadInProgress(mp4_videos, quality): # the process of downloading the video itself
    for video in mp4_videos: #loop over each stream to compare the quality 
        try: #error handling
            if int(video.resolution.replace("p", "")) >= quality: #compare the quality of the stream to the desired quality
                video.download(output_path=videos_path) #if found, download the video
                return 200 #return a success code
        except: # in case of an error (usually network error)
            return 503 #return a failure code

    mp4_videos.first().download(output_path=videos_path) #if the desired quality wasn't found, download the first stream (usually worse quality)
    return 200 #return a success code