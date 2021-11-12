#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def fine_calculator(area,speed):
	valid_areas = ["urban", "expressway", "motorway"]
	if type(area) != str:
		return "Invalid Area Type"
	if not area in valid_areas:
		return "Invalid Area Value"

	if type(speed) != int and type(speed) != float:
		return "Invalid Speed Type"
	if speed < 0:
		return "Invalid Speed Value"

	if area == "urban":
		if speed <= 50:
			return 0
		return round(pow((2*(speed-50)), 2))
	if area == "expressway":
		if speed <=100:
			return 0
		return round(0.8*pow((speed-100), 2))
	if area == "motorway":
		if speed <= 120:
			return 0
		return round(0.5*pow((speed-120)/1.2, 2))

print(fine_calculator("Urban".lower(), 250))