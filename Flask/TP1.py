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

@app.route("/number-prompt", methods=['GET', 'POST'])
def saisie_nombres() -> str:
    """Implémentation de la page de résultat de la saisie de bornes

    Returns:
        str: Résultat de la page de saisie des bornes
    """
    borne_inf = None
    borne_sup = None

    if (request.method == 'GET'):
        borne_inf = int(request.args.get('borne-inf'))
        borne_sup = int(request.args.get('borne-sup'))

    elif (request.method == 'POST'):
        borne_inf = int(request.form.get('borne-inf'))
        borne_sup = int(request.form.get('borne-sup'))

    if ((borne_inf is None) or (borne_sup is None)):
        return page_erreur()

    temp_list = []
    for i in range(borne_inf + 1, borne_sup):
        temp_list.append(f"<li>{i}</li>")
    
    numbers_between = '\n'.join(temp_list)
    
    # Solution alternative :
    # ---------------------
    # numbers_between = ""
    # for i in range(borne_inf + 1, borne_sup):
    #     numbers_between = numbers_between + f"<li>{i}</li>"


    borne_inf_squarred = borne_inf ** 2
    borne_sup_squarred = borne_sup ** 2

    page_content = "<html>\n"
    page_content = page_content + "<head>\n"
    page_content = page_content + "<title>\n"
    page_content = page_content + "Saisie de nombres\n"
    page_content = page_content + "</title>\n"
    page_content = page_content + "</head>\n"
    page_content = page_content + "<body>\n"
    page_content = page_content + "<div>"
    page_content = page_content + "    <table border=\"1\">"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Borne inférieure :</td>"
    page_content = page_content + f"            <td>{str(borne_inf)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Borne supérieure :</td>"
    page_content = page_content + f"            <td>{str(borne_sup)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Nombres entier entre ces deux bornes :</td>"
    page_content = page_content + f"            <td>{str(numbers_between)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Carré de la borne inférieure :</td>"
    page_content = page_content + f"            <td>{str(borne_inf_squarred)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Carré de la borne supérieure :</td>"
    page_content = page_content + f"            <td>{str(borne_sup_squarred)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "    </table>"
    page_content = page_content + "</div>"
    page_content = page_content + "</body>\n"
    page_content = page_content + "</html>\n"

    return page_content

@app.route("/color-choice", methods=['GET', 'POST'])
def saisie_couleur() -> str:
    """Implémentation de la page de résultat lors de la soumission du formulaire

    Returns:
        str: Résultat de la page du choix de couleur
    """
    
    color = None

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
    """Implémentation de la page d'erreur

    Returns:
        str: Chaîne de caractère construisant la page d'erreur
    """
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
