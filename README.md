# Hephestus

A skunkworks project to automate the windows image build

## Design Things

![design](docs/Windows-machine-updater.png)

A collection of python scripts to use on a scheduled AWS lambda to:

* Clone, branch, update, and push an updated packer file from the [machine-executor-images](https://github.com/circleci/machine-executor-images) repo 
* lambda will open a PR for `windows-update/*` branch
* when `windows-update/*` pr is opened workflow will notify #execution-teams about the PR being ready for merge
* when `windows-update/*` pr is merged to master workflow will trigger vm-service update lambda with image version names
* vm-service update lambda will clone, branch, and update the `config.edn` file with the new values
* vm-service update lambda will open PR for vm-service `windows-update/*` branch
* when `windows-update/*` pr is opened workflow will notify #execution-teams of PR being ready for merge
* when `windows-update/*` pr is merged to master, workflow will push a notification to #custeng-support #investigation and #execution-teams slack notifying of update

### Workflow changes

* windows update specific steps will trigger on `windows-update/*` titled branches 
* workflow behaviour will depend on if it is a `widnows-update/*` push or merge to master

### Configuration

All configuration data will be passed as environment variables:

* USERNAME : The git username to use for the git ops
* PASSWORD : The git password to use for the git ops

* CCI_USERNAME : The username to use for the CCI ops
* CCI_PASSWORD : The password to use for the CCI ops

## Development

A dockerfile exists to make a container to use as  development environment, the repo will have to be mounted into the container

### Image Diagram modification

use [draw.io](https://draw.io) to modify the image with the `docs/windows-machine-updater.drawio` file

## TODO

* write tests for update-machine-images script
  * add in pr monitoring to Gitter class
  * read in name and email from env for git commit message (currently hard coded to myself)

* write and test cci ops scripts

* do some architectual fanagling about how this will run in lambda (a single python program, some chained lambdas ??)


