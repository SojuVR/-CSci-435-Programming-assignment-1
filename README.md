# -CSci-435-Programming-assignment-1
This program takes an xml screenshot of an Android app and outputs the same screenshot with yellow boxes around leaf level components. It uses Pillow for image drawing and ElementTree to turn an xml file into a tree.

To run this code, download the content of this repository. Then, in powershell, go to the directory containing the folder CSci-435-Programming-assignment-1. From there, run "python Parser.py". The code will run and update you every time an image is processed. The processed images will be found in the folder Highlighted-Png.

If you want to try new xml and png files, add the xml file and associated png file (make sure they share the same name) to the folder Programming-Assignment-Data. It will be run along with the other files.

If you rerun a file, there is no need to get rid of the previous output png. It will be overwritten with your new attempt.

I chose to use python for this assignment and Pillow along with it because I am most familiar with this coding style, and Pillow I have used previously for png generation.
