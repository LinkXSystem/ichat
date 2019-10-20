import unittest

from ichat import Repository


class TestGithub(unittest.TestCase):
    def test_repository(self):
        repo = Repository('ichat', 'https://github.com/LinkXSystem/ichat', False, '2019-10-20T07:14:15Z',
                          '微信助手，Robot 模式', {})
        print(repo.markdown())


if __name__ == '__main__':
    unittest.main()
