import sys
#with "c:" I will mark my comments
# c: Already impressed what gemini did with my instructions BUT these are my observations:
#it did literally (almost) only what I told it to do. (Which is usually good)
# Now I am missing:
#A Welcome message that explains the player how he can play. For example: Choose your action by typing the number!
#(A message that tells the player if something does not work) I correct myself after reading the code: They exist but they need a time puffer.
#Longer showing time (of the sleeping message) for ALL messages -> time.sleep
#The use of the axt to get rid of planted plants so the player can plant new ones as a choice next to harvest
#I think it would be fun if the harvest gets rotten (only on the tree /bush= after 3 days of sleeping without harvesting. If the harvest is rotten offer the option to pick them and throw them away.

# --- Your exact ASCII Art definitions --- c: made the art myself
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

ground = ('''
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

appletree1 = ('''
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

appletree2 = ('''
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

appletree3 = ('''
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

berrybush1 = ('''
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

berrybush2 = ('''
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

berrybush3 = ('''
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

flower1 = ('''
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

flower2 = ('''
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

flower3 = ('''
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

# --- Game Lists & Dicts ---
shed_storage = [
    {"name": "watering can", "type": "tool", "use": 4, "count": 1},
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
    {"name": "flower", "type": "harvest", "count": 0, "price": 8}]

inventory = [
    {"name": "watering can", "type": "tool", "use": 0, "count": 0},
    {"name": "shovel", "type": "tool", "count": 0},
    {"name": "axt", "type": "tool", "count": 0},
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8},
    {"name": "money", "type": "currency", "count": 40}]  # Start with 40 to buy things

# Track plot states. Options: None (ground), "shoveled", or a dynamic plant dict
garden_plots = [None, None, None]


# --- Helper Functions ---
def get_inv_count():
    return sum(1 for item in inventory if item["type"] != "currency" and item["count"] > 0)


def get_item(source_list, name):
    for item in source_list:
        if item["name"] == name:
            return item
    return None


def clean_lines(lines_list):
    # Cleans trailing carriage returns and standardizes width <- c:before was very ugly, now very clean
    return [line.replace('\r', '').ljust(30) for line in lines_list if line.strip() or len(line) > 0][:21]


# Your signature print function, modified safely to load current garden state
def show_garden():
    # Setup standard assets
    s_lines = clean_lines(shed_lines)
    w_lines = clean_lines(well_lines)

    # Dynamically select what goes into the 3 middle spots
    middle_plots = []
    for plot in garden_plots:
        if plot is None:
            middle_plots.append(clean_lines(ground_lines))
        elif plot == "shoveled":
            middle_plots.append(clean_lines(shoveled_lines))
        else:
            g = plot["growth"]
            n = plot["name"]
            if n == "appletree":
                art = appletree1_lines if g == 1 else appletree2_lines if g == 2 else appletree3_lines #c:did not now u could do if else in one line
            elif n == "berrybush":
                art = berrybush1_lines if g == 1 else berrybush2_lines if g == 2 else berrybush3_lines
            elif n == "flowerseed":
                art = flower1_lines if g == 1 else flower2_lines if g == 2 else flower3_lines
            middle_plots.append(clean_lines(art))

    # Reassigning variable names to exactly match your requested zip format!
    # c:wanted gemini to keep the strategy I understood, gemini listened. But could have reduced shed and well since they don't change.
    berrybush2_lines_live = middle_plots[0]
    appletree3_lines_live = middle_plots[1]
    flower2_lines_live = middle_plots[2]

    print("\n" + "=" * 150)
    for a, b, c, d, e in zip(s_lines, berrybush2_lines_live, appletree3_lines_live, flower2_lines_live, w_lines):
        print(f"{a}{b}{c}{d}{e}")
    print("=" * 150)
    print(f" Wallet: {get_item(inventory, 'money')['count']} Money | Inventory Spaces: {get_inv_count()}/5")


# --- Location Routines ---
def go_shed():
    while True:
        print("\n--- SHED ---")
        for i, item in enumerate(shed_storage): #c: aha, enumerate keeps the +1 away and the list is created
            extra = f" (Uses: {item['use']})" if "use" in item else ""
            print(f"{i + 1}. {item['name'].capitalize()} [Qty: {item['count']}{extra}]")
        print("B. Back")

        choice = input("Pick an item number or 'B' to go back: ").strip().lower()
        if choice == 'b': break

        if choice.isdigit() and 1 <= int(choice) <= len(shed_storage): #c:seeing if input number is correct
            shed_item = shed_storage[int(choice) - 1]
            inv_item = get_item(inventory, shed_item["name"])
            act = input(f"Do you want to (P)ick up or (D)rop off {shed_item['name']}?: ").strip().lower()

            if act == 'p':
                if shed_item["count"] <= 0:
                    print("Shed is empty of this item!")
                elif get_inv_count() >= 5 and inv_item["count"] == 0:
                    print("Inventory full! drop something off first.")
                else:
                    shed_item["count"] -= 1
                    inv_item["count"] += 1
                    if "use" in shed_item: inv_item["use"] = shed_item["use"]
                    print(f"Picked up {shed_item['name']}.")
            elif act == 'd':
                if inv_item["count"] <= 0:
                    print("You don't have this item to drop off!")
                else:
                    inv_item["count"] -= 1
                    shed_item["count"] += 1
                    if "use" in inv_item: shed_item["use"] = inv_item["use"]
                    print(f"Stored {inv_item['name']} in the shed.")


def go_garden():
    while True:
        show_garden()
        print("\n--- GARDEN PLOTS ---")
        for i, plot in enumerate(garden_plots):
            status = "Empty Ground"
            if plot == "shoveled":
                status = "Shoveled Dirt"
            elif isinstance(plot, dict):
                status = f"{plot['name'].capitalize()} (Growth: {plot['growth']}/3, {'Watered' if plot['watered'] else 'Dry'})"
            print(f"{i + 1}. Plot {i + 1}: {status}")
        print("B. Back")

        choice = input("Select plot or 'B': ").strip().lower()
        if choice == 'b': break

        if choice.isdigit() and 1 <= int(choice) <= len(garden_plots):
            idx = int(choice) - 1
            plot = garden_plots[idx]

            print("\nActions: 1: Shovel | 2: Plant Seed | 3: Water | 4: Harvest")
            act = input("Action: ").strip()

            if act == '1':
                if get_item(inventory, "shovel")["count"] <= 0:
                    print("Need a shovel!")
                elif plot is not None:
                    print("Already worked ground!")
                else:
                    garden_plots[idx] = "shoveled"
                    print("Shoveled!")
            elif act == '2':
                if plot != "shoveled":
                    print("Shovel it first!")
                else:
                    seeds = [s for s in inventory if s["type"] == "seed" and s["count"] > 0]
                    if not seeds:
                        print("No seeds in inventory!")
                    else:
                        for s_idx, s in enumerate(seeds): print(f"{s_idx + 1}. {s['name']}")
                        s_choice = input("Pick a seed: ").strip()
                        if s_choice.isdigit() and 1 <= int(s_choice) <= len(seeds):
                            seed = seeds[int(s_choice) - 1]
                            seed["count"] -= 1
                            garden_plots[idx] = {"name": seed["name"], "growth": 1, "watered": False}
                            print(f"Planted {seed['name']}!")
            elif act == '3':
                can = get_item(inventory, "watering can")
                if can["count"] <= 0:
                    print("Need watering can!")
                elif can["use"] <= 0:
                    print("Can is empty!")
                elif not isinstance(plot, dict):
                    print("Nothing here to water!")
                elif plot["watered"]:
                    print("Already watered!")
                else:
                    can["use"] -= 1
                    plot["watered"] = True
                    print("Watered!")
            elif act == '4':
                if not isinstance(plot, dict):
                    print("Nothing to harvest here.")
                elif plot["growth"] < 3:
                    print("Not ready for harvesting.")
                else:
                    p_name = plot["name"]
                    yield_name = "apple" if p_name == "appletree" else "berry" if p_name == "berrybush" else "flower"
                    if p_name == "appletree" and get_item(inventory, "axt")["count"] <= 0:
                        print("Need an axt to cut down trees!")
                    else:
                        get_item(inventory, yield_name)["count"] += 1 #c:there needs to be an option if inventory is full, also this does not work. Axt needs to be a separate choice.
                        garden_plots[idx] = None
                        print(f"Harvested {yield_name}!")


def go_well():
    can = get_item(inventory, "watering can")
    if can["count"] <= 0:
        print("\nYou aren't carrying a watering can.")
    else:
        print(f"\nCan usage: [{can['use']}/4]")
        if input("Refill can? (y/n): ").strip().lower() == 'y':
            can["use"] = 4
            print("Refilled!")


def go_shop():
    wallet = get_item(inventory, "money")
    while True:
        print(f"\n--- SHOP (Wallet: {wallet['count']}) ---")
        print("1. Buy Seeds\n2. Sell Harvest\nB. Back")
        choice = input("Option: ").strip().lower()
        if choice == 'b': break

        if choice == '1':
            seeds = [s for s in shop if s["type"] == "seed"]
            for i, s in enumerate(seeds):
                print(f"{i + 1}. {s['name']} (${s['price']}) [Stock: {s['count']}]")
            idx = input("Buy seed number: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(seeds):
                s_item = seeds[int(idx) - 1]
                inv_item = get_item(inventory, s_item["name"])
                if s_item["count"] <= 0:
                    print("Out of stock!")
                elif wallet["count"] < s_item["price"]:
                    print("No money!")
                elif get_inv_count() >= 5 and inv_item["count"] == 0:
                    print("Inventory full!")
                else:
                    wallet["count"] -= s_item["price"]
                    s_item["count"] -= 1
                    inv_item["count"] += 1
                    print("Purchased!")
        elif choice == '2':
            harvests = [h for h in inventory if h["type"] == "harvest" and h["count"] > 0]
            if not harvests:
                print("Nothing to sell.")
            else:
                for i, h in enumerate(harvests):
                    print(f"{i + 1}. {h['name']} x{h['count']} (${h['price']} each)")
                idx = input("Sell number: ").strip()
                if idx.isdigit() and 1 <= int(idx) <= len(harvests):
                    h_item = harvests[int(idx) - 1]
                    qty = input(f"Amount (Max {h_item['count']}): ").strip()
                    if qty.isdigit() and 1 <= int(qty) <= h_item["count"]:
                        amt = int(qty)
                        h_item["count"] -= amt
                        wallet["count"] += amt * h_item["price"]
                        print("Sold!")


def look_inventory():
    print("\n--- INVENTORY ---")
    empty = True
    for item in inventory:
        if item["count"] > 0:
            empty = False
            extra = f" (Uses: {item['use']})" if "use" in item and item["type"] == "tool" else ""
            print(f"- {item['name'].capitalize()} x{item['count']}{extra}")
    if empty: print("Empty.")
    input("\nPress Enter to return...")


def sleep():
    print("\nSleeping... Zzz...")
    for plot in garden_plots:
        if isinstance(plot, dict) and plot["watered"]:
            if plot["growth"] < 3: plot["growth"] += 1
            plot["watered"] = False
    print("Morning! Plants grew!")


# --- Main Engine Loop ---
def main():
    while True:
        show_garden()
        print("\nMENU: 1: Shed | 2: Garden | 3: Well | 4: Shop | 5: Inventory | 6: Sleep | Q: Quit")
        choice = input("Choice: ").strip().lower()
        if choice == '1':
            go_shed()
        elif choice == '2':
            go_garden()
        elif choice == '3':
            go_well()
        elif choice == '4':
            go_shop()
        elif choice == '5':
            look_inventory()
        elif choice == '6':
            sleep()
        elif choice == 'q':
            sys.exit()


if __name__ == "__main__":
    main()