import praw
from textblob import TextBlob 

reddit = praw.Reddit('bot')


subreddit = reddit.subreddit('cs40_2022fall')

for submission in subreddit.top(limit=None):
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    not_my_comments = []

    for comment in all_comments:
        try:
            if comment.author=="botfly123":
                pass
            else:
                not_my_comments.append(comment)
                if "Biden" in comment.body:
                    blob= TextBlob(comment.body)
                    if blob.sentiment.polarity>0:
                        comment.upvote()
                        print('upvote: ',comment.title)
                    else:
                        comment.downvote()  
                        print('downvote: ',comment.title)      
        except AttributeError:
            print('not a comment')
    