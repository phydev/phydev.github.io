import markdown

with open('lotka.md', 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

with open('lotka.html', 'w') as f:
    f.write(html)