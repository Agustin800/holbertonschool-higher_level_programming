#!/usr/bin/python3
'''Modulo'''
import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        post_data = [{'id': posts['id'], 'title': posts['title'], 'body': posts['body']} for post in posts]

    with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fildnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(post_data)
