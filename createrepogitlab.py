import gitlab
import sys
tocken="put your acess tocken here" #put your access tocken here


def createrepogitlab():
    reponame=sys.argv[1]
    git = gitlab.Gitlab('https://gitlab.com', private_token=tocken)
    git.projects.create({'name': reponame})

if __name__ == "__main__":
    createrepogitlab()