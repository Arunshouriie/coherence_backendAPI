import git
import os
from getpass import getpass
    
project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
os.environ['GIT_USERNAME'] = username
os.environ['GIT_PASSWORD'] = getpass()
g = git.cmd.Git('/path/to/some/local/repo')
g.pull()