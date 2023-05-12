import git 

# Instantiate repo object
repo = git.Repo("C:\\Users\\aruni\\Backend\\coherence_backendAPI")
# pull down 
repo.remotes.origin.pull()
print('copied')