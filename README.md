# Austin Animal Center - *Plotly Dash Summer App Challenge*  

## Introduction  

The [AAC Insights]((https://austinanimalcenter.herokuapp.com/)) dashboard was created 
with [Plotly Dash](https://dash.plotly.com/) and ***Won 1st Place*** in 
[Plotly's Summer Community App Challenge](https://community.plotly.com/t/dash-club-dispatch-7-profiling-dash-apps-summer-app-challenge-winners-show-tell-cheat-sheets-fall-challenge/67140#summer-community-app-challenge-winners-6). 
The Challenge As described by Adam at Plotly,

> We know people love building Dash apps. We also know people strive to make this world a better place. So we thought, 
> why not combine the two and make an exciting community app-building challenge?! Plotly would like to challenge the 
> community to build a Dash app that will support people working at animal shelters in understanding their data better 
> and allow for higher rates of animal adoption. 
> [[1]](https://community.plotly.com/t/summer-community-app-challenge/65099)

## Technologies
- Python 3.9
- Plotly Dash 2.7  
- HTML  
- CSS

## Getting Started

- Create and activate a virtual environment with pip or conda
- Fork `austinanimalcenter` repository
- Install Requirements
  - `$ pip install -r requirements.txt`
  - `$ conda install -c conda-forge --file requirements.txt`  
- Run `app.py` Output should show the dashboard running on a local server: `Dash is running on http://127.0.0.1:8050/` 
- Open `http://127.0.0.1:8050/` in browser to view the dashboard


## Data Sources  


Data sources used in this dashboard went above the requirements of the
[Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099) and used full
datasets from [data.austintexas.gov](https://data.austintexas.gov/).

- [Austin Animal Center Outcomes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)  
  Animal Center Outcomes from Oct, 1st 2013 to present. Outcomes represent the status of animals as they leave the Animal
  Center. All animals receive a unique Animal ID during intake. Annually over 90% of animals entering the center, are
  adopted, transferred to rescue or returned to their owners. The Outcomes data set reflects that Austin, TX. is the
  largest "No Kill" city in the country.

- [Austin Animal Center Intakes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm)  
  Animal Center Intakes from Oct, 1st 2013 to present. Intakes represent the status of animals as they arrive at the
  Animal Center. All animals receive a unique Animal ID during intake. Annually over 90% of animals entering the center,
  are adopted, transferred to rescue or returned to their owners.

- [Austin Animal Center Stray Map API](https://dev.socrata.com/foundry/data.austintexas.gov/kz4x-q9k5)  
  Map shows all stray cats and dogs that are currently listed in AAC's database for no longer than a week.
  Most will be located at AAC, but some will be held by citizens, which will be indicated on the "At AAC" column.
  Please [click here](checkhttp://www.austintexas.gov/department/lost-found-pet) for more information.


