# sample-pre-commit

Sample repo for pre-commit

## about

- This repo is for demonstrating how to utilize `pre-commit`.
- It is written aside blogs described below.

## blog related

- [Blog] [Let's try: pre-commit before you commit](https://bluebirz.net/posts/try-pre-commit/)
- [Medium] [Let's try: pre-commit before you commit](https://medium.com/@bluebirz/lets-try-pre-commit-before-you-commit-3b3c6879e589)

## How to run

```sh
# install
homebrew install pre-commit
pip install pre-commit

# install hooks
pre-commit install

# create sample config file
pre-commit sample-config > .pre-commit-config.yaml

# run manually
git add .
pre-commit run
# run all files manually
pre-commit run -a
pre-commit run --all-files
# run all files manually with verbose
pre-commit run -a --verbose

# clean cache from the run
pre-commit clean

# update `rev` in `.pre-commit-config.yaml` to the latest
pre-commit autoupdate
```
