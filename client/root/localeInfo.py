
	# search
	
def SecondToHM(time):


	# add:
def FormatTime(time):
	if time < 0:
		return "0s" 

	(d, remainder) = divmod(time, 86400)
	(h, remainder) = divmod(remainder, 3600)
	(m, s) = divmod(remainder, 60)

	time_parts = [
		"{}d".format(d) if d > 0 else "",
		"{}h".format(h) if h > 0 else "",
		"{}m".format(m) if m > 0 else "",
		"{}s".format(s) if s > 0 else "",
	]

	formatted_time = " ".join(filter(None, time_parts))
	return formatted_time
