# -*- coding: utf-8 -*-
import os
from tika import parser
from configparser import RawConfigParser
import json

BASE_DIR = os.getcwd()
config = RawConfigParser()
config.read(BASE_DIR + '/settings.ini')

PATH_FILE = config.get('pathFile', 'PATH_FILE')

def get_skill(skills_by_category_array,category_index):
	data = []
	# Categories list (18)
	'''
	"Courier services",
	"Design",
	"Cleaning services",
	"Tutoring services",
	"Plumbing services",
	"Architects",
	"Care",
	"Beauty&Health services",
	"Repair and construction",
	"Shipping",
	"Virtual assistant",
	"Computer services",
	"Photo and video services",
	"Events and promotions",
	"Installation and repair of machinery",
	"Repair of digital equipment",
	"Legal services",
	"Repair of vehicles"
	'''
	categories_id = [
		"5e000580c76a8e047da94770",
		"5e000580c76a8e047da94771",
		"5e000580c76a8e047da94772",
		"5e000580c76a8e047da94773",
		"5e000580c76a8e047da94774",
		"5e000580c76a8e047da94781",
		"5e000580c76a8e047da94775",
		"5e000580c76a8e047da94776",
		"5e000580c76a8e047da94777",
		"5e000580c76a8e047da94778",
		"5e000580c76a8e047da94779",
		"5e000580c76a8e047da9477a",
		"5e000580c76a8e047da9477b",
		"5e000580c76a8e047da9477c",
		"5e000580c76a8e047da9477d",
		"5e000580c76a8e047da9477e",
		"5e000580c76a8e047da9477f",
		"5e000580c76a8e047da94780"
	]
	# Structure template needed:
	# {"_id":{"$oid":"<id>"},"isActive":true,"isDeleted":false,"name":"<name>","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}

	for index,skill in enumerate(skills_by_category_array):
		#print(category_index,"--",index,"--",skill)

		# index = 0 is the category Name
		if index > 0 and category_index < 15:
			data.append('{"categoryId":"' + categories_id[category_index] + '","isActive": true,"isDeleted": false,"name":"' + skill + '","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}')

			# Installation and repair of machinery/ Repair of digital equipment in pdf file
			if category_index == 14:
				data.append('{"categoryId":"' + categories_id[category_index+1] + '","isActive": true,"isDeleted": false,"name":"' + skill + '","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}')

		# Legal services and Repair of vehicles in pdf file
		if index > 0 and category_index >= 15:
			data.append('{"categoryId":"' + categories_id[category_index+1] + '","isActive": true,"isDeleted": false,"name":"' + skill + '","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}')

	return data

def main():
	skills_mongo_collection = []
	file = PATH_FILE

	raw_data = parser.from_file(file)

	# Remove break lines
	cleaned_data = raw_data['content'].replace('\n','')

	# Obtain data just by adding '*' for each category
	# (previousyly done directly in the document)
	cleaned_data = cleaned_data.split('*')

	for i in range(1,18):
		#print(i,cleaned_data[i].split('#'),cleaned_data[i].split('#')[0],"\n")
		skills_mongo_collection.append(
			get_skill(
				cleaned_data[i].split('#'),
				i-1)
			)

	# Remove ''
	cleaned_data = str(skills_mongo_collection).replace("'",'')

	with open(BASE_DIR + "/skills_mongo_collection.json", "+w") as text_file:
		text_file.write(cleaned_data)

if __name__ == '__main__':
    main()
