# Environment Setup
I don't know how much experience you have with python so don't take it personally if some of this is overly pedantic. This is all assuming you are running on MacOS.
#### python3
Ensure you python3 is up to date. See this [link](https://docs.python-guide.org/starting/install3/osx/).
#### pip
first make sure you have [pip](https://pip.pypa.io/en/stable/installing/) installed.
#### virtualenv
A virtual environment is used to ensure that all the various [versions of the] code libraries you use in this project don't conflict with the code libraries in other projects. First install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).
#### virtualenvwrapper
This just makes virtualenv much easier to use. First run
```
pip install virtualenvwrapper
```
Next, you need to edit your `~/.bash_profile`. First check if you have one already by running
```
ls ~/.bash_profile
```
If the response just lists the file, then you have it. If not, you'll get some response saying "No such file or directory". In that case you'll need to create it by running the line below. **Do not run this line if you already have a `~/.bash_profile` file** or you will overwrite it with a blank file and there's no way to retrieve the previous file.
```
# if the previous response contained "No such file or directory", run:
touch ~/.bash_profile
```
Next, edit your `~/.bash_profile` by running
```
nano ~/.bash_profile
```
Scroll to the bottom using the arrow keys and then copy paste the following in:
```
# Setup for using virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'

source /usr/local/bin/virtualenvwrapper.sh
```
Save the file by pressing CTRL-o (that's the letter "oh"), then press Enter, and then exit with CTRL-x.

Finally run
```
source ~/.bash_profile
```
in order to make those changes go into effect.
#### mkvirtualenv
Now you can make the virtual environment necessary for running the code. Make sure you're in the `sjwtrader` directory in your terminal. Run
```
mkvirtualenv sjwtrader
```
Your command prompt will now be prefixed by `(sjwtrader)`. To exit the virtual environment, you would run `deactivate`. To reactivate the environment, run `workon sjwtrader`. Make sure you are in the `sjwtrader` virtualenv before moving on.
#### Install requirements.txt
The file `requirements.txt` contains all of the python libraries necessary for running this code, written in a format that pip can understand. Simply run
```
pip install -r requirements.txt
```
and wait for all the required libraries to install into the virtualenv.
# Run the Jupyter notebook
Jupyter is an awesome project that essentially allows you to write documents that are themselves programs. I've created a Jupyter notebook that generates a prelimenary report on my reasoning re: this trading algorithm and generates graphs to give us some visual intuition about whether or not my hypothese is true. To run the notebook, run
```
jupyter notebook
```
This should pop you to your browser (or if not click the link displayed in the terminal). From that page, click on `sjw_controversy_and_corporate_impunity_preliminary_report.ipynb` to see the report.
