# beer-finder

Beer Finder is an application that will help you find great beer in your local area.

## Installation

Create and activate a new Anaconda virtual environment:

```bash
conda create -n beer-env python=3.7 # (first time only)
conda activate beer-env 
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

The Beer Finder application uses Selenium to open Chrome and then navigate to the BeerMenus site and it uses Beautiful Soup to scrape the data.   In order to use Selenium on Chrome, you will need to install Chromedriver.  For more information on how to install Chromedriver, see this link https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/chromedriver.md#installation.

Once Chromedriver is installed, you will need to set the variable CHROMEDRIVER_PATH = ("Insert the path to where Chromedriver is installed on your computer).

If you want to run the application through Python only, type the command below into your command line and follow the prompt to type in your zip_code.  

```bash
python app/beer_finder.py
```
The program will launch Chrome via Selenium and begin scraping data based on your zip code input

If you want to run it on a web app, type the command below into your command line

```bash
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # first time, to set the env var
flask run # subsequent times
```

Visit http://localhost:5000/zip_form and input your zip code.  The program takes about a minute to finish running.  Once it is completed, you will taken to http://localhost:5000/beer_ranking where the results will show in a table

```
