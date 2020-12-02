---
description: Process of contributing to the project.
---

# Contributing

## Philosophy
- The philosophy is borrowing much from UNIX philosophy and the golang programming language.Each sub command should do one thing and do it well
 - Every component behaviour should be covered with an e2e tests and if an  e2e tests is not appropriate should at least have unit tests for key components of a package.

## Feedback / Issues
If you encounter any issue or you have an idea to improve, please:

* Search through Google and [existing open and closed GitHub Issues](https://github.com/tellor-io/telliot/issues) for the
answer first. If you find relevant topic, please comment on the issue.
* If not found, please add an issue to [GitHub issues](https://github.com/tellor-io/telliot/issues). Please provide
all relevant information as template suggest.
* If you have a quick question you might want to also ask on our [Discord](https://discord.gg/n7drGjh).
We are recommending, using GitHub issues for issues and feedback, because GitHub issues are track-able.

If you encounter security vulnerability, please let us know privately via the Team email address: [info@tellor.io](mailto:info@tellor.io?subject=Security%20vulnerability%20report)

## Adding New Features / Components
For any major changes or new features, please first
discuss the change you wish to make via issue or Discord, or any other
method before making a change.

## Development
The following section explains various suggestions and procedures to note during development.

### First Steps
* Familiarizing yourself with our [coding style guidelines.](04_coding-style-guide.md).
* Familiarizing yourself with the [Makefile](../Makefile) commands, for example, `build`, `format`, `test`, `lint`.
`make help` will print all available commands with some description.

### Pull Request Process
1. Fork tellor-io/telliot.git and start development from your own fork. Here are sample steps to setup your development environment:

```console
$ GOPATH=$(go env GOPATH)
$ mkdir -p $GOPATH/src/github.com/tellor-io
$ cd $GOPATH/src/github.com/tellor-io
$ git clone https://github.com/tellor-io/telliot.git
$ cd telliot
$ git remote add fork git remote add fork git@github.com/<your_github_id>/telliot.git
$ make build
$ ./telliot -h
```


1. Keep PRs as small as possible. For each of your PRs, you create a new branch based on the latest master.
Chain them if needed (base one PR on other PRs). You can read more details about the workflow from [here](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

```console
$ git checkout master
$ git pull origin master
$ git checkout -b <your_PR_branch>
$ <Iterate your development>
$ git push fork <your_PR_branch>
```

1. If your change affects users (adds,removes or changes a feature) add the item to the [CHANGELOG](CHANGELOG.md).
1. Add e2e tests for new features and changes to functionality. Add unit tests for key components of the packages.
1. A PR will me merged once the PR has been approved by at least one developer with write access.
1. If you feel like your PR is waiting too long for a review, feel free to ping in the [Discord](https://discord.gg/n7drGjh) channel for a review!

### Dependency management
The project uses [Go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) to manage dependencies on external packages. This requires a working Go environment with version 1.11 or greater and git installed.

To add or update a new dependency, use the `go get` command:

```bash
# Pick the latest tagged release.
go get example.com/some/module/pkg

# Pick a specific version.
go get example.com/some/module/pkg@vX.Y.Z
```

Tidy up the `go.mod` and `go.sum` files:

```bash
make deps
git add go.mod go.sum
git commit
```

### Project development go tools
The project uses [Bingo](../.bingo/README.md) for adding any go tools required by the project.
