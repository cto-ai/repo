import unittest
import gitlab_create as gl 
import github_create as gh

class TestGitlab(unittest.TestCase): 
    def testInvalidGitlabToken(self): 
        sample_token="invalidtoken"
        self.assertEqual(gl.gitlab_login(sample_token), "Error: Invalid Credentials")

class TestGithub(unittest.TestCase): 
    def testInvalidGithubToken(self): 
        sample_token="invalidtoken"
        self.assertEqual(gh.github_login(sample_token), "Error: Invalid Credentials")


if __name__ == '__main__': 
    unittest.main()

