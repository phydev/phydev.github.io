import os

def generateIndex(folder, output, extensions = ['html']):

    articles = []
    for file in os.listdir('./'+folder):
        if any(x in file for x in extensions):
            articles.append(file)


    metadata = {}
    pattern = ''
    for n, article in enumerate(articles):
        link="/"+folder+"/"+article
        with open("."+link) as file:
            line = file.readline()
            metadata[n] = dict(eval(line[4:-4]))
        metadata[n]['link'] = link

        if metadata[n]['status'] == 'show':
            pattern += "<p><a href='"+metadata[n]['link']+"'> "+ metadata[n]['title_en']+" </a></p> \n"


    with open(output, "w") as file:
        file.write(pattern)


generateIndex(folder="articles", output="articles.html")
generateIndex(folder="articles/biocomp", output="./articles/biocomp/contents.html")


