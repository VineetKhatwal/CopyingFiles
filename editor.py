'''
************************************************************************************************************************
    AUTHOR: VINEET KHATWAL
    ======================

    DATE: OCT 11 2020
    ======================
************************************************************************************************************************

shutil.copy() :
shutil.copy() method in Python copies the content of source directory to destination directory.
Syntax : shutil.copy(source, destination, *, follow_symlinks = True)

shutil.copyfileobj():
shutil.copyfileobj()  method in Python is used to copy the contents of a file-like object to another file-like object.
Syntax : shutil.copyfileobj(fsrc, fdst[, length])

Using Thread:
Python standard library provides threading, which provides a clean interface to work with threads.
x = threading.Thread(target=thread_function, args=(1,)).start()
The start() method starts a thread by calling the run method.

Using Process:
In Python, the multiprocessing module includes a very simple and intuitive API for dividing work between multiple processes.
x = multiprocessing.Process(target=process_function, args=(1,)).start()
The start() method starts a thread by calling the run method.

************************************************************************************************************************
'''
import sys
import shutil
import os
import glob
from datetime import datetime
from threading import Thread
from multiprocessing import Process

class CopyFiles:

    # -----------------------------------------------------------------------------------------------------------------------
    #                                               INITIALISING THE CONSTRUCTOR
    # -----------------------------------------------------------------------------------------------------------------------
    def __init__(self, sourceDirectory, destinationDirectory, file_type):
        self.sourceDirectory = sourceDirectory
        self.destinationDirectory = destinationDirectory
        self.file_type = file_type
        self.buffer_size = 16000

    # -----------------------------------------------------------------------------------------------------------------------
    #                                             USING shutil.copy to copy files
    # -----------------------------------------------------------------------------------------------------------------------
    def UsingShutilCopy(self):
        try:
            for file in os.listdir(self.sourceDirectory):
                if file.endswith(self.file_type):
                    shutil.copy(self.sourceDirectory + '/' +
                                file, self.destinationDirectory)

        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)

    # -----------------------------------------------------------------------------------------------------------------------
    #                                             USING shutil.copyfileobj to copy files
    # -----------------------------------------------------------------------------------------------------------------------
    def UsingShutilCopyFileObj(self):
        try:
            for file in os.listdir(self.sourceDirectory):
                if file.endswith(self.file_type):
                    with open(self.sourceDirectory + '/' + file, 'rb') as fsrc:
                        with open(self.destinationDirectory + '/' + file, 'wb') as fdest:
                            shutil.copyfileobj(fsrc, fdest, self.buffer_size)

        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)

    # -----------------------------------------------------------------------------------------------------------------------
    #                                             USING Thread to copy files
    # -----------------------------------------------------------------------------------------------------------------------
    def UsingThread(self):
        for file in os.listdir(self.sourceDirectory):
            if file.endswith(self.file_type):
                Thread(target=shutil.copy, args=[
                       self.sourceDirectory + '/' + file, self.destinationDirectory + '/' + file]).start()

    # -----------------------------------------------------------------------------------------------------------------------
    #                                             USING Process to copy files
    # -----------------------------------------------------------------------------------------------------------------------
    def UsingProcess(self):
        for file in os.listdir(self.sourceDirectory):
            if file.endswith(self.file_type):
                Process(target=shutil.copy, args=[
                        self.sourceDirectory + '/' + file, self.destinationDirectory + '/' + file]).start()


# HELPER FUNCTION TO PRINT
def PrintTime(text, time):
    print("{:50}".format(text), ":", time)


# Getting the Source and Destination Directory
sourceDirectory = os.getcwd() + '/From'
destinationDirectory = os.getcwd() + '/To'

# Printing the Source and Destination Directory
print("{:20}".format('Source'), ":", sourceDirectory)
print("{:20}".format('Destiation'), ":", destinationDirectory)
print()

# Defining the name of the file to be copied
# ***************                               CONDITION 1                      ***************
# We can give the complete name of the file to be copied like : 'editor.py'
# In this case it will copy the file editor.py from Source to Destination


# ***************                               CONDITION 2                      ***************
# We can give the name of the file it ends with to be copied like : '.py'
# In this case it will copy all the files which has '.py' in the name from Source to Destination

file_type = ".py"

# Creating instance of the file
shutilCopy = CopyFiles(sourceDirectory, destinationDirectory, file_type)
shutilCopyFileObj = CopyFiles(sourceDirectory, destinationDirectory, file_type)
shutilThread = CopyFiles(sourceDirectory, destinationDirectory, file_type)
shutilProcess = CopyFiles(sourceDirectory, destinationDirectory, file_type)

# List to store the results
TimeTaken = []

# Capturing ghe time for shutil.copy
t1Start = datetime.now()
shutilCopy.UsingShutilCopy()
t1End = datetime.now() - t1Start

# Capturing ghe time for shutil.copyfileobj
t2Start = datetime.now()
shutilCopyFileObj.UsingShutilCopyFileObj()
t2End = datetime.now() - t2Start

# Capturing ghe time for Thread
t3Start = datetime.now()
shutilThread.UsingThread()
t3End = datetime.now() - t3Start

# Capturing ghe time for Process
t4Start = datetime.now()
shutilProcess.UsingProcess()
t4End = datetime.now() - t4Start

# Calling th print function to Print the values
PrintTime('Time Taken by Copy Using Shutil Copy()', t1End)
PrintTime('Time Taken by Copy Using Shutil CopyObj()', t2End)
PrintTime('Time Taken by Copy Using Thread', t3End)
PrintTime('Time Taken by Copy Using Process', t4End)

# Adding the timings to the list
TimeTaken.append([t1End, "Shutil Copy()"])
TimeTaken.append([t2End, "Shutil CopyObj()"])
TimeTaken.append([t3End, "Thread"])
TimeTaken.append([t4End, "Process"])
print()

# Displaying the results
TimeTaken.sort()
print("The best performing copy techniques:")
for i in range(len(TimeTaken)):
    print(i + 1, " - ", TimeTaken[i][1])
