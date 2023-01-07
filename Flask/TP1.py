"""
@author: manuvai.rehua@ut-capitole.fr
"""

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

if __name__ == '__main__':
    print(get_page())
