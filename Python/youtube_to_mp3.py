from pytube import YouTube
import  pytube
import os
import tkinter as tk

def convert_video(link):
    try:
        if (link != ""):
            yt = YouTube(link)

            video = yt.streams.filter(only_audio=True).first()

            print("Enter the audio destination")

            destination = str(input('>>')) or '.'

            out_file  = video.download(output_path=destination)

            base, ext = os.path.splitext(out_file)

            new_file = base+'.mp3'

            os.rename(out_file,new_file)

            success = (yt.title + "has been downloaded")
            return success
        else:
            print("Error")
    except pytube.exceptions.RegexMatchError as e:
        print(e)

r = tk.Tk()

r.geometry("700x350")
r.title("YouTube to Mp3 Converter")
tk.Label(r, text='YouTube Link').grid(row=1)


Youtube_link = tk.Entry(r)

video_link = str(Youtube_link)

Youtube_link.grid(row=1, column=1)

Convert_btn = tk.Button(r,text='Covert', width=25,command=convert_video(video_link)).grid(row=3)



r.mainloop()


