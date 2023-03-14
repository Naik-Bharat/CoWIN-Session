import json
import fetch_data


# getting the data for all centres in the given district and on the given date
def get_data():
	[state, district, date] = fetch_data.load_information()

	fetch_data.get_states()
	state_id = fetch_data.find_state(state)

	fetch_data.get_districts(state_id)
	district_id = fetch_data.find_district(district)

	fetch_data.get_sessions(district_id, date)


# Filtering out the centres on the basis of doses available, age and vaccine
def available():
	# List of available centres
	available_sessions = []

	# Loading age, vaccine and dose number in the program from "information.json"
	with open("information.json", 'r') as file:
		details = json.load(file)
		age = details["age"]
		vaccine = details["vaccine"]
		dose = details["dose"]

	# Loading the data of all centres from "data.json"
	with open("all_sessions_data.json", 'r') as file:
		data = json.load(file)

	# For every session
	for session in data["sessions"]:
		# If session meets all requirements
		if session[f'available_capacity_dose{dose}'] >= 1 and session["min_age_limit"] <= age and session["vaccine"] == vaccine:
			# Add this session to available sessions
			available_sessions.append(session)

	# Dump data into "available_doses.json"
	with open("available_sessions_data.json", 'w') as file:
		json.dump(available_sessions, file, indent=2)

	if available_sessions != []:
		print(
			f'There were a total of {len(available_sessions)} sessions available...')

	elif available_sessions == []:
		print("No sessions were available that satisfied all criterias...")


get_data()
available()
