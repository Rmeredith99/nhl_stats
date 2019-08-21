from stats.models import StatLine

def determine_relation(s):
    """
    [determine_relation] accepts a string, [s], and returns a
        string denoting whether the relation in [s] is <=, >=,
        <, >, or =. Also returned is the index where it occurs.
        Ex) input: "x <= 20" output: "<=", 2
    """
    if "<=" in s:
        return "<=", s.index("<=")
    elif ">=" in s:
        return ">=", s.index(">=")
    elif "<" in s:
        return "<", s.index("<")
    elif ">" in s:
        return ">", s.index(">")
    elif "=" in s:
        return "=", s.index("=")
    else:
        return "", -1

def update_url(base, current_url, new_filter_url):
    """
    [update_url] takes in the current url and a new url composed from
        recent filters and merges them into a new url which replaces
        the old filters.
    """
    new_url = base
    if "&sort=" in current_url:
        index = current_url.index("&sort=")
        if new_filter_url == "":
            new_url += "?" + current_url[index + 1:]
        else:
            new_url += new_filter_url + current_url[index:]
    elif "?sort=" in current_url:
        index = current_url.index("?sort=")
        if new_filter_url == "":
            new_url += current_url[index:]
        else:
            new_url += new_filter_url + "&" + current_url[index + 1:]
    else:
        new_url += new_filter_url

    return new_url
    

def filter_text_to_url(filter_text):
    """
    [filter_text_to_url] is a function which will be called upon
        submission of a filter request. It takes in the result of 
        that request and returns a string which can be appended
        to the stats url.
    """
    # will be used to find the valid form of the category
    lower_to_correct_map = {'year': 'year', 'playoffs': 'playoffs', 'assist1st': 'assist1st', 'assist2nd': 'assist2nd', 'assists': 'assists', 'assistsper60minutes': 'assistsPer60Minutes', 'assistspergame': 'assistsPerGame', 'avgshotlength': 'avgShotLength', 'blockedshots': 'blockedShots', 'blockedshotspergame': 'blockedShotsPerGame', 'defensivezonefaceoffs': 'defensiveZoneFaceoffs', 'engoals': 'enGoals', 'evassists': 'evAssists', 'evfaceoffwinpctg': 'evFaceoffWinPctg', 'evfaceoffslost': 'evFaceoffsLost', 'evfaceoffswon': 'evFaceoffsWon', 'evgoals': 'evGoals', 'evpoints': 'evPoints', 'evtimeonice': 'evTimeOnIce', 'evtimeonicepergame': 'evTimeOnIcePerGame', 'faceoffloss': 'faceoffLoss', 'faceofflossdefensivezone': 'faceoffLossDefensiveZone', 'faceofflossneutralzone': 'faceoffLossNeutralZone', 'faceofflossoffensivezone': 'faceoffLossOffensiveZone', 'faceofflosswhenahead': 'faceoffLossWhenAhead', 'faceofflosswhenbehind': 'faceoffLossWhenBehind', 'faceofflosswhenclose': 'faceoffLossWhenClose', 'faceoffwinpctg': 'faceoffWinPctg', 'faceoffwinpctgdefensivezone': 'faceoffWinPctgDefensiveZone', 'faceoffwinpctgneutralzone': 'faceoffWinPctgNeutralZone', 'faceoffwinpctgoffensivezone': 'faceoffWinPctgOffensiveZone', 'faceoffwins': 'faceoffWins', 'faceoffwinsdefensivezone': 'faceoffWinsDefensiveZone', 'faceoffwinsneutralzone': 'faceoffWinsNeutralZone', 'faceoffwinsoffensivezone': 'faceoffWinsOffensiveZone', 'faceoffwinswhenahead': 'faceoffWinsWhenAhead', 'faceoffwinswhenbehind': 'faceoffWinsWhenBehind', 'faceoffwinswhenclose': 'faceoffWinsWhenClose', 'faceoffs': 'faceoffs', 'faceoffslost': 'faceoffsLost', 'faceoffstaken': 'faceoffsTaken', 'faceoffswon': 'faceoffsWon', 'firstgoals': 'firstGoals', 'fiveonfiveshootingpctg': 'fiveOnFiveShootingPctg', 'gamewinninggoals': 'gameWinningGoals', 'gamesplayed': 'gamesPlayed', 'giveaways': 'giveaways', 'goals': 'goals', 'goalsbackhand': 'goalsBackhand', 'goalsdeflected': 'goalsDeflected', 'goalsper60minutes': 'goalsPer60Minutes', 'goalspergame': 'goalsPerGame', 'goalsslap': 'goalsSlap', 'goalssnap': 'goalsSnap', 'goalstipped': 'goalsTipped', 'goalswraparound': 'goalsWraparound', 'goalswrist': 'goalsWrist', 'hits': 'hits', 'hitspergame': 'hitsPerGame', 'homeplusminus': 'homePlusMinus', 'missedshots': 'missedShots', 'missedshotshitcrossbar': 'missedShotsHitCrossbar', 'missedshotshitpost': 'missedShotsHitPost', 'missedshotsovernet': 'missedShotsOverNet', 'missedshotspergame': 'missedShotsPerGame', 'missedshotswideofnet': 'missedShotsWideOfNet', 'offensivezonefaceoffs': 'offensiveZoneFaceoffs', 'otgoals': 'otGoals', 'penalties': 'penalties', 'penaltiesdrawn': 'penaltiesDrawn', 'penaltiesdrawnper60minutes': 'penaltiesDrawnPer60Minutes', 'penaltiesgamemisconduct': 'penaltiesGameMisconduct', 'penaltiesmajor': 'penaltiesMajor', 'penaltiesmatch': 'penaltiesMatch', 'penaltiesminor': 'penaltiesMinor', 'penaltiesmisconduct': 'penaltiesMisconduct', 'penaltiesper60minutes': 'penaltiesPer60Minutes', 'penaltyminutes': 'penaltyMinutes', 'penaltyminutespergame': 'penaltyMinutesPerGame', 'penaltyshotattempts': 'penaltyShotAttempts', 'penaltyshotgoals': 'penaltyShotGoals', 'playerbirthcity': 'playerBirthCity', 'playerbirthcountry': 'playerBirthCountry', 'playerbirthdate': 'playerBirthDate', 'playerbirthstateprovince': 'playerBirthStateProvince', 'playerdraftoverallpickno': 'playerDraftOverallPickNo', 'playerdraftroundno': 'playerDraftRoundNo', 'playerdraftyear': 'playerDraftYear', 'playerfirstname': 'playerFirstName', 'playerheight': 'playerHeight', 'playerid': 'playerId', 'playerinhockeyhof': 'playerInHockeyHof', 'playerisactive': 'playerIsActive', 'playerlastname': 'playerLastName', 'playername': 'playerName', 'playernationality': 'playerNationality', 'playerpositioncode': 'playerPositionCode', 'playershootscatches': 'playerShootsCatches', 'playerteamsplayedfor': 'playerTeamsPlayedFor', 'playerweight': 'playerWeight', 'plusminus': 'plusMinus', 'points': 'points', 'pointsper60minutes': 'pointsPer60Minutes', 'pointspergame': 'pointsPerGame', 'ppassists': 'ppAssists', 'ppfaceoffwinpctg': 'ppFaceoffWinPctg', 'ppfaceoffslost': 'ppFaceoffsLost', 'ppfaceoffswon': 'ppFaceoffsWon', 'ppgiveaways': 'ppGiveaways', 'ppgoals': 'ppGoals', 'pphits': 'ppHits', 'ppmissedshots': 'ppMissedShots', 'pppoints': 'ppPoints', 'ppshots': 'ppShots', 'pptakeaways': 'ppTakeaways', 'ppteamgoalsagainst': 'ppTeamGoalsAgainst', 'ppteamgoalsfor': 'ppTeamGoalsFor', 'pptimeonice': 'ppTimeOnIce', 'pptimeonicepergame': 'ppTimeOnIcePerGame', 'roadplusminus': 'roadPlusMinus', 'seasonid': 'seasonId', 'shassists': 'shAssists', 'shblockedshots': 'shBlockedShots', 'shfaceoffwinpctg': 'shFaceoffWinPctg', 'shfaceoffslost': 'shFaceoffsLost', 'shfaceoffswon': 'shFaceoffsWon', 'shgiveaways': 'shGiveaways', 'shgoals': 'shGoals', 'shhits': 'shHits', 'shmissedshots': 'shMissedShots', 'shpoints': 'shPoints', 'shshots': 'shShots', 'shtakeaways': 'shTakeaways', 'shtimeonice': 'shTimeOnIce', 'shtimeonicepergame': 'shTimeOnIcePerGame', 'shifts': 'shifts', 'shiftspergame': 'shiftsPerGame', 'shootingpctg': 'shootingPctg', 'shootingplussavepctg': 'shootingPlusSavePctg', 'shotattempts': 'shotAttempts', 'shotattemptsagainst': 'shotAttemptsAgainst', 'shotattemptsahead': 'shotAttemptsAhead', 'shotattemptsbehind': 'shotAttemptsBehind', 'shotattemptsclose': 'shotAttemptsClose', 'shotattemptsfor': 'shotAttemptsFor', 'shotattemptspctg': 'shotAttemptsPctg', 'shotattemptspctgahead': 'shotAttemptsPctgAhead', 'shotattemptspctgbehind': 'shotAttemptsPctgBehind', 'shotattemptspctgclose': 'shotAttemptsPctgClose', 'shotattemptspctgtied': 'shotAttemptsPctgTied', 'shotattemptsrelpctg': 'shotAttemptsRelPctg', 'shotattemptstied': 'shotAttemptsTied', 'shots': 'shots', 'shotsbackhand': 'shotsBackhand', 'shotsdeflected': 'shotsDeflected', 'shotspergame': 'shotsPerGame', 'shotsslap': 'shotsSlap', 'shotssnap': 'shotsSnap', 'shotstipped': 'shotsTipped', 'shotswraparound': 'shotsWraparound', 'shotswrist': 'shotsWrist', 'takeaways': 'takeaways', 'teamgoalsagainst': 'teamGoalsAgainst', 'teamgoalsfor': 'teamGoalsFor', 'timeonice': 'timeOnIce', 'timeonicepergame': 'timeOnIcePerGame', 'timeonicepershift': 'timeOnIcePerShift', 'unblockedshotattempts': 'unblockedShotAttempts', 'unblockedshotattemptsagainst': 'unblockedShotAttemptsAgainst', 'unblockedshotattemptsahead': 'unblockedShotAttemptsAhead', 'unblockedshotattemptsbehind': 'unblockedShotAttemptsBehind', 'unblockedshotattemptsclose': 'unblockedShotAttemptsClose', 'unblockedshotattemptsfor': 'unblockedShotAttemptsFor', 'unblockedshotattemptspctg': 'unblockedShotAttemptsPctg', 'unblockedshotattemptspctgahead': 'unblockedShotAttemptsPctgAhead', 'unblockedshotattemptspctgbehind': 'unblockedShotAttemptsPctgBehind', 'unblockedshotattemptspctgclose': 'unblockedShotAttemptsPctgClose', 'unblockedshotattemptspctgtied': 'unblockedShotAttemptsPctgTied', 'unblockedshotattemptsrelpctg': 'unblockedShotAttemptsRelPctg', 'unblockedshotattemptstied': 'unblockedShotAttemptsTied', 'zonestartpctg': 'zoneStartPctg'}
    # maps mathematical syntax to url syntax for the comparator
    relation_map = {"<=": "lte", ">=": "gte", "<": "lt", ">": "gt", "=": "eq"}

    url = ["?filter="]
    space = "%2C"
    filters = filter_text.split("\r\n")
    for f in filters:
        if f != "":
            # remove spaces
            f = f.replace(" ", "")
            relation, index = determine_relation(f)
            # if the relation isn't valid
            if relation == "":
                print("Invalid filters submitted: " + f)
                return ""
            # If there is a valid filter
            name_lower = f[:index].strip().lower()
            if name_lower in lower_to_correct_map:
                name = lower_to_correct_map[name_lower]
            else:
                print("Invalid filters submitted: " + f)
                return ""
            value = f[index + len(relation):]
            # if value is a boolean, put it into the right formatting
            if value.lower() == "true" or value.lower() == "false":
                value = value.capitalize()
            relation_string = relation_map[relation]

            # add all the pieces together to create a new filter
            url.append(name + space + relation_string + space + value + "&")

    return "".join(url).strip("&")



def url_string_to_queryset(url_string):
    """
    [url_string_to_queryset] takes in the url string submitted to
        stats and applies the formatted queries on a new instance
        of StatLine.objects.all() which is then returned.
    """
    # defining filter_string to be just the part of the url that 
    # deals with filters
    if "?filter=" in url_string:
        filter_start = url_string.index("?filter=")
        filter_end = []
        if "=&sort=" in url_string:
            filter_end.append(url_string.index("=&sort="))
        elif "&sort=" in url_string:
            filter_end.append(url_string.index("&sort="))
        if "=&page=" in url_string:
            filter_end.append(url_string.index("=&page="))
        elif "&page=" in url_string:
            filter_end.append(url_string.index("&page="))
            
        if len(filter_end) > 0:
            filter_string = url_string[filter_start + 8:min(filter_end)]
        else:
            filter_string = url_string[filter_start + 8:]
    else:
        return StatLine.objects.all()

    # separating various filters and iterating over them
    filters = filter_string.split("&")
    objects = StatLine.objects.all()
    relation_map = {"lte": "lte", "gte": "gte", "lt": "lt", "gt": "gt", "eq": "exact"}
    for f in filters:
        name, relation, value = f.split("%2C")
        # hard-coded check for specific values that have unique filtering
        if name == "playerTeamsPlayedFor":
            objects = objects.filter(playerTeamsPlayedFor__icontains = value)
        else:
            exec_dict = {"objects": objects}
            try:
                # if value is numeric then we don't need to apply extra quotation marks
                _ = float(value)
                code_string = "objects = objects.filter(" + name + "__" + relation_map[relation] + " = " + value + ")"
                exec(code_string, exec_dict)
                objects = exec_dict["objects"]
            except:
                # if the string contains a bool then we don't need to apply extra quotation marks
                if value == "True" or value == "False":
                    _ = bool(value)
                    code_string = "objects = objects.filter(" + name + "__" + relation_map[relation] + " = " + value + ")"
                    exec(code_string)
                else:
                    # if the string's underlying data is actually a string, we need to add extra quotation marks
                    code_string = "objects = objects.filter(" + name + "__" + relation_map[relation] + " = '" + str(value) + "')"
                    exec(code_string)

    return objects
            
def remove_filter(url_string):
    """
    [remove_filter] takes a url and removes the parts pertaining
        to filters. This will also remove the page number since
        that would no longer be relevant. Returns a new url.
    """
    sort_start = -1
    page_start = -1
    start_offset = 0
    if "=&sort=" in url_string:
        index = url_string.index("=&sort=")
        sort_start = index
        start_offset = 2
    elif "&sort=" in url_string:
        index = url_string.index("&sort=")
        sort_start = index
        start_offset = 1
    elif "sort=" in url_string:
        index = url_string.index("sort=")
        sort_start = index
        start_offset = 0
    if "=&page=" in url_string:
        index = url_string.index("=&page=")
        page_start = index
    elif "&page=" in url_string:
        index = url_string.index("&page=")
        page_start = index
            
    if sort_start == -1:
        return "/stats/"
    elif page_start == -1:
        return "/stats/?" + url_string[sort_start + start_offset:]
    elif page_start < sort_start:
        return "/stats/?" + url_string[sort_start + start_offset:]
    else: # page_start > sort_start
        return "/stats/?" + url_string[sort_start + start_offset:page_start]

def remove_sort(url_string):
    """
    [remove_sort] takes a url and removes the parts pertaining
        to sorting. This will also remove the page number since
        that would no longer be relevant. Returns a new url.
    """
    sort_start = -1
    page_start = -1
    if "=&sort=" in url_string:
        index = url_string.index("=&sort=")
        sort_start = index
    elif "&sort=" in url_string:
        index = url_string.index("&sort=")
        sort_start = index
    elif "?sort=" in url_string:
        index = url_string.index("?sort=")
        sort_start = index
    if "=&page=" in url_string:
        index = url_string.index("=&page=")
        page_start = index
    elif "&page=" in url_string:
        index = url_string.index("&page=")
        page_start = index
    elif "?page=" in url_string:
        index = url_string.index("?page=")
        page_start = index

    if max(sort_start, page_start) == -1:
        return url_string
    elif sort_start == -1:
        return url_string[:page_start]
    elif page_start == -1:
        return url_string[:sort_start]
    else: # sort and page both appear
        return url_string[:min(sort_start, page_start)]