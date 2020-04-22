![](https://cto.ai/static/oss-banner.png)

# Repo Op  🚀
Repo is an Op designed to manage a user's repos on Bitbucket, Gitlab, or Github allowing users to archive, create, delete, and list their repos. This Op will require Gitlab and Github users to access their account through a personal access token while Bitbucket uses a username and password combination. This Op can also be used in Slack allowing users to easily perform these functions without having to navigate to the respective websites.

## Requirements
To run this or any other Op, install the [Ops Platform](https://cto.ai/platform).

Find information about how to run and build Ops via the [Ops Platform Documentation](https://cto.ai/docs/overview).

This Op uses a personal access token for Github and Gitlab authentication. These can be obtained by following the guides below. 

[Github Personal Access Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
- The following scopes need to be selected: repo, delete_repo

[Gitlab Personal Access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
- The following scopes need to be selected:  api, read_user, read_repository, write_repository, read_registry

## Usage
The very first time you run this Op, you'll want to set up the appropriate secrets so you don't have to manually enter it in each time. 

To set secrets, run: 

```bash
ops secrets:set
```

Follow the prompts and enter in the name of the key and its value. This will save the secret so it can be accessed the next time you use the Op. 

This will set the secret to the team which you're currently on (The default is your personal team which is the same as your username). You can also check which team you're currently on by running:  

```bash
ops whoami
```

In order to use the secrets you just set, the Op needs to be published to this team. 

To run the public version of the Op in the command line, enter in: 

```bash
ops run @cto.ai/repo
```

To run the public version of the Op in a public Slack channel: 
```
/ops run cto.ai/repo
```

## Local Development/Running from Source
**1. 👯 Clone the repo:**

```bash
git clone <git url>
```

**2. 🔨 Navigate into the directory and build the image:**

```bash
cd repo && ops build . 
```

**3. ⚙️  Run the Op from your current working directory with:**

```bash
ops run .
```

**4. ⚙️  To publish the Op to your team:**

```bash
ops publish .
```
To run the Op in Slack, make sure that you have the [CTO.ai Bot](https://cto.ai/platform) installed
in your Slack workspace.

To run the Op in a Slack channel, enter: 
`/ops run repo` 

## Debugging Issues
When submitting issues or requesting help, be sure to also include the version information. To get your Ops version run:

```bash
ops -v
```
You can reach us at the [CTO.ai Community Slack](https://cto-ai-community.slack.com/) or email us at support@cto.ai. 

## Limitations & Future Improvements
Currently, this Op will not work on accounts with company domains.  

Future iterations of this Op can include the ability to create issues, list MRs a user is assigned to, and the list goes on. 

## Contributing
See the [Contributing Docs](CONTRIBUTING.md) for more information.

## Contributors
The following people have contributed to this project: 
<table>
  <tbody>
    <tr>
      <td align="center" style="width: 80px;">
        <a href="https://gitlab.com/_juliehuang">
          <img src="https://secure.gravatar.com/avatar/7759082a0d73e31d18a31ab195a0786c?s=100&d=identicon" style="width: 100px;"><br>
          <sub>_juliehuang</sub>
        </a><br>
      </td>
    </tr>
    </tbody>
</table>

## LICENSE
[MIT](LICENSE)

