import os

extensions = ['html']
articles = []
for file in os.listdir('articles'):
    if any(x in file for x in extensions):
        articles.append(file)


metadata = {}
pattern = ''
for n, article in enumerate(articles):
    link="./articles/"+article
    with open(link) as file:
        line = file.readline()
        metadata[n] = dict(eval(line[4:-4]))
    metadata[n]['link'] = link

    if metadata[n]['status'] != 'hidden':
        pattern += "<p><a href='"+metadata[n]['link']+"'> "+ metadata[n]['title_en']+" </a></p> \n"


with open("articles.html", "w") as file:
    file.write(pattern)

