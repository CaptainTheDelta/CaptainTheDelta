# coding: utf-8

#----------------------------------- import -----------------------------------

from argparse import ArgumentParser

#---------------------------------- fonction ----------------------------------

def get_args():
    """Renvoie les arguments passés en ligne de commande.

    Return:
        (tuple): Ensemble d'arguments.
    """
    parser = ArgumentParser(description="Convertit le fichier passé en "
        "argument en page HTML.")

    parser.add_argument('--file','-f',help="Chemin du fichier à traduire",required=True)
    parser.add_argument('--debug','-d',help="Affichage de debugs",required=False,action="store_true")
    # action='store_true' : De base, si aucune valeur n'est proposée, la 
    # variable vaut None. Avec cet argument, on idndique qu'on attend pas de
    # valeur, seulement la présence de cette argument, et s'il est là, on 
    # enregistre True.
    
    args = parser.parse_args()

    return args.__dict__


def debug(*args,**kwargs):
    """Fonction de debug."""
    if DEBUG:
        print("[DEBUG]",end=' ')
        print(*args,**kwargs)


def delete_space(txt):
    """Supprime les espaces au début et à la fin d'un string.

    Args:
        txt (str): Chaîne de caractères à simplifier.

    Return:
        (str): Chaîne de caractères.
    """
    res = txt
    c = res[0]
    
    while c == ' ':
        res = res[1:]
        c = res[0]

    c = res[-1]

    while c == ' ':
        res = res[:-1]
        c = res[-1]

    return res

#----------------------------------- classe -----------------------------------



#------------------------------------ main ------------------------------------

# initialisation
args      = get_args()
path_file = args['file']
DEBUG     = args['debug']

