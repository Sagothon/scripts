import os, re, glob


list_of_files = glob.glob('./Szkielet/*.cfg')  # list of cfg files  trzeba zmieniac ukosnik w zaleznowsci od systemu

match_string = "resolv.host.1.name" #searched phrase


for file_name in list_of_files: #opens files from list and reads content
    file = open(file_name, 'r')
    content = file.readlines()
    print(file)
    file.close()

    for line in content:    #search content for phrase
        m = re.search(match_string, line)
        if m:               #change file name if phrase match
            line = line.rstrip('\n')
            new_file_name = line[19:]+'.cfg'
            new_file_name = re.sub('[<>]','_', new_file_name)
            print(new_file_name)
            file.close()
            os.rename(file_name, new_file_name)


