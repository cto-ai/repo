from github import Github, GithubException

import utils
# authenticate user token
def github_login(token):
    git_auth_user = Github(token).get_user()
    try: 
        git_auth_user.login
        return git_auth_user, None
    except GithubException as auth_err: 
        if auth_err.status == 401: 
            err = "❗  Error: Invalid Credentials"
            return None, err

def get_user_repos(token): 
    gh_user, err = github_login(token)
    repo_names = []
    repo_urls= []
    msg = ""
    if err:  
        return err, repo_names, repo_urls
    else: 
        repos = gh_user.get_repos()
        for r in repos: 
            repo_names.append(r.name)
            repo_urls.append(r.clone_url)
        return msg, repo_names, repo_urls
    
def create_repo(token, repo_name, visibility):  
    user, err = github_login(token)
    if err: 
        return err 
    else: 
        try: 
            new_repo = user.create_repo(name=repo_name, private=visibility)
            msg = f"🎉  Successfully created {repo_name}!"
            return msg
        except GithubException as err: 
            if err.status == 422: 
                msg = f"❗  Error: A repo with the name {repo_name} already exists. Please try again."
                return msg

def get_githubRepo_url(token, repo_name):
    user, err = github_login(token)
    name = utils.fix_repo_name(repo_name)
    if err: 
        return err 
    else: 
        repo = user.get_repo(name)
        url = repo.clone_url
        return url

def delete_repo(token, repo_name): 
    user, err = github_login(token)
    name = utils.fix_repo_name(repo_name)
    if err: 
        return err 
    else:
        try: 
            repo_to_delete = user.get_repo(name).delete()       
            msg = f"🎉  Successfully deleted {name}!"
            return msg
        except GithubException as err: 
            if err.status ==404: 
                msg = f"❗  Error: {name} does not exist."
                return msg 

def archive_repo(token, repo_name): 
    user, err = github_login(token)
    name = utils.fix_repo_name(repo_name)
    if err: 
        return err 
    else:
        try: 
            repo_to_delete = user.get_repo(name).edit(archived=True)       
            msg = f"🎉  Successfully archived {name}!"
            return msg
        except GithubException as err: 
            if err.status ==404: 
                msg = f"❗  Error: {name} does not exist."   
                return msg 

