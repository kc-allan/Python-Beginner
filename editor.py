import os, re

directory = r"C:\Users\laptop\Desktop\test"

for filename in os.listdir(directory):
    f=os.path.join(directory,filename)
    if os.path.isfile(f) and filename!="editor.py":
        result=filename.replace('_',' ')
        final=re.split('\.',result)
        words = []
        for i in final:
            if i!='mp3':
                i=i.title()
                words.append(i)
        words.append('.mp3')
    text=(''.join(words))
    text=text.split(' ')
    for i in text:
        if i=='Y2MateCom':
            text.remove('Y2MateCom')
        if text[0]=='-':
            text.remove('-')

    output=(' '.join(text))
    try:
        os.rename(filename,output)
    except FileExistsError:
        pass