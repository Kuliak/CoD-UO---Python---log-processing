import os
import shutil


def create_map_file(file_name2, title2, games3, current_gam):
    if os.path.isfile(file_name2):
        file_name2 = file_name2[:-4] + "_2" + ".txt"
    with open(file_name2, "w") as outputfile:
        outputfile.write(title2 + "\n")
        games3[current_gam] = sorted(games3[current_gam].items(), key=lambda x: x[1]["kills"], reverse=True)

        for player in games3[current_gam]:
            outputfile.write(player[0].ljust(25))
            outputfile.write(str(player[1]["kills"]).rjust(10))
            outputfile.write(str(player[1]["deaths"]).rjust(10))
            outputfile.write("\n")
    return None


def create_new_game(games3, row_input1):
    """***************************************************************************"""
    """ Function ensures creating the new game.                                   """
    """ Firstly, function checks whether there was not a game with the same name, """
    """ if so, it puts 'x' in behind the map-name.                                """
    """ Secondly, function creates new dictionary for our new game in all-games   """
    """ dictionary.                                                               """
    """ Thirdly, function actualise the name of the current game.                 """
    """ -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - """
    """ Funkcia zaistuje vytvorenie novej hry.                                    """
    """ 1.) funkcia overi, ci uz neexistuje hra s rovnakym nazvom a typom hry,    """
    """     pokial ano, tak sa za meno mapy prida pismeno 'x'                     """
    """ 2.) funkcia vytvori novy slovnik pre nasu hru v slovniku vsetkych hier.   """
    """ 3.) funkcia aktualizuje sucasnu hru - zmeni nazov mapy a typ hry.         """
    """***************************************************************************"""
    my_index = 0
    row_input1 = row_input1[0:2] + row_input1[2].split(os.sep) + row_input1[3].split(os.sep)
    while (row_input1[row_input1.index("mapname") + 1], row_input1[row_input1.index("g_gametype") + 1],
           my_index) in games3:
        my_index += 1
    games3[(row_input1[row_input1.index("mapname") + 1], row_input1[row_input1.index("g_gametype") + 1], my_index)] = {}
    new_game1 = (row_input1[row_input1.index("mapname") + 1], row_input1[row_input1.index("g_gametype") + 1], my_index)
    return games3, new_game1


def game_initialization(row_input, games2, current_g, dir_name):
    if not (current_g is None):
        name = dir_name + "/Maps/" + current_g[0] + "_" + current_g[1] + ".txt"
        title = (current_g[0] + "_" + current_g[1]).ljust(25) + "Kills".rjust(10) + "Deaths".rjust(10)
        # create_map_file(name, title, games2, current_g)
        games2, new_game = create_new_game(games2, row_input) # vymazane current_g
    else:
        games2, new_game = create_new_game(games2, row_input)

    return games2, new_game


def check_color(row_input2, position):
    if "^" in row_input2[position]:
        row_input2[position] = row_input2[position][2:]
    return row_input2


def new_player(temp_dict, player_name, awards4):
    temp_dict[player_name] = {"total": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "dm": {"kills": 0, "deaths": 0},
                              "tdm": {"kills": 0, "deaths": 0},
                              "hq": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "ctf": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "sd": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "re": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "bel": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "dom": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "bas": {"kills": 0, "deaths": 0, "objective_score": 0},
                              "teamkills": 0,
                              "location": {},
                              # "location": {"head": 0,
                              #              "torso_upper": 0,
                              #              "torso_lower": 0,
                              #              "all_over": 0,
                              #              "leg_upper": 0,
                              #              "leg_lower": 0,
                              #              "arm_upper": 0,
                              #              "arm_lower"},
                              "weapons": {},
                              "wins": 0,
                              "longest_strike": 0,
                              "kills_sum": 0,
                              "multiple": {"2x": 0,
                                           "3x": 0,
                                           "4x": 0,
                                           "5x": 0,
                                           "6x": 0,
                                           "7x": 0,
                                           "8x": 0,
                                           "9x": 0,
                                           "10x": 0
                                           },
                              "multiple_temp": 0,
                              "first_kill": 0,
                              "ctf_captured": 0,
                              "ctf_assist": 0,
                              "ctf_pickup": 0,
                              "ctf_returned": 0,
                              "ctf_take": 0,
                              "ctf_defended": 0,
                              "radio_capture": 0,
                              "radio_destroy": 0,
                              "bomb_plant": 0,
                              "bomb_defuse": 0,
                              "bas_attacked": 0,
                              "bas_breached": 0,
                              "bas_defend": 0,
                              "bas_destroyed": 0,
                              "bas_defused": 0,
                              "bas_planted": 0,
                              "dom_captured": 0,
                              "bel_alive_tick": 0,
                              "re_pickup": 0,
                              "re_captured": 0
                             }
    for award in awards4:
        awards4[award][player_name] = 0
    return temp_dict, awards4


def game_join(row_input, players2, games2, awards2, current_g, player_aliases):
    row_input = check_color(row_input, 4)
    if not row_input[4] in player_aliases:
        # print(row_input)
        player_aliases[row_input[4]] = row_input[4]
        print("Dočasne pridaný hráč do aliasov: ", row_input[4])
        print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")
        # print(row_input)

    if not (player_aliases[row_input[4]] in players2):
        players2, awards2 = new_player(players2, player_aliases[row_input[4]], awards2)

    if not (player_aliases[row_input[4]] in games2[current_g]):
        games2[current_g][player_aliases[row_input[4]]] = {"kills": 0, "deaths": 0, "objective_score": 0}

    return players2, games2


def get_kill(row_input1, games3, current_gam, players3, num1, num2, kill_inc, player_aliases):
    row_input1 = check_color(row_input1, num1)
    row_input1 = check_color(row_input1, num2)

    players3[player_aliases[row_input1[num1]]]["total"]["deaths"] += 1
    players3[player_aliases[row_input1[num2]]]["total"]["kills"] += kill_inc

    players3[player_aliases[row_input1[num1]]][current_gam[1]]["deaths"] += 1
    players3[player_aliases[row_input1[num2]]][current_gam[1]]["kills"] += kill_inc

    games3[current_gam][player_aliases[row_input1[num1]]]["deaths"] += 1
    games3[current_gam][player_aliases[row_input1[num2]]]["kills"] += kill_inc

    players3[player_aliases[row_input1[num1]]]["longest_strike"] = max(players3[player_aliases[row_input1[num1]]]
                                                                       ["longest_strike"],
                                                                       players3[player_aliases[row_input1[num1]]]
                                                                       ["kills_sum"])
    players3[player_aliases[row_input1[num1]]]["kills_sum"] = 0
    players3[player_aliases[row_input1[num2]]]["kills_sum"] += kill_inc

    return games3, players3


def reset_multiple(players2):
    for player in players2:
        players2[player]["multiple_temp"] = 0
        players2[player]["first_kill"] = 0
    return players2


def add_multiple(row_input2, players4, numb2, player_aliases):
    if str(players4[player_aliases[row_input2[numb2]]]["multiple_temp"]) + "x" in \
            players4[player_aliases[row_input2[numb2]]]["multiple"]:
        players4[player_aliases[row_input2[numb2]]]["multiple"][str(players4[player_aliases[row_input2[numb2]]]
                                                                   ["multiple_temp"]) + "x"] += 1
    return players4


def check_multiple(row_input1, players3, num2, player_aliases):
    row_input1 = check_color(row_input1, num2)
    time_split = row_input1[0].split(":")
    time = int(time_split[0])*60 + int(time_split[1])

    if ((time - players3[player_aliases[row_input1[num2]]]["first_kill"] <= \
            players3[player_aliases[row_input1[num2]]]["multiple_temp"]*5) and (players3[player_aliases
            [row_input1[num2]]]["multiple_temp"] != 10)):
        players3[player_aliases[row_input1[num2]]]["multiple_temp"] += 1
    else:

        players3 = add_multiple(row_input1, players3, num2, player_aliases)
        players3[player_aliases[row_input1[num2]]]["multiple_temp"] = 1
        players3[player_aliases[row_input1[num2]]]["first_kill"] = time
        # print(time)

    return players3


def game_kill(row_input, players2, games2, awards2, awards_assign2, current_g, player_aliases):

    if current_g[1] == "dm":
        number1 = 4
        number2 = 7
    else:
        number1 = 5
        number2 = 9

    row_input = check_color(row_input, number1)
    row_input = check_color(row_input, number2)

    if row_input[-2] in awards_assign2:                                       # MOD_*
        if not row_input[-2] in ["MOD_MELEE", "MOD_FLAME"]:
            awards2[awards_assign2[row_input[-2]]][player_aliases[row_input[number1]]] += 1
            kill_increase = -1
            number2 = number1
        else:
            awards2[awards_assign2[row_input[-2]]][player_aliases[row_input[number2]]] += 1
            kill_increase = 1

    elif current_g[1] != "dm":
        if row_input[number1 - 1] == row_input[number2 - 1]:
            kill_increase = -1
            players2[player_aliases[row_input[number2]]]["teamkills"] += 1
            awards2["Double agent"][player_aliases[row_input[number2]]] += 1
        else:
            kill_increase = 1
    else:
        kill_increase = 1

    if not row_input[number1] in player_aliases:
        player_aliases[row_input[number1]] = row_input[number1]
        print("Dočasne pridaný hráč do aliasov: ", row_input[number1])
        print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")
        # print(row_input)
    if not row_input[number2] in player_aliases:
        player_aliases[row_input[number2]] = row_input[number2]
        print("Dočasne pridaný hráč do aliasov: ", row_input[number2])
        print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")
        # print(row_input)

    if not player_aliases[row_input[number1]] in players2:
        players2, awards2 = new_player(players2, player_aliases[row_input[number1]], awards2)
    if not player_aliases[row_input[number2]] in players2:
        players2, awards2 = new_player(players2, player_aliases[row_input[number2]], awards2)
    if not (player_aliases[row_input[number1]] in games2[current_g]):
        games2[current_g][player_aliases[row_input[number1]]] = {"kills": 0, "deaths": 0, "objective_score": 0}
    if not (player_aliases[row_input[number2]] in games2[current_g]):
        games2[current_g][player_aliases[row_input[number2]]] = {"kills": 0, "deaths": 0, "objective_score": 0}

    if kill_increase == 1:

        players2 = add_multiple(row_input, players2, number1, player_aliases)
        players2[player_aliases[row_input[number1]]]["multiple_temp"] = 0
        players2[player_aliases[row_input[number1]]]["first_kill"] = 0

        players2 = check_multiple(row_input, players2, number2, player_aliases)
        if row_input[-1] != "none":
            if row_input[-1] in players2[player_aliases[row_input[number2]]]["location"]:
                players2[player_aliases[row_input[number2]]]["location"][row_input[-1]]["kills"] += 1
            else:
                players2[player_aliases[row_input[number2]]]["location"][row_input[-1]] = {"kills": 1, "deaths": 0}
            if row_input[-1] in awards_assign2:                                   # HEADSHOT
                awards2[awards_assign2[row_input[-1]]][player_aliases[row_input[number2]]] += 1
            if row_input[-1] in players2[player_aliases[row_input[number1]]]["location"]:
                players2[player_aliases[row_input[number1]]]["location"][row_input[-1]]["deaths"] += 1
            else:
                players2[player_aliases[row_input[number1]]]["location"][row_input[-1]] = {"kills": 0, "deaths": 1}

        if row_input[-4] in awards_assign2:                                   # WEAPON in Team-game
            awards2[awards_assign2[row_input[-4]]][player_aliases[row_input[number2]]] += 1

            if row_input[-4] in players2[player_aliases[row_input[number1]]]["weapons"]:
                players2[player_aliases[row_input[number1]]]["weapons"][row_input[-4]]["deaths"] += 1
            else:
                players2[player_aliases[row_input[number1]]]["weapons"][row_input[-4]] = {"kills": 0, "deaths": 0}

            if row_input[-4] in players2[player_aliases[row_input[number2]]]["weapons"]:
                players2[player_aliases[row_input[number2]]]["weapons"][row_input[-4]]["kills"] += 1
            else:
                players2[player_aliases[row_input[number2]]]["weapons"][row_input[-4]] = {"kills": 0, "deaths": 0}

    games2, players2 = get_kill(row_input, games2, current_g, players2, number1, number2, kill_increase, player_aliases)

    return players2, games2, awards2


def game_action(row_input, players2, awards2, awards_assign2, objectives_assign, games2, current_g, player_aliases):
    row_input = check_color(row_input, -2)
    # print(row_input)
    if not (row_input[-2] in player_aliases):
        player_aliases[row_input[-2]] = row_input[-2]
        print("Dočasne pridaný hráč do aliasov: ", row_input[-2])
        print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")

    if not (player_aliases[row_input[-2]] in players2):
        players2, awards2 = new_player(players2, player_aliases[row_input[-2]], awards2)
    if not (player_aliases[row_input[-2]] in games2[current_g]):
        games2[current_g][player_aliases[row_input[-2]]] = {"kills": 0, "deaths": 0, "objective_score": 0}

    if row_input[-1] in awards_assign2:
        awards2[awards_assign2[row_input[-1]]][player_aliases[row_input[-2]]] += 1

    if row_input[-1] in objectives_assign:
        players2[player_aliases[row_input[-2]]]["total"]["objective_score"] += \
            objectives_assign[row_input[-1]]["points"]
        players2[player_aliases[row_input[-2]]][objectives_assign[row_input[-1]]["gametype"]]["objective_score"] += \
            objectives_assign[row_input[-1]]["points"]
        players2[player_aliases[row_input[-2]]][row_input[-1]] += 1
        games2[current_g][player_aliases[row_input[-2]]]["objective_score"] += \
            objectives_assign[row_input[-1]]["points"]

    return players2, awards2, games2


def add_win(row_input, players2, awards2, player_aliases):
    for i in range(len(row_input) // 2):
        row_input = check_color(row_input, 2*i + 1)
        if not (row_input[2*i + 1]) in player_aliases:
            player_aliases[row_input[2*i + 1]] = row_input[2*i + 1]
            print("Dočasne pridaný hráč do aliasov: ", row_input[2*i + 1])
            print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")

        if not (player_aliases[row_input[2*i + 1]] in players2):
            players2, awards2 = new_player(players2, player_aliases[row_input[2*i + 1]], awards2)
        players2[player_aliases[row_input[2*i + 1]]]["wins"] += 1
    return players2, awards2


def extract_info(row, players1, games1, awards1, awards_assign1, current, dir_name, win_count, objectives_assign,
                 player_aliases):
    # print(row)
    # print(players1)
    # print(row)
    if row[1] == "InitGame:":
        players1 = reset_multiple(players1)
        if current is None:
            games1, current = game_initialization(row, games1, current, dir_name)
        elif current[1] in ["re", "sd"]:
            if max(win_count[current[1]]["axis"], win_count[current[1]]["allies"]) == win_count[current[1]]["limit"]:
                win_count[current[1]]["axis"] = 0
                win_count[current[1]]["allies"] = 0
                games1, current = game_initialization(row, games1, current, dir_name)
            else:
                help_temp = row[3].split(os.sep)
                if not (help_temp[help_temp.index("mapname") + 1] in current[0]):
                    games1, current = game_initialization(row, games1, current, dir_name)

        else:
            games1, current = game_initialization(row, games1, current, dir_name)

    elif row[1] == "J":
        if len(row) != 5:    # nespravny pocet argumentov
            print("Nespravny pocet argumentov ({}), ocakavany pocet: {}".format(len(row), 5))
            print("Riadok: ", row)
            return -1, -1, -1, -1, -1
        players1, games1 = game_join(row, players1, games1, awards1, current, player_aliases)
    elif row[1] == "K":
        players1, games1, awards1 = game_kill(row, players1, games1, awards1, awards_assign1, current, player_aliases)
    elif row[1] == "A":
        if len(row) != 7:    # nespravny pocet argumentov
            print("Nespravny pocet argumentov ({}), ocakavany pocet: {}".format(len(row), 7))
            print("Riadok: ", row)
            return -1, -1, -1, -1, -1
        players1, awards1, games1 = game_action(row, players1, awards1, awards_assign1, objectives_assign, games1,
                                                current, player_aliases)
    elif row[1] == "W" and not(current[1] in ["dm", "bel"]):
        if current[1] in ["re", "sd"]:
            win_count[current[1]][row[2]] += 1
            if max(win_count[current[1]]["axis"], win_count[current[1]]["allies"]) == win_count[current[1]]["limit"]:
                players1, awards1 = add_win(row[3:], players1, awards1, player_aliases)
        else:
            players1, awards1 = add_win(row[3:], players1, awards1, player_aliases)
    elif row[1] == "Item":
        if row[-1] in awards_assign1:                                   # FIRST AID KIT
            if not (row[-2] in player_aliases):
                player_aliases[row[-2]] = row[-2]
                print("Dočasne pridaný hráč do aliasov: ", row[-2])
                print("Dôvod: Meno daného hráča nie je uvedené v súbore ALIASES.TXT\n")
            if not (player_aliases[row[-2]] in players1):
                players1, awards1 = new_player(players1, player_aliases[row[-2]], awards1)
            awards1[awards_assign1[row[-1]]][player_aliases[row[-2]]] += 1

    return players1, games1, awards1, current, win_count


def add_ratio(players1, games1, gametypes):
    for player in players1:
        for gtype in gametypes:
            if players1[player][gtype]["deaths"] == 0:
                players1[player][gtype]["ratio"] = 0
            else:
                players1[player][gtype]["ratio"] = round(players1[player][gtype]["kills"]
                                                         / players1[player][gtype]["deaths"], 2)

    for map in games1:
        for player in games1[map]:
            if games1[map][player]["deaths"] == 0:
                games1[map][player]["ratio"] = 0
            else:
                games1[map][player]["ratio"] = round(games1[map][player]["kills"] / games1[map][player]["deaths"], 2)
    return players1, games1


def add_difference(players1, games1, gametypes):
    for player in players1:
        for gtype in gametypes:
            players1[player][gtype]["difference"] = players1[player][gtype]["kills"] - players1[player][gtype]["deaths"]

    for map in games1:
        for player in games1[map]:
            games1[map][player]["difference"] = games1[map][player]["kills"] - games1[map][player]["deaths"]
    return players1, games1


def add_total_score(players1, games1, gametypes):
    for player in players1:
        for gtype in gametypes:
            players1[player][gtype]["total score"] = players1[player][gtype]["kills"] \
                                                     + players1[player][gtype]["objective_score"]
    for map in games1:
        for player in games1[map]:
            # print(map)
            # print(player)
            # print(games1)
            games1[map][player]["total score"] = games1[map][player]["kills"] + games1[map][player]["objective_score"]

    return players1, games1

