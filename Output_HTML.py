import os
import shutil


def write_to_file_kills(dir_name, file_template_name, sorted_players, gtype, category, categories, const1, dname,
                        player_aliases, map_name="", controller=0):
    filename = dir_name + "/" + dname + "/" + gtype + "/" + gtype + "_" + category + ".html"
    width = str(round(const1/(len(categories) + 2), 0))
    with open(file_template_name, "r") as template, open(filename, "w") as outputfile:
        for line in template:
            if "<table_head>" in line:
                for helpful_var in categories:
                    outputfile.write('<td width=' + width + '%><a href="./' + gtype + '_' + helpful_var
                                     + '.html" class=tablelink>' + helpful_var + '</a></td>\n')
            elif "<mapname>" in line:
                outputfile.write('<tr>\n')
                outputfile.write('<table style ="margin:auto;margin-top:40px">\n')
                outputfile.write('<tr style = "text-align:center;font-size:30px;color:white">\n')
                outputfile.write('<td>' + gtype + '</td>\n')
                outputfile.write('</tr >\n')
                outputfile.write('<tr style = "text-align:center;font-size:30px;color:white">\n')
                outputfile.write('<td><img src="../../../obrazky/' + map_name + '.jpg" height=300></td>\n')
                outputfile.write('</tr >\n')
                outputfile.write('<table>\n')
                outputfile.write('</tr>\n')
            elif not ("<results>" in line):
                outputfile.write(line)
            else:
                for player in sorted_players:
                    if not (player[0] in player_aliases):
                        player_name = "x"
                    else:
                        player_name = player_aliases[player[0]]

                    outputfile.write("<tr>\n")
                    outputfile.write('<td><img src="../../../hraci/' + player_name
                                     + '.jpg" width=100%></td>\n')
                    outputfile.write("<td class=tableresult1>"
                                     + str(sorted_players.index(player) + 1) + "</td>\n")
                    # outputfile.write("<td class=tableresult1 width=" + width + "%> " + player[0] + "</td>\n")
                    outputfile.write('<td class=namelink width=' + width + '%><a href="../../players/' +
                                     player[0] + '.html"> ' + player[0] + '</a></td>\n')
                    if controller:
                        for helpful_var in categories:
                            # print(gtype)
                            # print(player)
                            # print(helpful_var)
                            outputfile.write("<td class=tableresult1 width=" + width + "%> "
                                             + str(player[1][helpful_var]) + "</td>\n")
                    else:
                        for helpful_var in categories:
                            # print(gtype)
                            # print(player)
                            # print(helpful_var)
                            outputfile.write("<td class=tableresult1 width=" + width + "%> "
                                             + str(player[1][gtype][helpful_var]) + "</td>\n")
                    outputfile.write("</tr>\n")


def write_to_file_other(dir_name, file_template_name, sorted_players, othername1, category, categories, player_aliases):
    filename = dir_name + "/results/" + othername1 + "/" + category + ".html"
    width = str(round(80 / (len(categories) + 2), 0))
    with open(file_template_name, "r") as template, open(filename, "w") as outputfile:
        for line in template:
            # if "<results>" in line:
            #     for helpful_var in categories:
            #         outputfile.write('<td width=' + width + '%><a href="./' + helpful_var
            #                          + '.html" class=tablelink>' + helpful_var + '</a></td>\n')
            if not ("<results>" in line):
                outputfile.write(line)
            else:
                for helpful_var in categories:
                    outputfile.write('<td width=' + width + '%><a href="./' + helpful_var
                                     + '.html" class=tablelink>' + helpful_var + '</a></td>\n')
                for player in sorted_players:
                    if not (player[0] in player_aliases):
                        player_name = "x"
                    else:
                        player_name = player_aliases[player[0]]

                    outputfile.write("<tr>\n")
                    outputfile.write('<td><img src="../../../hraci/' + player_name
                                     + '.jpg" width=100%></td>\n')
                    outputfile.write("<td class=tableresult1 width=" + width + "%> "
                                     + str(sorted_players.index(player) + 1) + "</td>\n")
                    outputfile.write('<td class=namelink width=' + width + '%><a href="../../players/' +
                                     player[0] + '.html"> ' + player[0] + '</a></td>\n')
                    for helpful_var in categories:
                        outputfile.write("<td class=tableresult1 width=" + width + "%> "
                                         + str(player[1][helpful_var]) + "</td>\n")
                    outputfile.write("</tr>\n")


def create_file_kills(dir_name, file_template_name, players, gtype, categories, const1, dname, player_aliases):
    temp_dir_name = dir_name + "/results/" + gtype
    if os.path.isdir(temp_dir_name):
        shutil.rmtree(temp_dir_name)
    os.makedirs(temp_dir_name)
    for category in categories:
        sorted_players = sorted(players.items(), key=lambda x: x[1][gtype][category], reverse=True)
        write_to_file_kills(dir_name, file_template_name, sorted_players, gtype, category, categories, const1, dname,
                            player_aliases)


def create_file_awards(dir_name, file_template_name, awards, awards_top):
    filename = dir_name + "/awards.html"
    awards_info = {}
    with open(file_template_name, "r") as template, open(filename, "w") as outputfile:
        for line in template:
            if not ("<results>" in line):
                outputfile.write(line)
            else:
                outputfile.write('<tr>\n<table width=50% style="margin:auto; margin-top: 30px; margin-bottom: 100px;'
                                 ' font-size:15px" style="margin:auto; margin-top: 5px">\n'
                                 '<tr class="tablehead3">'
                                 '<td width=20%> Award </td>\n'
                                 '<td width=30%> Description </td>\n</tr>\n')
                for award in awards:
                    # print(award)
                    outputfile.write('<tr><td class="namelink"><a href=#' + award + '>' + award + '</td>\n'
                                     '<td class="tableresult1">' + awards[award]["information"] + '</td>\n' 
                                     '</tr>\n')
                outputfile.write('</table>\n</tr>\n')

                for award in awards:
                    awards_info[award] = awards[award]["information"]
                    del awards[award]["information"]
                    sorted_award = sorted(awards[award].items(), key=lambda x: x[1], reverse=True)
                    if sorted_award[0][1] > 0:
                        outputfile.write('<tr>\n<table width=60% style="margin:auto; margin-top: 30px; font-size:15px">'
                                         '\n<tr>\n<td style="color:white"><a name=' + award + ' >' + award + ': '
                                         + awards_info[award] + '</td>\n</tr>\n</table>\n<table width=60% '
                                                                'style="margin:auto; margin-top: 5px">\n'
                                         '<tr class="tablehead3">'
                                         '<td width=20%> Rank </td>\n'
                                         '<td width=20%> Player </td>\n'
                                         '<td width=20%> score </tr>\n</th>\n')
                        for position in range(awards_top):
                            if sorted_award[position][1] > 0:
                                outputfile.write('<tr>\n<td class="tableresult1" width=20%>'
                                                 + str(position+1) + '. </td>\n'
                                                 '<td class="namelink "width=20%><a href="./players/' +
                                                  sorted_award[position][0] + '.html">'
                                                 + sorted_award[position][0] + '</a></td>\n'
                                                 '<td class="tableresult1" width=20%>' +
                                                 str(sorted_award[position][1]) + '</td>\n</tr>\n')
                        outputfile.write('</table>\n</tr>\n')


def create_file_team_wins(dir_name, file_template_name, players):
    filename = dir_name + "/Team_wins.html"
    sorted_players = sorted(players.items(), key=lambda x: x[1]["wins"], reverse=True)
    with open(file_template_name, "r") as template, open(filename, "w") as outputfile:
        for line in template:
            if not ("<results>" in line):
                outputfile.write(line)
            else:
                for player in sorted_players:
                    outputfile.write("<tr>\n")
                    outputfile.write('<td><img src="../hraci/' + player[0].lower()
                                     + '.jpg" width=100%></td>\n')
                    outputfile.write("<td class=tableresult1 width=20%> "
                                     + str(sorted_players.index(player) + 1) + "</td>\n")
                    outputfile.write('<td class=namelink width=20%><a href="./players/' + player[0] + '.html">'
                                      + player[0] + '</td>\n')
                    outputfile.write("<td class=tableresult1 width=20%> " + str(player[1]["wins"])
                                     + "</td>\n")
                    outputfile.write("</tr>\n")


def create_file_other(dir_name, file_template_name, players, othername, categories, player_aliases):
    temp_dir_name = dir_name + "/results/" + othername
    if os.path.isdir(temp_dir_name):
        shutil.rmtree(temp_dir_name)
    os.makedirs(temp_dir_name)
    for category in categories:
        sorted_players = sorted(players.items(), key=lambda x: x[1][category], reverse=True)
        write_to_file_other(dir_name, file_template_name, sorted_players, othername, category, categories,
                            player_aliases)


def create_file_map(dir_name, file_template_name, games, categories, player_aliases):
    temp_dir_name = dir_name + "/Maps/"
    if os.path.isdir(temp_dir_name):
        shutil.rmtree(temp_dir_name)
    os.makedirs(temp_dir_name)

    del_list = []
    for map in games:
        if games[map] == {}:
            del_list.append(map)
    for map in del_list:
        del games[map]
    for map in games:
        # print("M A P A", map)
        map_name = map[0][:]
        # print(map_name, "   ", map_name[-1], "   ", map_name[:-1])
        while map_name[-1] == "x":
            # print("ANO")
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
            map_name = map_name[:-1]
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
        temp_dir_name = dir_name + "/Maps/" + map[0] + "_" + map[1] + "_" + str(map[2]) + "/"
        if os.path.isdir(temp_dir_name):
            shutil.rmtree(temp_dir_name)
        os.makedirs(temp_dir_name)
        for category in categories:
            # print(games[map])
            # print(map)
            sorted_players = sorted(games[map].items(), key=lambda x: x[1][category], reverse=True)
            write_to_file_kills(dir_name, file_template_name, sorted_players, map[0] + "_" + map[1] + "_" + str(map[2]),
                                category, categories, 80, "Maps", player_aliases, map_name, True)
            # write_map_file(temp_dir_name, file_template_name, games, map, category)

#
# def write_map_file(outputname, file_template_name, games, map, category):
#     outputname = outputname + map + "/"
#     if os.path.isdir(outputname):
#         shutil.rmtree(outputname)
#     os.makedirs(outputname)
#     outputname = outputname + category + ".html"
#     with open(file_template_name, "r") as template, open(outputname, "w") as outputfile:
#
#


def write_maps(games, current_player, outputfile):
    maps = {}
    for map in games:
        maps[map] = games[map]
    del_list = []
    # print(maps)
    for map in maps:
        # print(map)
        # print(maps)
        # print(maps[map])
        if not (current_player in maps[map]):
            del_list.append(map)
            # print("ZMAZAT  ", map)
            # print(current_player, maps[map])
    for map in del_list:
        del maps[map]
    sorted_maps = sorted(maps.items(), key=lambda x: x[1][current_player]["kills"], reverse=True)
    outputfile.write("<tr>")
    outputfile.write('<table width=60% style="margin:auto;margin-top:50px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td width=5%></td>\n"
                     "<td width=11%><tablehead1> Map </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Gametype </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Kills </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Deaths </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Ratio </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    # print(sorted_maps)
    for map in sorted_maps:
        # print(map)
        if map[1][current_player]["deaths"] == 0:
            ratio = 0
        else:
            ratio = round(map[1][current_player]["kills"] / map[1][current_player]["deaths"], 2)
        map_name = map[0][0][:]
        # print(map_name, "   ", map_name[-1], "   ", map_name[:-1])
        while map_name[-1] == "x":
            # print("ANO")
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
            map_name = map_name[:-1]
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
        # print(map[0])
        outputfile.write("<tr>\n")
        outputfile.write('<td><img src="../../obrazky/_' + map_name + '.jpg"></td>\n')
        outputfile.write('<td class=namelink><a href="../Maps/' + map[0][0] + '_' + map[0][1] + "_" + str(map[0][2]) +
                         "/" + map[0][0] + '_' + map[0][1] + "_" + str(map[0][2]) + '_kills.html">' + map[0][0] +
                         '</a></td>\n')
        outputfile.write('<td class=tableresult1>' + map[0][1] + '</td>\n')
        outputfile.write('<td class=tableresult1>' + str(map[1][current_player]["kills"]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(map[1][current_player]["deaths"]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(ratio) + '</td>')
        outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def write_weapons(players, current_player, outputfile):
    total_sum = 0
    for weapon in players[current_player]["weapons"]:
        total_sum += players[current_player]["weapons"][weapon]["kills"]
    if total_sum == 0:
        total_sum = 1000000
    sorted_weapons = sorted(players[current_player]["weapons"].items(),
                            key=lambda x: x[1]["kills"], reverse=True)
    outputfile.write("<tr>")
    outputfile.write('<table width=60% style="margin:auto;margin-top:50px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td width=11%><tablehead1> Weapon </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Kills </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Deaths </tablehead1></td>\n"
                     "<td width=11%><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    # print(sorted_weapons)
    for weapon in sorted_weapons:
        if (weapon[1]["kills"] > 0) or (weapon[1]["deaths"] > 0):
            outputfile.write("<tr>\n")
            outputfile.write('<td class=tableresult1>' + weapon[0] + '</td>\n')
            outputfile.write('<td class=tableresult1>' + str(weapon[1]["kills"]) + '</td>')
            outputfile.write('<td class=tableresult1>' + str(weapon[1]["deaths"]) + '</td>')
            outputfile.write('<td class=tableresult1>' + str(round(100 * weapon[1]["kills"] / total_sum, 2))
                             + ' %</td>')
            outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def write_location(players, current_player, outputfile):
    total_sum = 0
    for location in players[current_player]["location"]:
        total_sum += players[current_player]["location"][location]["kills"]
    if total_sum == 0:
        total_sum = 1000000
    sorted_locations = sorted(players[current_player]["location"].items(),
                            key=lambda x: x[1]["kills"], reverse=True)
    outputfile.write("<tr>")
    outputfile.write('<table width=60% style="margin:auto;margin-top:50px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td width=11%><tablehead1> Location </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Kills </tablehead1></td>\n"
                     "<td width=11%><tablehead1> Deaths </tablehead1></td>\n"
                     "<td width=11%><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    # print(sorted_locations)
    for location in sorted_locations:
        if (location[1]["kills"] > 0) or (location[1]["deaths"] > 0):
            outputfile.write("<tr>\n")
            outputfile.write('<td class=tableresult1>' + location[0] + '</td>\n')
            outputfile.write('<td class=tableresult1>' + str(location[1]["kills"]) + '</td>')
            outputfile.write('<td class=tableresult1>' + str(location[1]["deaths"]) + '</td>')
            outputfile.write('<td class=tableresult1>' + str(round(100 * location[1]["kills"] / total_sum, 2))
                             + ' %</td>')
            outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def create_file_one_player(temp_dir_name, file_template_name, players, current_player, games, player_aliases):
    name = temp_dir_name + current_player + ".html"
    with open(file_template_name, "r") as template, open(name, "w") as outputfile:
        for line in template:
            if not ("<results>" in line):
                outputfile.write(line)
            else:
                if not (current_player in player_aliases):
                    player_name = "x"
                else:
                    player_name = player_aliases[current_player]
                outputfile.write('<tr>\n')
                outputfile.write('<table style ="margin:auto;margin-top:40px">\n')
                outputfile.write('<tr style = "text-align:center;font-size:30px;color:white">\n')
                outputfile.write('<td>' + current_player + '</td>\n')
                outputfile.write('</tr >\n')
                outputfile.write('<tr style = "text-align:center;font-size:30px;color:white">\n')
                outputfile.write('<td><img src="../../hraci/' + player_name + '.jpg" height=250></td>\n')
                outputfile.write('</tr >\n')
                outputfile.write('<table>\n')
                outputfile.write('</tr>\n')
                write_maps(games, current_player, outputfile)
                write_weapons(players, current_player, outputfile)
                write_location(players, current_player, outputfile)


def create_file_players(dir_name, file_template_name, players, games, player_aliases):
    temp_dir_name = dir_name + "/players/"
    if os.path.isdir(temp_dir_name):
        shutil.rmtree(temp_dir_name)
    os.makedirs(temp_dir_name)
    for player in players:
        create_file_one_player(temp_dir_name, file_template_name, players, player, games, player_aliases)


def create_main_file_table():
    outputfile.write("<tr>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:50px">')
    outputfile.write('<tr style="margin-bot:10px;font-size:20px;color:white"><td>')
    outputfile.write("Map statistics")
    outputfile.write("</td></tr>\n")
    outputfile.write("</table>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:10px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td width=7%></td>\n"
                     "<td><tablehead1> Map </tablehead1></td>\n"
                     "<td><tablehead1> Gametype </tablehead1></td>\n"
                     "<td><tablehead1> Kills </tablehead1></td>\n"
                     "<td><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    sorted_maps = sorted(maps.items(), key=lambda x: x[1], reverse=True)
    if total_sum == 0:
        total_sum = 1000000
    # print(total_sum)
    # print(maps)
    for map in sorted_maps:
        # print(map[0])
        outputfile.write("<tr>\n")
        outputfile.write('<td></td>\n')
        outputfile.write('<td class=namelink><a href="./Maps/' + map[0][0] + '_' + map[0][1] + "/" +
                         map[0][0] + '_' + map[0][1] + '_kills.html">' + map[0][0] + '</a></td>\n')
        outputfile.write('<td class=tableresult1>' + map[0][1] + '</td>\n')
        outputfile.write('<td class=tableresult1>' + str(map[1]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(round(map[1] * 100 / total_sum, 2)) + ' %</td>')
        outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def main_file_maps(games, outputfile):
    maps = {}
    total_sum = 0
    for map in games:
        maps[map] = 0
        for player in games[map]:
            maps[map] += games[map][player]["kills"]
            total_sum += games[map][player]["kills"]
    outputfile.write("<tr>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:50px">')
    outputfile.write('<tr style="margin-bot:10px;font-size:20px;color:white"><td>')
    outputfile.write("Map statistics")
    outputfile.write("</td></tr>\n")
    outputfile.write("</table>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:10px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td width=7%></td>\n"
                     "<td><tablehead1> Map </tablehead1></td>\n"
                     "<td><tablehead1> Gametype </tablehead1></td>\n"
                     "<td><tablehead1> Kills </tablehead1></td>\n"
                     "<td><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    sorted_maps = sorted(maps.items(), key=lambda x: x[1], reverse=True)
    if total_sum == 0:
        total_sum = 1000000
    # print(total_sum)
    # print(maps)
    for map in sorted_maps:
        # print(map[0][0][-1])
        map_name = map[0][0][:]
        # print(map_name, "   ", map_name[-1], "   ", map_name[:-1])
        while map_name[-1] == "x":
            # print("ANO")
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
            map_name = map_name[:-1]
            # print("UPRAVENE", map_name, "   ", map_name[-1], "   ", map_name[:-1])
        # print(map_name)
        outputfile.write("<tr>\n")
        outputfile.write('<td><img src="../obrazky/_' + map_name + '.jpg"></td>\n')
        outputfile.write('<td class=namelink><a href="./Maps/' + map[0][0] + '_' + map[0][1] + "_" + str(map[0][2]) +
                         "/" + map[0][0] + '_' + map[0][1] + "_" + str(map[0][2]) + '_kills.html">' + map[0][0] +
                         '</a></td>\n')
        outputfile.write('<td class=tableresult1>' + map[0][1] + '</td>\n')
        outputfile.write('<td class=tableresult1>' + str(map[1]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(round(map[1] * 100 / total_sum, 2)) + ' %</td>')
        outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def main_file_weapons(players, outputfile):
    weapons = {}
    total_sum = 0
    for player in players:
        for weapon in players[player]["weapons"]:
            if not (weapon in weapons):
                weapons[weapon] = players[player]["weapons"][weapon]["kills"]
            else:
                weapons[weapon] += players[player]["weapons"][weapon]["kills"]
            total_sum += players[player]["weapons"][weapon]["kills"]
    if total_sum == 0:
        total_sum = 1000000

    outputfile.write("<tr>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:70px">')
    outputfile.write('<tr style="margin-bot:10px;font-size:20px;color:white"><td>')
    outputfile.write("Weapon statistics")
    outputfile.write("</td></tr>\n")
    outputfile.write("</table>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:10px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td><tablehead1> Weapon </tablehead1></td>\n"
                     "<td><tablehead1> Kills </tablehead1></td>\n"
                     "<td><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    sorted_weapons = sorted(weapons.items(), key=lambda x: x[1], reverse=True)
    for weapon in sorted_weapons:
        # print(map[0])
        outputfile.write("<tr>\n")
        outputfile.write('<td class=tableresult1>' + weapon[0] + '</td>\n')
        outputfile.write('<td class=tableresult1>' + str(weapon[1]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(round(weapon[1] * 100 / total_sum, 2)) + ' %</td>')
        outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def main_file_gametype_kills(players, outputfile, categories):
    gametype_kills = {}
    total_sum = 0
    for player in players:
        for category in categories:
            if not (category in gametype_kills):
                gametype_kills[category] = players[player][category]["kills"]
            else:
                gametype_kills[category] += players[player][category]["kills"]
            total_sum += players[player][category]["kills"]
    if total_sum == 0:
        total_sum = 1000000

    outputfile.write("<tr>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:70px">')
    outputfile.write('<tr style="margin-bot:10px;font-size:20px;color:white"><td>')
    outputfile.write("Kill statistics by gametype")
    outputfile.write("</td></tr>\n")
    outputfile.write("</table>")
    outputfile.write('<table width=55% style="margin:auto;margin-top:10px">\n')
    outputfile.write("<tr class=tablelink>\n")
    outputfile.write("<td><tablehead1> Gametype </tablehead1></td>\n"
                     "<td><tablehead1> Kills </tablehead1></td>\n"
                     "<td><tablehead1> % of all kills </tablehead1></td>\n")
    outputfile.write("</tr>\n")
    sorted_gametypes = sorted(gametype_kills.items(), key=lambda x: x[1], reverse=True)
    for category in sorted_gametypes:
        # print(map[0])
        outputfile.write("<tr>\n")
        outputfile.write('<td class=tableresult1>' + category[0] + '</td>\n')
        outputfile.write('<td class=tableresult1>' + str(category[1]) + '</td>')
        outputfile.write('<td class=tableresult1>' + str(round(category[1] * 100 / total_sum, 2)) + ' %</td>')
        outputfile.write('</tr>\n')
    outputfile.write("</table>")
    outputfile.write("</tr>")


def create_main_file(dir_name, file_template_name, players, games, categories):
    temp_dir_name = dir_name + "/Stats.html"
    with open(file_template_name, "r") as template, open(temp_dir_name, "w") as outputfile:
        for line in template:
            if "<results>" in line:
                main_file_maps(games, outputfile)
                main_file_weapons(players, outputfile)
                main_file_gametype_kills(players, outputfile, categories)
            else:
                outputfile.write(line)
