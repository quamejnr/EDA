# EDA
A project simulating an event driven architecture

This is a mini project simulating an event-driven architecture using the observer pattern.
There are producers, brokers and services(aka consumers). As at the moment, it's just one event that is being generated.
Anytime there is an event, a producer then creates an event object, notifies the broker of this event supplying the broker with the event object
which contains all the data pecuiliar to that event. The services who are listening to that event type then consumes the event.

## Running the program
You can run this project on your device by cloning the project and running the main.py file in the project.
1. `git clone https://github.com/quamejnr/EDA.git`
2. Run `python3 main.py`
