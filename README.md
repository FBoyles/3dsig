Collaberative structural biology using machine learning and Jupyter notebook
============================================================================
## Fergus Boyles and Fergus Imrie
### _Department of Statistics, University of Oxford_
### ISMB 2018

__Introduction:__

Welcome to the GitHub repository containing all materials (excl. raw data) used in the above ISMB workshop.
This workshop will include a live demonstration that we invite you to join in and follow along on your laptop, or to simply use these materials as a reference. 
NOTE: There is no requirement to download anything to particpate in the workshop.

__Instructions:__

A zip containing all materials (incl. data) can be found at http://opig.stats.ox.ac.uk/webapps/ISMB2018


0.5: If you downloaded this from GitHub, download the data

TODO explain directory structure?

There are two data files for this workshop, found in the 'data' folder:

Data_3Dsig.txt - Computed features for pairs of protein sequences, together with labels that state whether the two proteins belong to the same family, superfamily, or fold.
Data_Split.txt - Clustering information used to split the data set.

There are two .ipynb files and one .py file, found in the 'notebooks' folder:

Workshop.ipynb - This is an incomplete, lightweight version of the problem notebook that we'll use during the demonstration.
Solution.ipynb - This is a complete notebook containing the full solution to the toy problem we'll be exploring in the demonstration, together with extensive markdown documentation and some extra code and figures.
plotting.py - This is some code we'll be using to generate figures in the notebooks.

There is a file called fergalicious.yml in the top-level directory. This file specifies the conda environment we'll be using during the workshop, and can be used by conda to automatically build the environment for us.

1: Install and update conda

We'll be using conda to create an isolated Python installation. If you don't have a conda installation, you can follow the instructions at https://conda.io/docs/user-guide/install/index.html#system-requirements to set up a conda installation on Windows, MacOS, or Linux. We recommend installing Miniconda rather than Anaconda as it is much smaller, and we'll be installing the python packages we need later anyway. It doesn't matter which version of Python you initially install with conda since we'll be creating a new python installation for the workshop. If you already have a conda installation, you'll want to make sure both conda and conda build are reasonably up-to-date. You can update conda and conda build in a Terminal window or Anaconda prompt by running:

conda update conda
conda update conda-build

If for whatever reason you don't have conda build, you can install it by running:

conda install conda-build

2: Create a conda environment for the workshop

The file fergalicious.yml specifies the python version and all packages used when running the notebooks. To create the conda environment from a Terminal window or Anaconda prompt, run:

conda env build -f fergalicious.yml

This should create a new conda environment with an installation of python 3.6 and the packages numpy, pandas, scikit-learn, matplotlib, and seaborn. It will also install jupyter, jupyter lab, and nb_conda_kernels (required for jupyter lab to use the python interpreter in this installation as a kernel).

You can verify that conda has created an environment called 'fergalicious' by running:

conda info --envs

and that the correct packages have been installed by running:

conda list -n fergalicious

3: Launch Jupyter and verify that you can use fergalicious as a kernel

If you didn't have jupyter installed before creating the environment fergalicious, you'll first need to activate the environment so that your system can find jupyter. To do this in a Terminal (on Linux, MacOS, or on Windows using git-bash), run:

source activate fergalicious

If you're working on Windows, you can instead activate the environment in a command prompt or powershell session by running:

activate fergalicious

Finally, in an Anaconda prompt, you can run:

conda activate fergalicious

As long as the environment remains active, any commands you run in this window will use the python interpreter installed in the environment instead of your default python interpreter.

If you want to deactivate the environment simply run:

source deactivate fergalicious
deactivate fergalicious
conda deactivate fergalicious

If you already have a jupyter installation, you can launch jupyter using your existing installation. Because we install nb_conda_kernels you can select fergalicious as a kernel from within a jupyter session even if the environment isn't active.

To launch jupyter notebook, run:

jupyter-notebook

You can create a new notebook by clicking the 'new' button in the top right of the window. This will show a drop-down menu listing all the kernels jupyter can use. You should be able to select conda env:fergalicious from this menu.

You can also select an existing notebook to load from the files displayed. Load data/Workshop.ipynb. You can change the kernel used via the 'Kernel' menu on the toolbar at the top of the window.

For the demonstration we'll be using JupyterLab, a browser-based computational environment that marries full support for jupyter notebooks with a host of handy features, such as a file browser, console, and support for multiple notebooks and test files in tabs. Although still in beta, the current release of JupyterLab is stable for daily use. If you appreciate the interactivity of jupyter notebooks but want some of the powerful features normally found in an IDE, I strongly recommend giving JupyterLab a try.

To launch JupyterLab, run:

jupyter-lab

From here, you can view the files in your current directory, and choose a kernel to start a new notebook. Try loading Workshop.ipynb and experimenting with the features available.

Have fun, and we're looking forward to seeing you on Tuesday!

Fergus and Fergus
