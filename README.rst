Caveat: this is a work in progress. More details and examples will be added here

GammapyXray 
=======
A Python tool for the analysis of Gamma-ray and X-ray data in a unified framework, using physically-motivated spectral models.

The scripts provided in this folder are built on Numpy, Scipy, Astropy, Gammapy, Naima, Sherpa and Xspec. A software description is provided in the following publication: TBD

Installation and Set-up
+++++++++++++++++++++++++++++++++++++++++++++
These instructions assume that you have previously installed a version of `Anaconda <https://www.anaconda.com/products/distribution>`_ or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ on your machine.

Set-up the work environment with conda::

  conda create -n gammapyXray
  conda activate gammapyXray
  conda install -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa
  conda install -c conda-forge gammapy

`Install JupyterLab or Jupyter Notebook <https://jupyter.org/install>`_ (recommended). 

If you need to use the physical models provided by `Naima <https://naima.readthedocs.io/en/latest/>`_, follow `these instructions <https://naima.readthedocs.io/en/latest/installation.html>`_ (optional).

Download the ZIPped contents of this folder directly from the main GitHub `page <https://github.com/luca-giunti/gammapyXray>`_, or equivalently from the `Zenodo <TBD>`_ or `Software Heritage <TBD>`_ archives. Extract under your home directory::

  cd
  unzip ~/Downloads/gammapyXray-main.zip
  
To check that the installation has succeeded and start using the package, navigate to the ``gammapyXray-main`` folder and try to execute the example notebook::

  cd gammapyXray-main
  jupyter notebook example_nb.ipynb 

Citing
+++++++++++++++++++++++++++++++++++++++++++++


If you use gammapyXray for work/research presented in a publication (whether directly, or as a dependency to another package), we ask that you please cite it using the following links

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4701488.svg?style=flat
    :target: TBD
.. image:: https://archive.softwareheritage.org/badge/swh:1:dir:02e8a702ef6c9558a9f96d99bf6b9f41b5edcd34/
    :target: TBD

We encourage you to also include citations to the paper in the main text
wherever appropriate, using the recommended BibTeX entry:

Bibtex

Contributing Code and Feedback
+++++++++++++++++++++++++++++++++++++++++++++
.. image:: https://img.shields.io/github/issues-pr/registerrier/gammapy-ogip-spectra
    :target: https://github.com/registerrier/gammapy-ogip-spectra/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/registerrier/gammapy-ogip-spectra    
    :target: https://github.com/registerrier/gammapy-ogip-spectra/pulls


.. image:: https://img.shields.io/github/issues/registerrier/gammapy-ogip-spectra
    :target: https://github.com/registerrier/gammapy-ogip-spectra/issues
.. image:: https://img.shields.io/github/issues-closed/registerrier/gammapy-ogip-spectra?color=yellow    
    :target: https://github.com/registerrier/gammapy-ogip-spectra/issues

Licence
+++++++
This folder is licensed under a 3-clause BSD style license - see the
`LICENSE.rst <https://github.com/gammapy/gammapy/blob/master/LICENSE.rst>`_ file.

.. image:: https://anaconda.org/conda-forge/gammapy/badges/license.svg
    :target: TBD
    :alt: Licence
