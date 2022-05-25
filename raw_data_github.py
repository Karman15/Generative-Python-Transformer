import time
from datetime import datetime
from github import Github
import os

end_time = time.time()
start_time = end_time - 86400
ACCESS_TOKEN = open('token.txt', 'r').read()
g = Github(ACCESS_TOKEN)

for i in range(3):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%Y-%m-%d')
    query = f"language:python created:{start_time_str}..{end_time_str}"
    end_time -= 86400
    start_time -= 86400

    result = g.search_repositories(query)
    print(result.totalCount)
    count = 0

    for repository in result:
        print(f"{repository.clone_url}")
        # print(f"{repository.owner.name}")
        
        #print(f"{repository.description}")
        #print(f"{repository.full_name}")
        #print(f"{repository.get_git_tag}")
        #print(f"{repository.get_labels}")
        #print(f"{repository.get_tags}")

        #print(f"{repository.get_topics()}")
        os.system(f"git clone {repository.clone_url} repos/{repository.owner.login}/{repository.name}")
        count += 1
        if (count > 30):
            break