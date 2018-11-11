# MLA Qualifying Offer
### What does it do?
    This app calculates an qualifying offer for a departing free agent player. The offer value is the average of the 125 highest salaries from the past season, which can be found [here](https://questionnaire-148920.appspot.com/swe/data.html).
    It also visualizes the salaries from the past season using Google charts.
### Online Demo:
    https://mla-offer-api-heroku.herokuapp.com/
### Run The Code Locally:
#### Install:
    git clone https://github.com/chanyoonzhu/baseball-qualifying-offer.git
    cd baseball-qualifying-offer
    sudo pip install -r requirements.txt
#### Run:
    python app.py
#### Test:
    python data_analysis/setup.py pytest
### References:
    [Deploying Flask to Heroku](https://www.youtube.com/watch?v=pmRT8QQLIqk)
    [Flask render_template()](https://stackoverflow.com/questions/10810206/flask-render-template-returning-nameerror-name-app-is-not-defined)

    