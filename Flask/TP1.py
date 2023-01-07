"""
@author: manuvai.rehua@ut-capitole.fr
"""
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def get_page() -> str:
    page_content = "<html>\n"
    page_content = page_content + "<head>\n"
    page_content = page_content + "<title>\n"
    page_content = page_content + "Changer la couleur de fond (résultat)\n"
    page_content = page_content + "</title>\n"
    page_content = page_content + "</head>\n"
    page_content = page_content + "<body>\n"
    page_content = page_content + "<p>La couleur du texte change à la demande!</p>\n"
    page_content = page_content + "</body>\n"
    page_content = page_content + "</html>\n"

    return page_content

@app.route("/color-choice", methods=['GET', 'POST'])
def saisie_couleur() -> str:
    if (request.method == 'GET'):
        color = request.args.get('color-choice')
        
    elif (request.method == 'POST'):
        color = request.form.get('color-choice')
    
    if (color is None):
        return page_erreur()

    page_content = "<html>\n"
    page_content = page_content + "<head>\n"
    page_content = page_content + "<title>\n"
    page_content = page_content + "Changer la couleur de fond (résultat)\n"
    page_content = page_content + "</title>\n"
    page_content = page_content + "</head>\n"
    page_content = page_content + "<body>\n"
    page_content = page_content + f"<p><font color=\"{color}\"> La couleur du texte change à la demande! </font></p>\n"
    page_content = page_content + "</body>\n"
    page_content = page_content + "</html>\n"

    return page_content

def page_erreur() -> str:
    page_content = "<html>\n"
    page_content = page_content + "<head>\n"
    page_content = page_content + "<title>\n"
    page_content = page_content + "400\n"
    page_content = page_content + "</title>\n"
    page_content = page_content + "</head>\n"
    page_content = page_content + "<body>\n"
    page_content = page_content + "<p>Erreur</p>\n"
    page_content = page_content + "</body>\n"
    page_content = page_content + "</html>\n"
    return page_content

if __name__ == '__main__':
    print(get_page())
