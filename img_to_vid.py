import os
from moviepy.editor import *

def make_video(folder,music_path,output):
  clips = []

  for image in os.listdir(f"./{folder}/"):
    if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg") or image.endswith(".gif"):
      path = os.path.join(f"./{folder}", image)
      clip = ImageClip(path).set_duration(3).resize(0.5)
      clips.append(clip)
  
  video_clip = concatenate_videoclips(clips,method='compose').fx(vfx.resize,width=1920,height=1080)
  duration = video_clip.duration
  audioclip = AudioFileClip(music_path).subclip(0, duration) 
  new_audioclip = CompositeAudioClip([audioclip])
  video_clip.audio = new_audioclip
  video_clip.write_videofile(f"{output}.mp4",fps=23,remove_temp=True,audio_codec='aac')
 
  dir = './memes/'
  for image in os.listdir(dir):
    if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg"):
      print(f"deleting {image}")
      os.remove(os.path.join(dir, image))
  
  return True
  print(f"video exported to {output}")