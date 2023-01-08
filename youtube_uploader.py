from youtube_upload.client import YoutubeUploader

client_id = "851810660056-m7jqu1mfe5nl160gqnnq7ji0cf7trmbe.apps.googleusercontent.com"
client_secret = "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"



# Video options
options = {
    "title" : "Funny meme that make me laugh", # The video title
    "description" : "guess what? you liked the video #shorts #youtubeshorts #trending #viral #ytshorts #memes #dankmemes", # The video description
    "tags" : ["#shorts", "#ytshorts", "#viral","#memes","#dankmemes","#trending"],
    "categoryId" : "22",
    "privacyStatus" : "public", # Video privacy. Can either be "public", "private", or "unlisted"
    "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
}

# upload video
def upload_video(video):
    uploader = YoutubeUploader(client_id,client_secret)
    uploader.authenticate(oauth_path='oauth.json')
    uploader.upload(video, options) 
    print("successfully uploaded meme to youtube! ❤️")
    
    uploader.close()