from pytube import YouTube

url=input('Enter the url you want to download the video of')

my_video = YouTube(url)

#Title Of The YouTube Video

print(my_video.title)

#Thumbnail Image Of The Video

print(my_video.thumbnail_url)
my_video = my_video.streams.get_highest_resolution()

#my_video = my_video.streams.first()

#for stream in my_video.stream:
 #print(stream)

my_video.download()
