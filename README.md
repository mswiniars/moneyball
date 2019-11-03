# Hands on Moneyball!

## Enviroment Setup
If you do not have any IDE for formating python scripts
I recommend to [download PyCharm Community IDE](https://www.jetbrains.com/pycharm/download/#section=windows).
I will be using this IDE during our courses.

1. Download the repository, you can do it by git(if installed)
    * Open command line in directory where you want to put the repository
    * Type ```git clone https://github.com/marcinswiniarski20/moneyball.git```
2. Setup Conda Enviroment
    * [Download Miniconda3](https://docs.conda.io/en/latest/miniconda.html) - minimal installer for conda
    * Once Miniconda have installed, open `Anaconda Prompt(Miniconda3)`, you should be able to find it by `win+search`
    * Create conda enviroment with python 3.6 and default name "ML" simply by: <br/>
    `conda create -n ML python=3.6` <br/>
    * Activate conda enviroment: <br/>
    `conda activate ML` <br/>
    * Install all required packages: <br/> 
        * Go to folder with the repository in that Anaconda Prompt console with the enviroment activated <br/>
        * Run `pip install -r requirements.txt` - "requirements.txt" file should be present in directory
3. Test if everything is configured well simply by: <br/>
``python test.py``


In case of any problems contact: marcinswiniarski20@gmail.com

Google Collab: https://colab.research.google.com/drive/1Ap2YRnYfMj3OJTafO82GqsiABCmtTPyg
