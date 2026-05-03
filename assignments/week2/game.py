import time,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#text
line1= "It's a new morning and you wake up..."
line2= "You think to yourself: What season was it again?"
line3= "Oh, it's"
line4= "that's right!"
line5= "Oops, that did not work. Try to write spring, summer, autumn or winter without any spaces!"
line6= "The flowers are really starting to bloom."
line7= "The sun really is scorching hot..."
line8= "The leafs are already falling and the pumpkins are growing more and more... time sure flies by."
line9= "Yay, my snowman is still standing."

typingPrint(line1)

time.sleep(1)

while True:
        season = input(line2).lower()
        time.sleep(1)
        season=str(season)


        if season =="spring"or season=="summer"or season=="autumn" or season=="winter":
            print(line3, season, line4)
            time.sleep(2)
            typingPrint("Look out the window you can see it!")
            time.sleep(2)
            break


        elif season != "spring"or"summer"or"autumn" or "winter":
            typingPrint(line5)

if season=="spring":
    print(fr'''       
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
      |    |    |     ''')
    typingPrint(line6)

elif season=="summer":
    print('''   
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
}}}U∙∙∙∙∞∙∙∙∙N}}}}}}N∙∙∙∙∙∙∞∞∙
''')
    print(line7)

elif season=="autumn":
    print('''                           
                        
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
     ▓▓░░░▓░░░░░░▓▓░░░░░░▓░░░░░░░▓░▓  ''')
    typingPrint(line8)

else:
    print('''   °            o          
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
    └                 ┘       ''')
    typingPrint(line9)



while True:

    temperature = input("You look on the thermometer. What temperature is it?")
    time.sleep(1)

    try:
        temperature = int(temperature)
    except ValueError:
        print("Oops! That's not a number. Please enter a temperature using digits (e.g., 20 or -5).")
        continue

    # SPRING & AUTUMN
    if season == "spring" or season == "autumn":
        if temperature > 30 or temperature < -5:
            typingPrint("That cannot be. Look again.")
        elif temperature >= 16:
            typingPrint("That's quite warm for this time around.")
            break
        else:
            typingPrint("That's quite cool.")
            break

    # SUMMER
    elif season == "summer":
        if temperature > 45 or temperature < 0:
            typingPrint("That cannot be. Look again.")
        elif temperature >= 31:
            typingPrint("It's a really hot day today.")
            break
        elif temperature >= 20:
            typingPrint("Nice weather.")
            break
        else:
            typingPrint("It's a bit cool for summertime...")
            break

    # WINTER
    elif season == "winter":

        if temperature >= 20 or temperature < -20:
            typingPrint("That cannot be. Look again.")

        elif temperature > 12:
            typingPrint("It is a really warm day for a winter day.")
            break

        else:
            typingPrint("Cold. As expected.")
            break

while True:
    walk = input("Should I go for a walk then?").lower()
    time.sleep(1)
    walk=str(walk)

    if walk == "yes" or walk == "no":

        if walk == "yes":
            if temperature > 30:
                typingPrint("Nah, actually I shouldn't. It is way to hot."
                            "Don't want to get a heatstroke.")
                break


            elif temperature <= 30 or temperature > 15:
                typingPrint("Then lets go get those 10000 steps.")
                break

            elif temperature <=15:
                typingPrint("It's chilly I'd rather stay home.")
                break

        elif walk == "no":
            if temperature > 30:
                typingPrint("Right, I shouldn't. It is way to hot."
                            "Don't want to get a heatstroke.")
                break

            elif temperature <= 30 or temperature > 15:
                typingPrint("Don't even think about not going! I need to go get those 10000 steps.")
                break

            elif temperature <= 15:
                typingPrint("Right. It's chilly I'd rather stay home.")
                break

    else:
        typingPrint("That's no short answer. Try yes or no without any spaces.")

typingPrint(fr'''

Thank you for checking out the weather with me! \(*0 0*)/''')
