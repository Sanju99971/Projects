#Program to download YOUTUBE videos
from pytube import YouTube
link=input("Please Enter your Link..\n")
store=YouTube(link)
print(store.title)
print(store.thumbnail_url)
videos=store.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
choice=int(input("Please Enter your Choice.."))
        
videos[choice].download()
print("Your Video Downloaded Successfully.")


#To solve download error problem just install upgrade the pytube by pip install --upgradepytube. 
