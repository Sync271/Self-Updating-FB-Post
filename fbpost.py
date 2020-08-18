import facebook
import time
import reactions
import comments
import requests
from collections import Counter

access_token = 'your_access_token'
graph = facebook.GraphAPI(access_token=access_token)

# graph.put_object(
#    parent_object = "me",
#    connection_name="feed",
#    message="Test#1")
# feed = graph.get_connections("me", "feed")
#
# post = feed['data']
# postid = post[0]['id']
postid = "your_post_id"
print(postid)

while True:
    comm = comments.comments(postid, graph)
    react = reactions.reactions(postid, access_token)
    message = (f'This Post Has :\n{comm}\n{react}\nUpdating Every 30s')
    # graph.put_object(
    #    parent_object = postid,
    #    connection_name="feed",
    #    message = f"?{message}")
    requests.post(
        f"https://graph.facebook.com/{postid}?message={message}&access_token={access_token}")
    time.sleep(30)
