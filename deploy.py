import os

def generateIndex(folder, output, extensions = ['html']):

    articles = []
    for file in os.listdir('./'+folder):
        if any(x in file for x in extensions):
            articles.append(file)


    metadata = {}
    pattern = {}
    n = 0
    for n, article in enumerate(articles):
        link="/"+folder+"/"+article
        with open("."+link) as file:
            line = file.readline()
            metadata[n] = dict(eval(line[4:-4]))
        metadata[n]['link'] = link

        if metadata[n]['status'] == 'show':
            pattern[metadata[n]["order"]] = "<p><a href='"+metadata[n]['link']+"'> "+ metadata[n]["order"] + metadata[n]["title"]+" </a></p> \n"
            n = n+1

    with open(output, "w") as file:
        for i in range(n):
            file.write(pattern[str(n)])


generateIndex(folder="articles", output="articles.html")
generateIndex(folder="articles/biocomp", output="./articles/biocomp/contents.html")


