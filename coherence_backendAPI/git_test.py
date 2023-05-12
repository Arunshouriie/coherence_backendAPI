import git 

# Instantiate repo object
repo = git.Repo("/home/azureuser/coherence_backendAPI/")

#stash changes
#repo.git.stash('save')
# pull down 
repo.remotes.origin.pull()
print('copied')