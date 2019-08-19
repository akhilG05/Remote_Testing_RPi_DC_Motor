# Open Source Virtual Instrumentation
# Remote Testing RPi: DC Motor

# Usage Instructions

1. Install the required packages. ```pip3 install -r requirements.txt```
2. ```source venv/bin/activate```
3. ```python3 manage.py makemigrations```
4. ```python3 manage.py migrate```
5. Install ```motion``` using ```sudo apt install motion```
6. Add your system user password in ```runcode/views.py : start_vid and stop_vid and accounts/signals.py```
7. Comment GPIO functions in ```accounts/signals.py``` when not on RPi


