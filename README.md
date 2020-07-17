# Hephestus

A skunkworks project to automate the windows image build

## Design Things

A collection of python scripts to use on a scheduled AWS lambda to:*

* Clone, branch, update, and push an updated packer script from the [machine-executor-images](https://github.com/circleci/machine-executor-images) repo (update-machine-images.py)

* Monitor branch on CCI for pass / fail

* Attempt 1 retry on a fail

* Open up a PR for the changes

* Monitor vm-service PR status until merged

* Once merged clone, branch, update, and push the required updates to [vm-service](https://github.com/circleci/vm-service)

* Monitor vm-service branch until pass

* Attempt 1 retry on fail

* Monitor vm-service PR status until merged

* Post an update to slack on #execution-teams , #custeng-support , #investigation when vm-service PR is merged

* Post an error to above channels when one of the steps fails horribly


### Configuration

All configuration data will be passed as environment variables:

* USERNAME : The git username to use for the git ops
* PASSWORD : The git password to use for the git ops

* CCI_USERNAME : The username to use for the CCI ops
* CCI_PASSWORD : The password to use for the CCI ops

## Development

A dockerfile exists to make a container to use as  development environment, the repo will have to be mounted into the container

## TODO

* write tests for update-machine-images script
  * add in pr monitoring to Gitter class
  * read in name and email from env for git commit message (currently hard coded to myself)

* write and test cci ops scripts

* do some architectual fanagling about how this will run in lambda (a single python program, some chained lambdas ??)
