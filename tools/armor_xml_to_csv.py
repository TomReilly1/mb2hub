import xml.etree.ElementTree as ET
import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
from pandas import ExcelWriter
import csv
import numpy as np
import json

'''
Order of armor headers
---------------------------		
HEAD:		head
SHOULDER:	body, arm
BODY:		body, arm, leg
ARM:		arm
LEG:		leg
'''


def make_header(xml_file):
	tmp = ("ID", "Name", "Culture", "Weight")

	if xml_file == "head_armors.xml":
		headers_tuple = tmp + ("Head Armor",)
	elif xml_file == "shoulder_armors.xml":
		headers_tuple = tmp + ("Body Armor", "Arm Armor")
	elif xml_file == "body_armors.xml":
		headers_tuple = tmp + ("Body Armor", "Arm Armor", "Leg Armor")
	elif xml_file == "arm_armors.xml":
		headers_tuple = tmp + ("Arm Armor",)
	elif xml_file == "leg_armors.xml":
		headers_tuple = tmp + ("Leg Armor",)

	return headers_tuple


def get_armor_rating(xml_file, ar):
	armor_list = []

	if xml_file == "head_armors.xml":
		armor_list.append(ar.find('ItemComponent').find('Armor').get('head_armor'))
	elif xml_file == "shoulder_armors.xml":
		armor_list.append(ar.find('ItemComponent').find('Armor').get('body_armor'))
		armor_list.append(ar.find('ItemComponent').find('Armor').get('arm_armor'))
	elif xml_file == "body_armors.xml":
		armor_list.append(ar.find('ItemComponent').find('Armor').get('body_armor'))
		armor_list.append(ar.find('ItemComponent').find('Armor').get('arm_armor'))
		armor_list.append(ar.find('ItemComponent').find('Armor').get('leg_armor'))
	elif xml_file == "arm_armors.xml":
		armor_list.append(ar.find('ItemComponent').find('Armor').get('arm_armor'))
	elif xml_file == "leg_armors.xml":
		armor_list.append(ar.find('ItemComponent').find('Armor').get('leg_armor'))

	return armor_list


def make_armor_template(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	# INITIALIZES 2D LIST FOR ARMOR PEICES
	ar_2D_list = []

	# CREATES HEADER
	headers_tuple = make_header(xml_file)

	# FOR EACH PEICE OF ARMOR IN THE ROOT
	for ar in root.findall('Item'):
		id_ar = ar.get('id')
		name = ar.get('name').partition("}")[2]
		culture = ar.get('culture').partition(".")[2]
		if culture == "neutral_culture":
			culture = "neutral"
		weight = ar.get('weight')

		first_half_list = [id_ar, name, culture, weight]
		second_half_list = get_armor_rating(xml_file, ar)
		single_armor_list = first_half_list + second_half_list
		# turns every "None" to "0"
		single_armor_list = ["0" if i == None else i for i in single_armor_list]

		ar_2D_list.append(single_armor_list)		

	# MAKES CSV FILE NAME
	tmp = xml_file.split(".")[0]
	csv_file_name = f"{tmp}.csv"

	# WRITES 2D LIST TO CSV FILE
	with open(csv_file_name, 'w', newline ='') as file:
		write = csv.writer(file)
		write.writerow(headers_tuple)
		write.writerows(ar_2D_list)


if __name__ == '__main__':
	make_armor_template('head_armors.xml')
	make_armor_template('shoulder_armors.xml')
	make_armor_template('body_armors.xml')
	make_armor_template('arm_armors.xml')
	make_armor_template('leg_armors.xml')
