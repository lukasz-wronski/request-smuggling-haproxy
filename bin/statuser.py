#!/usr/bin/env python3
import argparse
import os
import sys
import time
import traceback


import requests

SLEEP_TIME = float(os.getenv("SLEEP_TIME", 2))
URL = "http://127.0.0.1:1337/stats"


def main():
    run_loop()


def request_stats():
    files = {
        'login': (None, 'szkola'),
        'password': (None, 'security'),
    }
    response = requests.post(
        URL,
        files=files,
        timeout=1
    )

def run_loop():
    while True:
        try:
            request_stats()
        except Exception as ex:
            print(ex)
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    sys.exit(main())