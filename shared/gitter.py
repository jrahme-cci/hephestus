from git import Repo
from shutil import rmtree
import os 

class Gitter(object):
    def __init__(self, target, repo, newBranch):
        self.repoDir = os.path.join("/tmp/repos", target)
        self.username = os.environ["USERNAME"]
        self.password = os.environ["PASSWORD"]
        self.repoURL = "https://"+self.username+":"+self.password+"@"+repo
        self.repo = None
        self.branchName = newBranch

    def clone(self):
        if os.path.isdir(self.repoDir):
            try:
                rmtree(self.repoDir)
            except Exception as e:
                print(e)
                raise e

        try:
            Repo.clone_from(self.repoURL, self.repoDir)
            self.repo = Repo(self.repoDir)
            self.repo.config_writer().set_value("user", "name", "Jacob Rahme").release()
            self.repo.config_writer().set_value("user", "email", "jacob.rahme@circleci.com").release()
        except Exception as e:
            print(e)
            raise e

    def branch(self):
        if self.repo != None:
            current = self.repo.create_head(self.branchName)
            current.checkout()
        else:
            raise Exception("No cloned")

    def commit_n_push(self):
        master = self.repo.heads.master 
        self.repo.git.pull('origin', master)
        self.repo.git.add(A=True)
        self.repo.git.commit(m="Update changeable thing for Windows image update")
#        self.repo.git.push('--set-upstream', 'origin', 'self.branchName')
