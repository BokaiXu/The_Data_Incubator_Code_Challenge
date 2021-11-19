# Introduction:

### This is a demo for a Steam recommender system. I downloaded Steam game data using the Steam API. The game data includes ~120,000 game information like description, publiser, developer and type. Then I built a content-based recommender system using the game data and built a mini web-app. This web app was deployed to Heroku.

# How to use it

### https://game-rec.herokuapp.com/go?query=56456 In is website, type in the steam game id you have, and it will return the top 10 similar games.
![alt text](https://github.com/BokaiXu/GameRec/blob/master/demo.jpg?raw=true)

# Files:

### Jupyter Notebook: Obtain_Data.ipynb: The process of using Steam API to download meta data. Clean_Data.ipynb: The process of wrangling and cleaning the meta data. Content-based-rec-system.ipynb: The process of building the recommender system.

### dataset: The dataset used in the recommender system.

### templates: The template of the website for the recommender system.

### app.py: The front-end file of the recommender system.

### recommendation.py: The back-end of the recommender system.
