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

@app.route("/4-numbers-prompt", methods=['GET', 'POST'])
def saisie_4_nombres() -> str:
    """Implémentation de la page de saisie de 4 nombres

    Returns:
        str: Résultat de la page
    """

    numbers = get_numbers_prompted(request.method)

    if ((not numbers is None) and (len(numbers) != 4)):
        return page_erreur()

    numbers = tri(numbers)

    page_content = get_page_4_nombres(numbers)

    return page_content

def get_numbers_prompted(method: str) -> list:
    """Implémentation de la récupération des nombres entrés par l'utilisateur

    Args:
        method (str): Méthode utilisée

    Returns:
        list: La liste entrée par l'utilisateur
    """
    numbers = []

    nombre1 = None
    nombre2 = None
    nombre3 = None
    nombre4 = None

    if (method == 'GET'):
        nombre1 = request.args.get('nombre1')
        nombre2 = request.args.get('nombre2')
        nombre3 = request.args.get('nombre3')
        nombre4 = request.args.get('nombre4')

    elif (method == 'POST'):
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')
        nombre4 = request.form.get('nombre4')

    if (not nombre1 is None):
        numbers.append(int(nombre1))

    if (not nombre2 is None):
        numbers.append(int(nombre2))

    if (not nombre3 is None):
        numbers.append(int(nombre3))

    if (not nombre4 is None):
        numbers.append(int(nombre4))

    return numbers

def get_page_4_nombres(numbers: list) -> str:
    """Implémentation du retour du template de la page de résultat

    Args:
        numbers (list): Liste contenant les données à manipuler

    Returns:
        str: Contenu de la page à afficher
    """
    nombre_min = numbers[0]
    nombre_max = numbers[-1]

    numbers_prompted = ""
    for num in numbers:
        numbers_prompted += f"<li>{str(num)}</li>"
    
    page_content = "<html>\n"
    page_content = page_content + "<head>\n"
    page_content = page_content + "<title>\n"
    page_content = page_content + "Changer la couleur de fond (résultat)\n"
    page_content = page_content + "</title>\n"
    page_content = page_content + "</head>\n"
    page_content = page_content + "<body>\n"
    page_content = page_content + "<div>"
    page_content = page_content + "    <table border=\"1\">"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Nombres entrés :</td>"
    page_content = page_content + f"            <td><ul>{str(numbers_prompted)}</ul></td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Nombre minimum :</td>"
    page_content = page_content + f"            <td>{str(nombre_min)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "        <tr>"
    page_content = page_content + "            <td>Nombre maximum :</td>"
    page_content = page_content + f"            <td>{str(nombre_max)}</td>"
    page_content = page_content + "        </tr>"
    page_content = page_content + "    </table>"
    page_content = page_content + "</div>"
    page_content = page_content + "</body>\n"
    page_content = page_content + "</html>\n"
    return page_content

def tri(liste: list) -> list:
    """Implémentation du tri d'une liste contenant des entiers

    Args:
        liste (list): Liste d'entier

    Returns:
        list: Liste résultat du tri
    """
    for i in range(len(liste)):
        min_index = i
        for j in range(i+1, len(liste)):
            if liste[min_index] > liste[j]:
                min_index = j

        liste[i], liste[min_index] = liste[min_index], liste[i]

    return liste

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
    print(tri([0, -5, 6, 4]))
