liste = ["a","b","c","d","e","f","g","f","i","j","k","m","n","i","o","p","r","s","t","u","v","w","x","y","z"]

mot = input("Enter votre mot de passe : ")
chaine = str()

def text(chaine, mot):
    if chaine == mot:
        print("Mot de passe correct")
    
    

for l in liste:
    chaine = l
    text(chaine, mot)
    
    for l2 in liste:
        chaine = l + l2
        text(chaine, mot)
        
        for l3 in liste:
            chaine = l + l2 + l3
            text(chaine, mot)
            
            for l4 in liste:
                chaine = l + l2 + l3 + l4
                text(chaine, mot)
                
                for l5 in liste:
                    chaine = l + l2 + l3 + l4 + l5
                    text(chaine, mot)
                    
                    for l6 in liste:
                        chaine = l + l2 + l3 + l4 + l5 + l6
                        text(chaine, mot)
                        
                        for l7 in liste:
                            chaine = l + l2 + l3 + l4 + l5 + l6 + l7
                            text(chaine, mot)
                            
                            for l8 in liste:
                                chaine = l + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                text(chaine, mot)
                                
                                
    
    