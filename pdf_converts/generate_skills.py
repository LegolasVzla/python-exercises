# -*- coding: utf-8 -*-
import os
from tika import parser
from settings import *

def main():
	categories = {}
	file = PATH_FILE

	raw_data = parser.from_file(file)

	# Remove break lines
	cleaned_data = raw_data['content'].replace('\n','')

	# Obtain data just by adding '*' for each category
	# (previousyly done directly in the document)
	cleaned_data = cleaned_data.split('*')

	categories['Courier services'] = cleaned_data[1].split('#')

	categories['Web Design'] = cleaned_data[2].split('#')

	categories['Cleaning services'] = cleaned_data[3].split('#')

	categories['Tutoring services'] = cleaned_data[4].split('#')

	categories['Plumbing services'] = cleaned_data[5].split('#')

	categories['Architects skills'] = cleaned_data[6].split('#')

	categories['Care services'] = cleaned_data[7].split('#')

	categories['Beauty&Health services'] = cleaned_data[8].split('#')

	categories['Repair and construction'] = cleaned_data[9].split('#')

	categories['Shipping'] = cleaned_data[10].split('#')

	categories['Virtual assistant'] = cleaned_data[11].split('#')

	categories['Computer services'] = cleaned_data[12].split('#')

	categories['Photo and video services'] = cleaned_data[13].split('#')

	categories['Events and promotions'] = cleaned_data[14].split('#')

	categories['Installation and repair of machinery/ Repair of digital equipment'] = cleaned_data[15].split('#')

	categories['Legal services'] = cleaned_data[16].split('#')

	categories['Repair of vehicles'] = cleaned_data[17].split('#')


if __name__ == '__main__':
    main()
