
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
            
            notsaid=True
            while notsaid:
                letter=input("Your Letter : ")
                if letter in m:
                    #unlock
                else:
                    print(letter,"not found")
        else:
            #player 2
        turn+=1
        
    
play()