import praw
from textblob import TextBlob

reddit = praw.Reddit('bot')

key = ['biden']

subreddit = reddit.subreddit('cs40_2022fall')
while True:
    for submission in list((reddit.subreddit("cs40_2022fall").hot(limit=None))):
        submission.comments.replace_more(limit=None)
        normalized_title = submission.title.lower()
        normalized_comments = submission.comments.list()
        for phrase in key:
            if phrase in normalized_title:
                textblob=TextBlob(submission.title)
                polarity=textblob.sentiment.polarity
                print('polarity=',polarity)
                if polarity>=0.0:
                    submission.upvote()
                    print('Submission Upvoted') 
                    break
                else:
                    submission.downvote()
                    print('Submission Downvoted')
                    break 

        for comment in normalized_comments:
            lowercase = comment.body.lower()
            for phrase in key:
                if phrase in lowercase:
                    textblob=TextBlob(comment.body)
                    polarity=textblob.sentiment.polarity
                    print('polarity=',polarity)
                    if polarity>=0.0:
                        comment.upvote()
                        print('Comment Upvoted') 
                        break
                    else:
                        comment.downvote()
                        print('Comment Downvoted')
                        break 
