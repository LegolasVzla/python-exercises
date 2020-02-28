# -*- coding: utf-8 -*-
import os
from tika import parser
from configparser import RawConfigParser
import json

BASE_DIR = os.getcwd()
config = RawConfigParser()
config.read(BASE_DIR + '/settings.ini')

PATH_FILE = config.get('pathFile', 'PATH_FILE')

def get_skill(category_skills_array,categoryId):
	data = []
	for index,skill in enumerate(category_skills_array):
		if index > 1:
			data.append({
				"isActive": True,
				"isDeleted": False,
				"name": skill,
				"categoryId": categoryId
			})
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

	i=1
	while(i !=18):
		skills_mongo_collection.append(
			get_skill(
				cleaned_data[i].split('#'),
				cleaned_data[i].split('#')[0])
			)
		i+=1

	with open(BASE_DIR + "/skills_mongo_collection.json", "+w") as text_file:
		text_file.write(json.dumps(skills_mongo_collection))

if __name__ == '__main__':
    main()
