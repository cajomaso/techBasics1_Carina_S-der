import sys
import time

# c: This shall be the final version
# c: The Ascii-Art as well as the dictionaries are 99% written by me. (I added 1% of the dictionaries through prompts, since that is faster than adding them manually.
# c: The functions are written by gemini. But I prompted gemini how they should be written. Since there was a lot of what I wanted to do with this game, this was way faster. Writing the functions by myself would have taken too long for a weeks assignment.
# c: I read through the whole code and made sure that I understood what Gemini did. Through this I learn of more uses of code, example: enumerate().
# c: If my game was a little smaller I would've written the code myself but my Imagination ran wild and I was too impatient :)
# c: Impressed how well Gemini interpreted my prompts. But sometimes it needed nudges in the right direction.

# c: First prompt: also given were my ascii art and the dictionaries, so gemini could work with given keys such as growth or use.
# #functions
# #inventory limited by 5 spaces
# #garden is always shown but updated after changes
# #starting point of garden is shed, ground, ground, ground, well. only ground can be changed by shoveling and then planting seed. Shoveling is pnly able through using the shovel in inventory.
# #inventory in beginning only has money. Player needs to buy seeds in shop and get shovel and watering can from shed to progress.
# #menu shown below garden. Options: Go to shed, go to garden, go to well, go to shop, look in inventory, go sleep. Enable a go back.
# #Go to Shed: Menu now shows options of listing sheds item names. one can pickup those items or leave tools and seeds.
# #sleep: if plant is watered growth goes up, picture presented goes up. Max is 3.
# # go to garden: First only shoveling is possible, after shoveling planting, after planting watering.
# #go to well: here you can fill watering can: use goes up to 4 again. watering is limited by use
# #open shop
# #buy
# #list of seeds and how many are available as well as price
# #sell
# #list of your harvest, how many you can sell and for what price
# # go to inventory: shows what is in your inventory

# more prompts below the game

# --- Your exact ASCII Art definitions ---
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
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25, "fruit": 3,
     "times_harvested": 0},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15, "fruit": 5,
     "times_harvested": 0},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5, "fruit": 1,
     "times_harvested": 0},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8}]

shop = [
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 4, "price": 25, "fruit": 3,
     "times_harvested": 0},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 4, "price": 15, "fruit": 5,
     "times_harvested": 0},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 10, "price": 5, "fruit": 1,
     "times_harvested": 0},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8}]

inventory = [
    {"name": "watering can", "type": "tool", "use": 0, "count": 0},
    {"name": "shovel", "type": "tool", "count": 0},
    {"name": "axt", "type": "tool", "count": 0},
    {"name": "appletree", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 25, "fruit": 3,
     "times_harvested": 0},
    {"name": "berrybush", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 15, "fruit": 5,
     "times_harvested": 0},
    {"name": "flowerseed", "type": "seed", "growth": 1, "watered": False, "count": 0, "price": 5, "fruit": 1,
     "times_harvested": 0},
    {"name": "apple", "type": "harvest", "count": 0, "price": 5},
    {"name": "berry", "type": "harvest", "count": 0, "price": 1},
    {"name": "flower", "type": "harvest", "count": 0, "price": 8},
    {"name": "money", "type": "currency", "count": 40}]

garden_plots = [None, None, None]


# --- Helper Functions ---
def msg(text, delay=1.8):
    print(f"\n>> {text}")
    time.sleep(delay)


def get_inv_count():
    return sum(1 for item in inventory if item["type"] != "currency" and item["count"] > 0)


def get_item(source_list, name):
    for item in source_list:
        if item["name"] == name:
            return item
    return None


def clean_lines(lines_list):
    return [line.replace('\r', '').ljust(30) for line in lines_list if line.strip() or len(line) > 0][:21]


def show_garden():
    s_lines = clean_lines(shed_lines)
    w_lines = clean_lines(well_lines)

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
                art = appletree1_lines if g == 1 else appletree2_lines if g == 2 else appletree3_lines
            elif n == "berrybush":
                art = berrybush1_lines if g == 1 else berrybush2_lines if g == 2 else berrybush3_lines
            elif n == "flowerseed":
                art = flower1_lines if g == 1 else flower2_lines if g == 2 else flower3_lines
            middle_plots.append(clean_lines(art))

    print("\n" + "=" * 150)
    for combined_row in zip(s_lines, *middle_plots, w_lines):
        print("".join(combined_row))
    print("=" * 150)
    print(f" Wallet: {get_item(inventory, 'money')['count']} Money | Inventory Spaces: {get_inv_count()}/5")


# --- Location Routines ---
def go_shed():
    while True:
        print("\n--- SHED ---")
        act = input("Do you want to (P)ick up or (D)rop off items? ('B' to go back): ").strip().lower()
        if act == 'b': break

        if act == 'p':
            available_items = [i for i in shed_storage if i["count"] > 0]
            if not available_items:
                msg("The shed is empty right now!")
                continue

            print("\nAvailable in Shed:")
            for i, item in enumerate(available_items):
                extra = f" (Uses: {item['use']})" if "use" in item else ""
                print(f"{i + 1}. {item['name'].capitalize()} [Qty: {item['count']}{extra}]")
            print("B. Back")

            choice = input("Pick an item number to pick up or 'B': ").strip().lower()
            if choice == 'b': continue

            if choice.isdigit() and 1 <= int(choice) <= len(available_items):
                shed_item = available_items[int(choice) - 1]
                inv_item = get_item(inventory, shed_item["name"])

                if get_inv_count() >= 5 and inv_item["count"] == 0:
                    msg("Inventory full! Drop something off first.")
                else:
                    shed_item["count"] -= 1
                    inv_item["count"] += 1
                    if "use" in shed_item: inv_item["use"] = shed_item["use"]
                    msg(f"Picked up {shed_item['name']}.")
            else:
                msg("Invalid item choice.")

        elif act == 'd':
            carried_items = [i for i in inventory if i["type"] != "currency" and i["count"] > 0]
            if not carried_items:
                msg("You don't have anything to drop off!")
                continue

            print("\nYour Carryings:")
            for i, item in enumerate(carried_items):
                extra = f" (Uses: {item['use']})" if "use" in item and item["type"] == "tool" else ""
                print(f"{i + 1}. {item['name'].capitalize()} x{item['count']}{extra}")
            print("B. Back")

            choice = input("Pick an item number to store in the shed or 'B': ").strip().lower()
            if choice == 'b': continue

            if choice.isdigit() and 1 <= int(choice) <= len(carried_items):
                inv_item = carried_items[int(choice) - 1]
                shed_item = get_item(shed_storage, inv_item["name"])

                inv_item["count"] -= 1
                shed_item["count"] += 1
                if "use" in inv_item: shed_item["use"] = inv_item["use"]
                msg(f"Stored {inv_item['name']} safely in the shed.")
            else:
                msg("Invalid item choice.")
        else:
            msg("Command option not recognized.")


def go_garden():
    while True:
        show_garden()
        print("\n--- GARDEN PLOTS ---")
        for i, plot in enumerate(garden_plots):
            status = "Empty Ground"
            if plot == "shoveled":
                status = "Shoveled Dirt"
            elif isinstance(plot, dict):
                water_status = 'Watered' if plot['watered'] else 'Dry'

                if plot.get("rotten"):
                    condition = "ROTTEN!"
                    days_str = ""
                elif plot.get("needs_recovery"):
                    condition = "Recovering"
                    days_str = f" | Days till harvest: {plot['recovery_days_left']}"
                else:
                    condition = f"Growth: {plot['growth']}/3"
                    days_left = 3 - plot["growth"]
                    days_str = f" | Days till harvest: {days_left}" if days_left > 0 else " | Ready!"

                status = f"{plot['name'].capitalize()} ({condition}, {water_status}){days_str}"
            print(f"{i + 1}. Plot {i + 1}: {status}")
        print("B. Back")

        choice = input("Select plot or 'B': ").strip().lower()
        if choice == 'b': break

        if choice.isdigit() and 1 <= int(choice) <= len(garden_plots):
            idx = int(choice) - 1
            plot = garden_plots[idx]

            print("\nActions: 1: Shovel | 2: Plant Seed | 3: Water | 4: Harvest | 5: Axe Clean")
            act = input("Action: ").strip()

            if act == '1':
                if get_item(inventory, "shovel")["count"] <= 0:
                    msg("Need a shovel!")
                elif plot is not None:
                    msg("Already worked ground!")
                else:
                    garden_plots[idx] = "shoveled"
                    msg("Shoveled!")
            elif act == '2':
                if plot != "shoveled":
                    msg("Shovel it first!")
                else:
                    seeds = [s for s in inventory if s["type"] == "seed" and s["count"] > 0]
                    if not seeds:
                        msg("No seeds in inventory!")
                    else:
                        for s_idx, s in enumerate(seeds): print(f"{s_idx + 1}. {s['name']}")
                        s_choice = input("Pick a seed: ").strip()
                        if s_choice.isdigit() and 1 <= int(s_choice) <= len(seeds):
                            seed = seeds[int(s_choice) - 1]
                            seed["count"] -= 1
                            garden_plots[idx] = {
                                "name": seed["name"],
                                "growth": 1,
                                "watered": False,
                                "days_at_max": 0,
                                "rotten": False,
                                "fruit": seed["fruit"],
                                "times_harvested": 0,
                                "needs_recovery": False,
                                "recovery_days_left": 0
                            }
                            msg(f"Planted {seed['name']}!")
            elif act == '3':
                can = get_item(inventory, "watering can")
                if can["count"] <= 0:
                    msg("Need a watering can!")
                elif can["use"] <= 0:
                    msg("Can is empty! Refill at the well.")
                elif not isinstance(plot, dict):
                    msg("Nothing here to water!")
                elif plot["watered"]:
                    msg("Already watered today!")
                else:
                    can["use"] -= 1
                    plot["watered"] = True
                    msg("Watered!")
            elif act == '4':
                if not isinstance(plot, dict):
                    msg("Nothing here to harvest.")
                elif plot.get("rotten"):
                    clean = input("The crop is rotten! Throw it away to clear the plot? (y/n): ").strip().lower()
                    if clean == 'y':
                        garden_plots[idx] = None
                        msg("Threw away the rotten crop. The ground is clear again.")
                elif plot.get("needs_recovery") or plot["growth"] < 3:
                    msg("The plant isn't ready to harvest yet.")
                else:
                    # HEARTH ACTION: Cleaned out the axt check entirely here!
                    p_name = plot["name"]
                    yield_name = "apple" if p_name == "appletree" else "berry" if p_name == "berrybush" else "flower"

                    yield_amount = plot["fruit"]
                    get_item(inventory, yield_name)["count"] += yield_amount
                    plot["times_harvested"] += 1

                    if p_name == "flowerseed":
                        garden_plots[idx] = None
                        msg(f"Harvested {yield_amount} fresh {yield_name}(s)! The flower is spent.")
                    elif p_name == "berrybush" and plot["times_harvested"] >= 3:
                        garden_plots[idx] = None
                        msg(f"Harvested {yield_amount} fresh {yield_name}(s)! The berrybush reached its final cycle and died.")
                    elif p_name == "appletree" and plot["times_harvested"] >= 5:
                        garden_plots[idx] = None
                        msg(f"Harvested {yield_amount} fresh {yield_name}(s)! The appletree reached its final cycle and died.")
                    else:
                        plot["needs_recovery"] = True
                        plot["recovery_days_left"] = 2
                        plot["days_at_max"] = 0
                        plot["rotten"] = False
                        msg(f"Harvested {yield_amount} fresh {yield_name}(s)! The plant is harvested but remains standing while it grows new fruit.")
            elif act == '5':
                # AXE ACTION: Strictly kept for premature removal actions
                if get_item(inventory, "axt")["count"] <= 0:
                    msg("You need an axt in your inventory to clear plants!")
                elif not isinstance(plot, dict):
                    msg("There is no plant here to clear.")
                else:
                    confirm = input(
                        f"Are you sure you want to chop down the {plot['name']}? You won't yield anything. (y/n): ").strip().lower()
                    if confirm == 'y':
                        garden_plots[idx] = None
                        msg("Chop! The plant was removed and the plot is reset.")
        else:
            msg("Invalid plot selection.")


def go_well():
    can = get_item(inventory, "watering can")
    if can["count"] <= 0:
        msg("You aren't carrying a watering can.")
    else:
        print(f"\nCan usage: [{can['use']}/4]")
        if input("Refill can? (y/n): ").strip().lower() == 'y':
            can["use"] = 4
            msg("Refilled watering can!")


def go_shop():
    wallet = get_item(inventory, "money")
    while True:
        print(f"\n--- SHOP (Wallet: {wallet['count']} Money) ---")
        print("1. Buy Seeds\n2. Sell Harvest\nB. Back")
        choice = input("Option: ").strip().lower()
        if choice == 'b': break

        if choice == '1':
            seeds = [s for s in shop if s["type"] == "seed"]
            for i, s in enumerate(seeds):
                print(f"{i + 1}. {s['name'].capitalize()} (${s['price']}) [Stock: {s['count']}]")
            idx = input("Buy seed number: ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(seeds):
                s_item = seeds[int(idx) - 1]
                inv_item = get_item(inventory, s_item["name"])
                if s_item["count"] <= 0:
                    msg("Out of stock!")
                elif wallet["count"] < s_item["price"]:
                    msg("Not enough money!")
                elif get_inv_count() >= 5 and inv_item["count"] == 0:
                    msg("Inventory full!")
                else:
                    wallet["count"] -= s_item["price"]
                    s_item["count"] -= 1
                    inv_item["count"] += 1
                    msg(f"Purchased 1 {s_item['name']}!")
            else:
                msg("Invalid seed item number chosen.")
        elif choice == '2':
            harvests = [h for h in inventory if h["type"] == "harvest" and h["count"] > 0]
            if not harvests:
                msg("Nothing to sell in your inventory.")
                continue

            for i, h in enumerate(harvests):
                print(f"{i + 1}. {h['name'].capitalize()} x{h['count']} (${h['price']} each)")
            print("B. Back")

            idx = input("Sell number or 'B': ").strip().lower()
            if idx == 'b': continue

            if idx.isdigit() and 1 <= int(idx) <= len(harvests):
                h_item = harvests[int(idx) - 1]
                qty = input(f"Amount (Max {h_item['count']}): ").strip()
                if qty.isdigit() and 1 <= int(qty) <= h_item["count"]:
                    amt = int(qty)
                    h_item["count"] -= amt
                    earnings = amt * h_item["price"]
                    wallet["count"] += earnings
                    msg(f"Sold {amt} {h_item['name']}(s) for {earnings} Money!")
                else:
                    msg("Invalid quantity amount specified.")
            else:
                msg("Invalid input. That number does not fit any listed item.")


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
    print("\n*Yawn* Going to bed... ")
    msg("Sleeping... Zzz...", delay=2.5)

    for plot in garden_plots:
        if isinstance(plot, dict):
            if plot["growth"] == 3 and not plot.get("needs_recovery"):
                plot["days_at_max"] += 1
                if plot["days_at_max"] >= 3:
                    plot["rotten"] = True

            if plot["watered"]:
                if plot.get("needs_recovery"):
                    plot["recovery_days_left"] -= 1
                    if plot["recovery_days_left"] <= 0:
                        plot["needs_recovery"] = False
                elif plot["growth"] < 3:
                    plot["growth"] += 1

                plot["watered"] = False

    msg("Good morning! A brand new day has arrived.")


# --- Main Engine Loop ---
def main():
    print("\n" + "=" * 60)
    print("      WELCOME TO MINI TEXT-GARDENER!")
    print("=" * 60)
    print("How to play: ")
    print("- Interact with your world by typing the listed option number.")
    print("- To progress, go to the SHED to grab tools (Shovel, Can, Axe).")
    print("- Buy seeds from the SHOP and look in your INVENTORY to manage space.")
    print("- Shovel ground first, then plant, water, and sleep to watch it grow!")
    print("- Warning: Fully grown crops rot if left unharvested for 3 days!")
    print("=" * 60)
    input("Press Enter to begin your journey...")

    while True:
        show_garden()
        print("\nMAIN MENU: 1: Shed | 2: Garden | 3: Well | 4: Shop | 5: Inventory | 6: Sleep | Q: Quit")
        choice = input("Where do you want to go?: ").strip().lower()
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
            print("\nThanks for playing!")
            sys.exit()
        else:
            msg("Command not recognized. Please choose a valid menu number.")


if __name__ == "__main__":
    main()

#prompts
 # Now I am missing:
#A Welcome message that explains the player how he can play. For example: Choose your action by typing the number!
#(A message that tells the player if something does not work) I correct myself after reading the code: They exist but they need a time puffer.
#Longer showing time (of the sleeping message) for ALL messages
#The use of the axt to get rid of planted plants so the player can plant new ones as a choice next to harvest
#I think it would be fun if the harvest gets rotten (only on the tree /bush= after 3 days of sleeping without harvesting. If the harvest is rotten offer the option to pick them and throw them away.

# c: The shed also shows items that are not there, I want to change that. But still give directions to drop an item. First ask for input if player wants to drop item, then let him choose. He cannot drop money.
# c: only one apple is a bit weak, make it 3, also make it 5 berries. You can add these to the dictionaries as "fruit": 3 or "fruit": 5 and only make them available if growth == 3
# c: do we still need a, b, c, d and e for printing? Just put a, b and c and add the s_lines and w_lines. Maybe similar to this: s_lines + a + b+ c+ w_lines

# c: after choosing to pick up something at the shed you cannot go back. Add that option.
 # c: when selling harvest give a message for invalid input if the input does not fit any list number.
# c: the berrybush only dies after its been harvested three times. After it has been harvested it needs 2 sleeps to be able to harvest again. For this add to the dictionary "times_harvested": 0 when the count reaches 4 it dies. Do the same for apples but after 5 harvestings.
# c: Also for every planted plant show "Days till harvest: "

