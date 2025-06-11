#!/usr/bin/python3
'''Modulo'''
import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(url)

    print(f'Status Code: {response.status_codes}')

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    