#!/home/fy/.virtualenvs/spider_py2/bin/python2.7
# coding=utf-8
import pymongo
import sys
import time
import init_Client

reload(sys)
sys.setdefaultencoding('utf-8')
appkey = "3284008752"
appsecret = "3574a5440ed9dba27c74fa235d23f6a8"
callback = "http://api.weibo.com/oauth2/default.html"
access_token = "2.00LCUPJDGh3PaDfc987d51280DBZzI"


m_client = pymongo.MongoClient('localhost', 27017)
m_client.sinaAPI.authenticate('root', 'root', mechanism='MONGODB-CR')
sinaAPI = m_client['sinaAPI']
item_info = sinaAPI['item_info']

# 新浪微博某条微博的评论抓取，总共抓取到了40页，每页大概50条，远远不够！总共120000的评论，
# 只抓取到了不到2000条，API的限制太严重！准备解析网页！


def get_data():
    client = init_Client.get_client(appkey, appsecret, callback, access_token)
    for j in range(1, 2001):
        # time.sleep(1)
        comments = client.comments.show.get(
            id='4192103401927498', page=j)['comments']
        comments_size = len(comments)
        print comments_size, j
        for i in range(0, comments_size):
            data = {
                "created_at": comments[i]['created_at'],
                "id": comments[i]['id'],
                "rootid": comments[i]['rootid'],
                "floor_number": comments[i]['floor_number'],
                "text": comments[i]['text'],
                "user_id": comments[i]['user']['id'],
                "user_name": comments[i]['user']['name'],
                "user_location": comments[i]['user']['location'],
                "user_description": comments[i]['user']['description'],
                "user_followers_count": comments[i]['user']['followers_count'],
                "user_friends_count": comments[i]['user']['friends_count'],
                "user_statuses_count": comments[i]['user']['statuses_count'],
                "user_favourites_count": comments[i]['user']['favourites_count'],
                "user_created_at": comments[i]['user']['created_at'],
            }
            item_info.insert_one(data)


if __name__ == '__main__':
    get_data()
