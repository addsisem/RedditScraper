import praw
from praw.models import MoreComments
import pandas as pd
from collections import Counter

def getSubmissions(subreddit):

    submission = []

    for post in subreddit.top(limit=10):
        submission.append(post)

    return submission

def printSubmissionComments(submission):

    for i in range(len(submission)):
        print(submission[i].title)
        submission[i].comments.replace_more(limit=0)

        for comments in submission[i].comments.list():
            print(comments.author)
            print(comments.body, "\n")

def saveSubmissions(subreddit):

    sub = []
    title = []

    for post in subreddit.top(limit=50):
        sub.append(post.subreddit)
        title.append(post.title)

    df = pd.DataFrame(columns = ['Subreddit', 'Top'])

    for i in range(len(sub)):
        df.loc[i, 'Subreddit'] = sub[i]
        df.loc[i, 'Top'] = title[i]

    df.to_csv('A5.csv')

def processSubmissions():

    sub = []
    title = []
    counter = []
    point = {}
    count = 0

    df = pd.read_csv('A5.csv')
    list = df.values.tolist()

    for i in range(len(list)):
        sub.append(list[i][1])
        title.append(list[i][2])

    for j in range(len(title)):
        for element in title[j]:
            if element == '!':
                count = count + 1
        counter.append(count)
        count = 0

    for x, y in zip(sub, counter):
        if x not in point:
            point[x] = y
        else:
            point[x] += y

    temp = Counter(sub)
    top = temp.most_common(10)

    for i in range(len(top)):
        for j in point:
            if j == top[i][0]:
                print("{} :".format(top[i][0]), "{}".format(point[j]))

def main():

    redditInstance = praw.Reddit(user_agent='A5', client_id='c9MX-PNSpd4Tjw',
                                 client_secret="kI-F1f7g1-cWqujoQYIgwaG6-QE",
                                 username='sisemorea', password='khg=QrekT78335T')

    subreddit = redditInstance.subreddit('all')
    #submission = []

    #submission = getSubmissions(subreddit)
    #printSubmissionComments(submission)
    saveSubmissions(subreddit)
    processSubmissions()


if __name__ == '__main__':
    main()