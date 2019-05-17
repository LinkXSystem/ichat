import logging
from concurrent.futures import ThreadPoolExecutor, wait
from threading import Lock

from requests import get, head

look = Lock()


class Info(object):
    def __init__(self, size):
        self.size = size


class Downloader(object):
    def __init__(self, nums):
        self._nums = nums

    def run(self, url):
        # instance = self._transfer(target) if type else self._store(target)
        info = self.info(url)
        part = info.size // self._nums
        pool = ThreadPoolExecutor(max_workers=self._nums)
        futures = []
        for i in range(self._nums):
            start = part * i
            end = info.size if i != self._nums - 1 else start + part - 1
            futures.append(pool.submit(self.down, url, start, end))
        wait(futures)
        print(futures)

    @staticmethod
    def down(url, start, end):
        headers = {'Range': 'bytes={}-{}'.format(start, end)}
        r = get(url, headers=headers, stream=True)
        print(type(r.content))
        return r.content

    @staticmethod
    def info(url):
        href = url
        r = head(href)
        while r.status_code is 302:
            href = r.headers['Location']
            logging.info(logging.INFO, "Redirect: {}".format(href))
            r = head(href)
        return Info(size=int(r.headers['Content-Length']))

    @staticmethod
    def store(file, mode='wb'):
        f = open(file, mode)
        return f

    @staticmethod
    def transfer(target):
        return target
