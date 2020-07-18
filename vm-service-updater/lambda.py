from gitter import Gitter
from uuid import uuid4
from ruamel.yaml import YAML
from edn_format import Keyword, loads, dumps
import edn_format
import os

def updateVmServiceImage(windowsVersions):
    vmServiceRepo = "github.com/circleci/vm-service.git"
    vmConfigFile = "config/config.edn"
    vmChartFile = "chrats/vm-service/templates/vm-service-config.yaml"

    vmServiceGit = Gitter("vm_service", vmServiceRepo, "windows-update/" + str(uuid4()))
    vmServiceGit.clone()
    vmServiceGit.branch()

    vmConfigPath = os.path.join(vmServiceGit.repoDir, vmConfigFile)
    vmChartPath = os.path.join(vmServiceGit.repoDir, vmChartFile)

    chartData = YAML()
    chartConfig = None

    config = None

    with open(vmChartPath, 'r') as chartFile:
        imageStubs = ["windows-server-2019-vs2019:", "windows-server-2019-nvidia-small:",
                "windows-server-2019-nvidia-medium:", "windows-server-2019-nvidia-large:"]
        imageTags = ["stable", "edge", "canary"]

        chartConfig = loads(chartData.load(chartFile)["data"]) # image config is in EDN format
        vmImages = chartConfig[Keyword("vm-manager")][Keyword("images")]
        for i in imageStubs:
            for tag in imageTags:
                vmImages[i+tag] = windowsVersions[i]

        chartConfig[Keyword("vm-manager")][Keyword("images")] = vmImages
        

    with open(vmConfigPath, 'r') as configFile:
        config = loads(configFile.read())
        configImages = config[Keyword("vm-manager")][Keyword("images")]["gce"]
        configImages["windows-server-2019:e2e-test"] = windowsVersions["windows-server-2019-base"]
        configImages["windows-server-2019-vs2019:e2e-test"] = windowsVersions["windows-server-2019-nvidia-small"]

        
updateVmServiceImage({"windows-server-2019-base" : "base",
    "windows-server-2019-nvidia-small" : "nvidia-small",
    "windows-server-2019-nvidia-medium" : "nvidia-medium",
    "windows-server-2019-nvidia-large" : "nvidia-large"})

