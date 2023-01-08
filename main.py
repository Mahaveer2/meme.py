import click
from colorama import Fore, Back, Style
from name import print_name
from img_to_vid import make_video
from meme_download import download_memes
from youtube_uploader import upload_video

def main():
  print_name()
  subbredit = input("Please enter the name of subreddit: ")
  limit = int(input("Please enter the number of memes you want in your video: "))
  memes = download_memes(subbredit,limit)
  if memes:
    video = make_video("./memes/","music.mp3","./meme_compilation")
    if video:
      print("uploading to youtube...")
      upload_video("meme_compilation.mp4")


if __name__ == "__main__":
  main()