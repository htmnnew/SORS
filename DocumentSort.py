import os
import shutil
import sys
import PictureLabels
from PictureSort import PictureSort

#Module to create the folders based on the the file type
#returns the updated directory of the folder
def createFolder(newDirectory, folderName):
    newDir = newDirectory + '\\' + folderName
    try:
        if not os.path.exists(newDir):
            os.makedirs(newDir)
    except OSError:
        print ('Error')
    return newDir

#Takes a picture, processes it and stores in correct folder
#This codes sends to the PictureLabels file to sort the pictures
def Pic_Control_Unit(original_path, path_to_store):
    #Inputs directory of the picture file and runs Picture Label Script
    picture_label_array = PictureLabels.detect_labels(original_path)
    #Input directory of the picture file and runs Picture Sort Script
    PictureSort(original_path, path_to_store, picture_label_array)

#Takes a picture, processes it and stores in correct folder
def Doc_Control_Unit(doc, original_path, path_to_store):
    #define the folder to be sotred in
    newDir = path_to_store + '\\' + 'Documents'
    try:
        if not os.path.exists(newDir):
            os.makedirs(newDir)
    except OSError:
        print ('Error')
    destination = newDir

  #Sort the type of Doc file
    if doc.endswith(".txt"):
        newDirTxt = destination + '\\' + 'Text'
        #creates new Folder for Text Documents if it is not created
        try:
            if not os.path.exists(newDirTxt):
                os.makedirs(newDirTxt)
        except OSError:
            print ('Error')
        destination = newDirTxt
        #copy the files into the new destination
        shutil.move(original_path + '\\' + doc,destination)
        os.System("Close cmd")

    elif doc.endswith(".doc") or doc.endswith(".docx"):
        newDirDoc = destination + '\\' + 'Word Documents'
        #creates new Folder for Word Documents if it is not created
        try:
            if not os.path.exists(newDirDoc):
                os.makedirs(newDirDoc)
        except OSError:
            print ('Error')
        destination = newDirDoc
        #copy the files into the new destination
        shutil.move(original_path + '\\' + doc, destination)

    elif doc.endswith(".ppt") or doc.endswith(".pptx"):
        newDirPpt = destination + '\\' + 'Power Points'
        #creates new Folder for PowerPoint Documents if it is not created
        try:
            if not os.path.exists(newDirPpt):
                os.makedirs(newDirPpt)
        except OSError:
            print ('Error')
        destination = newDirPpt
        #copy the files into the new destination
        shutil.move(original_path + '\\' + doc, destination)

    elif doc.endswith(".xlsx") or doc.endswith("xls"):
        newDirXls = destination + '\\' + 'Excel Spreadsheets'
        # creates new Folder for Excel Documents if it is not created
        try:
            if not os.path.exists(newDirXls):
                os.makedirs(newDirXls)
        except OSError:
            print ('Error')
        destination = newDirXls
        #copy the files into the new destination
        shutil.move(original_path + '\\' + doc, destination)
    else:
        destination = createFolder(destination, "Misc")
        shutil.move(original_path + '\\' + doc, destination)


#Takes a picture, processes it and stores in correct folder
def Music_Control_Unit(music, original_path, path_to_store):
    #define the folder to be sotred in
    newDir = path_to_store + '\\' + 'Music'
    # creates new Folder for PowerPoint Documents if it is not created
    try:
        if not os.path.exists(newDir):
            os.makedirs(newDir)
    except OSError:
        print ('Error')
    destination = newDir
    #Sort the type of music file
    if music.endswith(".wav"):
          newDirWave = destination + '\\' + 'Wave'
          # creates new Folder for PowerPoint Documents if it is not created
          try:
              if not os.path.exists(newDirWave):
                  os.makedirs(newDirWave)
          except OSError:
              print ('Error')
          destination = newDirWave
          #copy the files into the new destination
          shutil.move(original_path + '\\' + music, destination)

    elif music.endswith(".mp3"):
          newDirMp3 = destination + '\\' + 'Mp3'
          # creates new Folder for PowerPoint Documents if it is not created
          try:
              if not os.path.exists(newDirMp3):
                  os.makedirs(newDirMp3)
          except OSError:
              print ('Error')
          destination = newDirMp3
          #copy the files into the new destination
          shutil.move(original_path + '\\' + music, destination)

#move these files into the "Other folder"
def Other_Control_Unit(other, original_path, path_to_store):
    #define the folder to be sotred in
    destination = path_to_store + "/Other"
    #check the directory
    if not os.path.exists(destination):
      #oldmask = os.umask(000)
      os.makedirs(destination, 0o777)
      #os.chmod(destination,0o666)
    else:
      print("-Coping into " + destination)

    #copy the files into the new destination
    shutil.move(original_path + "\\" + other, destination)
    return True

############################################################################

#This gets the directory of the selected unsorted file and runs through each
#file and sends them to there respected sorter.
def fileSplitter(directory):
    source_path = directory
    basename = os.path.basename(source_path)
    destin_path = os.path.dirname(source_path) + '/' + 'Sorted'

    createFolder(os.path.dirname(source_path),'Sorted')

    try:
        if not os.path.exists(source_path):
            os.makedirs(destin_path)
    except OSError:
        print ('Error')
    #temporarily defining destination path static
    destination = destin_path
    #Iretare Through all the files in directory
    for filename in os.listdir(source_path):
        #Documents
      if filename.endswith(".txt") or filename.endswith(".doc") or \
              filename.endswith(".pptx") or filename.endswith(".ppt") or \
              filename.endswith(".xlsx") or filename.endswith(".docx") or \
              filename.endswith(".pdf" or filename.endswith(".PDF")):
          Doc_Control_Unit(filename, source_path, destination)

      #Music
      elif filename.endswith(".mp3") or filename.endswith(".wav"):
          Music_Control_Unit(filename,source_path, destination)

      #Pictures    
      elif filename.endswith(".jpeg") or filename.endswith(".jpg") or \
              filename.endswith(".png") or filename.endswith(".tif"):
          Pic_Control_Unit(source_path + '/' + filename, destination)

      #Unrecognized Types    
      else:
          Other_Control_Unit(filename, source_path, destination)

    #This deletes the old unsorted folder by checking if there is any files left
    #Also opens a file dialog of the updated sorted folder
    if not os.listdir(source_path):
        os.rmdir(source_path)
        os.startfile(destin_path)
        sys.exit()

    print("Completed. The sorted path is: ", destin_path)