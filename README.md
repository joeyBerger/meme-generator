# Meme Generator

## Project Overview
This python app generates memes from locally stored files (.txt, .pdf, .docx, .csv, .jpg) in a local and browser environment.

## Install Instructions
Download this project and cd into the root directory.

To generate a meme locally, run ```python3 main.py``` and a local image and stored text will be used to generate a random dog meme with quote. The local image picked will be one of four stored files and the random quote will be pulled from a number of different formats: .pdf, .docx, .txt and .csv. By supplying parameters to the command line, a user can generate a custom meme.

In addition to running locally, this app can be interacted within a browser when launched as a backend server. Using Flask, a random meme can be generated in a browser (defaulting to localhost:5000) or a user can create their own meme by supplying an image url, quote and author.

### Python Toolsets

This python application demonstrates the following toolsets:
* CLI tools using argparse
* Use of subprocesses
* Use of OOP by way of inheritance, abstraction, encapsulation and class methods
* Modules and use of external libraries
* Reading of various file types for extraction of data
* GET and POST requests using Flask


### Interacting with the command line

Once the project is installed, run ```python3 main.py``` to generate a local meme with a random picture with random quote.

Accessible parameters are:
* ```--body``` - the body of the quote.
* ```--author``` - the author of the quote.
* ```--path``` - the path to the user defined image file

All generated memes using ```python3 main.py``` are outputted to the ```tmp``` directory at in the root of the project folder.

## Interacting with a browser

To run the backend server, run ```python3 app.py```. HTML will be served at localhost:5000. The 'Random' button will generate a random meme, wheras the 'Creator' button will serve options for generating one's one meme. If the file url is invalid, a message will be displayed to the user ('Please enter a valid URL image.'). 

Examples of usable links are:
```https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg```
```https://static01.nyt.com/images/2019/06/17/science/17DOGS/17DOGS-superJumbo.jpg?quality=90&auto=webp```

## Module Responsibilities

### app.py
Uses Flask framework to serve html, and receive requests.

### main.py
Generates meme locally based on user defined parameters.

### MemeGenerator.py
Generates meme based on supplied image, body and author.

### quote_model
Holds body and author information for use in creating meme.

### ingestor.py
Given a path, searches available ingestors based on given path file extension.

### ingestor_interface.py
Abstact method to be realized by various file type ingestors.

### csv_ingestor.py
Ingests .csv filetypes and exports found QuoteModel instances.

### docx_ingestor.py
Ingests .docx filetypes and exports found QuoteModel instances.

### pdf_ingestor.py
Ingests .pdf filetypes and exports found QuoteModel instances.

### txt_ingestor.py
Ingests .txt filetypes and exports found QuoteModel instances.