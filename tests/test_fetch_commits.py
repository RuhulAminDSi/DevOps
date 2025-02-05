import unittest
from fetch_commits import fetch_commits

class TestFetchCommits(unittest.TestCase):

    def test_fetch_commits(self):
        commits = fetch_commits()
        self.assertIsInstance(commits, list)  # Should be a list
        self.assertGreater(len(commits), 0)   # Should have at least one commit

if __name__ == '__main__':
    unittest.main()
