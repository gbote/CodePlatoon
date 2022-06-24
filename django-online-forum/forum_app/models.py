from hashlib import new
from django.db import models
from datetime import datetime

## main classes

class Comment:
    last_id = 0
    file_headers = ["id", "post_id", "author", "body", "creation_time"]

    def __init__(self, post_id, author, body, id = None, creation_time = None):
        self.id = int(id) if id else Comment.last_id + 1 
        self.post_id = int(post_id)
        self.body = body
        self.author = author
        self.creation_time = creation_time or datetime.now().strftime('%Y-%m-%d')

        # auto-generate next id
        Comment.last_id = max(Comment.last_id, self.id)

    def __repr__(self):
        return f"COMMENT: {self.id} for POST: {self.post_id}"

class Post:
    last_id = 0
    file_headers = ["id", "title", "author", "body", "creation_time"]

    def __init__(self, title, author, body, id = None, creation_time = None):
        self.id = int(id) if id else Post.last_id + 1
        self.title = title
        self.body = body
        self.author = author
        self.creation_time = creation_time or datetime.now().strftime('%Y-%m-%d')
        self.comments = []

        # auto-generate next id
        Post.last_id = max(Post.last_id, self.id)
        
    def __repr__(self):
        return f"POST: {self.id}: {self.title}"

    def add_comment(self, new_comment, update_file = True):
        self.comments.append(new_comment)
        if update_file:
            print(new_comment.__dict__.keys)
            # append_data(COMMENTS_FILE, [new_comment], new_comment.__dict__.keys())
            append_data(COMMENTS_FILE, [new_comment], Comment.file_headers)


    @classmethod
    def add_post(cls, new_post):
        append_data(POSTS_FILE, [new_post], cls.file_headers)
        all_posts.append(new_post)


## csv functions

import csv
import os

POSTS_FILE = "./data/posts.csv"
COMMENTS_FILE = "./data/comments.csv"
BASE_PATH = os.path.dirname(__file__)

def read_data(filepath, ClassName):
    data = []
        
    with open(os.path.join(BASE_PATH, filepath), "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row)
            person = ClassName(**row)
            data.append(person)

    return data

def append_data(filepath, data, headers):
    with open(os.path.join(BASE_PATH, filepath), "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, extrasaction='ignore')
        for item in data:
            writer.writerow(item.__dict__)


## data loading

all_posts = read_data(POSTS_FILE, Post)
all_comments = read_data(COMMENTS_FILE, Comment)

for c in all_comments:
    for p in all_posts:
        if p.id == c.post_id:
            p.add_comment(c, False)

