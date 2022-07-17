
from video.yt_concate.steps.get_video_list import GetVideoList
from video.yt_concate.steps.step import StepException


CHANNEL_ID = 'UC1Oq-B1TgUzMTz0zSb8ZDrA'
steps = [
    GetVideoList(),
]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happened: ', e)
        break
    
    

#video_list = get_all_video_in_channel(CHANNEL_ID)
#print(len(video_list))

