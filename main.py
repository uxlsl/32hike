from collections import defaultdict
import click
import dataset
from tqdm import tqdm
from a32hike import getactivitycomment

from recommendations import sim_distance, topMatches, getRecommendations,getRecommendedItems,transformPrefs,calculateSimilarItems


DB = dataset.connect('sqlite:///32hike.db')
COMMENT_TABLE =  DB['comment']


@click.group()
def cli():
    pass

@cli.command()
def download():
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


@cli.command()
def recommend():
    print('初始化')
    users = {}
    comments = defaultdict(dict)
    for item in COMMENT_TABLE.all():
        if item['hikerId'] is None:
            continue
        comments[item['hikerId']][item['atid']] = float(item['score'])
        users[item['hikerId']] = item['nickname']
    comments_t = transformPrefs(comments)
    itemMatch = calculateSimilarItems(comments_t)
    print('初始化完成')
    while True:
        try:
            user_m = {}
            name = input('user:')
            for num, user in enumerate(DB.query("select distinct(nickname),hikerId from comment where nickname like '%{}%'".format(name))):
                user_m[num] = user['hikerId']
                print(num,user['hikerId'], user['nickname'])
            num = int(input('num:'))
            if num in user_m:
                for score, hikerId in topMatches(comments, user_m[num], 10, sim_distance):
                    print(score, hikerId, users[hikerId])
                print(getRecommendedItems(comments, itemMatch,user_m[num]))
        except Exception as e:
            print('出现异常错误,重来')

if __name__ == '__main__':
    cli()
