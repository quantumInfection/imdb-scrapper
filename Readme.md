# README

## There are total of 3 .py files
#### 1) main.py (main handler)
#### 2) section_1.py (Data collection).
#### 3) section_2.py (Data analysis).

## Output:
### Section 1:
#### This process takes time and outputs a movies_data.csv file.

### Section 2:
#### This process uses `movies_data.csv` file as an input and generate two graphs and opens it in a browser. And outputs an average of all Genres in console.


## How to Run
##### Make sure to have python 3 installed for this task
#### 1) Setup virtual environment for python.
```
$ virtualenv -p python3.7 env
```
#### 2) Activate virtual environment.
```
$ source env/bin/activate
```
#### 3) Install requirements using requirements.txt
```
$ pip install -r requirements.txt
```
#### 4) Run the program using following command

```
$ python main.py
```

## Assumptions
#### 1) This code is very short lived because once imdb decides to change the front end code then this code won't work.
#### 2) Some of the movies didn't have correct data so I had to add some default fall backs to keep the code from crashing.
#### 3) Data of all movies will require a lot of network time so I took the liberty of adding a count to limit the number of movies data.
#### 4) I took this assignment as an opportunity to design the whole system as well and that's why section 1 and section 2 can work independently.

