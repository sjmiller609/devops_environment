==================
devops_environment
==================


.. image:: https://img.shields.io/pypi/v/devops_environment.svg
        :target: https://pypi.python.org/pypi/devops_environment

.. image:: https://img.shields.io/travis/sjmiller609/devops_environment.svg
        :target: https://travis-ci.org/sjmiller609/devops_environment

.. image:: https://readthedocs.org/projects/devops-environment/badge/?version=latest
        :target: https://devops-environment.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



Development environment for DevOps


* Free software: MIT license
* Documentation: https://devops-environment.readthedocs.io/en/latest/readme.html

A Python module to manage a CLI development environment.

You can pip install, then launch the same development environment on any machine with Docker.

Installation
------------

``pip install -U devops_environment``

Use
---

``devenv``

Recommendations
---------------

- Install Docker on host machine
- Configure git on host machine
- Set up ssh keys for git authentication in ~/.ssh/

Custom commands
---------------

- cfn-man: Look up cloud formation docs from command line.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
