import unittest
from docs.conf import SSH_HOST, SSH_PORT, SSH_USERNAME, SSH_PASSWORD
from ichat import Downloader, ScpServer


class TestLoader(unittest.TestCase):

    def test_download(self):
        href = 'https://hbimg.huabanimg.com/813038ff7ebe307d1e3bed34825e7da402af535d9b2b3-AvBw2Z_fw658'
        download = Downloader(10)
        download.run(href)

    def test_server(self):
        ScpServer(SSH_HOST, SSH_PORT, SSH_USERNAME, SSH_USERNAME)


if __name__ == '__main__':
    unittest.main()
