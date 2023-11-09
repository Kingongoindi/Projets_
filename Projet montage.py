from moviepy import*
from moviepy.editor import VideoFileClip
from tkinter import *
import pygame
import tkinter as tk
from tkVideoPlayer import TkinterVideo
import matplotlib.pyplot as plt
from scipy.io import wavfile
import imageio
import numpy as np

pygame.mixer.init

cheminvideo = "LEQUEL D'ENTRE NOUS EST....mp4"


regarder = imageio.get_reader(cheminvideo)

def separeraudiodevideo (video_path,audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, codec = "pcm_s16le")

video = separeraudiodevideo("LEQUEL D'ENTRE NOUS EST....mp4","LEQUEL D'ENTRE NOUS EST.wav")
son = "LEQUEL D'ENTRE NOUS EST.wav"

def lanceraudio():
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer_music.load (son)
    pygame.mixer.music.play(loops= 0)

def couperaudio():
    pygame.mixer.music.stop()
def quitterfenetre():
    pygame.quit()
    fen.destroy()

taux_echantillonnage, donnees = wavfile.read("LEQUEL D'ENTRE NOUS EST.wav")





fen = Tk()
fen.title("Arrêter/Ecouter l'audio de la video.")

fen.geometry("800x450+290+10")
boutonbruit= Button (fen, text = "Ecouter l'audio",font = 'Times',command = lanceraudio) 
boutonbruit.pack(pady=20)

boutonsilence= Button (fen, text ="Arrêter l'audio",font = 'Times',command = couperaudio)
boutonsilence.pack(pady=30)

fen.mainloop()

fenetre = tk.Tk()
fenetre.title("Video sans le son.")
fenetre.geometry("800x450+290+10")


videoplayer = TkinterVideo(master=fenetre, scaled=True)
videoplayer.load(cheminvideo)
videoplayer.pack(expand=True, fill="both")

videoplayer.play() 


fenetre.mainloop()