#Etape 3 VICTOR TANCREZ CLEMENT PERIN , modele :
class Pile :
    '''Definition d'une pile - structure de données LIFO (Last In First Out)
    '''

    def __init__(self) : 
        '''Pile -> Pile
        construit une pile vide
        '''
        # basée sur une liste
        self.__pile = []
        # self.__pile = list()
        
    
    def empiler(self,elt) :
        '''(modif) Pile, Objet -> Rien
        ajoute un élément au sommet de la pile.
        '''
        self.__pile.append(elt)    


    def est_vides(self) : 
        '''Pile -> Boolean
        teste si la pile est vide. '''
        return len(self.__pile) == 0
        # return self.__pile == []

  
    def sommet(self) : 
        '''Pile -> Objet
        retourne l'élément au sommet de la pile.
        '''
        assert not self.est_vides(), 'Erreur : pile vide'
        return self.__pile[-1]
        # return self.__pile[len(self.__pile) - 1]
       
       
    def depiler(self) : 
        '''(modif) Pile -> Objet
        enlève l'élément au sommet de la pile.
        ''' 
        assert not self.est_vides(), 'Erreur : pile vide'
        elt = self.sommet()
        del(self.__pile[-1])
        return elt
    
    def affiche(self):
        
        return self.__pile

#-----------------------------------------------------------

class Case :
    '''classe qui modélise une bille du jeu Same'''
    
    def __init__(self, couleur):
        '''Constructeur de la classe Case'''
        self.__couleur = couleur
        self.__compo = -1
        
    def couleur(self):
        '''Méthode qui retourne la couleur de la bille
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : self.__couleur : int --- couleur de la bille'''
        return self.__couleur
    
    def change_couleur(self, valeur):
        '''Méthode qui permet de changer la couleur de la bille
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
            valeur : int -- entier
        Retour : None'''
        self.__couleur = valeur
        self.__compo = -1
        
    def supprime(self):
        '''Méthode qui supprime la bille de la case
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : None'''
        self.__couleur = -1
        self.__compo = 0
        
    def est_vide(self):
        '''Méthode qui vérifie si la case est vide
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : Bool'''
        return self.__couleur == -1
    
    def composante(self):
        '''Méthode qui retourne le numéro de la composante
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : int -- numéro de la composante'''
        return self.__compo
    
    def pose_composante(self, entier):
        '''Méthode qui affecte un entier au numéro de composante
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : None'''
        self.__compo = int(entier)
        
    def supprime_compo(self):
        '''Méthode qui désaffecte un mnuméro de composante à la case
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : None'''
        if self.__couleur == -1 :
            self.__compo = 0
        else :
            self.__compo = -1
            
    def parcourue(self):
        '''Méthode qui teste si la case a été affectée à un numéro de composante
        Arguments :
            self : Objet de Case
            couleur : int -- couleur de la bille
        Retour : Bool'''
        return self.__compo != -1
            

from random import randint

class ModeleSame :
    '''classe qui modélise le jeu Same'''
    
    def __init__(self, nblig=10, nbcol=15, nbcouleurs=4):
        '''constructeur de la classe ModeleSame'''
        self.__nblig = nblig
        self.__nbcol = nbcol
        self.__nbcouleurs = nbcouleurs
        self.__mat = []
        for ligne in range(self.__nblig):
            ligne = []
            for colonne in range(self.__nbcol):
                ligne.append(Case(randint(0,self.__nbcouleurs-1)))
            self.__mat.append(ligne)
        self.__score = 0
        self.__nb_elts_compo = []
        self.calcule_composantes()
    
    def score(self):
        '''Méthode qui retourne le score du joueur
        Argument : self -- Objet de ModeleSame
        Retour : self.__score : int -- score du joueur'''
        return self.__score
    
    def nblig(self):
        '''Méthode qui retourne le nombre de lignes de ModeleSame
        Argument : self -- Objet de ModeleSame
        Retour : self.__nblig : int -- nombre de lignes de ModeleSame'''
        return self.__nblig
    
    def nbcol(self):
        '''Méthode qui retourne le nombre de colonnes de ModeleSame
        Argument : self -- Objet de ModeleSame
        Retour : self.__nbcol : int -- nombre de lignes de ModeleSame'''
        return self.__nbcol
    
    def nbcouleurs(self):
        '''Méthode qui retourne le nombre de couleurs de ModeleSame
        Argument : self -- Objet de ModeleSame
        Retour : self.__nbcouleurs : int -- nombre de couleurs de ModeleSame'''
        return self.__nbcouleurs
    
    def coords_valides(self, i, j):
        '''Méthode qui vérifie si le point (i,j) appartient au jeu
        Arguments :
            self -- Objet de ModeleSame
            i : int -- coordonnée en abcisse
            j : int -- coordonnée en ordonnée
        Retour : Bool'''
        return 0 <= i < self.__nblig and 0 <= j < self.__nbcol
        
    def couleur(self, i, j):
        '''Méthode qui retourne la couleur de la bille au coordonnée (i,j)
        Arguments :
            self -- Objet de ModeleSame
            i : int -- coordonnée en abcisse
            j : int -- coordonnée en ordonnée
        Retour : int -- couleur de la bille en (i,j)'''
        
        return self.__mat[i][j].couleur()
    def affiche_couleurs(self,k):
        '''
        Méthode pour afficher les couleurs de la matrice
        Arguments :
            self -- Objet de ModeleSame
            k : int
        Retour : None'''
        casu=[]
        colonne=[]
        for i in range(self.__nblig):
            colonne.append(self.__mat[i][k].couleur())
            ligne=[]
            for j in range(self.__nbcol):
                ligne.append(self.__mat[i][j].couleur())
            casu.append(ligne)
        print(colonne)
        print(casu)
        
    def supprime_bille(self,i,j):
        '''Méthode qui supprime la bille en (i,j)
        Arguments :
            self -- Objet de ModeleSame
            i : int -- coordonnée en abcisse
            j : int -- coordonnée en ordonnée
        Retour : None'''
        assert self.coords_valides(i,j)
        self.__mat[i][j].supprime()
    
    def nouvelle_partie(self):
        '''Méthode qui réinitialise toutes les cases en changeant leur couleur
        Arguments : None
        Retour : None'''
        for ligne in range(self.__nblig):
            for colonne in range(self.__nbcol):
                self.__mat[ligne][colonne]=Case(randint(0,self.__nbcouleurs-1))

    def composante(self,i,j):
        '''Méthode qui renvoie la composante de la bille en (i,j)
        Arguments :
            self : Objet de ModeleSame
            i : int -- coordonée en abcisse
            j : int -- coordonée en ordonnée
        Retour : int -- composante de la bille en (i,j)'''
        assert self.coords_valides(i,j)
        return self.__mat[i][j].composante()
    
    def calcule_composantes(self):
        '''Méthode qui lance le calcul des composantes sur toutes les cases de la matrice
        Argument : self -- Objet de ModeleSame
        Retour : None'''
        self.__nb_elts_compo.append(0)
        num_compo = 1
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                if not self.__mat[i][j].parcourue():
                    couleur = self.couleur(i,j)
                    self.__nb_elts_compo.append(self.calcule_composante_numero(i,j,num_compo,couleur))
                    num_compo+=1
    
    def calcule_composante_numero(self, i, j, num_compo, couleur):
        '''Méthode qui attribue le numéro num_compo aux cases qu'elle peut toucher depuis la case en (i,j)
        Arguments :
            self -- Objet de ModeleSame
            couleur : int -- numéro associé à la couleur de la case
        Retour : None'''
        if self.__mat[i][j].parcourue() or self.couleur(i,j) != int(couleur):
            return 0
        else :
            self.__mat[i][j].pose_composante(num_compo)
            valeur1=valeur2=valeur3=valeur4=0
            if self.coords_valides(i+1,j):
                    valeur1+=self.calcule_composante_numero(i+1,j,num_compo,couleur)
            if self.coords_valides(i-1,j):
                    valeur2+=self.calcule_composante_numero(i-1,j,num_compo,couleur)
            if self.coords_valides(i,j+1):
                    valeur3+=self.calcule_composante_numero(i,j+1,num_compo,couleur)
            if self.coords_valides(i,j-1):
                    valeur4+=self.calcule_composante_numero(i,j-1,num_compo,couleur)
            return 1+valeur1+valeur2+valeur3+valeur4
        
    def recalc_composantes(self):
        '''Méthode qui supprimela composante attribuée à chaque case puis recalcule les composantes
        Argument : self -- Objet de ModeleSame
        Retour : None'''
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                self.__mat[i][j].supprime_compo()
        self.calcule_composantes()
        
    def supprime_composante(self, num_compo):
        '''Méthode qui supprime toutes les billes de la matrice qui sont dans la composante de num_compo et actualise le score
        Arguments :
            self -- Objet de ModeleSame
            num_compo : numéro de la composante
        Retour : Bool'''
        if num_compo==0:
            return False
        billes_compo=[]
        for i in range (self.__nblig):
            for j in range (self.__nbcol):
                if self.composante(i,j)==num_compo:
                    billes_compo.append([i,j])
        n=len(billes_compo)
        if n>=2:
            for k in range (self.__nbcol):
                self.supprime_composante_colonne(k,num_compo)
            self.__score+=(n-2)*(n-2)
            self.supprime_colonnes_vides()
            self.recalc_composantes()
            return True
        else :
            return False

    def est_vide(self,i,j):
        '''Méthode qui renvoie si la case est vide en (i,j)
        Arguments :
            self : Objet de ModeleSame
            i : int -- coordonée en abcisse
            j : int -- coordonée en ordonnée
        Retour : Bool'''
        return self.__mat[i][j].est_vide()==True and self.composante(i,j)==0
    
    def colonne_vide(self,j):
        '''Méthode qui indique si la colonne j est vide
        Arguments :
            self : Objet de ModeleSame
            j : int -- coordonée en ordonnée'''
        compteur=0
        for i in range(self.__nblig):
            if self.__mat[i][j].couleur()==-1 :
                compteur+=1
        return compteur==self.__nblig
    
    def change_colonne(self,j,k):
        '''Méthode qui échange 2 colonnes de place
        Arguments :
            self : Objet de ModeleSame
            k : int
            j : int -- coordonée en ordonnée
        Retour : '''
        var=[]
        for i in range(self.__nblig):
            self.__mat[i][j],self.__mat[i][k]=self.__mat[i][k],self.__mat[i][j]
            
    def supprime_colonnes_vides(self):
        '''Méthode qui utilise les méthodes change_colonne et colonne_vide pour faire les deux
        Argument : self -- Objet de ModeleSame
        Retour : None'''
        for k in range(self.__nbcol):
            if self.colonne_vide(k)==True:
                for j in range(k,self.__nbcol):
                    if self.colonne_vide(j)==False:
                        self.change_colonne(k,j)
                
    def supprime_composante_colonne(self,j,num_compo):
        '''Méthode qui supprime les billes de la composante num_compo qui si trouvent dans la colonne j
        Arguments :
            self : Objet de ModeleSame
            num_compo : int -- numéro de la composante
            j : int -- coordonée en ordonnée
        Retour : None'''
        p1=Pile() # on va empiler les billes non supprimées
        compteur=0
        for i in range(self.__nblig):
            if self.composante(i,j)==num_compo:
                compteur+=1  # nombre de bille à supprimé 
            else:
                p1.empiler(self.__mat[i][j])
        for i in range(compteur):
            self.__mat[i][j].supprime()
        i=self.__nblig
        while not p1.est_vides():
            self.__mat[i-1][j]=p1.depiler()
            i-=1
            
    def score_compo(self,num_compo):
        '''méthode qui renvois le score si on élimine la composante num_compo
            arguments : num_compo : int
            return int
        '''
        billes_compo=[]
        for i in range (self.__nblig):
            for j in range (self.__nbcol):
                if self.composante(i,j)==num_compo:
                    billes_compo.append([i,j])
        n=len(billes_compo)
        return (n-2)*(n-2)
          
    def indice(self):
        '''méthode qui renvoit le num_compo de la composition qui augmente le plus  le score
        return int '''
        self.calcule_composantes()
        score_max=self.__nb_elts_compo[0]
        for num_compo in range(len(self.__nb_elts_compo)):
            if self.score_compo(self.__nb_elts_compo[num_compo])>score_max:
                score_max=self.score_compo(self.__nb_elts_compo[num_compo])
                var=self.__nb_elts_compo[num_compo]
        return var

        
            

        
        
        