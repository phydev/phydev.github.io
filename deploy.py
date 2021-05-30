import os

def generateIndex(folder, output, extensions = ['html']):

    articles = []
    for file in os.listdir('./'+folder):
        if any(x in file for x in extensions):
            articles.append(file)


    metadata = {}
    pattern = {}
    article_number = 0
    for n, article in enumerate(articles):
        link="/"+folder+"/"+article
        with open("."+link) as file:
            line = file.readline()
            metadata[n] = dict(eval(line[4:-4]))

        metadata[n]['link'] = link
        
        if metadata[n]['status'] == 'show':
            pattern[n][metadata[n]["order"]] = "<p><a href='"+metadata[n]['link']+"'> "+ metadata[n]["order"]+ " - " + metadata[n]["title"]+" </a></p>"
            article_number +=1

    pattern = sorted(pattern.items(), key=lambda x: x[1], reverse=False)
    with open(output, "w") as file:
        for line in range(article_number):
            file.write(pattern[line])


generateIndex(folder="articles", output="articles.html")
generateIndex(folder="articles/biocomp", output="./articles/biocomp/contents.html")


