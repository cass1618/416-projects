Cassandra Copp

CS 416P Assignment 2

### Modem

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
cd modem
python3 modem.py
```

The program will print the secret message and save it to message.txt.

### What I Did

1. load wave file and store the sample rate and samples
2. normalized samples by converting to float and divide by maximum possible value
3. computed reference tones for space frequency and mark frequency
4. compared each tone to the reference tones to determine if it's 1 or 0
5. iterated over each 8N1 frame and calculated the value of the character
6. converted ASCII values to characters and added to the string
7. tested this out for test1.wav and test2.wav and got the correct answers
8. decoded the given message and wrote to text file

### How It Went

I feel like this assignment was fairly straigtforward. The main thing I had difficulty with was figuring out how to use the bitwise operators in python. I have really enjoyed learning about how sounds can be analyzed and represented mathematically.
