import praw

user_agent = "osx:prawtestproject:v0.01 (by /u/dirtymonkey)"

r = praw.Reddit(user_agent=user_agent)

user_name = "dirtymonkey"
user = r.redditor('dirtymonkey')
