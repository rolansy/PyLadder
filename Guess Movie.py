
import random
m = [
    "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers",
    "The Lord of the Rings: The Return of the King",
    "The Dark Knight",
    "Avatar",
    "Inception",
    "The Social Network",
    "The Avengers",
    "Frozen",
    "Interstellar",
    "Mad Max: Fury Road",
    "La La Land",
    "Get Out",
    "Black Panther",
    "Parasite",
    "1917",
    "Joker",
    "The Irishman",
    "Tenet",
    "Nomadland",
    "Dune",
    "Spider-Man: No Way Home",
    "No Time to Die",
    "The Matrix Reloaded",
    "The Matrix Revolutions",
    "Gladiator",
    "The Departed",
    "The Revenant",
    "Gravity",
    "Birdman",
    "The Shape of Water",
    "The Grand Budapest Hotel",
    "Whiplash",
    "The Wolf of Wall Street",
    "Slumdog Millionaire",
    "A Beautiful Mind",
    "Eternal Sunshine of the Spotless Mind",
    "Avatar",
    "Gone Girl",
    "The Great Gatsby",
    "The King's Speech",
    "Bohemian Rhapsody",
    "Green Book",
    "Blade Runner 2049",
    "12 Years a Slave",
    "Moonlight",
    "Her",
    "The Big Short",
    "A Star Is Born",
    "The Martian",
    "The Shape of Water",
    "Black Swan",
    "The Help",
    "Django Unchained",
    "The Hurt Locker",
    "American Hustle",
    "Dallas Buyers Club",
    "The Artist",
    "Argo",
    "The Descendants",
    "Life of Pi",
    "12 Monkeys",
    "Inglourious Basterds",
    "The Prestige",
    "Memento",
    "City of God",
    "Requiem for a Dream",
    "Donnie Darko",
    "The Pianist",
    "Mystic River",
    "Avatar",
    "The Curious Case of Benjamin Button",
    "The Aviator",
    "Finding Nemo",
    "Brokeback Mountain",
    "Little Miss Sunshine",
    "There Will Be Blood",
    "No Country for Old Men",
    "The Queen",
    "Million Dollar Baby",
    "Chicago",
    "The Lord of the Rings: The Two Towers",
    "The Lord of the Rings: The Return of the King",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Gladiator",
    "The Dark Knight",
    "Forrest Gump",
    "Pulp Fiction",
    "Inception",
    "The Shawshank Redemption",
    "The Matrix",
    "Saving Private Ryan",
    "The Green Mile",
    "A Beautiful Mind",
    "Titanic",
    "Avatar",
    "The Revenant",
    "Gravity",
    "Birdman",
    "The Shape of Water"
]
def play():
    p1=input("Enter Name of Player 1 : ")
    p2=input("Enter Name of Player 2 : ")
    pp1=pp2=0
    turn=0
    will=True
    while will:
        if turn%2==0:
            print("Turn of",p1)
            mm=random.choice(m)
            qn=createqn(mm)
            print (qn)
            modqn=qn
            notsaid=True
            while notsaid:
                l=input("Your Letter : ")
                if l in m:
                    #unlock
                    modqn=unlock(modqn,mm,l)
                    print(modqn)
                    d=input("Choose : \n1. Guess movie name or \n2. Unlock another letter : ")
                    if d==1:
                        ans=input("Enter movie Name : ")
                        if ans==mm:
                            pp1+=1
                            print("Answer is Correct")
                            notsaid=False
                            print(p1,"Your Score is : ",pp1)
                        else:
                            print("Wrong Answer. Try again")
                else:
                    print(l,"not found")
            c=input("Press 1 to continue or 0 to quit : ")
            if c==0:
                print(p1,"score : ",pp1)
                print(p2,"score : ",pp2)
                will=False
        else:
            print("Turn of",p2)
            mm=random.choice(m)
            qn=createqn(mm)
            print (qn)
            modqn=qn
            notsaid=True
            while notsaid:
                l=input("Your Letter : ")
                if l in m:
                    #unlock
                    modqn=unlock(modqn,mm,l)
                    print(modqn)
                    d=input("Choose : \n1. Guess movie name or \n2. Unlock another letter : ")
                    if d==1:
                        ans=input("Enter movie Name : ")
                        if ans==mm:
                            pp2+=1
                            print("Answer is Correct")
                            notsaid=False
                            print(p2,"Your Score is : ",pp2)
                        else:
                            print("Wrong Answer. Try again")
                else:
                    print(l,"not found")
            c=input("Press 1 to continue or 0 to quit : ")
            if c==0:
                print(p1,"score : ",pp1)
                print(p2,"score : ",pp2)
                will=False
        turn+=1
        
    
play()