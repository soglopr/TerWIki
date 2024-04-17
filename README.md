# TerWiki
Wikipedia right in your terminal. 
<!--Badges-->
![Static Badge](https://img.shields.io/badge/TerWiki-Soglopr-Soglopr)
![GitHub](https://img.shields.io/github/license/TerWiki/Soglopr)

![Logotype](./screenshots/terwiki.jpg)
<!-- About the program -->
## About the program

Using the program, you can search for Wikipedia articles directly from the terminal. After you have entered the topic you are interested in into the search, the code will process and display brief information on it.

<!--Installation-->
## Installation (Linux)

1. Cloning the repository

```git clone https://github.com/soglopr/TerWiki.git```

2. Go to the TerWiki directory

```cd TerWiki```

3. Creating a virtual environment

```python3 -m venv terwiki```

4. Activating the virtual environment

```source terwiki/bin/activate```

5. Installing dependencies

```pip3 install -r requirements.txt```

6. Running the script

```python3 main.py```
<!-- Commands -->
## Commands

Help: ```--help``` or ```-h```

Exit: ```--exit``` or ```-e```
<!-- Switch language -->
## Switch language

There is support for Russian and English. In the ***config.py*** file in the first line you can change the value (***ru*** or ***en***)

```python
lang = "en" #"ru"
```
<!--Dependencies-->
## Dependencies
Python version 3.7 or higher, PIP 22.0.2 or higher.
