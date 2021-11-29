import praw
import random
import datetime
import time


# FIXME:
# copy your generate_comment function from the madlibs assignment here
reddit = praw.Reddit('bot', user_agent='cs40')
madlibs = [
    "Dan Crenshaw is an [AMAZING] [POLITICIAN]. I recommend [EVERYONE] read his [ARTICLE] for the [TIMES]",
    "Crenshaw will [WIN] in 2022 [BECAUSE] of his [SKILL]. He is doing [WELL] with [MINORITIES] in the polls",
    "I went for Crenshaw's [SPEECH] last [YEAR]. The [ATMOSPHERE] was great, and I met many of his [FRIENDS]. I hope he runs for [OFFICE] in the future!",
    "Crenshaw is a true American [PATRIOT], his service [ABROAD] was incredibly [BRAVE]. He is an inspiration for my [SON], and for many in my [COMMUNITY]",
    "I heard Crenshaw's speech on [CNN] about the [ECONOMY]. Everything he said was [CORRECT], even though the [PRESENTERS] [CHALLENGED] his views.",
    "Crenshaw was just voted most [INTELLIGENT] in a survey by [PEW]. He has an IQ of [150], listens to [BEETHOVEN] in his spare time, and reads [CLASSICS] in his free time, so it's not too surprising"
    ]

replacements = {
    'AMAZING': ['awesome','unbelieveable','intelligent'],
    'POLITICIAN': ['leader','Representative','public official'],
    'ARTICLE': ['piece','editorial','column'],
    'EVERYONE': ['people','families','sports lovers'],
    'TIMES': ['Wall Street Journal','LA Times','New York Times'],
    'WATCH': ['get into', 'start following', 'view'],
    'WIN':['be victorious','come out on top','outclass the rest of the field'],
    'BECAUSE':['due to','as a result of','thanks to'],
    'SKILL': ['political accumen','intelligence','public speaking skills'],
    'WELL': ['amazingly','excellently','surprisingly good'],
    'MINORITIES':['the poor','women','the LGBTQIA+ community'],
    'SPEECH':['townhall','rally','TV debate'],
    'ATMOSPHERE': ['food','seats','hospitality'],
    'YEAR': ['time','week','month'],
    'FRIENDS':['staffers','family members','collegues'],
    'OFFICE':['Senate','the House,','President'],
    'PATRIOT': ['hero','legend','warrior'],
    'ABROAD': ['Overseas','Afghanistan','in the Middle East'],
    'BRAVE': ['admirable','courageous','memorable'],
    'SON':['children','child,','boys'],
    'COMMUNITY': ['town','neighborhood','state'],
    'CNN': ['ABC','NBC','MSNBC'],
    'ECONOMY': ['border','supply chain crisis','rising inflation'],
    'CORRECT': ['logical','factual','true'],
    'PRESENTERS':['interviewer','hosts','anchors'],
    'CHALLENGED':['disagreed with','debated','disputed'],
    'INTELLIGENT': ['savvy','wily','clever'],
    'PEW': ['American Enterprise Institute','Heritage Foundation','Brookings Institute'],
    '150': ['160','170','180'],
    'BEETHOVEN': ['Mozart','Chopin','Bach'],
    'CLASSICS': ['Shakespeare','poetry','crime novels']
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    
    s=random.choice(madlibs)
    for k in replacements.keys():
        s=s.replace('['+k+']', random.choice(replacements[k]))
    return s



# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r1q6op/wikipedia_users_try_to_change_waukesha_parade_car/'
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

while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=', submission.title)
    print('submission.url=',reddit.submission('https://www.reddit.com/r/BotTown2/comments/r1q6op/wikipedia_users_try_to_change_waukesha_parade_car/'))

    submission.comments.replace_more(limit=None)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    #submission.comments.replace_more(limit=None)
    all_comments = []
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
    for comment in all_comments:
        #print('comment.author=', comment.author)
        #print('type(comment.author)=', type(comment.author))
        if comment.author !='hambotver4lyfe':
            not_my_comments.append(comment)
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
    print('has not commented=',has_not_commented)
    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text= generate_comment()
        submission.reply(text)
        

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        #comments_without_replies = [not_my_comments]
        comments_without_replies=[]
        for comment in not_my_comments:
            havent_replied=True
            for replies in comment.replies:
                try:
                    if replies.author=='hambotver4lyfe':
                        havent_replied= False
                        break
                except NameError:
                    pass
            if havent_replied:
                comments_without_replies.append(replies)
        print('len(comments_without_replies)=',len(comments_without_replies))
    

            
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
       
        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        comment=random.choice(comments_without_replies)
        try:
            comment.reply(generate_comment()) 
        except praw.exceptions.APIException:
            print('not replying to a comment that has been deleted')
    


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    pass
    # submission=random.choice('add right thing here')

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    
    hots=list(reddit.subreddit("BotTown2").hot(limit=5))
    submission=reddit.submission(id=random.choice(hots).id)
    print(submission.title)
    time.sleep(5)
