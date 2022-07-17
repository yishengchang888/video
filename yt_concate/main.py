from pipeline.pipeline import Pipeline
from pipeline.steps.get_video_list import GetVideoList

CHANNEL_ID = 'UC1Oq-B1TgUzMTz0zSb8ZDrA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    print(p.run(inputs))


if __name__ == '__main__':
    main()

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
