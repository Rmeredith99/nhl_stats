#from models import StatLine, CustomStat, CustomMetric

# useful pre_defined values
lower_to_correct_map = {'year': 'year', 'playoffs': 'playoffs', 'assist1st': 'assist1st', 'assist2nd': 'assist2nd', 'assists': 'assists', 'assistsper60minutes': 'assistsPer60Minutes', 'assistspergame': 'assistsPerGame', 'avgshotlength': 'avgShotLength', 'blockedshots': 'blockedShots', 'blockedshotspergame': 'blockedShotsPerGame', 'defensivezonefaceoffs': 'defensiveZoneFaceoffs', 'engoals': 'enGoals', 'evassists': 'evAssists', 'evfaceoffwinpctg': 'evFaceoffWinPctg', 'evfaceoffslost': 'evFaceoffsLost', 'evfaceoffswon': 'evFaceoffsWon', 'evgoals': 'evGoals', 'evpoints': 'evPoints', 'evtimeonice': 'evTimeOnIce', 'evtimeonicepergame': 'evTimeOnIcePerGame', 'faceoffloss': 'faceoffLoss', 'faceofflossdefensivezone': 'faceoffLossDefensiveZone', 'faceofflossneutralzone': 'faceoffLossNeutralZone', 'faceofflossoffensivezone': 'faceoffLossOffensiveZone', 'faceofflosswhenahead': 'faceoffLossWhenAhead', 'faceofflosswhenbehind': 'faceoffLossWhenBehind', 'faceofflosswhenclose': 'faceoffLossWhenClose', 'faceoffwinpctg': 'faceoffWinPctg', 'faceoffwinpctgdefensivezone': 'faceoffWinPctgDefensiveZone', 'faceoffwinpctgneutralzone': 'faceoffWinPctgNeutralZone', 'faceoffwinpctgoffensivezone': 'faceoffWinPctgOffensiveZone', 'faceoffwins': 'faceoffWins', 'faceoffwinsdefensivezone': 'faceoffWinsDefensiveZone', 'faceoffwinsneutralzone': 'faceoffWinsNeutralZone', 'faceoffwinsoffensivezone': 'faceoffWinsOffensiveZone', 'faceoffwinswhenahead': 'faceoffWinsWhenAhead', 'faceoffwinswhenbehind': 'faceoffWinsWhenBehind', 'faceoffwinswhenclose': 'faceoffWinsWhenClose', 'faceoffs': 'faceoffs', 'faceoffslost': 'faceoffsLost', 'faceoffstaken': 'faceoffsTaken', 'faceoffswon': 'faceoffsWon', 'firstgoals': 'firstGoals', 'fiveonfiveshootingpctg': 'fiveOnFiveShootingPctg', 'gamewinninggoals': 'gameWinningGoals', 'gamesplayed': 'gamesPlayed', 'giveaways': 'giveaways', 'goals': 'goals', 'goalsbackhand': 'goalsBackhand', 'goalsdeflected': 'goalsDeflected', 'goalsper60minutes': 'goalsPer60Minutes', 'goalspergame': 'goalsPerGame', 'goalsslap': 'goalsSlap', 'goalssnap': 'goalsSnap', 'goalstipped': 'goalsTipped', 'goalswraparound': 'goalsWraparound', 'goalswrist': 'goalsWrist', 'hits': 'hits', 'hitspergame': 'hitsPerGame', 'homeplusminus': 'homePlusMinus', 'missedshots': 'missedShots', 'missedshotshitcrossbar': 'missedShotsHitCrossbar', 'missedshotshitpost': 'missedShotsHitPost', 'missedshotsovernet': 'missedShotsOverNet', 'missedshotspergame': 'missedShotsPerGame', 'missedshotswideofnet': 'missedShotsWideOfNet', 'offensivezonefaceoffs': 'offensiveZoneFaceoffs', 'otgoals': 'otGoals', 'penalties': 'penalties', 'penaltiesdrawn': 'penaltiesDrawn', 'penaltiesdrawnper60minutes': 'penaltiesDrawnPer60Minutes', 'penaltiesgamemisconduct': 'penaltiesGameMisconduct', 'penaltiesmajor': 'penaltiesMajor', 'penaltiesmatch': 'penaltiesMatch', 'penaltiesminor': 'penaltiesMinor', 'penaltiesmisconduct': 'penaltiesMisconduct', 'penaltiesper60minutes': 'penaltiesPer60Minutes', 'penaltyminutes': 'penaltyMinutes', 'penaltyminutespergame': 'penaltyMinutesPerGame', 'penaltyshotattempts': 'penaltyShotAttempts', 'penaltyshotgoals': 'penaltyShotGoals', 'playerbirthcity': 'playerBirthCity', 'playerbirthcountry': 'playerBirthCountry', 'playerbirthdate': 'playerBirthDate', 'playerbirthstateprovince': 'playerBirthStateProvince', 'playerdraftoverallpickno': 'playerDraftOverallPickNo', 'playerdraftroundno': 'playerDraftRoundNo', 'playerdraftyear': 'playerDraftYear', 'playerfirstname': 'playerFirstName', 'playerheight': 'playerHeight', 'playerid': 'playerId', 'playerinhockeyhof': 'playerInHockeyHof', 'playerisactive': 'playerIsActive', 'playerlastname': 'playerLastName', 'playername': 'playerName', 'playernationality': 'playerNationality', 'playerpositioncode': 'playerPositionCode', 'playershootscatches': 'playerShootsCatches', 'playerteamsplayedfor': 'playerTeamsPlayedFor', 'playerweight': 'playerWeight', 'plusminus': 'plusMinus', 'points': 'points', 'pointsper60minutes': 'pointsPer60Minutes', 'pointspergame': 'pointsPerGame', 'ppassists': 'ppAssists', 'ppfaceoffwinpctg': 'ppFaceoffWinPctg', 'ppfaceoffslost': 'ppFaceoffsLost', 'ppfaceoffswon': 'ppFaceoffsWon', 'ppgiveaways': 'ppGiveaways', 'ppgoals': 'ppGoals', 'pphits': 'ppHits', 'ppmissedshots': 'ppMissedShots', 'pppoints': 'ppPoints', 'ppshots': 'ppShots', 'pptakeaways': 'ppTakeaways', 'ppteamgoalsagainst': 'ppTeamGoalsAgainst', 'ppteamgoalsfor': 'ppTeamGoalsFor', 'pptimeonice': 'ppTimeOnIce', 'pptimeonicepergame': 'ppTimeOnIcePerGame', 'roadplusminus': 'roadPlusMinus', 'seasonid': 'seasonId', 'shassists': 'shAssists', 'shblockedshots': 'shBlockedShots', 'shfaceoffwinpctg': 'shFaceoffWinPctg', 'shfaceoffslost': 'shFaceoffsLost', 'shfaceoffswon': 'shFaceoffsWon', 'shgiveaways': 'shGiveaways', 'shgoals': 'shGoals', 'shhits': 'shHits', 'shmissedshots': 'shMissedShots', 'shpoints': 'shPoints', 'shshots': 'shShots', 'shtakeaways': 'shTakeaways', 'shtimeonice': 'shTimeOnIce', 'shtimeonicepergame': 'shTimeOnIcePerGame', 'shifts': 'shifts', 'shiftspergame': 'shiftsPerGame', 'shootingpctg': 'shootingPctg', 'shootingplussavepctg': 'shootingPlusSavePctg', 'shotattempts': 'shotAttempts', 'shotattemptsagainst': 'shotAttemptsAgainst', 'shotattemptsahead': 'shotAttemptsAhead', 'shotattemptsbehind': 'shotAttemptsBehind', 'shotattemptsclose': 'shotAttemptsClose', 'shotattemptsfor': 'shotAttemptsFor', 'shotattemptspctg': 'shotAttemptsPctg', 'shotattemptspctgahead': 'shotAttemptsPctgAhead', 'shotattemptspctgbehind': 'shotAttemptsPctgBehind', 'shotattemptspctgclose': 'shotAttemptsPctgClose', 'shotattemptspctgtied': 'shotAttemptsPctgTied', 'shotattemptsrelpctg': 'shotAttemptsRelPctg', 'shotattemptstied': 'shotAttemptsTied', 'shots': 'shots', 'shotsbackhand': 'shotsBackhand', 'shotsdeflected': 'shotsDeflected', 'shotspergame': 'shotsPerGame', 'shotsslap': 'shotsSlap', 'shotssnap': 'shotsSnap', 'shotstipped': 'shotsTipped', 'shotswraparound': 'shotsWraparound', 'shotswrist': 'shotsWrist', 'takeaways': 'takeaways', 'teamgoalsagainst': 'teamGoalsAgainst', 'teamgoalsfor': 'teamGoalsFor', 'timeonice': 'timeOnIce', 'timeonicepergame': 'timeOnIcePerGame', 'timeonicepershift': 'timeOnIcePerShift', 'unblockedshotattempts': 'unblockedShotAttempts', 'unblockedshotattemptsagainst': 'unblockedShotAttemptsAgainst', 'unblockedshotattemptsahead': 'unblockedShotAttemptsAhead', 'unblockedshotattemptsbehind': 'unblockedShotAttemptsBehind', 'unblockedshotattemptsclose': 'unblockedShotAttemptsClose', 'unblockedshotattemptsfor': 'unblockedShotAttemptsFor', 'unblockedshotattemptspctg': 'unblockedShotAttemptsPctg', 'unblockedshotattemptspctgahead': 'unblockedShotAttemptsPctgAhead', 'unblockedshotattemptspctgbehind': 'unblockedShotAttemptsPctgBehind', 'unblockedshotattemptspctgclose': 'unblockedShotAttemptsPctgClose', 'unblockedshotattemptspctgtied': 'unblockedShotAttemptsPctgTied', 'unblockedshotattemptsrelpctg': 'unblockedShotAttemptsRelPctg', 'unblockedshotattemptstied': 'unblockedShotAttemptsTied', 'zonestartpctg': 'zoneStartPctg'}
single_tokens = set(["=", "+", "-", "*", "/", "^", "(", ")"])
aggregate_tokens = set(["max", "min", "avg", "std"])
non_pre_subtraction_ops = set(["+", "*", "/", "^", "=", "~"])

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
    #   - "ASSIGN_VAR" (this is only used during assignment)
    #   - unary: "MAX", "MIN", "AVG", "STD", "NEGATE"
    #   - binary: "EXP", "MULT", "DIV", "ADD", "SUB", "ASSIGN"
    #   - "ERROR"
    def __init__(self, expr_type, value):
        self.type = expr_type
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

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
        if stack == [] and token in ["(", ")"]:
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
    

def create_ast(token_list, left, right, parens_index_map):
    """
    [create_ast] takes in a list of tokens, a range of indices (in
        form of a left and right index), and a map containing locations
        of matching parentheses and returns a completed abstract syntax
        tree.
    [token_list]: list of strings
    [left]: int
    [right]: int
    [parens_index_map]: int -> int map
    """
    # Check if the expression is empty
    # If it is, return the null AST
    if left >= right:
        return AST("ERROR", "Empty evaluation")

    # Check if the expression is a single value
    if right - left == 1:
        if token_list[left].lower() in lower_to_correct_map:
            # token is a stat category
            return AST("STAT", token_list[left])
        else:
            try:
                # token is a pure float
                num = float(token_list[left])
                return AST("FLOAT", num)
            except:
                # token is a variable
                return AST("VAR", token_list[left])

    # Check if entrire expression is enclosed in parens
    # if it is, return the enclosed expression
    #print(left, token_list[left], parens_index_map[left], right - 1)
    if token_list[left] == "(" and parens_index_map[left] == right - 1:
        return create_ast(token_list, left + 1, right - 1, parens_index_map)

    # Search for assignment
    i = left
    while i < right:
        # making sure to save parentheses for later
        if token_list[i] == "(":
            i = parens_index_map[i]
        elif token_list[i] == "=":
            if i == left or i == right - 1: # one side is empty
                return AST("ERROR", "Assignment missing one or more element")
            else:
                ast = AST("ASSIGN", "=")
                var_ast = AST("ASSIGN_VAR", token_list[i-1])
                val_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [var_ast, val_ast]
                return ast
        i += 1

    # Search for addition, subtraction
    i = right - 1
    while i >= left:
        # making sure to save parentheses for later
        if token_list[i] == ")":
            i = parens_index_map[i]
        elif token_list[i] == "+":
            if i == left or i == right - 1:
                return AST("ERROR", "Addition missing one or more elements")
            else:
                ast = AST("ADD", "+")
                left_ast = create_ast(token_list, left, i, parens_index_map)
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [left_ast, right_ast]
                return ast

        elif token_list[i] == "-":
            # making sure to save parentheses for later
            if i == right - 1:
                return AST("ERROR", "Subtraction missing one or more elements")
            elif i == left or token_list[i - 1] in non_pre_subtraction_ops:
                # if the '-' is actually a negation and not a subtraction
                # change the token to '~'
                token_list[i] = '~'
                return create_ast(token_list, left, right, parens_index_map)
            else:
                ast = AST("SUB", "-")
                left_ast = create_ast(token_list, left, i, parens_index_map)
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [left_ast, right_ast]
                return ast

        i -= 1

    # Search for multiplication, division
    i = right - 1
    while i >= left:
        # making sure to save parentheses for later
        if token_list[i] == ")":
            i = parens_index_map[i]
        elif token_list[i] == "*":
            if i == left or i == right - 1:
                return AST("ERROR", "Multiplication missing one or more elements")
            else:
                ast = AST("MULT", "*")
                left_ast = create_ast(token_list, left, i, parens_index_map)
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [left_ast, right_ast]
                return ast

        elif token_list[i] == "/":
            # making sure to save parentheses for later
            if i == left or i == right - 1:
                return AST("ERROR", "Division missing one or more elements")
            else:
                ast = AST("DIV", "/")
                left_ast = create_ast(token_list, left, i, parens_index_map)
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [left_ast, right_ast]
                return ast

        i -= 1

    # Search for exponentiation and negation
    # exponentiation and negation are of equal precedence because an 
    # imbalance would lead errors or incorrect outcomes
    i = left
    while i < right:
        # making sure to save parentheses for later
        if token_list[i] == "(":
            i = parens_index_map[i]
        elif token_list[i] == "^":
            if i == left or i == right - 1:
                return AST("ERROR", "Exponentiation missing one or more elements")
            else:
                ast = AST("EXP", "^")
                left_ast = create_ast(token_list, left, i, parens_index_map)
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [left_ast, right_ast]
                return ast
        elif token_list[i] == '~':
            # unary includes the case where if i isn't the left-most index, theres a problem
            if i != left:
                return AST("ERROR", "Unexpected element preceding negation")
            elif i == right - 1:
                return AST("ERROR", "Negation missing one or more elements")
            else:
                ast = AST("NEGATE", "~")
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [right_ast]
                return ast
        i += 1

    # Search for aggregate functions
    i = left
    while i < right:
        # making sure to save parentheses for later
        if token_list[i] == "(":
            i = parens_index_map[i]
        elif token_list[i] in aggregate_tokens:
            # unary includes the case where if i isn't the left-most index, theres a problem
            if i != left:
                return AST("ERROR", "Unexpected element preceding " + token_list[i].upper())
            elif i == right - 1:
                return AST("ERROR", token_list[i].upper() + " missing one or more elements")
            else:
                ast = AST(token_list[i].upper(), token_list[i])
                right_ast = create_ast(token_list, i + 1, right, parens_index_map)
                ast.children = [right_ast]
                return ast
        i += 1

    # if nothing else is found to match
    return AST("ERROR", "Unknown symbol(s)")


def parser(tokens):
    """
    [parser] creates an abstract syntax tree from a 2D list of tokens
        that will be created by the lexer.
    [tokens]: 2D list of tokens (strings) that represent float values
        when evaluated.
    """
    ast_list = []

    for token_list in tokens:
        valid_parens, parens_index_map = find_parentheses_relation(token_list)
        num_assigns = token_list.count("=")
        if num_assigns > 1 or (num_assigns == 1 and token_list.index("=") != 1):
            ast_list.append(AST("ERROR", "Invalid assignment syntax"))

        if valid_parens:
            ast_list.append(create_ast(token_list, 0, len(token_list), parens_index_map))
        else:
            ast_list.append(AST("ERROR", "Unmatched parentheses"))

    return ast_list

def check_float(n1, n2=0):
    """
    [check_float] checks whether or not n1 and n2 are (or can be converted to)
        floats. If they can, this function will return True. Otherwise False.
    Returns: Bool
    """
    try:
        _ = float(n1)
        _ = float(n2)
        return True
    except:
        return False


def evaluator(ast, env):
    """
    [evaluator] takes in an abstract syntax tree, [ast], and an
        environment, [env], which is a dictionary from variable name 
        to value. Outputs the value of the evaluation as well as the
        new environment.
    [ast]: AST object
    [env]: (variable -> value) hashmap
    """
    # possible types (strings): 
    # ERROR, ADD, SUB, MULT, DIV, EXP, NEGATE, ASSIGN, FLOAT, VAR, MAX, MIN, AVG, STD, STAT 

    ast_type = ast.type

    if ast_type == "ERROR":
        env["ERROR"] = ast.value
        return "ERROR"

    elif ast_type == "ADD":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(left, right):
            env["ERROR"] = "Cannot add with non-numbers"
            return "ERROR"
        else:
            return float(left) + float(right)

    elif ast_type == "SUB":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(left, right):
            env["ERROR"] = "Cannot subtract with non-numbers"
            return "ERROR"
        else:
            return float(left) - float(right)

    elif ast_type == "MULT":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(left, right):
            env["ERROR"] = "Cannot multiply with non-numbers"
            return "ERROR"
        else:
            return float(left) * float(right)

    elif ast_type == "DIV":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(left, right):
            env["ERROR"] = "Cannot divide with non-numbers"
            return "ERROR"
        elif float(right) == 0:
            env["ERROR"] = "Can not divide by 0"
            return "ERROR"
        else:
            return float(left) / float(right)

    elif ast_type == "EXP":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(left, right):
            env["ERROR"] = "Cannot exponentiate with non-numbers"
            return "ERROR"
        elif float(left) == 0 and float(right) == 0:
            env["ERROR"] = "0 ^ 0 is undefined"
            return "ERROR"
        else:
            # we are only concerned with the real part of 
            # any exponentiation. In practice, there won't
            # be an imaginary part
            return (float(left) ** float(right)).real

    elif ast_type == "NEGATE":
        right = evaluator(ast.children[0], env)
        if right == "ERROR":
            return "ERROR"
        if not check_float(right):
            env["ERROR"] = "Cannot negate non-numbers"
            return "ERROR"
        else:
            return -1 * float(right)

    elif ast_type == "ASSIGN":
        left = evaluator(ast.children[0], env)
        right = evaluator(ast.children[1], env)
        if left == "ERROR" or right == "ERROR":
            return "ERROR"
        if not check_float(right):
            env["ERROR"] = "Cannot assign a non-number"
            return "ERROR"
        else:
            # assign doesn't truly return anything, however to prevent
            # multiple assignments in the same line, it will return a
            # an error informing that assignment is a null operation
            # env[str(left)] = float(right)
            # env["ERROR"] = "Variable assignment does not evaluate to a number"
            # return "ERROR"
            env[str(left)] = float(right)
            return 0


    elif ast_type == "FLOAT":
        return float(ast.value)

    elif ast_type == "VAR":
        if ast.value in env:
            return env[ast.value]
        else:
            env["ERROR"] = "Variable '" + ast.value + "' is used before assignment"
            return "ERROR"

    elif ast_type == "ASSIGN_VAR":
        return ast.value

def interpreter(ast_list):

    if len(ast_list) == 0:
        return 0

    env = {}
    values = []
    for i, ast in enumerate(ast_list):
        value = evaluator(ast, env)
        if value == "ERROR":
            return "Error (line " + str(i + 1) + "): " + env["ERROR"]
        values.append(value)

    return values[-1]


input_string = "n = -2 * 4^1.5 \r\n k = 5/n \r\n k + 0.2"
token_array = lexer(input_string)
ast_list = parser(token_array)
env = {}
evaluation = interpreter(ast_list)
print(evaluation)



