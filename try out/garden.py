
#programm a game as descripted in the comments below. Keep it as simple as possible. It should be playable by text commands only.

#art selfdrawn on https://www.asciiart.eu/ascii-draw-studio/app
shed = ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                  ////        \n
             /////  ║         \n
         ////       ║         \n
    /////           ║         \n
 ///                ║         \n
  ║ ┌─┬─┐ ┌──────┐  ║         \n
  ║ │ │ │ │      │  ║         \n
  ║ │ │ │ │      │  ║         \n
  ║ ╘═╧═╛ │    ¬ │  ║         \n
  ║       │      │  ║         \n
__║_______│______│__║_________''')
shed_lines = shed.split('\n')

well = ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
            ▄▄▄▄▄▄            \n
          ▄▀  ▀▀  ▀▄          \n
        ▄▀┌════════┐▀▄        \n
         ││        ││         \n
         │╞══≡≡≡≡══╡│┐        \n
         ││   │    ││└─       \n
         │╘════════╛│         \n
_________├──────────┤_________\n
         ╘══════════╛         ''')
well_lines = well.split('\n')

ground =('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
______________________________''')
ground_lines = ground.split('\n')

shoveled = ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
shoveled_lines = shoveled.split('\n')

appletree1= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
            (~~)              \n
           (~  ~)             \n
          ( ~   ~)            \n
            ~││~              \n
             ││               \n
             ││               \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
appletree1_lines = appletree1.split('\n')

appletree2= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
           (~~~~)             \n
         (    ~   )           \n
        (  ~~    ~ )          \n
         (   ~ ~  )           \n
           ~~║║~~             \n
             ║║               \n
             ║║               \n
             ║║               \n
             ║║               \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
appletree2_lines = appletree2.split('\n')

appletree3= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
          (~~~~~~)            \n
       (~~ ~      ~~)         \n
     (                )       \n
    (          ~~~     )      \n
   (   ~                )     \n
  (                   ~  )    \n
   (       ~      ~~    )     \n
    ( ~                )      \n
      ~(      ~     )         \n
         ~~~║  ║~~~           \n
            ║  ║              \n
            ║  ║              \n
            ║ O║              \n
            ║  ║              \n
            ║  ║              \n
            ║  ║              \n
            ║  ║              \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
appletree3_lines = appletree3.split('\n')

berrybush1=('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
            (~~)              \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
berrybush1_lines = berrybush1.split('\n')

berrybush2=('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
           ( ~~ )             \n
          ( ~ ~ ~)            \n
           (~  ~)             \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
berrybush2_lines = berrybush2.split('\n')

berrybush3=('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
             ~~               \n
          (~   ~ )            \n
        (    ~  ~  )          \n
       ( ~          )         \n
        (   ~   ~  )          \n
          (   ~~ )            \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
berrybush3_lines = berrybush3.split('\n')

flower1= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
            _  _              \n
           |_|/_/             \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
flower1_lines = flower1.split('\n')

flower2= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
             O _              \n
             │/_/             \n
             │                \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
flower2_lines = flower2.split('\n')

flower3= ('''
.oOo.oOo.oOo.oOo.oOo.oOo.oOo. \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
                              \n
             _                \n
           _( )_              \n
          (_(0)_)             \n
            (_)_              \n
             │/_/             \n
             │                \n
             │                \n
___________/ⁿⁿⁿⁿⁿⁿ|_____________''')
flower3_lines = flower3.split('\n')

# lists of dictionaries

shed = [
    {"name": "watering can", "type": "tool", "use": 4, "count": 1 },
    {"name": "shovel", "type": "tool", "count": 1},
    {"name": "axt", "type": "tool", "count": 1},
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8}]

shop = [
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 4, "price": 25},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 4, "price": 15},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 10, "price": 5},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8},
    #{"name": "money", "type": "currency", "count": 0}
    ]

inventory = [
    {"name": "watering can", "type": "tool", "use": 4, "count": 0 },
    {"name": "shovel", "type": "tool", "count": 0},
    {"name": "axt", "type": "tool", "count": 0},
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8},
    {"name": "money", "type": "currency", "count": 0}]

garden= [
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8}  ]

#this method of printing was introduced by gemini
def show_garden():
    for a, b, c, d, e in zip(shed_lines, berrybush2_lines,appletree3_lines, flower2_lines, well_lines):
        print(f"{a}{b}{c}{d}{e}")

#functions
#inventory limited by 5 spaces
#garden is always shown but updated after changes
#starting point of garden is shed, ground, ground, ground, well. only ground can be changed by shoveling and then planting seed. Shoveling is pnly able through using the shovel in inventory.
#inventory in beginning only has money. Player needs to buy seeds in shop and get shovel and watering can from shed to progress.
#menu shown below garden. Options: Go to shed, go to garden, go to well, go to shop, look in inventory, go sleep. Enable a go back.
#Go to Shed: Menu now shows options of listing sheds item names. one can pickup those items or leave tools and seeds.
#sleep: if plant is watered growth goes up, picture presented goes up. Max is 3.
# go to garden: First only shoveling is possible, after shoveling planting, after planting watering.
#go to well: here you can fill watering can: use goes up to 4 again. watering is limited by use
#open shop
    #buy
        #list of seeds and how many are available as well as price
    #sell
        #list of your harvest, how many you can sell and for what price

# go to inventory: shows what is in your inventory
