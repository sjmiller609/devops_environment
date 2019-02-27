# CLI Development ![alt text](https://travis-ci.com/stelligent/devops_environment.svg?branch=master)

A Python module to manage a CLI development environment.

You can pip install, then launch the same development environment on any machine with Docker.

# Installation:

```
pip install -U development_environment 
```

# Use:

```
devenv
```

# Recommendations:

- Install Docker on host machine
- Configure git on host machine
- Set up ssh keys for git authentication in ~/.ssh/

# Custom commands:

- cfn-man: Look up cloud formation docs from command line. Examples:
```
# cfn-man, followed by what you want the docs for
cfn-man security group
cfn-man auto scaling group

# just type in whatever, it will probably work (powered by Google search)
cfn-man asg
cfn-man auato scaligng groudp
```
