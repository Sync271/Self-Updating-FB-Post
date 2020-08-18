import facebook
from collections import Counter
import pprint
import requests
import json
list = ['LIKE', 'LOVE', 'CARE', 'HAHA', 'WOW', 'SAD', 'ANGRY']

def reactions(postid,access_token):
    r = requests.get(f"https://graph.facebook.com/{postid}?fields=reactions.summary(total_count)&access_token={access_token}").json()
    r = r["reactions"]["summary"]["total_count"]
    rlist = (f'Total Reactions = {r}\n')
    i = 0
    while i<7:
        c = requests.get(f"https://graph.facebook.com/{postid}?fields=reactions.type({list[i]}).limit(0).summary(total_count)&access_token={access_token}").json()
        c = c["reactions"]["summary"]["total_count"]
        rlist = rlist + (f"{list[i]} = {c}\n")
        i+=1
    return rlist
