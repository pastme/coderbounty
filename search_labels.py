from github import Github
import json

# get the label name from the environment variable
label_name = '$10'  # replace with '${{ env.LABEL_NAME }}' if using the defined environment variable

# create a Github instance
g = Github()

# search all public repositories for the label
results = g.search_labels(query=label_name)

# extract the name, repository URL, and repository name of each label found
labels = [{'name': label.name, 'repository_url': label.repository.html_url, 'repository_name': label.repository.full_name} for label in results]

# write the labels to a JSON file
with open('labels.json', 'w') as f:
    json.dump({'labels': labels}, f)
