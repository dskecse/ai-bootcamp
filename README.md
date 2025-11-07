# AI Bootcamp

## Tools

* [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) - environment for interactive computing with computational notebooks

## Prerequisites

* git
* Docker Desktop / OrbStack

## Setup

```sh
git clone https://github.com/dskecse/ai-bootcamp
cd $_
docker compose up
```

This will:

* clone the repo
* `cd` into the repo dir
* pull up the official [`minimal-notebook` Docker image](https://quay.io/repository/jupyter/minimal-notebook?tab=tags) - includes JupyterLab and common useful utilities, [based off of the `base-notebook`](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#image-relationships)
* map the repo's root dir to the container's work dir
* spin up the Jupyter Server on port `8888`
* serve notebooks from the repo dir.

To access the server (Jupyter Dashboard), open up http://localhost:8888/lab?token=TOKEN.

## Creating Jupyter Notebooks

By default Jupyter Dashboard points to the user's `HOME` dir.

Switch to the `work` dir there and create a Jupyter notebook:

```
Launcher -> Notebook -> Python 3 (ipykernel)
```

This will create a notebook file with an `.ipynb` extension.
