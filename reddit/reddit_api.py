#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:24:09 2018

@author: fz
"""
import praw
import time
import csv


#get authorization
def authorize():
    reddit = praw.Reddit(client_id='nGzUlTCl1QHuDg',
                     client_secret='4rSq4CFPsbjzU2RbBwf0tGIV9u0',
                     redirect_uri='http://localhost:8080',
                     user_agent='testscript by /u/fzEro5')
    return reddit

def extractdata():
    reddit = authorize()
    csvfile=open("reddit_api_data.csv", 'w')
    writer = csv.writer(csvfile)
    #the first line of the csv file.
    writer.writerow(["Hurricane_Name", "Submission_Title", "Submission_Content", "Submission_Time",
                 "Total_Comment_Number", "Comment_Content", "Comment_Time"])
    hurricaneList = {"hurricane irma", "hurricane harvey", "hurricane maria", "hurricane irene"}
    for hurricane in hurricaneList:
        #search in all subreddits
        for submission in reddit.subreddit('all').search(hurricane):
            # Convert Unix Time to est time
            ltime_submission = time.localtime(submission.created_utc)
            timeStr_submission=time.strftime("%Y-%m-%d %H:%M:%S", ltime_submission)
            submission.comments.replace_more(limit=None)
            # Get the top_level_comments
            for top_level_comment in submission.comments:
                ltime_top_comment = time.localtime(top_level_comment.created_utc)
                timeStr_top_comment=time.strftime("%Y-%m-%d %H:%M:%S", ltime_top_comment)
                top_list = []
                top_list.append(hurricane)
                top_list.append(submission.title)
                top_list.append(submission.selftext)
                top_list.append(timeStr_submission)
                top_list.append(submission.num_comments)
                top_list.append(top_level_comment.body)
                top_list.append(timeStr_top_comment)
                writer.writerow(top_list)
                #print(top_list)
                #print("\n***************")
                #Get the second_level_comments
                for second_level_comment in top_level_comment.replies:
                    ltime_second_comment = time.localtime(second_level_comment.created_utc)
                    timeStr_second_comment=time.strftime("%Y-%m-%d %H:%M:%S", ltime_second_comment)
                    send_list = []
                    send_list.append(hurricane)
                    send_list.append(submission.title)
                    send_list.append(submission.selftext)
                    send_list.append(timeStr_submission)
                    send_list.append(submission.num_comments)
                    send_list.append(second_level_comment.body)
                    send_list.append(timeStr_second_comment)
                    writer.writerow(send_list)
                    #print(send_list)
                    #print("\n***************")
    csvfile.close()

if __name__ == "__main__":
    extractdata()