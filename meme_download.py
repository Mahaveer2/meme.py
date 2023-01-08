import praw
import ssl
from urllib.request import urlopen
from PIL import Image


# Create a Reddit instance
def download_memes(subreddit,limit):
  client_id = 'uTWVRq5sF4wGN47faIXIHw'
  client_secret = '9jBBK1n5D8hIaB_eEq1Dons2Z4PWqA'
  reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='my_user_agent')
  
  # Get the top memes from the r/memes subreddit
  subreddit = reddit.subreddit(subreddit)
  top_memes = subreddit.hot(limit=limit)
  
  # Download each meme and save it to a file
  index= 0
  for meme in top_memes:
    if str(meme.url).endswith(".jpg") or str(meme.url).endswith(".jpeg") or str(meme.url).endswith(".png") or str(meme.url).endswith(".gif"):
      img1 = Image.open(urlopen(meme.url,context=ssl._create_unverified_context()))
      newsize =(800,1200)
      img = img1.resize(newsize)
      if img.mode != 'RGB':
        img = img.convert('RGB')
      print(f"Downloading {meme.url}")
      img.save("memes/"+meme.title + '.jpg')
      index +=1
    else:
      limit -= 1
    if index == (limit):
      return True
    