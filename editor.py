import os, re

#create a test folder and add test mp3 files
#Add path to folder below
directory = r"C:\Users\laptop\Desktop\test"

#Checks if fils exist in the directory
for filename in os.listdir(directory):
    f=os.path.join(directory,filename)

    #Excludes the editor file from renaming
    if os.path.isfile(f) and filename!="editor.py":
        result=filename.replace('_',' ')
        final=re.split('\.',result)
        words = []

        #Get the split words and append to a new list
        for i in final:
            if i!='mp3':
                i=i.title()
                words.append(i)
        words.append('.mp3')

    #Rejoin the words
    text=(''.join(words))
    text=text.split(' ')

    #Remove common unecessary words from the file
    #In this case "y2mate.com"
    for i in text:
        if i=='Y2MateCom':
            text.remove('Y2MateCom')
        if text[0]=='-':
            text.remove('-')

    #Get the final filename and rename all the files in the directory
    output=(' '.join(text))
    try:
        os.rename(filename,output)
    except FileExistsError:
        pass
