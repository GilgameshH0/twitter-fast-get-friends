from itertools import count
from turtle import Screen

import tweepy

#Твиттер бирер токен (берем из браузера)
auth = tweepy.OAuth2BearerHandler("")
api = tweepy.API(auth)

# В screen_name указываем юзернейм нужного пользователя
for page in tweepy.Cursor(api.get_friends, screen_name="cozypront").pages():
    for user in page:
        print(user.screen_name)

#Для подписчиков:
# friends_list= api.get_followers(screen_name ="CommCatHealth",count=200)