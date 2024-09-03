import os #to read through folder
import xml.etree.ElementTree as ET #for parsing xml files like trees
from PIL import Image, ImageDraw #for drawing new pngs

#opens folder with all the data
data_folder = os.listdir('Programming-Assignment-Data') 
for xml in data_folder:
    if ".xml" in xml:
        #xml files found with associated png
        xml_file = 'Programming-Assignment-Data/' + xml
        current_file = xml.strip('.xml')
        png_image = Image.open('Programming-Assignment-Data/' + current_file + '.png')
        #draw the png image and prepare it to add yellow boxes
        draw = ImageDraw.Draw(png_image)
        #creates a tree to be parsed
        tree = ET.parse(xml_file)
        root = tree.getroot()

        #checks if we have reached a leaf node
        def is_leaf(node):
            return len(node) == 0

        #recursively will go down nodes until a leaf node is reached
        def check_node(node, draw):
            #if a leaf, run this process
            if is_leaf(node):
                #gets the bounds of the leaf to draw a rectangle around it
                bounds = node.get('bounds')
                bounds = bounds.strip('[]').replace('][', ',').split(',')
                bounds = [int(b) for b in bounds]
                draw.rectangle(bounds, outline='yellow', width=5)

            #recursion process through all nodes in tree
            for child in node:
                check_node(child, draw)

        #this will start the recursion process of checking nodes
        for child in root:
            check_node(child, draw)

        #save the new image in specific folder
        png_image.save('Highlighted-png/' + current_file + '.highlighted.png')

        print("Image processing finished. You can find the results in Highlighted-Png folder.")

    #not an xml file
    else:
        continue
