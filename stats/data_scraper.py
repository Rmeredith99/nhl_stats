import json
import requests
from stats.models import StatLine


class Skater:
	def __init__(self, player_id):
		self.id = player_id
		self.data = {}

	def __str__(self):
		return self.data["playerName"]


def get_json(url):
	"""
	[get_json] takes in a url and returns a json object with the contents.
	url: string
	"""
	response = requests.get(url).text
	return json.loads(response)


def get_urls(year, playoffs):
	"""
	Given the year in '20182019' formatting and a boolean denoting whether
		or not this is playoffs, [get_urls] returns a list of urls from which to 
		pull data.
	year: string
	playoffs: boolean
	returns: list<string>
	"""
	if playoffs:
		season = "%223%22"
	else:
		season = "%222%22"

	# URLs from which to pull data
	urls = []
	url1 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url1)

	url2 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatergoals&sort=[{%22property%22:%22evGoals%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url2)

	url3 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skaterpoints&sort=[{%22property%22:%22evPoints%22,%22direction%22:%22DESC%22},{%22property%22:%22points%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url3)

	url4 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=faceoffs&sort=[{%22property%22:%22faceoffsWon%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url4)

	url5 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skaterpowerplay&sort=[{%22property%22:%22ppPoints%22,%22direction%22:%22DESC%22},{%22property%22:%22ppGoals%22,%22direction%22:%22DESC%22},{%22property%22:%22ppAssists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url5)

	url6 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skaterpenaltykill&sort=[{%22property%22:%22shPoints%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url6)

	url7 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=realtime&sort=[{%22property%22:%22hits%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url7)

	url8 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=penalties&sort=[{%22property%22:%22penaltyMinutes%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url8)

	url9 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=timeonice&sort=[{%22property%22:%22timeOnIce%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url9)

	url10 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=shootout&isGame=false&reportName=skatershootout&sort=[{%22property%22:%22shootoutGoals%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url10)

	url11 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=plusminus&sort=[{%22property%22:%22plusMinus%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url11)

	url12 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=shooting&isGame=false&reportName=skaterpercentages&sort=[{%22property%22:%22shotAttemptsPctg%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url12)

	url13 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=shooting&isGame=false&reportName=skatersummaryshooting&sort=[{%22property%22:%22shotAttempts%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url13)

	url14 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=core&isGame=false&reportName=skaterscoring&sort=[{%22property%22:%22pointsPer60Minutes%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url14)

	url15 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=core&isGame=false&reportName=faceoffsbyzone&sort=[{%22property%22:%22faceoffWins%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url15)

	url16 = "http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=core&isGame=false&reportName=shottype&sort=[{%22property%22:%22shots%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=" + season + "%20and%20seasonId%3E=" + year + "%20and%20seasonId%3C=" + year
	urls.append(url16)

	return urls


def update_models(year, playoffs, player):
	"""
	[update_models] takes in information about what player to update, including
		the year, whether or not it's the playoffs, and a player object and 
		makes all necessary changes to the model pertaining to that player
		and saves the model.
	year: string
	playoffs: boolean
	player: player instance
	returns: None
	"""
	stat_queryset = StatLine.objects.filter(
			year__exact = int(year)
		).filter(
			playoffs__exact = playoffs
		).filter(
			playerId__exact = player.data["playerId"]
		)

	if stat_queryset.count() == 0:
		stat_model = StatLine(year = year, playoffs = playoffs)
	else:
		stat_model = stat_queryset.get(playerId = player.data["playerId"])

	###############################################
	# Start of original list of data points
	###############################################
	stat_model.assist1st = player.data['assist1st']
	stat_model.assist2nd = player.data['assist2nd']
	stat_model.assists = player.data['assists']
	stat_model.assistsPer60Minutes = player.data['assistsPer60Minutes']
	stat_model.assistsPerGame = player.data['assistsPerGame']
	stat_model.avgShotLength = player.data['avgShotLength']
	stat_model.blockedShots = player.data['blockedShots']
	stat_model.blockedShotsPerGame = player.data['blockedShotsPerGame']
	stat_model.defensiveZoneFaceoffs = player.data['defensiveZoneFaceoffs']
	stat_model.enGoals = player.data['enGoals']
	stat_model.evAssists = player.data['evAssists']
	stat_model.evFaceoffWinPctg = player.data['evFaceoffWinPctg']
	stat_model.evFaceoffsLost = player.data['evFaceoffsLost']
	stat_model.evFaceoffsWon = player.data['evFaceoffsWon']
	stat_model.evGoals = player.data['evGoals']
	stat_model.evPoints = player.data['evPoints']
	stat_model.evTimeOnIce = player.data['evTimeOnIce']
	stat_model.evTimeOnIcePerGame = player.data['evTimeOnIcePerGame']
	stat_model.faceoffLoss = player.data['faceoffLoss']
	stat_model.faceoffLossDefensiveZone = player.data['faceoffLossDefensiveZone']
	stat_model.faceoffLossNeutralZone = player.data['faceoffLossNeutralZone']
	stat_model.faceoffLossOffensiveZone = player.data['faceoffLossOffensiveZone']
	stat_model.faceoffLossWhenAhead = player.data['faceoffLossWhenAhead']
	stat_model.faceoffLossWhenBehind = player.data['faceoffLossWhenBehind']
	stat_model.faceoffLossWhenClose = player.data['faceoffLossWhenClose']
	stat_model.faceoffWinPctg = player.data['faceoffWinPctg']
	stat_model.faceoffWinPctgDefensiveZone = player.data['faceoffWinPctgDefensiveZone']
	stat_model.faceoffWinPctgNeutralZone = player.data['faceoffWinPctgNeutralZone']
	stat_model.faceoffWinPctgOffensiveZone = player.data['faceoffWinPctgOffensiveZone']
	stat_model.faceoffWins = player.data['faceoffWins']
	stat_model.faceoffWinsDefensiveZone = player.data['faceoffWinsDefensiveZone']
	stat_model.faceoffWinsNeutralZone = player.data['faceoffWinsNeutralZone']
	stat_model.faceoffWinsOffensiveZone = player.data['faceoffWinsOffensiveZone']
	stat_model.faceoffWinsWhenAhead = player.data['faceoffWinsWhenAhead']
	stat_model.faceoffWinsWhenBehind = player.data['faceoffWinsWhenBehind']
	stat_model.faceoffWinsWhenClose = player.data['faceoffWinsWhenClose']
	stat_model.faceoffs = player.data['faceoffs']
	stat_model.faceoffsLost = player.data['faceoffsLost']
	stat_model.faceoffsTaken = player.data['faceoffsTaken']
	stat_model.faceoffsWon = player.data['faceoffsWon']
	stat_model.firstGoals = player.data['firstGoals']
	stat_model.fiveOnFiveShootingPctg = player.data['fiveOnFiveShootingPctg']
	stat_model.gameWinningGoals = player.data['gameWinningGoals']
	stat_model.gamesPlayed = player.data['gamesPlayed']
	stat_model.giveaways = player.data['giveaways']
	stat_model.goals = player.data['goals']
	stat_model.goalsBackhand = player.data['goalsBackhand']
	stat_model.goalsDeflected = player.data['goalsDeflected']
	stat_model.goalsPer60Minutes = player.data['goalsPer60Minutes']
	stat_model.goalsPerGame = player.data['goalsPerGame']
	stat_model.goalsSlap = player.data['goalsSlap']
	stat_model.goalsSnap = player.data['goalsSnap']
	stat_model.goalsTipped = player.data['goalsTipped']
	stat_model.goalsWraparound = player.data['goalsWraparound']
	stat_model.goalsWrist = player.data['goalsWrist']
	stat_model.hits = player.data['hits']
	stat_model.hitsPerGame = player.data['hitsPerGame']
	stat_model.homePlusMinus = player.data['homePlusMinus']
	stat_model.missedShots = player.data['missedShots']
	stat_model.missedShotsHitCrossbar = player.data['missedShotsHitCrossbar']
	stat_model.missedShotsHitPost = player.data['missedShotsHitPost']
	stat_model.missedShotsOverNet = player.data['missedShotsOverNet']
	stat_model.missedShotsPerGame = player.data['missedShotsPerGame']
	stat_model.missedShotsWideOfNet = player.data['missedShotsWideOfNet']
	stat_model.offensiveZoneFaceoffs = player.data['offensiveZoneFaceoffs']
	stat_model.otGoals = player.data['otGoals']
	stat_model.penalties = player.data['penalties']
	stat_model.penaltiesDrawn = player.data['penaltiesDrawn']
	stat_model.penaltiesDrawnPer60Minutes = player.data['penaltiesDrawnPer60Minutes']
	stat_model.penaltiesGameMisconduct = player.data['penaltiesGameMisconduct']
	stat_model.penaltiesMajor = player.data['penaltiesMajor']
	stat_model.penaltiesMatch = player.data['penaltiesMatch']
	stat_model.penaltiesMinor = player.data['penaltiesMinor']
	stat_model.penaltiesMisconduct = player.data['penaltiesMisconduct']
	stat_model.penaltiesPer60Minutes = player.data['penaltiesPer60Minutes']
	stat_model.penaltyMinutes = player.data['penaltyMinutes']
	stat_model.penaltyMinutesPerGame = player.data['penaltyMinutesPerGame']
	stat_model.penaltyShotAttempts = player.data['penaltyShotAttempts']
	stat_model.penaltyShotGoals = player.data['penaltyShotGoals']
	stat_model.playerBirthCity = player.data['playerBirthCity']
	stat_model.playerBirthCountry = player.data['playerBirthCountry']
	stat_model.playerBirthDate = player.data['playerBirthDate']
	stat_model.playerBirthStateProvince = player.data['playerBirthStateProvince']
	stat_model.playerDraftOverallPickNo = player.data['playerDraftOverallPickNo']
	stat_model.playerDraftRoundNo = player.data['playerDraftRoundNo']
	stat_model.playerDraftYear = player.data['playerDraftYear']
	stat_model.playerFirstName = player.data['playerFirstName']
	stat_model.playerHeight = player.data['playerHeight']
	stat_model.playerId = player.data['playerId']
	stat_model.playerInHockeyHof = player.data['playerInHockeyHof']
	stat_model.playerIsActive = player.data['playerIsActive']
	stat_model.playerLastName = player.data['playerLastName']
	stat_model.playerName = player.data['playerName']
	stat_model.playerNationality = player.data['playerNationality']
	stat_model.playerPositionCode = player.data['playerPositionCode']
	stat_model.playerShootsCatches = player.data['playerShootsCatches']
	stat_model.playerTeamsPlayedFor = player.data['playerTeamsPlayedFor']
	stat_model.playerWeight = player.data['playerWeight']
	stat_model.plusMinus = player.data['plusMinus']
	stat_model.points = player.data['points']
	stat_model.pointsPer60Minutes = player.data['pointsPer60Minutes']
	stat_model.pointsPerGame = player.data['pointsPerGame']
	stat_model.ppAssists = player.data['ppAssists']
	stat_model.ppFaceoffWinPctg = player.data['ppFaceoffWinPctg']
	stat_model.ppFaceoffsLost = player.data['ppFaceoffsLost']
	stat_model.ppFaceoffsWon = player.data['ppFaceoffsWon']
	stat_model.ppGiveaways = player.data['ppGiveaways']
	stat_model.ppGoals = player.data['ppGoals']
	stat_model.ppHits = player.data['ppHits']
	stat_model.ppMissedShots = player.data['ppMissedShots']
	stat_model.ppPoints = player.data['ppPoints']
	stat_model.ppShots = player.data['ppShots']
	stat_model.ppTakeaways = player.data['ppTakeaways']
	stat_model.ppTeamGoalsAgainst = player.data['ppTeamGoalsAgainst']
	stat_model.ppTeamGoalsFor = player.data['ppTeamGoalsFor']
	stat_model.ppTimeOnIce = player.data['ppTimeOnIce']
	stat_model.ppTimeOnIcePerGame = player.data['ppTimeOnIcePerGame']
	stat_model.roadPlusMinus = player.data['roadPlusMinus']
	stat_model.seasonId = player.data['seasonId']
	stat_model.shAssists = player.data['shAssists']
	stat_model.shBlockedShots = player.data['shBlockedShots']
	stat_model.shFaceoffWinPctg = player.data['shFaceoffWinPctg']
	stat_model.shFaceoffsLost = player.data['shFaceoffsLost']
	stat_model.shFaceoffsWon = player.data['shFaceoffsWon']
	stat_model.shGiveaways = player.data['shGiveaways']
	stat_model.shGoals = player.data['shGoals']
	stat_model.shHits = player.data['shHits']
	stat_model.shMissedShots = player.data['shMissedShots']
	stat_model.shPoints = player.data['shPoints']
	stat_model.shShots = player.data['shShots']
	stat_model.shTakeaways = player.data['shTakeaways']
	stat_model.shTimeOnIce = player.data['shTimeOnIce']
	stat_model.shTimeOnIcePerGame = player.data['shTimeOnIcePerGame']
	stat_model.shifts = player.data['shifts']
	stat_model.shiftsPerGame = player.data['shiftsPerGame']
	stat_model.shootingPctg = player.data['shootingPctg']
	stat_model.shootingPlusSavePctg = player.data['shootingPlusSavePctg']
	stat_model.shotAttempts = player.data['shotAttempts']
	stat_model.shotAttemptsAgainst = player.data['shotAttemptsAgainst']
	stat_model.shotAttemptsAhead = player.data['shotAttemptsAhead']
	stat_model.shotAttemptsBehind = player.data['shotAttemptsBehind']
	stat_model.shotAttemptsClose = player.data['shotAttemptsClose']
	stat_model.shotAttemptsFor = player.data['shotAttemptsFor']
	stat_model.shotAttemptsPctg = player.data['shotAttemptsPctg']
	stat_model.shotAttemptsPctgAhead = player.data['shotAttemptsPctgAhead']
	stat_model.shotAttemptsPctgBehind = player.data['shotAttemptsPctgBehind']
	stat_model.shotAttemptsPctgClose = player.data['shotAttemptsPctgClose']
	stat_model.shotAttemptsPctgTied = player.data['shotAttemptsPctgTied']
	stat_model.shotAttemptsRelPctg = player.data['shotAttemptsRelPctg']
	stat_model.shotAttemptsTied = player.data['shotAttemptsTied']
	stat_model.shots = player.data['shots']
	stat_model.shotsBackhand = player.data['shotsBackhand']
	stat_model.shotsDeflected = player.data['shotsDeflected']
	stat_model.shotsPerGame = player.data['shotsPerGame']
	stat_model.shotsSlap = player.data['shotsSlap']
	stat_model.shotsSnap = player.data['shotsSnap']
	stat_model.shotsTipped = player.data['shotsTipped']
	stat_model.shotsWraparound = player.data['shotsWraparound']
	stat_model.shotsWrist = player.data['shotsWrist']
	stat_model.takeaways = player.data['takeaways']
	stat_model.teamGoalsAgainst = player.data['teamGoalsAgainst']
	stat_model.teamGoalsFor = player.data['teamGoalsFor']
	stat_model.timeOnIce = player.data['timeOnIce']
	stat_model.timeOnIcePerGame = player.data['timeOnIcePerGame']
	stat_model.timeOnIcePerShift = player.data['timeOnIcePerShift']
	stat_model.unblockedShotAttempts = player.data['unblockedShotAttempts']
	stat_model.unblockedShotAttemptsAgainst = player.data['unblockedShotAttemptsAgainst']
	stat_model.unblockedShotAttemptsAhead = player.data['unblockedShotAttemptsAhead']
	stat_model.unblockedShotAttemptsBehind = player.data['unblockedShotAttemptsBehind']
	stat_model.unblockedShotAttemptsClose = player.data['unblockedShotAttemptsClose']
	stat_model.unblockedShotAttemptsFor = player.data['unblockedShotAttemptsFor']
	stat_model.unblockedShotAttemptsPctg = player.data['unblockedShotAttemptsPctg']
	stat_model.unblockedShotAttemptsPctgAhead = player.data['unblockedShotAttemptsPctgAhead']
	stat_model.unblockedShotAttemptsPctgBehind = player.data['unblockedShotAttemptsPctgBehind']
	stat_model.unblockedShotAttemptsPctgClose = player.data['unblockedShotAttemptsPctgClose']
	stat_model.unblockedShotAttemptsPctgTied = player.data['unblockedShotAttemptsPctgTied']
	stat_model.unblockedShotAttemptsRelPctg = player.data['unblockedShotAttemptsRelPctg']
	stat_model.unblockedShotAttemptsTied = player.data['unblockedShotAttemptsTied']
	stat_model.zoneStartPctg = player.data['zoneStartPctg']
	###############################################
	# End of original list of data points
	###############################################


	stat_model.save()



def update_data(year, playoffs):
	"""
	[update_data] takes in a year in "20182019" format and a boolean denoting
		whether or not this is the playoffs and updates all the objects in
		the StatLine model for the given season.
	year: string
	playoffs: boolean
	returns: None
	"""

	urls = get_urls(year, playoffs)

	player_lookup = {}
	for url in urls:
		try:
			data = get_json(url)['data']
		except:
			print(get_json(url))
			quit()
		for player in data:
			player_id = player["playerId"]
			if player_id in player_lookup:
				player_instance = player_lookup[player_id]
			else:
				player_instance = Skater(player_id)
			for key in player:
				player_instance.data[key] = player[key]
				player_lookup[player_id] = player_instance

	# List of player
	players = list(player_lookup.values())

	# updates models
	for player in players:
		update_models(year, playoffs, player)