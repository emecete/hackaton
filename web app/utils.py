import datetime
import json
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:32769/")
mydb = myclient["ocupa2"]


def get_credentials():
    """
    Read the file 'user_credentials.json' in which there is information about the developer user (api key and email)
    :return: dictionary with 'user_credentials.json' content
    """
    with open('user_credentials.json') as f:
        return json.load(f)


def get_meta_hashtags():
    """

    :return:
    """
    with open('hashtag.json') as f:
        return (meta.replace('hashtags_', '') for meta in json.load(f))


def get_hashtags_from_meta(meta):
    with open('hashtag.json') as f:
        hashtags = json.load(f)
        return hashtags['hashtags_' + meta]


def add_usage():
    mycol = mydb["usage"]
    now = datetime.datetime.now()
    mycol.insert_one({'date': now.strftime("%d-%m-%Y")})
