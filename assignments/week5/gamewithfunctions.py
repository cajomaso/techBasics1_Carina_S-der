# I will update my first site ReadMe every week to be transparent about AI and sources used.
import time
import sys

# Dictionary within a dictionary including keys and their values
SEASON_ASSETS = {

    "spring": {
        "art": fr'''       
         _( )_        
        (_(o)_)       
          (_)         
           |          
           | __       
           |/_/ _( )_ 
 _( )_     |   (_(o)_)
(_(o)_)    |    /(_)  
  (_)\     |    |     
      | __ |    |     
      |/_/ | __ |     
      |    |/_/ |     
      |    |    |     ''',
        "line": "The flowers are really starting to bloom."
    },

    "summer": {
        "art": '''   
          NUUUUU}}}}}}}}}}}}}}   
           S}UUUU}}}}∙∙∙∙∙∙∙∙∙
            U}}}}}UUUUUUUU∙∙∙∙
            N}}}NN∙}}}}∙∙}}UUU
          SUU}}}}NN∙∙∙∙∙}}}}}
        SUN∙∞UU}}}}NN∙∙∙∙∙∙∙
SUNSUN}}}N∙∞∞∙∙UU}}}∙NN∙∙∙∙∙∙∙
}U∙∞∙∙N}}}N∙∙∞∙∙∙U}}}}∙NN∙∙∙∙∙
}U∙∞∙∙∙N}}}N∙∙∞∙∙∙UU}}}}∙NN∙∙∙
}U∙∙∞∙∙N}}}}N∙∙∞∞∙∙∙UU}}}}∙NN∙
}U∙∙∞∙∙∙N}}}}N∙∙∙∞∙∙∙∙UU}}}}∙N
}}U∙∙∞∙∙NM}}}N∙∙∙∙∞∙∙∙∙∙U}}}}}
}}U∙∙∞∙∙∙N}}}}N∙∙∙∙∞∞∙∙∙∙UU}}}
}}U∙∙∙∞∙∙∙N}}}}N∙∙∙∙∙∞∙∙∙∙∙UU}
}}U∙∙∙∞∙∙∙N}}}}}N∙∙∙∙∙∞∙∙∙∙∙∙U
}}U∙∙∙∞∙∙∙∙N}}}}}N∙∙∙∙∙∞∞∙∙∙∙∙
}}U∙∙∙∙∞∙∙∙NM}}}}}N∙∙∙∙∙∙∞∙∙∙∙
}}}U∙∙∙∞∙∙∙∙N}}}}}}N∙∙∙∙∙∙∞∙∙∙
}}}U∙∙∙∙∞∙∙∙∙N}}}}}}N∙∙∙∙∙∙∞∞∙''',
        "line": "The sun really is scorching hot..."
    },

    "autumn": {
        "art": '''                           

                        ▄█▀     
                      ▄▄█▀     
                    ▄█▀█       
       ▓▓▓ ▓▓     ████▌  ▓▓▓▓▓▓     
   ▓▓▓▓░░░░░░░▓▓░▀▀██▀▀░▓▓▓▓░░░░ ▓▓   
   ▓░░░░░░▓▓▓░░░░░░░▓░░▓▓░░░░▓▓░░░░░▓▓  
 ▓▓░░░░░░▓▓░░░░░░░░▓▓░░░▓░░░░░░░░▓░░░▓▓ 
▓▓░░░░░▓▓░░░░░░░▓▓░░░░░░░▓▓░░░░░░░▓▓░░░▓ 
▓░░░░░▓▓░░░░░░░▓░░░░░░░░░▓▓░░░░░░░▓▓░░░░▓
░░░░░░▓▓░░░░░░▓▓░░░░░░░░░░▓▓░░░░░░░▓░░░░░▓
░░░░░▓░░░░░░░░▓░░░░░░░░░░░░▓░░░░░░░▓▓░░░░▓
░░░░░░▓░░░░░░░▓░░░░░░░░░░░░▓░░░░░░░░▓░░░░▓
░░░░░░░▓░░░░░░░▓░░░░░░░░░░░▓░░░░░░░▓▓░░░▓
▓▓░░░░░▓▓░░░░░░▓▓░░░░░░░░░▓░░░░░░░░▓░░▓ 
 ▓▓▓░░░░▓░░░░░░░▓▓░░░░░░░░▓░░░░░░░▓░░▓▓ 
     ▓▓░░░▓░░░░░░▓▓░░░░░░▓░░░░░░░▓░▓  ''',
        "line": "The leafs are already falling and the pumpkins are growing more and more... time sure flies by."
    },

    "winter": {
        "art": '''   °            o          
                    °      
       °                   
     o                     

         °     °           
                 o           
    °    °                °
            ╒══╕ o  °         
            │  │       °     °
           ─┴══┴─    o       °
         ┌  σ<σ  ┐            
 °       └  ···  ┘           °
    o    =-=-=-=-=-           
       └     .     ┘     °°    
 °    └      .      ┘          
      └      .      ┘          
   °   └           ┘  °        
      └      .      ┘         °  
  °  └       .       ┘          
    └        .        ┘     °    
°   └        .        ┘         
    └                 ┘       ''',
        "line": "Yay, my snowman is still standing."
    }
}


def slow_print(text, delay=0.04):
    #typewriter effect from a library the internet told me to use, also help from gemini
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Adds a newline at the end

#choosing the season
def get_season():
    #defining a list including the seasons(keys) from the dictionary above
    valid_seasons = list(SEASON_ASSETS.keys())
    while True:
        season_input = input("You think to yourself: What season was it again?\n> ").strip().lower()
        time.sleep(0.5)

        if season_input in valid_seasons:
            print(f"Oh, it's {season_input}, that's right!")
            time.sleep(1)
            slow_print("Look out the window, you can see it!")
            time.sleep(1)
            return season_input
        else:
            slow_print("Oops, that did not work. Try to write spring, summer, autumn or winter without any spaces!")

#printing the art of the season
def display_seasonal_art(season):
    assets = SEASON_ASSETS[season]
    print(assets["art"])
    slow_print(assets["line"])


def get_temperature(season):
    #temperature input
    while True:
        temp_input = input("You look on the thermometer. What temperature is it?\n> ").strip()
        time.sleep(0.5)

        try: #making sure its a number
            temp = int(temp_input)
        except ValueError:
            print("Oops! That's not a number. Please enter a temperature using digits (e.g., 20 or -5).")
            continue

        # Logic for Spring & Autumn
        if season in ["spring", "autumn"]:
            if temp > 30 or temp < -5:
                slow_print("That cannot be. Look again.")
            elif temp >= 16:
                slow_print("That's quite warm for this time around.")
                return temp
            else:
                slow_print("That's quite cool.")
                return temp

        # Logic for Summer
        elif season == "summer":
            if temp > 45 or temp < 0:
                slow_print("That cannot be. Look again.")
            elif temp >= 31:
                slow_print("It's a really hot day today.")
                return temp
            elif temp >= 20:
                slow_print("Nice weather.")
                return temp
            else:
                slow_print("It's a bit cool for summertime...")
                return temp

        # Logic for Winter
        elif season == "winter":
            if temp >= 20 or temp < -20:
                slow_print("That cannot be. Look again.")
            elif temp > 12:
                slow_print("It is a really warm day for a winter day.")
                return temp
            else:
                slow_print("Cold. As expected.")
                return temp


def go_for_walk(temperature):

    while True:
        walk = input("Should I go for a walk then?\n> ").strip().lower()
        time.sleep(0.5)

        if walk not in ["yes", "no"]: #excluding answers that dont make sense
            slow_print("That's no short answer. Try yes or no without any spaces.")
            continue

        if walk == "yes":
            if temperature > 30:
                slow_print("Nah, actually I shouldn't. It is way too hot. Don't want to get a heatstroke.")
            elif temperature > 15:
                slow_print("Then let's go get those 10,000 steps.")
            else:
                slow_print("It's chilly, I'd rather stay home.")
            break

        elif walk == "no":
            if temperature > 30:
                slow_print("Right, I shouldn't. It is way too hot. Don't want to get a heatstroke.")
            elif temperature > 15:
                slow_print("Don't even think about not going! I need to go get those 10,000 steps.")
            else:
                slow_print("Right. It's chilly, I'd rather stay home.")
            break


def main():
    #the actual story line in a minimalist way
    slow_print("It's a new morning and you wake up...")
    time.sleep(1)

    # 1. Season
    season = get_season()

    # 2. Art display
    display_seasonal_art(season)

    # 3. Temperature
    temperature = get_temperature(season)

    # 4. Walk or no walk
    go_for_walk(temperature)

    # Outro
    slow_print("\nThank you for checking out the weather with me! \\(*0 0*)/")


if __name__ == "__main__":
    main()
