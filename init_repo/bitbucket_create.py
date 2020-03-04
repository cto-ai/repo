from bitbucket.bitbucket import Bitbucket
import utils 

def authenticateUser(username, password):
    bb = Bitbucket(username, password)
    success, existing_repos = bb.repository.all()
    return bb, success, existing_repos


def create_repo(username, password, repo_name, isPrivate): 
    bb, success, existing_repos = authenticateUser(username, password)
    if success: 
        for repo in existing_repos: 
            if repo['name'] == repo_name: 
                msg = "❗ Error: A repo under {repo_name} already exists. Please choose a different name."
                return msg 
        bb.repository.create(repo_name, private=isPrivate)
        return f"🎉 Successfully created {repo_name}!"
    else: 
        return "❗ Error: Credentials are incorrect. Please try again." 


def delete_repo(username, password, repo_name): 
    bb, success, existing_repos = authenticateUser(username, password)
    if success: 
        name = utils.fix_repo_name(repo_name)
        isDeleted, info = bb.repository.delete(name)
        if isDeleted: 
            msg = f"🎉  Successfully deleted {repo_name}"
        else: 
            msg = f"❗  Error: {repo_name} does not exist. Please try again"
        return msg
    else: 
        return "❗  Error: Credentials are incorrect. Please try again."       


def build_repo_url(username, user_repo): 
    return f"https://{username}@bitbucket.org/{user_repo}.git"


def get_bbRepo_url(username, password, repo_name): 
    bb, success, existing_repos = authenticateUser(username, password)
    if success: 
        repo_name = utils.fix_repo_name(repo_name)
        success, info = bb.repository.get(repo_name)
        if success: 
            user_repo = info["resource_uri"].split("repositories/")[1]
            full_url =  build_repo_url(username, repo_name)
            return full_url
    else: 
        return "❗  Error: Credentials are incorrect. Please try again."


def get_user_repos(username, password):
    repo_urls = []
    repos = []
    msg = ""
    bb, success, existing_repos = authenticateUser(username, password)
    if success: 
        for repo in existing_repos: 
            user_repo = repo["resource_uri"].split("repositories/")[1]
            repo_name = user_repo.split("/")[1]
            full_url = "https://" + username + "@bitbucket.org/" + user_repo + ".git"
            repos.append(repo_name)
            repo_urls.append(full_url)
        return msg, repos, repo_urls 
    else: 
        msg = "❗  Error: Credentials are incorrect. Please try again."
        return msg, repos, repo_urls

