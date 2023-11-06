from datetime import datetime
import json

# TODO: sort entries by date
# we can use pandas.json_normalize(cv["experience"])
# to get a dataframe object and sort

# useful html tags
tab = "&nbsp &nbsp &nbsp &nbsp"
p = lambda x:"<p>"+x+"</p>" # paragraph
h1 = lambda x: "<h1>"+x+"</h1> " # first header
h2 = lambda x: "<h2>"+x+"</h2>" # second header
h3 = lambda x: "<h3>"+x+"</h3>"
bf = lambda x: "<b>"+x+"</b>" # bold
it = lambda x:"<i>"+x+"</i>" # italic
href = lambda link, text:"<a href='"+link+"'>" + text + "</a>"
invited = {"yes": "(Invited), ", "no": ""}
# formatting
n = "\n"
comma = ", "

class html:
    
    @staticmethod
    def print_header(f, personal):
        title = personal["name"] + " " + personal["surname"]
        header = """<!DOCTYPE html> \n
        <html lang="en">\n
        <head>\n
        <meta charset="UTF-8">\n
        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n
        <link rel="stylesheet" href="style.css">\n
        <title>""" + title + """</title>\n
        </head>\n
        <body>
        <h1> Résumé </h1>"""
        f.write(header)
    
    @staticmethod
    def print_footer(f):
        footer = """</body>\n
                </html>\n"""
        f.write(footer)

    def print_location(location, opt=""):
        return opt + location["city"] + ", " + location["country"]

    @staticmethod
    def print_personal(f, personal):
        f.write(h2(personal['name']+" "+personal['surname'])+n)
        f.write(h3(it(personal["title"])))

    @staticmethod
    def print_experience(f, experience):

        f.write(h1("Work Experience") +n)
        
        for entry in experience:
            start_date = datetime.strptime(entry["start_date"], "%Y-%m-%d")
            end_date = datetime.strptime(entry["end_date"], "%Y-%m-%d")
            f.write(p(str(start_date.year)+" - " +str(end_date.year) + 
                    tab+entry["title"])+n)
            f.write(p(4*tab+entry["institution"]["name_en"]))
            f.write(p(__class__.print_location(entry["location"], 4*tab)))
            if len(entry["deliverables"])>0:
                for deliverable in entry["deliverables"]:
                    f.write(p(4*tab  + "- " + str(deliverable) ))
            #f.write(p(4 * tab + bf("Main skills: ") + str(entry["skills"]) ))
    
    @staticmethod
    def print_education(f, education):
        f.write(h1("Education") + n)

        for entry in reversed(education):
            start_date = datetime.strptime(entry["start_date"], "%Y-%m-%d")
            end_date = datetime.strptime(entry["end_date"], "%Y-%m-%d")
            f.write(p(str(start_date.year)+" - " +str(end_date.year) + 
                    tab + entry["degree"] + " in " + entry["subject"] + comma +
                    entry["institution"]["name_en"] + 
                    __class__.print_location(entry["institution"]["location"], comma)) + n
                    )

    @staticmethod
    def print_publications(f, publications):

        f.write(h1("Publications") + n)
        for entry in publications:
            if entry["type"]=="article":
                f.write(p(entry["authors"] + " ("+entry["date"]+") "
                 + href(entry["url"], entry["title"]) + comma + entry["publisher"]) + n
                 )

    @staticmethod
    def print_communications(f, communications):
        f.write(h1("Communications") + n)

        for entry in communications:
            f.write(
                p(
                    bf(entry["venue"]) + comma +
                    invited[entry["invited"]] +
                    entry["city"] + comma +
                    entry["country"] + comma +
                    entry["year"] + comma +
                    it(entry["title"])
                ) + n
            )

    @staticmethod
    def print_languages(f, languages):
        f.write(h1("Languages") + n)
        for entry in languages:
            f.write(
                p(
                    entry["language"] + comma +
                    entry["level"]
                ) + n
            )

    @staticmethod
    def print_picture(f, picture):
        f.write('<img src="data:image/jpeg;base64,'+ picture["image"]["data"])


    @staticmethod
    def print_foot(f):
        f.write(p('<center> This CV was proudly generated with python + JSON + HTML. </center>'))

if __name__ == "__main__":

    cv = json.load(open("cv/cv.json", "rb"))

    # device = input("Select device (html, pdf, docx):")

    if(True):

        output_file = open("cv/cv.html", "w")

        #html.print_header(output_file, cv["personal"])
        html.print_personal(output_file, cv["personal"])
        html.print_experience(output_file, cv["experience"])
        html.print_education(output_file, cv["education"])
        html.print_publications(output_file, cv["publications"])
        #html.print_communications(output_file, cv["communications"])
        html.print_languages(output_file, cv["languages"])
        html.print_foot(output_file)
        #html.print_footer(output_file)
        
        output_file.close()


        # print only publications
        output_file = open("cv/publications_list.html", "w")
        html.print_publications(output_file, cv["publications"])

        output_file.close()

    elif(device=="pdf"):
        # TODO: implement pdf output using LaTeX 
        print("To be implemented")  
    elif(device=="docx"):
        print("To be implemented")