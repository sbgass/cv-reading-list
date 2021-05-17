import os

header = 'Historic Computer Vision Papers'
preamble = '' 
repo_name = 'cv-reading-list' 
ignore_files = ["",""] #to do 
ignore_dirs = ["",""] 

#write readme document to this directory 
with open("Readme.md","w+") as f: #w+ overwrites the existing readme file 
    f.write(f'# {header}\n')
    f.write(f'{preamble}\n\n')
    #traverse the root directory, and list directories as dirs and files as files
    for root, subdirs, files in os.walk("."): 
        foldername = os.path.basename(root) 
        if '.git' in subdirs:
            subdirs.remove('.git') #remove this folder from the list of directories to iterate over 
        path = root.split(os.sep) #split string by os's separator
        indent = (len(path) - 1) * " "
        f.write(f'{indent}* {foldername}\n') if foldername != "." else None
        for file in files:
            if file == "makereadme.py" or file.upper() == "README.MD":
                continue
            year = file[:4] #get the first four digits as the year 
            title = os.path.splitext(file)[0][5:] #remove extension, then remove date
            url = f'https://github.com/sbgass/{repo_name}/{file}'.replace(" ", "%20")
            f.write(f'{indent} * [{title}]({url}) ({year})\n')