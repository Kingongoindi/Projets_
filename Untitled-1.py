from moviepy import*
from moviepy.editor import VideoFileClip



def separeraudiodevideo (video_path,audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, codec = "pcm_s16le")

separeraudiodevideo("Dunbuggy_Clip.mp4","Dunbuggy2.wav")