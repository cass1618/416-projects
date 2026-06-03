Cassandra Copp

CS 416P Assignment 3

### Aleatoric

### Instructions to Run the Program

#### 1. [Have python installed](https://www.python.org/downloads/)

#### 2. [Create a virtual environment](https://docs.python.org/3/library/venv.html)

###### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

##### Windows:

```bash
python -m venv venv
venv\Scripts\activate.bat
```

#### 3. Install requirements `pip install -r requirements.txt`

#### 4.

```bash
cd code/aleatoric
python3 aleatoric.py
```

### What I Did

1. created a sawtooth wave to represent a specified note at given duration
2. used choice, sample, and randint to select random values
3. created a melody by adding 8 notes selected from chord if random gives < 0.8 or otherwise select from scale
4. generated a scale based on the major steps and the selected root note
5. combined all the sawtooth waves into one audio array

### How It Went

It went pretty well overall. I got confused about the different music theory terms even though I've studied classical music theory it's very different when thinking about it in terms of computer programming.
It was really interesting to look at it this way.
I enjoyed completing this project and learned a lot.
