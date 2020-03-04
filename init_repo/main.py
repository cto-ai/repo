import json
import os
import requests

from cto_ai import ux, prompt,sdk

import bitbucket_create as bb
import github_create as github
import gitlab_create as gitlab
import logos 

def repo_details(): 
    repo_name = prompt.input(name = "repo", 
                        message = "🆔  Name of repo to be initialized")
    visibility = prompt.list(name = "visibility", 
                        choices = ["public", "private"], message = "👀  Select visibility of your repo")
    if visibility == "public": 
        isPrivate = False
    else: 
        isPrivate = True
    return repo_name, isPrivate 


# credentials for bitbucket
def get_user_creds(): 
    username = prompt.input(name = "user", 
                        message = "👤  Please enter in your username")

    password = prompt.password(name = "password", 
                        message = "🔑  Please enter in your password")
    return username, password


def auth_token(platform): 
    token = prompt.secret(name = "token", 
            message = "🔑  Please enter in your token")

    if platform == "GitLab": 
        user, msg = gitlab.gitlab_login(token)
        if msg: 
            ux.print(msg)
            return msg, None

    elif platform == "GitHub": 
        user, msg = github.github_login(token)
        if msg:            
            ux.print(msg)
            return msg, None

    return user, token


def clone_statement(url): 
    ux.print("📂  To clone your repo, run git clone " + url + '')


def get_action(): 
    action = prompt.list(name = "resp",
                        choices = ["Archive a repo", "Create a repo", "Delete a repo", "List all repos"], 
                        message  = "✨  Select a command")
    return action


def archive_repo(platform, token, repo_name): 
    if platform == "GitLab": 
        msg = gitlab.archive_project(token, repo_name)
        ux.print(msg)
    else:       
        msg = github.archive_repo(token, repo_name)
        ux.print(msg)


def create_repo(platform, git, token): 
    repo_name, visibility = repo_details()

    if platform == "GitLab": 
        # gitlab takes in these strings for visibility
        if visibility: 
            visibility = "private"
        else: 
            visibility = "public"
        msg = gitlab.create_project(token, repo_name, visibility)
        ux.print(msg)
        if "Error" not in msg: 
            clone_statement(gitlab.get_gitlabRepo_url(token, repo_name))
    else:       
        msg = github.create_repo(token, repo_name, visibility)
        ux.print(msg)
        if "Error" not in msg: 
            clone_statement(github.get_githubRepo_url(token, repo_name))


def delete_repo(platform, token,  repo_name): 
    if platform == "GitLab": 
        isSuccess = gitlab.delete_project(token, repo_name)
        ux.print(isSuccess)

    elif platform == "GitHub":
        isSuccess = github.delete_repo(token, repo_name)
        ux.print(isSuccess)


def list_repos(platform, token): 
    if platform == "GitLab":
        msg, project_names, project_urls = gitlab.get_user_repos(token) 
        if msg: 
            ux.print(msg)
        return msg, project_names, project_urls

    elif platform == "GitHub": 
        msg, repo_names, repo_urls = github.get_user_repos(token) 
        if "Error" in msg: 
            ux.print(msg)
        return msg, repo_names, repo_urls


def confirm_archive(repos):
    repoToArchive = prompt.list(name = "choice", 
                            message = "👉  Choose repo to be archived", 
                            choices = repos) 
    return repoToArchive


def confirm_delete(repos): 
    repoToDelete = prompt.list(name = "choice",
                                message = "👉  Choose repo to be deleted",
                                choices =  repos)
    willDelete = prompt.confirm(name = "resp", 
                                message = f"‼️   Are you sure you want to delete {repoToDelete}? This CANNOT be undone.")
    if willDelete: 
        return repoToDelete
    else: 
        ux.print("🚫  Cancelling, exiting op ...")


def main():
    logos.logo_print()
    ux.print(logos.intro)

    platform = prompt.list(message = "✅  Select a version control platform",
                            choices = ["Bitbucket", "GitHub", "GitLab"],
                            name = "platform")

    if platform == "Bitbucket":  
        username, password = get_user_creds()
        action = prompt.list(name = "resp",
                        choices = ["Create a repo", "Delete a repo", "List all repos"], 
                        message = "✨  Select a command")

        if action == "Create a repo": 
            repo_name, visibility = repo_details()
            result = bb.create_repo(username, password,repo_name, visibility)
            if "Error" not in result: 
                clone_statement(bb.get_bbRepo_url(username, password, repo_name))
            ux.print(result)

        elif action == "List all repos": 
            msg, repos, _ = bb.get_user_repos(username, password) 
            if "Error" in msg: 
                ux.print(msg)
                return              
            else: 
                for repo in repos: 
                    ux.print(repo)
        else: 
            msg, repos, _ = bb.get_user_repos(username, password) 
            if "Error" in msg: 
                ux.print(msg)
                return              
            if repos: 
                repo_to_delete = confirm_delete(repos)
                if repo_to_delete:  
                    isSuccess = bb.delete_repo(username, password, repo_to_delete) 
                    ux.print(isSuccess)
            else: 
                ux.print("🚫  Error: There are no repos available to be deleted")

    # if platform is github or gitlab    
    else: 
        git, token = auth_token(platform) 
        if token: 
            action = get_action()
            if action == "Archive a repo": 
                msg, repo_names, _ = list_repos(platform, token)
                repoToArchive = confirm_archive(repo_names)
                archive_repo(platform, token, repoToArchive)

            elif action == "Create a repo": 
                create_repo(platform, git, token)

            elif action == "List all repos": 
                msg, repo_names, _ = list_repos(platform, token)
                if not msg: 
                    for repo in repo_names: 
                        ux.print(repo)

            elif action == "Delete a repo": 
                msg, repo_names, _ = list_repos(platform, token)
                repo_to_delete = confirm_delete(repo_names)

                if repo_to_delete: 
                    delete_repo(platform, token, repo_to_delete)
        else: 
            ux.print("💤  Exiting op ...")


if __name__ == "__main__": 
    main()
