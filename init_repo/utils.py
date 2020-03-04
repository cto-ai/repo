# github and bitbucket does not automaticallly replace spaces with -
def fix_repo_name(repo_name): 
    return repo_name.replace(" ", "-")
