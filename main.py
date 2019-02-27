from pprint import pprint
import dataset
from tqdm import tqdm
from a32hike import getactivitycomment


DB = dataset.connect('sqlite:///32hike.db')
COMMENT_TABLE =  DB['comment']


def main():
    for atid in tqdm(range(1,1000)):
        try:
            page = 1
            while True:
                result = getactivitycomment(atid, page)
                if result['status'] != 1 or len(result['comment']['coments']) <=0:
                    break
                for comment in result['comment']['coments']:
                    item = {'atid': atid}
                    hiker = comment.pop('hiker')
                    activity = comment.pop('activity')
                    comment.pop('stars')
                    item.update(hiker)
                    item.update(activity)
                    item.update(comment)
                    print(item)
                    COMMENT_TABLE.upsert(item, ['hikerId', 'activityId'])
                page += 1
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
