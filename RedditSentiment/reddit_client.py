import praw
import config

def get_posts():
    reddit = praw.Reddit(
    client_id=config.reddit_client_id,
    client_secret = config.reddit_client_secret,
    user_agent="my user agent"
    )

    submission_titles = []
    submission_comments = []
    for submission in reddit.subreddit("cryptocurrency").hot(limit=25):
        submission_titles.append(submission.title)
        for comment in submission.comments.list():
            if not hasattr(comment, 'body'):
                continue
            submission_comments.append(comment.body)

    return (submission_titles, submission_comments)