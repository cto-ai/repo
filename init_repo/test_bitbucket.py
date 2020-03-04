import unittest
import bitbucket_create as bb
import utils

class TestRepoNameFix(unittest.TestCase): 
    def test_repo_with_spaces(self): 
        repo_name = "a new repo"
        fixed_repo_name = utils.fix_repo_name(repo_name)
        self.assertEqual(fixed_repo_name, "a-new-repo")

    def test_repo_without_spaces(self): 
        repo_name = "repository"
        fixed_repo_name = utils.fix_repo_name(repo_name)
        self.assertEqual(fixed_repo_name, "repository")

class TestBuildRepoURL(unittest.TestCase): 
    def test_url_build(self): 
        username = "testuser"
        user_repo = "repository"
        repo_url = bb.build_repo_url(username, user_repo)
        self.assertEqual(repo_url, "https://testuser@bitbucket.org/repository.git")

if __name__ == '__main__':
    unittest.main()
