from uuid import uuid4
from ruamel.yaml import YAML
import os 

def updateMachineImage():
    windowsPackerFile = "windows/default/packer.yaml"
    machineImageRepo = "github.com/circleci/machine-executor-images.git"

    machineImageGit = Gitter("machine_image", machineImageRepo, "patch-tuesday")
    machineImageGit.clone()

    machineImageGit.branch()

    packerFilePath = os.path.join(machineImageGit.repoDir, windowsPackerFile)
    packerData = YAML()
    packer = None
    with open(packerFilePath, 'r') as packerFile:
        packer = packerData.load(packerFile)
        packer["variables"]["changeable_thing"] = str(uuid4())
    
    with open(packerFilePath, 'w') as packerFile:
        packerData.dump(packer, packerFile)

    machineImageGit.commit_n_push()

updateMachineImage()
