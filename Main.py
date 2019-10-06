from Output_HTML import create_main_file, create_file_awards, create_file_kills, create_file_map, \
                        create_file_other, create_file_players, create_file_team_wins
from Input import get_aliases, get_configuration, create_awards_assign, create_objective_assign, erase_blank_space
from CORE import extract_info, add_ratio, add_difference, add_total_score
import os


def analyze(input_file2, objectives_input):
    players = {}
    games = {}
    awards = {}
    current_game = None
    gametypes_categories = ["total", "dm", "tdm", "hq", "ctf", "sd", "re", "bel", "dom", "bas"]
    win_count = {"sd": {"axis": 0, "allies": 0, "limit": 3},
                 "re": {"axis": 0, "allies": 0, "limit": 3}
                 }

    if os.path.isfile("./config.txt"):
        dir_name, win_count, awards_top, input_file1 = get_configuration("./config.txt", win_count)
        if dir_name == -1:
            return 1
    else:
        print("*****************   E R R O R   *****************\n"
              "Nenasiel sa konfiguracny subor pomocou relativnej cesty => './config.txt'\n")
        return 2

    if not os.path.isfile(input_file1):
        print("*****************   E R R O R   *****************\n"
              "Nenasiel sa log subor cez relativnu cestu =>'", input_file1, "'\n")
        return 2

    temp_dir_name = dir_name + "/Maps"
    os.makedirs(temp_dir_name)
    temp_dir_name = dir_name + "/results"
    os.makedirs(temp_dir_name)

    """" Now we will create dictionary based on awards names from "awards_criteria.txt" file.
         Then, we will create dictionary that will help us assign specific award to the input given,
         for example: "enfield_mp" -> "Rifleman"
    """
    awards_assign = create_awards_assign(input_file2, awards)
    objectives_assign = create_objective_assign(objectives_input)
    player_aliases = get_aliases("./aliases.txt")
    # print(player_aliases)

    with open(input_file1, "r") as game_log, open("./results.txt", "w") as results:
        for line in game_log:            # for each line in game_log
            line_split = line.split(";")
            line_split = line_split[0].split(" ") + line_split[1:]

            line_split = erase_blank_space(line_split)
            if len(line_split) > 2:
                # if "none" in line_split:
                #     print(line_split)
                players, games, awards, current_game, win_count = extract_info(line_split,
                                                                               players,
                                                                               games,
                                                                               awards,
                                                                               awards_assign,
                                                                               current_game,
                                                                               dir_name,
                                                                               win_count,
                                                                               objectives_assign,
                                                                               player_aliases)
                if players == -1:
                    return 3
                output = ""
                for string in line_split:
                    output = output + string
                results.write(output)

    players, games = add_ratio(players, games, gametypes_categories)
    players, games = add_difference(players, games, gametypes_categories)
    players, games = add_total_score(players, games, ["total", "hq", "ctf", "sd", "re", "bel", "dom", "bas"])

    # name = dir_name + "/Maps/" + current_game[0] + "_" + current_game[1] + ".txt"
    # title = (current_game[0] + "_" + current_game[1]).ljust(25) + "Kills".rjust(10) + "Deaths".rjust(10)
    # create_map_file(name, title, games, current_game)
    player_aliases = get_aliases("./aliases.txt")

    gametypes_categories = ["total", "hq", "ctf", "sd", "re", "bel", "dom", "bas"]
    for gametype in gametypes_categories:
        create_file_kills(dir_name, "./HTML/Deathmatch.html", players, gametype, ["kills", "deaths", "ratio",
                                     "difference", "objective_score", "total score"], 83, "results", player_aliases)

    create_file_kills(dir_name, "./HTML/Deathmatch.html", players, "dm", ["kills", "deaths", "ratio", "difference"], 83,
                      "results", player_aliases)

    create_file_kills(dir_name, "./HTML/Deathmatch.html", players, "tdm",
                      ["kills", "deaths", "ratio", "difference"], 83, "results", player_aliases)

    create_file_awards(dir_name, "./HTML/Awards.html", awards, awards_top)

    create_file_team_wins(dir_name, "./HTML/Team_wins.html", players)

    create_file_kills(dir_name, "./HTML/special.html", players, "multiple",
                      ["2x", "3x", "4x", "5x", "6x", "7x", "8x", "9x", "10x"], 97, "results", player_aliases)

    create_file_other(dir_name, "./HTML/special.html", players, "ctf_stats",
                      ["ctf_captured", "ctf_assist", "ctf_returned", "ctf_take", "ctf_defended"],
                      player_aliases)

    create_file_other(dir_name, "./HTML/special.html", players, "bas_stats",
                      ["bas_attacked", "bas_breached", "bas_defend", "bas_destroyed", "bas_defused", "bas_planted"],
                      player_aliases)

    create_file_other(dir_name, "./HTML/special.html", players, "other",
                      ["longest_strike", "radio_capture", "radio_destroy", "bomb_plant", "bomb_defuse", "dom_captured",
                       "bel_alive_tick", "re_pickup", "re_captured"], player_aliases)

    create_file_players(dir_name, "./HTML/player.html", players, games, player_aliases)

    create_file_map(dir_name, "./HTML/map.html", games, ["kills", "deaths", "ratio", "difference", "objective_score",
                    "total score"], player_aliases)

    # print(dir_name)
    create_main_file(dir_name, "./HTML/stats.html", players, games, ["dm", "tdm", "hq", "ctf", "sd", "re", "bel", "dom",
                                                                     "bas"])

    # create_file_map()
    # print(games)
    # for player in players:
    # print(player, " => ", players[player])


def main(input_criteria="./Awards_criteria.txt",
         objectives_input="./objective_points.txt"):   # Count of people in each award

    print()
    if os.path.isfile(input_criteria):
        if os.path.isfile(objectives_input):
            if analyze(input_criteria, objectives_input):
                return 4
        else:
            print("*****************   E R R O R   *****************\nNenasiel sa subor s bodmi za jednotlive "
                  "objectivy cez relativnu cestu => '", objectives_input, "'\n")
            return 3
    else:
        print("*****************   E R R O R   *****************\nNenasiel sa subor s kriteriami pre AWARDY "
              "cez relativnu cestu => '", input_criteria, "'\n")
        return 2

    print("\n-----------------------------------------------")
    print("=> Game log processing has been successful ! <=\n")
    return 0


main()
