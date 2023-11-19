#Etape 1, vue :
#Victor Tancrez Clément Perin

import tkinter
import modele
from pygame import mixer
from random import randint


class VueSame :
    '''classe qui affiche le jeu Same'''
    
    def __init__(self, same = modele.ModeleSame()):
        '''constructeur de la classe VueSame'''
        self.__same = same
    #La première chose est de créer la fenêtre principale :
        self.__fen = tkinter.Tk()
        self.__fen.title("Jeu Same")
        mixer.init()
        self.__music=["pistolet_laser_2.mp3","sabre_laser.mp3","r2d2.mp3"] #Liste de son
        self.__music2=["Non_star_wars.mp3","cest_impossible.mp3"]
        #Label pour l'affichage du score :
        lbl_score=tkinter.Label(self.__fen,text="Score : "+str(self.__same.score()), width = 12).grid(row=self.__same.nblig()//2, column=self.__same.nbcol(), rowspan=1)
    #Bouton pour relancer l'application :
        bouton_relancer=tkinter.Button(self.__fen,text="Nouvelle Partie", width = 12, command=self.nouvelle_partie).grid(row=self.__same.nblig()//2+1, column=self.__same.nbcol(), rowspan=2)
    #Bouton pour les indices
        self.__bouton_indice=tkinter.Button(self.__fen,text="Indice", width = 12,command=self.indice).grid(row=self.__same.nblig()//2+2, column=self.__same.nbcol(), rowspan=2)
    #Bouton pour quitter l'application :
        btn_quitter = tkinter.Button(self.__fen, text="Quitter", command = self.__fen.destroy)
        btn_quitter.grid(row=(self.__same.nblig()//2)+2, column=self.__same.nbcol())
    # on créé les images : elles sont mémorisées dans une liste de PhotoImage
        self.__images = []
        for i in range(1,5) :
            img = tkinter.PhotoImage(file="img/sphere"+str(i)+".gif")
            self.__images.append(img)

        self.__images.append(tkinter.PhotoImage(file="img/spherevide.gif")) #ajout de la sphere vide à la fin de la liste        
        self.__images_noires = []
        for i in range(1,5) :
            img = tkinter.PhotoImage(file="img/sphere"+str(i)+"black"+".gif")
            self.__images_noires.append(img)
    #On construit la grille de bouton à gauche :
        self.__les_btns=[]
        for ligne in range (self.__same.nblig()):
            val_ligne=[]
            for colonne in range( self.__same.nbcol()):
                self.__same.couleur(ligne,colonne) #la couleur à la case(j,k)
                if self.__same.couleur(ligne,colonne) == -1 :
                    val_ligne.append(tkinter.Button(self.__fen, image=self.__images[self.__same.nbcouleurs()-1]))
                    val_ligne[colonne].grid(row=ligne,column=colonne)
                else :
                    val_ligne.append(tkinter.Button(self.__fen, image=self.__images[self.__same.couleur(ligne,colonne)],command=self.creer_controleur_btn(ligne,colonne)))
                    val_ligne[colonne].bind("<Motion>",self.go_in(ligne,colonne))
                    val_ligne[colonne].bind("<Leave>",self.go_out(ligne,colonne))
                    val_ligne[colonne].grid(row=ligne,column=colonne)        
            self.__les_btns.append(val_ligne)
           
    #On lance la boucle d'écoute des événements :
        self.__fen.mainloop()
        
        
    def redessine(self):
        '''méthode qui sert à réactualiser les boutons '''
        for j in range (self.__same.nblig()) :
            for k in range(self.__same.nbcol()):
                couleur_case = self.__same.couleur(j,k)
                if self.__same.couleur(j,k)==-1 :
                    self.__les_btns[j][k]["image"]=self.__images[self.__same.nbcouleurs()]
                else :
                    self.__les_btns[j][k]["image"]=self.__images[couleur_case]
        lbl_score=tkinter.Label(self.__fen,text="Score : "+str(self.__same.score()), width = 12).grid(row=self.__same.nblig()//2, column=self.__same.nbcol(), rowspan=1)
        self.__bouton_indice=tkinter.Button(self.__fen,text="Indice", width = 12,command=self.indice).grid(row=self.__same.nblig()//2+2, column=self.__same.nbcol(), rowspan=2)
    def nouvelle_partie(self):
        self.__same=modele.ModeleSame()
        self.__les_btns=[] #matrice de Button
        mixer.music.load("musique_nouvelle_partie.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()
        for j in range (self.__same.nblig()) :
            ligne=[]
            for k in range (self.__same.nbcol()) :
                couleur_case = self.__same.couleur(j,k) #la couleur à la case(j,k)
                if couleur_case == -1 :
                    ligne.append(tkinter.Button(self.__fen, image=self.__images[self.__same.nbcouleurs()-1]))
                    ligne[k].grid(row=j,column=k)
                else :
                    ligne.append(tkinter.Button(self.__fen, image=self.__images[couleur_case], command=self.creer_controleur_btn(j,k)))
                    ligne[k].bind("<Motion>",self.go_in(j,k))
                    ligne[k].bind("<Leave>",self.go_out(j,k))
                    ligne[k].grid(row=j,column=k)
            self.__les_btns.append(ligne)
    def creer_controleur_btn(self,j,k):
        '''VueSame,int,int->VueSame
        Retourne la fonction ci-dessous'''
            
        def controleur_btn():
            '''Rien->Rien
            Demande au modèle de supprimer la bille en (i,j) puis demande à la vue de se redessiner'''
            num_compo=self.__same.composante(j,k)
            if self.__same.supprime_composante(num_compo)  :
                self.redessine()
                hasard=randint(0,len(self.__music)-1)
                mixer.music.load(self.__music[hasard])
                mixer.music.set_volume(0.2)
                mixer.music.play()
            else:
                hasard=randint(0,len(self.__music2)-1)
                mixer.music.load(self.__music2[hasard])
                mixer.music.set_volume(0.2)
                mixer.music.play()
                
        return controleur_btn
    def go_in(self, j, k):
        '''VueSame->VueSame
        Retourne la fonction ci-dessous'''
        
        def go_in_btn(event):
            '''Rien->Rien
            Fait en sorte que lorsque le curseur va sur une compo , les billes à l'intérieur deviennent noire et créer un label montrant le score que le joueur pourrait gagner s'il supprimait les billes sur son curseur'''              
            num_compo=self.__same.composante(j,k)
            billes_num_compo=[[j,k]]
            for m in range (self.__same.nblig()):
                for n in range (self.__same.nbcol()):
                    if self.__same.composante(m,n)==num_compo and not [m,n] in billes_num_compo:
                        billes_num_compo.append([m,n])
                        if self.__same.couleur(m,n)==-1 :
                            self.__les_btns[m][n]["image"]=self.__images[self.__same.nbcouleurs()]
                        else :
                            self.__les_btns[m][n]["image"]=self.__images_noires[self.__same.couleur(m,n)]
                
            if self.__same.composante(j,k)==0 or self.__same.score_compo(self.__same.composante(j,k))==-1:
                lbl_score_ajout=tkinter.Label(self.__fen,text="", width = 12).grid(row=self.__same.nblig()//2, column=self.__same.nbcol(), rowspan=2)
                
            else:
                lbl_score_ajout=tkinter.Label(self.__fen,text="+ "+str(self.__same.score_compo(self.__same.composante(j,k))), width = 12).grid(row=self.__same.nblig()//2, column=self.__same.nbcol(), rowspan=2)
                #le score est parfois égal à 0 alors qu'on peut supprimer les 2 billes car le score est compté avec la formule (n-2)*(n-2)=(2-2)*(2-2)=0'''
        
        return go_in_btn
    def go_out(self,j,k):
        '''VueSame-->VueSame
            retourne la fonction ci-dessous '''
        def go_out_btn(event):
            '''Rien--> Rien
            Fait en sorte que lorsque le curseur part d'un compo , les billes à l'intérieur redevienne blanche'''
            num_compo=self.__same.composante(j,k)
            for m in range (self.__same.nblig()):
                for n in range (self.__same.nbcol()):
                    if self.__same.composante(m,n)==num_compo :
                        if self.__same.couleur(m,n)==-1 :
                            self.__les_btns[m][n]["image"]=self.__images[self.__same.nbcouleurs()]
                        else :
                            self.__les_btns[m][n]["image"]=self.__images[self.__same.couleur(m,n)]

        return go_out_btn
    def indice(self):
        '''méthode qui affiche en couleur sombre une  composition possible'''
        
        num_compo=self.__same.indice()
        billes_num_compo=[]
        for m in range (self.__same.nblig()):
            for n in range (self.__same.nbcol()):
                if self.__same.composante(m,n)==num_compo and not [m,n] in billes_num_compo:
                    billes_num_compo.append([m,n])
                    if self.__same.couleur(m,n)==-1 :
                        self.__les_btns[m][n]["image"]=self.__images[self.__same.nbcouleurs()]
                    else :
                        self.__les_btns[m][n]["image"]=self.__images_noires[self.__same.couleur(m,n)]
        
        
            
                
           
        
        #le score est parfois égal à 0 alors qu'on peut supprimer les 2 billes car le score est compté avec la formule (n-2)*(n-2)=(2-2)*(2-2)=0'''
        
if __name__ == '__main__' :
    same=modele.ModeleSame(10,15,4)
    jeu_same=VueSame(same)