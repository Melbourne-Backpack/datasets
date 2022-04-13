# COLLECTING, SCRAPING, CLEANING, EDA, and UPLOAD DATA ON FIREBASE

About Dataset

### Context
Melbourne real estate near RMIT University.

### Content
This is a snapshot of a dataset created by Thu Tran.

It was scraped from publicly available results posted every week from AMelbourne Student Living [Dwell Village](https://www.dwellstudent.com.au/melbourne/#rooms),[Unilodge Carlton](https://www.unilodge.com.au/student-accommodation-melbourne/carlton?_ga=2.202010833.1533874551.1649827599-1331530598.1649827598), [UNILODGE VICTORIA](https://www.unilodge.com.au/student-accommodation-melbourne/vu?_ga=2.268096846.1533874551.1649827599-1331530598.1649827598). 



The dataset includes `title`, `price`, `image`, `name`, `address`, `link`, `transportation`, `bed`, `bath`, `latitude`, `longitude`, `altitude`

Notes on Specific Variables
+ `price`: Price in AUD
+ `bath`: Number of Bathrooms



### Acknowledgements
This is intended as a static (unchanging) snapshot of Melbourne Backpack. It was created in April 2022. Additionally, homes with no `price` have been removed.


## Repository Structure

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
|
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   │
│   │
│   └── cleaning.py  <- Scripts to perform basic cleaning 
│
|
│── web_app                <- Source code for web app.
│   │
│   ├── dash           <- Scripts to visualize data using Dash
│   │   └── app.py
│   │
│   ├── streamlit       <- Scripts to build preditive model using Streamlit -  an open-source Python library 
│     └── app.py
|
|── upload-json-file-to-firestore.py        <- Scripts to push .json data to the FireStore
|
|
│── .gitignore                <- plain text file contains files/directories to ignore

```
