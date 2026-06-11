Cassandra Copp

CS 416P Assignment 4

### Synth

### Instructions to Run the Program

#### 1. [Have python installed](https://www.python.org/downloads/)

#### 2. [Create a virtual environment](https://docs.python.org/3/library/venv.html)

```bash
cd code/synth
```

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

#### 4. Open MIDI setup and enable IAC Driver

#### 5. Use a virtual keyboard such as [midiano.com](https://app.midiano.com/)

#### 6. Set the MDID device Output to IAC Driver Bus 1

#### 7. Start the program

```bash
python3 synth.py
```

#### 8. Play any key on the virutal MIDI keyboard

#### 9. Sawtooth wave will be played and will also be displayed in text

### What I Did

1. used mido to open the driver and recieve the signal from a midi keyboard including note on and note off and the velocity
2. created a sawtooth wave that takes a midi value and converts to desired frequency for the wave
3. used a threading lock and stored state variables to keep track of note already being played and next input
4. created key off and on events setting desired frequency and starting or releasing the phase and stage
5. added values to the AR envelope for attack and sustain
6. used audio callback to retrieve next block of samples
7. used mido to wait for input from IAC driver
8. used OutputStream to play the audio and output note names and frequency to the console

### How It Went

This project was not quite as difficult as I was expecting it to be. I have had a lot going on so I haven't been able to work on it as much as I'd like but I am planning on continuing after class ends. It was interesting using the liistener and figuring out how to use multiple threads to account for the possibility of multiple notes played.
