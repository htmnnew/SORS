import os
import shutil


class PictureSort:
    '''These are "global" array that contain keywords tha will categorize
    the the picture into the correct folder. the accuracy is provided by google vision'''
    person = ['Man', 'Women', 'Child', 'Teenager', 'Boy',
              'Girl', 'Person', 'Human', 'Dad', 'Mom',
              'Father', 'Mother', 'Grandmother', 'Face','Facial Expression',
              'Nose', 'Chin', 'Emotion', 'Music Artist','Photograph',
              'Hairstyle', 'Person', 'Eyewear', 'Human behavior','Moustache',
              'Facial hair', 'Skin', 'Hair', 'Homosapien', 'Politician'
              'Business man','Forehead','Black hair','Fictional character']

    animal = ['Pet', 'Dog', 'Cat', 'Tiger', 'Animal',
              'Monkey', 'Fish', 'Cow', 'Lion', 'Wild animal',
              'Bird','Beak', 'Livestock', 'Grass', 'Mammal',
              'Snout', 'Carnivore', 'Wildlife']

    abstract = ['Handwriting', 'Text', 'Writing', 'Font', 'Paper',
                'Homework', 'Graffiti', 'Document', 'Calligraphy', 'Advertising',
                'Banner', 'Signage', 'Billboard', 'Line', 'Logo',
                'Brand', 'Broduct', 'Heat','Lighting accessory','Red', 'Orange', 'Yellow','Pattern']

    place = ['Historic site', 'Ancient history', 'Tourist attraction', 'Ruins',
             'History', 'Statue', 'Landmark', 'Monument',
             'Sculpture', 'Tourism', 'Hill',
             'Mountain', 'Building', 'Sky', 'Water','Biome']

    '''Array within the category arrays as elements to help with recursive method'''
    categories = [person, animal, abstract, place, 'person', 'animal', 'abstract', 'place']

    '''olddirectory'''
    old_directory = ''

    '''newdirectory'''
    new_directory = ''

    '''Constructor'''
    def __init__(self, old, new, array_labels):
        self.old_directory += old
        self.new_directory += new
        self.__isCategory(array_labels, 0)

    '''Recursive to find the category in which the picture belongs'''
    def __isCategory(self, labels, category):
        print(category)
        print(labels)
        if (set(labels) & set(self.categories[category])):
            print('if')
            print(category)
            self.__createFolder(self.new_directory, self.categories[category + 4])
            #loops to the others in the categories to figure out which element
            #it belongs to
        elif (category < 4):
            return self.__isCategory(labels, category + 1)
        else:
            print(self.old_directory)
            print("error alot")

    '''Creates the folder in which the category and the directory are going to
    be placed'''
    def __createFolder(self, dirr, folderName):
        newDirr = dirr + "/" + folderName
        self.directory = newDirr
        try:
            if not os.path.exists(newDirr):
                os.makedirs(newDirr)
        except OSError:
            print ('test')

        self.__redirect( newDirr)

    '''Moves the original directory of the selected files and moves it to the new directory'''
    def __redirect(self, new):
        shutil.move(self.old_directory,new)