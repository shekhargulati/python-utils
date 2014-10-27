import os,requests
import json

base_url = "https://api.github.com/"
token = os.environ.get("GITHUB_OAUTH_TOKEN")
user = os.environ.get("GITHUB_USERNAME")

headers = {"Authorization": "token %s" % token}

def all_fork_names():
	forks = []
	for i in range(1,9):
		r = requests.get(base_url+"user/repos?page="+i,headers=headers)
		response = r.json()
		for repo in response:
			if repo['fork']  == True:
				forks.append(repo['name'])
	return forks

def delete_all_forks(forks):
	for fork in forks:
		print "Deleting fork %s" % fork
		r = requests.delete("https://api.github.com/repos/%s/%s" % (user,fork),headers=headers)
		if r.ok:
			print "Deleted fork %s" % fork


if __name__ == "__main__":
        forks = all_fork_names()
        delete_all_forks(forks)