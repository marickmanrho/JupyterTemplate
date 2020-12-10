# JupyterTemplate
A nice Jupyter notebook template for scientific projects.

#### Features:
- Almost publication ready `pdf` output
- Easy interactive `html` exports
- `Latex` integration
- Citations from `Zotero`


#### Example pdf output


## Installation
After cloning the repository follow the next two steps.

### 1. Install prerequisites
#### apt-get
```
# Jupyter notebook
apt-get install notebook

# Jupyter extensions
python3 -m pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Zotero cite
python3 -m pip install cite2c
python3 -m cite2c.install

# Latex for pdf output
apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic

# nglview for MDAnalysis users
python3 -m pip install nglview
jupyter-nbextension enable nglview --py --sys-prefix
```

#### conda
```
# Jupyter notebook
conda install -c conda-forge notebook

# Jupyter extensions
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Zotero cite
python3 -m pip install cite2c
python3 -m cite2c.install

# Latex for pdf output
apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic

# nglview for MDAnalysis users
conda install nglview -c conda-forge
```

Note: for lower versions of `Ubuntu` or `macOS` one may need `texlive-generic-recommended` instead of `texlive-plain-generic`.

#### Windows
I havn't tested this, but it should work by installing `anaconda3`, use the `conda` and `pip` install commands as much as possible and install `MikTex` to obtain `Latex`. I also recommend installing `TeXstudio` for windows users.

### 2. Enable extensions
Open up the jupyter notebook by going to the `JupyterTemplate` folder and run

```
jupyter notebook
```

On top there are some tabs, one of which is the nbextensions tab. In there you can enable the following extensions
- Codefolding
- Equation auto numbering
- cite2c
- Python Markdown
- nglview (if installed)
- plotly (if installed)

## Generating output
To generate `html` output
```
jupyter nbconvert --to html --TemplateExporter.exclude_input=True [Example].ipynb
```

To generate `pdf` output
```
jupyter nbconvert --to latex --LatexExporter.template_file=./config/revtex_nocode.tplx [Example].ipynb
pdflatex [example].tex
```

For more details please consult the following tutorials:
1. [Ultimate jupyter notebook (for scientific use)](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook)
2. [Custom template for converting jupyter notebooks to latex](https://michaelgoerz.net/notes/custom-template-for-converting-jupyter-notebooks-to-latex.html)

## How it works
Upon calling `nbconvert` the script `jupyter_nbconvert_config.py` is run. This processes the bibliography and markdown elements of the notebook. It also sets the template to `revtex` and preprocesses the notebook for latex export.

## Links
- [Jupyter extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)
- [cite2c Zotero references](https://github.com/takluyver/cite2c)
- [Ultimate Jupyter notebook guide](http://blog.juliusschulz.de/blog/ultimate-ipython-notebook)
- [Custom latex template for notebooks](https://michaelgoerz.net/notes/custom-template-for-converting-jupyter-notebooks-to-latex.html)
- [Jupyter publication scripts (GitHub)](https://github.com/schlaicha/jupyter-publication-scripts)
