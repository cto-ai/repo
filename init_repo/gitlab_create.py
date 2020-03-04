import gitlab

def gitlab_login(token): 
    gl = gitlab.Gitlab("https://gitlab.com/", private_token=token)
    try: 
        gl.auth()
        return gl, None 
    except Exception as err: 
        err = "❗  Error: Invalid Credentials"
        return None, err


def get_gitlabRepo_url(token,name): 
    user, err = gitlab_login(token)
    if err: 
        return err 
    else: 
        projects = user.projects.list(owned=True, search=name, all=True)
        for project in projects: 
            url = project.http_url_to_repo
            return url 


# visibility = public or private
def create_project(token, name, visibility): 
    user, err = gitlab_login(token)
    if err: 
        return err 
    else: 
        try: 
            user.projects.create({"name": name, "visibility": visibility }) 
            return f"🎉  Successfully created {name}!" 
        except Exception as error: 
            if error.response_code ==400: 
                msg = f"❗  Error: {name} already exists."
                return msg
            else: 
                return err


def get_user_repos(token):
    project_names = []
    project_urls  = []
    msg = ""
    user, err = gitlab_login(token)
    if err: 
        return err, project_names, project_urls
    else:
        try:
            projects = user.projects.list(owned=True, all=True)
            for project in projects: 
                project_names.append(project.name) 
                project_urls.append(project.http_url_to_repo)
            return msg, project_names, project_urls  
        except Exception as error: 
            return error, project_names, project_urls

def check_project_exists(token, name):
    user, err = gitlab_login(token)
    if err: 
        return err 
    else:
        projects = user.projects.list(owned=True, search=name, all=True)
        if projects: 
            return [project for project in projects if project.name == name]
        else: 
            return f"❗  Error: {name} does not exist"


def archive_project(token, name): 
    user, err = gitlab_login(token)
    if err: 
        return err 
    else:
        projectToArchive= check_project_exists(token, name)
        if not projectToArchive:
            return f"❗  Error: {name} does not exist"
        else: 
            projectToArchive[0].archive()
            return f"🎉  Successfully archived {name}!"

def delete_project(token, name):
    user, err = gitlab_login(token)
    if err:  
        return err 
    else:
        projectToDelete = check_project_exists(token, name)
        if not projectToDelete: 
            return f"❗  Error: {name} does not exist"
        else: 
            projectToDelete[0].delete()
            return f"🎉  Successfully deleted {name}!"
