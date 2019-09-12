#from models import StatLine, CustomStat, CustomMetric

# useful pre_defined values
lower_to_correct_map = {'year': 'year', 'playoffs': 'playoffs', 'assist1st': 'assist1st', 'assist2nd': 'assist2nd', 'assists': 'assists', 'assistsper60minutes': 'assistsPer60Minutes', 'assistspergame': 'assistsPerGame', 'avgshotlength': 'avgShotLength', 'blockedshots': 'blockedShots', 'blockedshotspergame': 'blockedShotsPerGame', 'defensivezonefaceoffs': 'defensiveZoneFaceoffs', 'engoals': 'enGoals', 'evassists': 'evAssists', 'evfaceoffwinpctg': 'evFaceoffWinPctg', 'evfaceoffslost': 'evFaceoffsLost', 'evfaceoffswon': 'evFaceoffsWon', 'evgoals': 'evGoals', 'evpoints': 'evPoints', 'evtimeonice': 'evTimeOnIce', 'evtimeonicepergame': 'evTimeOnIcePerGame', 'faceoffloss': 'faceoffLoss', 'faceofflossdefensivezone': 'faceoffLossDefensiveZone', 'faceofflossneutralzone': 'faceoffLossNeutralZone', 'faceofflossoffensivezone': 'faceoffLossOffensiveZone', 'faceofflosswhenahead': 'faceoffLossWhenAhead', 'faceofflosswhenbehind': 'faceoffLossWhenBehind', 'faceofflosswhenclose': 'faceoffLossWhenClose', 'faceoffwinpctg': 'faceoffWinPctg', 'faceoffwinpctgdefensivezone': 'faceoffWinPctgDefensiveZone', 'faceoffwinpctgneutralzone': 'faceoffWinPctgNeutralZone', 'faceoffwinpctgoffensivezone': 'faceoffWinPctgOffensiveZone', 'faceoffwins': 'faceoffWins', 'faceoffwinsdefensivezone': 'faceoffWinsDefensiveZone', 'faceoffwinsneutralzone': 'faceoffWinsNeutralZone', 'faceoffwinsoffensivezone': 'faceoffWinsOffensiveZone', 'faceoffwinswhenahead': 'faceoffWinsWhenAhead', 'faceoffwinswhenbehind': 'faceoffWinsWhenBehind', 'faceoffwinswhenclose': 'faceoffWinsWhenClose', 'faceoffs': 'faceoffs', 'faceoffslost': 'faceoffsLost', 'faceoffstaken': 'faceoffsTaken', 'faceoffswon': 'faceoffsWon', 'firstgoals': 'firstGoals', 'fiveonfiveshootingpctg': 'fiveOnFiveShootingPctg', 'gamewinninggoals': 'gameWinningGoals', 'gamesplayed': 'gamesPlayed', 'giveaways': 'giveaways', 'goals': 'goals', 'goalsbackhand': 'goalsBackhand', 'goalsdeflected': 'goalsDeflected', 'goalsper60minutes': 'goalsPer60Minutes', 'goalspergame': 'goalsPerGame', 'goalsslap': 'goalsSlap', 'goalssnap': 'goalsSnap', 'goalstipped': 'goalsTipped', 'goalswraparound': 'goalsWraparound', 'goalswrist': 'goalsWrist', 'hits': 'hits', 'hitspergame': 'hitsPerGame', 'homeplusminus': 'homePlusMinus', 'missedshots': 'missedShots', 'missedshotshitcrossbar': 'missedShotsHitCrossbar', 'missedshotshitpost': 'missedShotsHitPost', 'missedshotsovernet': 'missedShotsOverNet', 'missedshotspergame': 'missedShotsPerGame', 'missedshotswideofnet': 'missedShotsWideOfNet', 'offensivezonefaceoffs': 'offensiveZoneFaceoffs', 'otgoals': 'otGoals', 'penalties': 'penalties', 'penaltiesdrawn': 'penaltiesDrawn', 'penaltiesdrawnper60minutes': 'penaltiesDrawnPer60Minutes', 'penaltiesgamemisconduct': 'penaltiesGameMisconduct', 'penaltiesmajor': 'penaltiesMajor', 'penaltiesmatch': 'penaltiesMatch', 'penaltiesminor': 'penaltiesMinor', 'penaltiesmisconduct': 'penaltiesMisconduct', 'penaltiesper60minutes': 'penaltiesPer60Minutes', 'penaltyminutes': 'penaltyMinutes', 'penaltyminutespergame': 'penaltyMinutesPerGame', 'penaltyshotattempts': 'penaltyShotAttempts', 'penaltyshotgoals': 'penaltyShotGoals', 'playerbirthcity': 'playerBirthCity', 'playerbirthcountry': 'playerBirthCountry', 'playerbirthdate': 'playerBirthDate', 'playerbirthstateprovince': 'playerBirthStateProvince', 'playerdraftoverallpickno': 'playerDraftOverallPickNo', 'playerdraftroundno': 'playerDraftRoundNo', 'playerdraftyear': 'playerDraftYear', 'playerfirstname': 'playerFirstName', 'playerheight': 'playerHeight', 'playerid': 'playerId', 'playerinhockeyhof': 'playerInHockeyHof', 'playerisactive': 'playerIsActive', 'playerlastname': 'playerLastName', 'playername': 'playerName', 'playernationality': 'playerNationality', 'playerpositioncode': 'playerPositionCode', 'playershootscatches': 'playerShootsCatches', 'playerteamsplayedfor': 'playerTeamsPlayedFor', 'playerweight': 'playerWeight', 'plusminus': 'plusMinus', 'points': 'points', 'pointsper60minutes': 'pointsPer60Minutes', 'pointspergame': 'pointsPerGame', 'ppassists': 'ppAssists', 'ppfaceoffwinpctg': 'ppFaceoffWinPctg', 'ppfaceoffslost': 'ppFaceoffsLost', 'ppfaceoffswon': 'ppFaceoffsWon', 'ppgiveaways': 'ppGiveaways', 'ppgoals': 'ppGoals', 'pphits': 'ppHits', 'ppmissedshots': 'ppMissedShots', 'pppoints': 'ppPoints', 'ppshots': 'ppShots', 'pptakeaways': 'ppTakeaways', 'ppteamgoalsagainst': 'ppTeamGoalsAgainst', 'ppteamgoalsfor': 'ppTeamGoalsFor', 'pptimeonice': 'ppTimeOnIce', 'pptimeonicepergame': 'ppTimeOnIcePerGame', 'roadplusminus': 'roadPlusMinus', 'seasonid': 'seasonId', 'shassists': 'shAssists', 'shblockedshots': 'shBlockedShots', 'shfaceoffwinpctg': 'shFaceoffWinPctg', 'shfaceoffslost': 'shFaceoffsLost', 'shfaceoffswon': 'shFaceoffsWon', 'shgiveaways': 'shGiveaways', 'shgoals': 'shGoals', 'shhits': 'shHits', 'shmissedshots': 'shMissedShots', 'shpoints': 'shPoints', 'shshots': 'shShots', 'shtakeaways': 'shTakeaways', 'shtimeonice': 'shTimeOnIce', 'shtimeonicepergame': 'shTimeOnIcePerGame', 'shifts': 'shifts', 'shiftspergame': 'shiftsPerGame', 'shootingpctg': 'shootingPctg', 'shootingplussavepctg': 'shootingPlusSavePctg', 'shotattempts': 'shotAttempts', 'shotattemptsagainst': 'shotAttemptsAgainst', 'shotattemptsahead': 'shotAttemptsAhead', 'shotattemptsbehind': 'shotAttemptsBehind', 'shotattemptsclose': 'shotAttemptsClose', 'shotattemptsfor': 'shotAttemptsFor', 'shotattemptspctg': 'shotAttemptsPctg', 'shotattemptspctgahead': 'shotAttemptsPctgAhead', 'shotattemptspctgbehind': 'shotAttemptsPctgBehind', 'shotattemptspctgclose': 'shotAttemptsPctgClose', 'shotattemptspctgtied': 'shotAttemptsPctgTied', 'shotattemptsrelpctg': 'shotAttemptsRelPctg', 'shotattemptstied': 'shotAttemptsTied', 'shots': 'shots', 'shotsbackhand': 'shotsBackhand', 'shotsdeflected': 'shotsDeflected', 'shotspergame': 'shotsPerGame', 'shotsslap': 'shotsSlap', 'shotssnap': 'shotsSnap', 'shotstipped': 'shotsTipped', 'shotswraparound': 'shotsWraparound', 'shotswrist': 'shotsWrist', 'takeaways': 'takeaways', 'teamgoalsagainst': 'teamGoalsAgainst', 'teamgoalsfor': 'teamGoalsFor', 'timeonice': 'timeOnIce', 'timeonicepergame': 'timeOnIcePerGame', 'timeonicepershift': 'timeOnIcePerShift', 'unblockedshotattempts': 'unblockedShotAttempts', 'unblockedshotattemptsagainst': 'unblockedShotAttemptsAgainst', 'unblockedshotattemptsahead': 'unblockedShotAttemptsAhead', 'unblockedshotattemptsbehind': 'unblockedShotAttemptsBehind', 'unblockedshotattemptsclose': 'unblockedShotAttemptsClose', 'unblockedshotattemptsfor': 'unblockedShotAttemptsFor', 'unblockedshotattemptspctg': 'unblockedShotAttemptsPctg', 'unblockedshotattemptspctgahead': 'unblockedShotAttemptsPctgAhead', 'unblockedshotattemptspctgbehind': 'unblockedShotAttemptsPctgBehind', 'unblockedshotattemptspctgclose': 'unblockedShotAttemptsPctgClose', 'unblockedshotattemptspctgtied': 'unblockedShotAttemptsPctgTied', 'unblockedshotattemptsrelpctg': 'unblockedShotAttemptsRelPctg', 'unblockedshotattemptstied': 'unblockedShotAttemptsTied', 'zonestartpctg': 'zoneStartPctg'}
single_tokens = set(["=", "+", "-", "*", "/", "^", "(", ")"])
aggregate_tokens = set(["max", "min", "avg", "std"])

def lexer(string):
    """
    [lexer] takes in an input string and separates it into
        pre-defined tokens which will later be assembled into
        an abstract syntax tree.
    [string]: input string
    """
    lines = string.split("\r\n")
    output = []

    for line in lines:
        line_tokens = []

        # remove spaces and convert to lowercase
        line = line.replace(" ", "").lower()

        token_start = 0
        for i in range(len(line)):
            if line[i] in single_tokens:
                if token_start < i:
                    line_tokens.append(line[token_start:i])
                line_tokens.append(line[i])
                token_start = i + 1
            elif line[token_start:i + 1] in aggregate_tokens:
                line_tokens.append(line[token_start:i + 1])
                token_start = i + 1
        
        if token_start < len(line):
            line_tokens.append(line[token_start:])

        # Iterate through tokens and change model values to their correct capitalization
        for i, token in enumerate(line_tokens):
            if token in lower_to_correct_map:
                line_tokens[i] = lower_to_correct_map[token]
        if len(line_tokens) > 0:
            output.append(line_tokens)

    return output
        

class AST:

    # expr_type should be any of the following strings;
    #   - "FLOAT"
    #   - "STAT"
    #   - "VAR"
    #   - unary: "MAX", "MIN", "AVG", "STD"
    #   - binary: "EXP", "MULT", "DIV", "ADD", "SUB", "ASSIGN"
    #   - "NONE"
    def __init__(self, expr_type):
        self.type = expr_type
        self.children = []

def find_parentheses_relation(token_list):
    """
    [find_parentheses_relation] determines whether or not the parens
        whithin token_list are valid. If they are, it returns True and 
        a map with the associated indices for each set. If they aren't, 
        it will return False and an empty map.
    [token_list]: a list of tokens (strings) where some of them may be parens
    Returns: (Boolean, map)
    """
    stack = [] # (parens, index)
    index_map = {}
    for i, token in enumerate(token_list):
        if stack == []:
            stack.append((token, i))
        elif token == ")":
            if stack[-1][0] == "(":
                parens, index = stack.pop()
                index_map[index] = i
                index_map[i] = index
            else:
                return False, {}
        elif token == "(":
            stack.append((token, i))

    if len(stack) == 0:
        return True, index_map
    else:
        return False, {}
    

def parser(tokens):
    """
    [parser] creates an abstract syntax tree from a 2D list of tokens
        that will be created by the lexer.
    [tokens]: 2D list of tokens (strings) that represent float values
        when evaluated.
    """
    ast_list = []

    def create_ast(token_list, left, right, parens_index_map):
        # TODO: do stuff
        pass
        # TODO: return ast

    for token_list in tokens:
        valid_parens, parens_index_map = find_parentheses_relation(token_list)
        if valid_parens:
            ast_list.append(create_ast(token_list, 0, len(token_list), parens_index_map))
        else:
            return AST("NONE")

    return ast_list






