# Image Resizer

The programm designed to change image resolution by a few simple ways.

# Setup

The program requires for working Python version 3 or higher. Before starting needs to install Pil(image processing modul) by using:

```
$ pip install -r requirements.txt
```

# How it work?

To view helper information on using the program, use the -h or --help: 
```
$ python3 image_resize.py -h
```
# Сommand-line arguments

  - -h - HELP - Show this help message and exit
  - -fp - FILEPATH - Image that user want to change
  - -s - SCALE - Scale multiplier
  - -w - WIDTH - New image width
  - -he - HEIGHT - New image height
  - -sp - SAVEPATH - Path to save resized image

Example of script launch on Windows, Python 3.5:

```
$ python3 image_resize.py -fp 1.jpg -s 2
```

Result:

```bush
Image 1__200x200.jpg was succesfully resized and save to C:\devman\12_image_resize
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)