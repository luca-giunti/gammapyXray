GammapyXray 
=======
A Python code for the spectral analysis of Gamma-ray and X-ray data in a unified framework, using physically-motivated spectral models. The data handling and fitting relies on the Gammapy architecture, while the multi-wavelength spectral modeling can be performed using an arbitrary combination of the functions included in the Gammapy, Xspec and Naima libraries.

This code is built on Numpy, Scipy, Astropy, Gammapy, Naima, Sherpa and Xspec. A working example is provided in the ``tutorial.ipynb`` notebook, while a software description can be found in the following publication: TBD

If you wish to give us your feedback, report bugs or ask for help please open an issue or send us an email.

.. image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
    :target: http://www.astropy.org/

.. image:: https://anaconda.org/conda-forge/gammapy/badges/installer/conda.svg

Citing
+++++++++++++++++++++++++++++++++++++++++++++


If you use the GammapyXray code for work/research presented in a publication (whether directly, or as a dependency to another package), we ask that you please cite it using the following links

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.4701488.svg?style=flat
    :target: TBD
.. image:: https://archive.softwareheritage.org/badge/swh:1:dir:02e8a702ef6c9558a9f96d99bf6b9f41b5edcd34/
    :target: TBD

We encourage you to also include citations to the related paper in the main text of your article wherever appropriate, using the recommended BibTeX entry:

TBD

Installation and Set-up
+++++++++++++++++++++++++++++++++++++++++++++
These instructions assume that you have previously installed a version of `Anaconda <https://www.anaconda.com/products/distribution>`_ or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ on your machine.

- Set-up the work environment with conda::

    conda create -n gammapyXray
    conda activate gammapyXray
    conda install -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa
    conda install -c conda-forge gammapy=0.20.1
  
- `Install JupyterLab or Jupyter Notebook <https://jupyter.org/install>`_ (recommended). 

- If you need to use physically-motivated radiative models, install `Naima <https://naima.readthedocs.io/en/latest/>`_ following `these instructions <https://naima.readthedocs.io/en/latest/installation.html>`_ (optional).

- Download the ZIPped contents of this folder directly from the main GitHub `page <https://github.com/luca-giunti/gammapyXray>`_, or equivalently from the `Zenodo <TBD>`_ or `Software Heritage <TBD>`_ archives. Then extract under your home directory::

    cd
    unzip ~/Downloads/gammapyXray-main.zip
  
- To check that the installation has succeeded and start using the package, navigate to the ``gammapyXray-main`` folder and execute the tutorial notebook::

    cd gammapyXray-main
    jupyter notebook tutorial.ipynb 


Testing
+++++++++++++++++++++++++

If you wish to execute the tests associated to this code (using `pytest <https://docs.pytest.org/en/7.1.x/getting-started.html#install-pytest>`_) you need to:

- set up the ``XMM_DATA`` environment variable::

    export XMM_DATA=<absolute path>/gammapyXray/XMM_test_files/
- run pytest from the ``gammapyXray`` folder::

    pytest gammapyXray/tests/test_models.py
    pytest gammapyXray/tests/test_ogip_spectrum_dataset.py 

Licence
+++++++
This folder is licensed under a 3-clause BSD style license - see the
`LICENSE.rst <https://github.com/gammapy/gammapy/blob/master/LICENSE.rst>`_ file.

.. image:: https://anaconda.org/conda-forge/gammapy/badges/license.svg
    :target: TBD
    :alt: Licence
