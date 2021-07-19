# CriCom
Live cricket commentary bot that reduced the data consumption rate by 100 times in comparison to live coverage telecast. Used Selenium for dynamic web scraping and PyQt5 for GUI.

# Usage

run the CriCom.py file 

```python
python CriCom.py
```

To start a coverage of live match going on, write
```
teama vs teamb
```
Use names mentioned on - [ESPN live](https://www.espncricinfo.com/live-cricket-score)

Ex. india vs sri lanka

![image](https://user-images.githubusercontent.com/59113057/126100222-042fb062-45b6-4e0e-b7e8-3dd1ec9fdbf8.png)



The bot will start the coverage till application is closed. It gives commentary over each delivery. Match should be shown as live on ESPN live, otherwise it will show 'match not live yet'.



# Features
* simple to use UI.
* Consumes very less data.
* Natural bot voice and crowd sounds to add to the feel.
* Updated live scores.

# Note
* Install dependencies using requirements.txt
```python
pip install -r requirements.txt
```
* Replace chromedriver.exe to match your Google chrome current version.
