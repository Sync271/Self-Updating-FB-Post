import facebook
from collections import Counter
import pprint

def comments(postid,graph):
    
    commentsWithReplies = graph.get_connections(id=postid, connection_name='comments?summary=1&filter=stream')
    justComments = graph.get_connections(id=postid, connection_name='comments?summary=1&filter=toplevel')
    c = int(justComments['summary']['total_count'])
    cr = int(commentsWithReplies['summary']['total_count'])
    return (f'Total = {cr} Comments And Replies\nComments = {c}\nReplies = {cr-c}')

