# StAP
StAP (statistics and probability) repository from the GuckLab.


## What is in StAP?

StAP contains resources, examples and tutorials on statistics and probability.
- [Resources can be found here](stap/resources).
- [Workshops can be found here](stap/workshops). Workshop example notebooks
  can be run by clicking on the button in the next section.


## Running StAP examples in the browser

You can run any jupyter notebooks in the browser by clicking on the below
button:

**button to be added**

There are Python and Wolfram Mathematica versions of each notebook.


### Using Jupyter Notebooks

- Here is a great [tutorial on Jupyter Notebooks](<https://www.youtube.com/watch?v=HW29067qVWk>)
  from Corey Schafer.


## Installing StAP

This section is only for users. If you are a developer and want to contribute
to StAP, you have to clone the repository and install in editable
mode (see below).

Depending on how you set up your GitHub/Lab, one of those
commands will work (should be using ssh!):

ssh
```bash
pip install StAP@git+ssh://git@github.com:GuckLab/StAP.git@X.Y.Z
```

https
```bash
pip install StAP@git+https://github.com:GuckLab/StAP.git@X.Y.Z
```

where ``X.Y.Z`` is the version of the package you are interested in.
For example to install `StAP==0.0.1` via SSH
(works if you have two-factor authentication enabled), run:

```bash
pip install StAP@git+ssh://git@github.com:GuckLab/StAP.git@0.0.1
```

and https:

```bash
pip install StAP@git+https://github.com:GuckLab/StAP.git@0.0.1
```


Windows users please note that this might only work with git bash, depending on
permissions.

To **upgrade** to a new version, use the ``--upgrade`` argument:

```bash
pip install --upgrade StAP@git+ssh://git@github.com:GuckLab/StAP.git@0.0.2
```
and https:

```bash
pip install --upgrade StAP@git+https://github.com:GuckLab/StAP.git@0.0.2
```

<!--
## For Developers

Activate your virtual environment and install this repo in editable mode,
i.e. in the root of the repository, run:

```bash
pip install -e .
```

### Testing

First install the testing requirements:

```bash
pip install -r tests/requirements.txt
```

Then run the tests with `pytest`:

```
pytest tests
```

and lint your code with flake8:

```bash
flake8 StAP tests
```
-->

## Releasing New Versions

1. Create a new tag:

```bash
git tag -a "0.1.0" -m "new release"  
git push --tags origin
```

At this point, users will be able to install this package with the description
provided at the top of this readme.

2. Create a distribution package e.g. ``StAP_XYZ.tar.gz`` with:

```bash
python setup.py sdist
```

3. Give the ``.tar.gz`` file to users and tell them to pip-install it with:

```bash
pip install StAP_XYZ.tar.gz
```
