# -*- coding: utf-8 -*-
import os
from tika import parser
from configparser import RawConfigParser
import json

BASE_DIR = os.getcwd()
config = RawConfigParser()
config.read(BASE_DIR + '/settings.ini')

PATH_FILE = config.get('pathFile', 'PATH_FILE')

def get_skill(category_skills_array,categoryId,category_index):
	data = []
	# Categories list
	'''
	"Courier services",
	"Design",
	"Cleaning services",
	"Tutoring services",
	"Plumbing services",
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
		"5e000580c76a8e047da9477e",
		"5e000580c76a8e047da9477f",
		"5e000580c76a8e047da94780"
	]
	# Structure template needed:
	# {"_id":{"$oid":"<id>"},"isActive":true,"isDeleted":false,"name":"<name>","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}
	for index,skill in enumerate(category_skills_array):
		if index > 0:
			data.append('{"_id":{"$oid":' + categories_id[category_index] + '},"isActive": true,"isDeleted": false,"name":"' + skill + '","createAt":{"$date":{"$numberLong":"1577126355672"}},"updateAt":{"$date":{"$numberLong":"1577126355672"}},"__v":{"$numberInt":"0"}}')
		#print(category_index,"--",index,"--",skill)
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
	if i == 6:	# Architects skills
		pass
	else:
		skills_mongo_collection.append(
			get_skill(
				cleaned_data[i].split('#'),
				cleaned_data[i].split('#')[0],
				i)
			)

with open(BASE_DIR + "/skills_mongo_collection.json", "+w") as text_file:
	text_file.write(str(skills_mongo_collection))

if __name__ == '__main__':
    main()
