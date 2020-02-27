import praw
import re
reddit = praw.Reddit('bot1')#initialize
alreadydone = []#file that stores posts to which you have already applied
subreddit = reddit.subreddit('memes')#name of the subreddit
for submission in subreddit.hot(limit=2):#how many posts
    if submission.id not in alreadydone:#every post has a unique submission id
        #search for the below words
        if re.search("was i a good meme", submission.title, re.IGNORECASE):#igonore case of what you want
            submission.reply("ofcourse. Now bye")#your comment
            print("Bot replying to : ", submission.title)#name of the post you replied to
            alreadydone.append(submission.id)#adding the id to the list
