# SORS
Software for organizing a directory with any type of files using Google Vision AI.
SORS or Software for Organizing Random Stuff is a python program that sorts a given folder with any type of files in it.
SORS uses Google Vision AI for sorting picture files. 
You have the ability to specify what types of pictures you want to be sorted in PictureSorrt.py file. All labels are from Google Vision.
Make sure for the new labels the first letters of first words are capitalized.

You can create a google cloud account here: https://cloud.google.com
After creating an account save the JSON file with private key in your device and add that path into the PictureLabels.py
The link to create and download the private key: https://cloud.google.com/vision/docs/libraries
Make sure billing is enabled in your google cloud account. 

To install Google Vision Client Libraries, follow the step in: https://cloud.google.com/vision/docs/libraries
Or for python you can just run this command: pip install --upgrade google-cloud-vision

To start the program simple run the UserInterface.py file in any IDE.
