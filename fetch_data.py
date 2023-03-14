import json
import requests


# Get data of sessions given the district and the date
def get_sessions(district_id: int, date: str):
	url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={date}'

	data = requests.get(url)

	# Dump data in "data.json"
	with open("all_sessions_data.json", 'w') as file:
		json.dump(data.json(), file, indent=2)


# Object area
class Area:
	def __init__(self, data: dict):
		for i in data:
			if "id" in i:
				self.id = data[i]
			elif "name" in i:
				self.name = data[i]


# Get list of all states
def get_states():
	data = requests.get(
		"https://cdn-api.co-vin.in/api/v2/admin/location/states")

	# Store the data in "states.json"
	with open("states.json", 'w') as file:
		json.dump(data.json(), file, indent=2)

	print("Data of all states received...")


# Find state and return the state ID
def find_state(state_name: str):
	# Load data of states
	with open("states.json", 'r') as file:
		data = json.load(file)

	states = data["states"]

	# For every state
	for state in states:
		current_state = Area(state)
		# if current state == state
		if current_state.name == state_name:
			state_id = current_state.id
			break

	print(f'State name : {state_name}')
	print(f'State ID : {state_id}')

	return state_id


# Get list of all districts
def get_districts(state_id: int):
	data = requests.get(
		f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}')

	# Store data in "districts.json"
	with open("districts.json", 'w') as file:
		json.dump(data.json(), file, indent=2)

	print("Data of all districts received...")


# Find district and return the district ID
def find_district(district_name: str):
	# Load data of districts
	with open("districts.json", 'r') as file:
		data = json.load(file)

	districts = data["districts"]

	# For every district
	for district in districts:
		current_district = Area(district)
		# if current district == district
		if current_district.name == district_name:
			district_id = current_district.id
			break

	print(f'District name : {district_name}')
	print(f'District ID : {district_id}')

	return district_id


# Load all the requirements
def load_information():
	with open("information.json", 'r') as file:
		data = json.load(file)
		state = data["state"]
		district = data["district"]
		date = data["date"]

	print("Loaded required information...")

	return [state, district, date]


if __name__ == "__main__":
	[state, district, date] = load_information()

	get_states()
	state_id = find_state(state)

	get_districts(state_id)
	district_id = find_district(district)

	get_sessions(district_id, date)
