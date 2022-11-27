import praw
import random
import datetime
import time

madlibs = [
    "President [BIDEN] continues to [CONFRONT] [TRUMP] regarding his [OUTLANDISH] [IDEAS]. [BIDEN] has the American [PEOPLE] behind him.",
    "President [BIDEN] has been [PRESIDENT] for the past two years. In his time in power, he has [ACCOMPLISHED] [MUCH] in [SPACES] such as social reform and prison reform",
    "Former [PRESIDENT] [TRUMP] misused [POWER] while he was president. One example was when he tried to [NULLIFY] the 2020 election. This caused [PEOPLE] to question many of his actions.",
    "The [DEMOCRATS] have been pressing for [SOCIAL] [CHANGE]. [MOVEMENTS] such as BLM and prison [REFORM]",
    "Former [PRESIDENT] [TRUMP] was [SUSPENDED] from Twitter for his [OUTLANDISH] [REMARKS]. His tweets were in violatio of twitter's policy to not glorify violence.",
    "[PRESIDENT] [BIDEN] calls for an assault weapons ban after a nightclub [SHOOTING]. The left has been [CALLING] for gun control for quite [SOME_TIME]"
    ]

replacements = {
    'BIDEN' : ['Joe Biden', 'Joe'],
    'TRUMP' : ['Mr. Trump', 'Donald Trump', 'Donald'],
    'CONFRONT' : ['ridicule', 'argue with'],
    'OUTLANDISH' : ['crazy', 'ridiculous', 'wild'],
    'IDEAS'  : ['points', 'goals', 'schemes'],
    'PEOPLE' : ['civilians', 'populace'],
    'PRESIDENT' : ['leader', 'in charge'],
    'ACCOMPLISHED' : ['finished', 'fulfilled', 'achieved'],
    'MUCH' : ['a lot', 'plenty', 'loads'],
    'SPACES' : ['sectors', 'sections'],
    'POWER' : ['strength', 'force', 'ability'],
    'NULLIFY' : ['void', 'annul', 'invalidate'],
    'CHANGE' : ['reform', 'improvement', 'betterment'],
    'DEMOCRATS' : ['left', 'liberals'],
    'SOCIAL' : ['judicial'],
    'REFORM' : ['rectification', 'improvement', 'refinement'],
    'SUSPENDED' : ['void', 'annul', 'invalidate'],
    'OUTLANDISH' : ['void', 'annul', 'invalidate'],
    'REMARKS' : ['void', 'annul', 'invalidate'],
    'SHOOTING' : ['attack', 'assault'],
    'SOME_TIME' : ['a while', 'a stretch of time'],
    'CALLING' : ['asking for', 'wanting', 'craving'],
    'MOVEMENTS' : ['Organizations', 'Fronts', 'Campaigns'],
    }

# FIXME:
# copy your generate_comment function from the madlibs assignment here

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''

    madlib=random.choice(madlibs)
    for replacement in replacements.keys():
        madlib=madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yz64qm/my_wife_is_a_poll_worker_has_this_report/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
sleep_count=0
while True:
    try:

        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        submission.comments.replace_more(limit=None)
        all_comments = submission.comments.list()
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        my_comments = []
        for comment in all_comments:
            try:
                if comment.author == 'botfly123':
                    my_comments.append(comment)
                else:
                    not_my_comments.append(comment)
            except:
                print('comment deleted')

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (your bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)
        
        if has_not_commented:
        #    try:
        #        submission.reply(generate_comment())
        #    except: 
        #        print('exception found')
        #        print('starting to sleep')
        #        time.sleep(60)
        #        print('done sleeping')

        #    print(generate_comment())
        

            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # a top level comment is created when you reply to a post instead of a message
            try:
                submission.reply(generate_comment())
            except: 
                print('exception found')
                print('starting to sleep')
                time.sleep(60)
                print('done sleeping')

            print(generate_comment())
        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                replied = True
                for comment.reply in not_my_comments: 
                    if comment.author == 'botfly123':
                        replied = True
                        break 
                    if comment.author != 'botfly123':
                        replied = False 
                if replied:
                    continue
                else:
                    comments_without_replies.append(comment)

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly;
            # many students struggle with getting a large number of "valid comments"
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #try:
            #    random_comment=random.choice(comments_without_replies)
             #   print("still works here")
            #    random_comment.reply(body=generate_comment())
            #except Exception as e:
            #    print(e)
            '''
            if len(comments_without_replies)>0:
                try:
                    random_comment = random.choice(comments_without_replies)
                    #random_comment.reply(body=generate_comment())
                    text = generate_comment()
                    random_comment.reply(body=text)
                    print('reply to a comment')
                except Exception as e:
                    print(e)
            '''

            if len(comments_without_replies)>0:
                random_comment = random.choice(comments_without_replies)
                text = generate_comment()
                random_comment.reply(body=text)
                #random_comment.reply(body=generate_comment())
                print('reply to a comment')
                
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # these will not be top-level comments;
            # so they will not be replies to a post but replies to a message

        # FIXME (task 5): select a new submission for the next iteration;
        # your newly selected submission should be randomly selected from the 5 hottest submissions

        submission_list=list(reddit.subreddit('cs40_2022fall').hot(limit=5))
        submission=random.choice(submission_list)

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.
        time.sleep(1)
    except praw.exceptions.RedditAPIException as e:
            for subexception in e.items:
                if subexception.error_type == 'RATELIMIT':
                    error_str = str(subexception)
                    print(error_str)

                    if 'minute' in error_str:
                        delay = error_str.split('for ')[-1].split(' minute')[0]
                        delay = int(delay) * 60.0
                    else:
                        delay = error_str.split('for ')[-1].split(' second')[0]
                        delay = int(delay)

                    print("delay=", delay)
                    time.sleep(delay)
                    sleep_count += 1
                    print ("sleep count=", sleep_count)
