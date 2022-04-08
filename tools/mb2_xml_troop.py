import xml.etree.ElementTree as ET
import openpyxl
from openpyxl import Workbook, load_workbook
import pandas as pd
from pandas import ExcelWriter
import csv
import numpy as np
import json


def get_armor(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	ar_2D_list = []
	headers_tuple = ("ID", "Name", "Culture", "Head Armor", "Body Armor", "Arm Armor", "Leg Armor", "Weight")

	# FOR EACH PEICE OF ARMOR IN THE ROOT
	for ar in root.findall('Item'):
		id_ar = ar.get('id')
		name = ar.get('name').partition("}")[2]
		culture = ar.get('culture').partition(".")[2]
		if culture == "neutral_culture":
			culture = "neutral"
		weight = ar.get('weight')

		ar_rating_head = ar.find('ItemComponent').find('Armor').get('head_armor')
		ar_rating_body = ar.find('ItemComponent').find('Armor').get('body_armor')
		ar_rating_arm = ar.find('ItemComponent').find('Armor').get('arm_armor')
		ar_rating_leg = ar.find('ItemComponent').find('Armor').get('leg_armor')
		entry = [id_ar, name, culture, ar_rating_head, ar_rating_body, ar_rating_arm, ar_rating_leg, weight]
		entry = ["0" if i == None else i for i in entry]
		print(entry)
		ar_2D_list.append(entry)

	# CREATES CSV FILE NAME
	tmp = xml_file.split(".")[0]
	csv_file_name = "mb2_" + tmp + ".csv"

	with open(csv_file_name, 'w', newline ='') as file:
		write = csv.writer(file)
		write.writerow(headers_tuple)
		write.writerows(ar_2D_list)

	df = pd.read_csv(csv_file_name)

	ws_name = xml_file.partition('_')[0]

	with ExcelWriter('MB2.xlsx', mode='a') as writer:
		df.to_excel(writer, sheet_name=ws_name, index=False, header=["ID", "Name", "Culture", "Head Armor", "Body Armor", "Arm Armor", "Leg Armor", "Weight"])

def get_horses(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	horse_list = []
	headers_tuple = ("ID", "Name", "Culture", "Subtype", "Charge Damage", "Maneuver", "Speed", "Health")

	for horse in root.findall('Item'):
		id_horse = horse.get('id')
		name = horse.get('name').partition('}')[2]
		culture = horse.get('culture')
		if culture is None:
			culture = "neutral"
		else:
			culture = culture.partition('.')[2]
		subtype = horse.get('item_category')

		print(name)

		item_component = horse.find('ItemComponent')
		horse_stats = item_component.find('Horse')

		charge_dmg = int(horse_stats.get('charge_damage'))
		maneuver = int(horse_stats.get('maneuver'))
		speed = int(horse_stats.get('speed'))
		health = horse_stats.get('extra_health')
		if health is None:
			health = 200
		else:
			health = int(health)
			health += 200

		entry = [id_horse, name, culture, subtype, charge_dmg, maneuver, speed, health]
		horse_list.append(entry)

	file = open('mb2_horses.csv', 'w', newline ='')

	with file:
		write = csv.writer(file)
		write.writerow(headers_tuple)
		write.writerows(horse_list)

	df = pd.read_csv("mb2_horses.csv")
	print('hello')
	with ExcelWriter('MB2.xlsx', mode='a') as writer:
		df.to_excel(writer, sheet_name='horses', index=False, header=["ID", "Name", "Culture", "Subtype", "Charge Dmg", "Maneuver", "Speed", "Health"])
	print('goodbye')


def get_harness(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	harness_list = []
	headers_tuple = ("ID", "Name", "Culture", "Armor", "Weight")

	for harness in root.findall('Item'):
		id_harness = harness.get('id')
		name = harness.get('name').partition('}')[2]
		culture = harness.get('culture')
		if culture is None:
			culture = "neutral"
		else:
			culture = culture.partition('.')[2]
		weight = float(harness.get('weight'))

		print(name)

		item_component = harness.find('ItemComponent')
		harness_stats = item_component.find('Armor')

		body_armor = int(harness_stats.get('body_armor'))

		entry = [id_harness, name, culture, body_armor, weight]
		harness_list.append(entry)


	# file = open('mb2_harness.csv', 'w', newline ='')

	with open('mb2_harness.csv', 'w', newline ='') as file:
		write = csv.writer(file)
		write.writerow(headers_tuple)
		write.writerows(harness_list)

	df = pd.read_csv("mb2_harness.csv")

	with ExcelWriter('MB2.xlsx', mode='a') as writer:
		df.to_excel(writer, sheet_name='harnesses', index=False, header=["ID", "Name", "Culture", "Armor", "Weight"])




def get_npc(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	# INITIALIZES A 2D LIST TO STORE NPC'S AND THEIR STATS/EQUIPMENT; WILL BE USED TO PUT INTO A PANDAS DATAFRAME
	npc_2D_list = []
	game_skill_list = ('OneHanded', 'TwoHanded', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics')
    
    # FOR EACH NPC IN THE XML FILE
	for npc in root.findall('NPCCharacter'):
		id_npc = npc.get('id')
		name = npc.get('name').partition("}")[2]
		culture = npc.get('culture').partition(".")[2]
		troop_type = npc.get('default_group')
		occupation = npc.get('occupation')
		level = int(npc.get('level'))
		

		# CREATES THE AN ENTRY LIST; EACH ENTRY LIST REPRESENTS AN NPC
		entry = [id_npc, name, culture, troop_type, occupation, level]
		# INITIALIZES DICT FOR SKILLS
		skill_dict = {}
		
		template = npc.get('skill_template')
		print(template)
		# IF THEIR IS NO TEMPLATE, GET SKILLS AS NORMAL
		if template is None or template == '':
			print("NONE NONE NONE")
			skills = npc.find('skills')
    
			print(name)
			for skill in skills.findall('skill'):
				skill_id = skill.get('id')
				skill_value = skill.get('value')
				print(skill_id, skill_value)
				skill_dict[skill_id] = skill_value

				# Check if there is a missing skill; sometimes happens if skill value is zero
				for mia_skill in game_skill_list:
					if mia_skill not in skill_dict.keys():
						skill_dict[mia_skill] = "0"
		# IF THERE IS A TEMPLATE, FIND IT IN SEPARATE XML TO OBTAIN SKILLS
		else:
			print("YES YES YES")
			template = template.split('.')[1]
			print(template)

			temp_tree = ET.parse('sandboxcore_skill_sets.xml')
			temp_root = temp_tree.getroot()
			
			for skillset in temp_root.findall('SkillSet'):
				skillset_id = skillset.get('id')
				if skillset_id == template:
					print("FOUND")
					for skill in skillset.findall('skill'):
						skill_id = skill.get('id')
						skill_value = skill.get('value')
						print(skill_value, skill_id)
						skill_dict[skill_id] = skill_value

						# Check if there is a missing skill; sometimes happens if skill value is zero
						for mia_skill in game_skill_list:
							if mia_skill not in skill_dict.keys():
								skill_dict[mia_skill] = "0"


		entry.append(skill_dict['OneHanded'])
		entry.append(skill_dict['TwoHanded'])
		entry.append(skill_dict['Polearm'])
		entry.append(skill_dict['Bow'])
		entry.append(skill_dict['Crossbow'])
		entry.append(skill_dict['Throwing'])
		entry.append(skill_dict['Riding'])
		entry.append(skill_dict['Athletics'])

		# equipments = npc.find('Equipments')
		# for eq_roster in equipments.findall('EquipmentRoster'):
		# 	for eq in eq_roster:
		# 		slot = eq.get('slot')
		# 		id_eq = eq.get('id').partition(".")[2]
		# 		entry.append(slot + "_" + id_eq)

		npc_2D_list.append(entry)

	with open('mb2_npcs.csv', 'w', newline ='') as file:
		write = csv.writer(file)
		write.writerow(
			('Troop_ID',
			'Name',
			'Culture',
			'Group',
			'Occupation',
			'Level',
			'OneHanded',
			'TwoHanded',
			'Polearm',
			'Bow',
			'Crossbow',
			'Throwing',
			'Riding',
			'Athletics'))
		write.writerows(npc_2D_list)

	df = pd.DataFrame(npc_2D_list)

	with ExcelWriter('MB2.xlsx', mode='a') as writer:
		df.to_excel(writer, sheet_name='npcs', index=False)


def convert_id_to_name(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()
	eqpmnt_dict = {}

	for child in root:
		eqpmnt_id = child.get('id')
		eqpmnt_name = child.get('name').partition('}')[2]
		eqpmnt_dict[eqpmnt_id] = eqpmnt_name

	print(eqpmnt_dict)

	df = pd.read_excel('MB2.xlsx', sheet_name='npcs')
	for rowIndex, row in df.iterrows():
		for columnIndex, value in row.items():
			if type(value) == str:
				value_tag = value.partition('_')[0]
				value_id = value.partition('_')[2]
				if value_tag in ['Item0', 'Item1', 'Item2', 'Item3', 'Head', 'Cape', 'Body','Gloves', 'Leg']:
					df.at[rowIndex, columnIndex] = eqpmnt_dict.get(value_id)

	with ExcelWriter('MB2.xlsx', mode='a') as writer:
		df.to_excel(writer, sheet_name='npcRevised', index=False)

def get_npc_armor_avg():
	# ACCESS EVERY SHEET IN THE XLSX FILE
	df_npc = pd.read_excel('MB2.xlsx', sheet_name='npcs')
	df_head = pd.read_excel('MB2.xlsx', sheet_name='head')
	df_shld = pd.read_excel('MB2.xlsx', sheet_name='shoulder')
	df_body = pd.read_excel('MB2.xlsx', sheet_name='body')
	df_arm = pd.read_excel('MB2.xlsx', sheet_name='arm')
	df_leg = pd.read_excel('MB2.xlsx', sheet_name='leg')
	df_horse = pd.read_excel('MB2.xlsx', sheet_name='horses')
	df_harn = pd.read_excel('MB2.xlsx', sheet_name='harnesses')
	troop_2D_list = []

	# FOR EVERY TROOP
	for rowIndex, row in df_npc.iterrows():
		head, shld, body, arm, leg = ([] for i in range(5))
		name = row[2]
		troop_group = row[3]
		print(name)

		horse_breed = "n/a"
		horse_chrg_dmg = 0
		horse_speed = 0
		horse_maneuver = 0
		horse_health = 0
		harness_armor = 0


		# FOR EVERY ITEM THAT A TROOP CAN HAVE
		for columnIndex, value in row.items():

			if type(value) == str:
				value_tag = value.partition('_')[0]
				value_id = value.partition('_')[2]

				# HEAD ARMOR
				if value_tag == 'Head':
					Head_head_armor = df_head.loc[df_head.ID == value_id, 'Head Armor'].to_numpy()
					Head_head_armor = float(Head_head_armor)

					weight = df_head.loc[df_head.ID == value_id, 'Weight'].to_numpy()
					weight = float(weight)

					head.append([Head_head_armor, weight])
				# SHOULDER ARMOR
				elif value_tag == 'Cape':
					Shoulder_body_armor = df_shld.loc[df_shld.ID == value_id, 'Body Armor'].to_numpy()
					Shoulder_body_armor = float(Shoulder_body_armor)
					if Shoulder_body_armor is None:
						Shoulder_body_armor = 0

					Shoulder_arm_armor = df_shld.loc[df_shld.ID == value_id, 'Arm Armor'].to_numpy()
					Shoulder_arm_armor = float(Shoulder_arm_armor)
					if Shoulder_arm_armor is None:
						Shoulder_arm_armor = 0

					weight = df_shld.loc[df_shld.ID == value_id, 'Weight'].to_numpy()
					weight = float(weight)

					shld.append([Shoulder_body_armor, Shoulder_arm_armor, weight])
				# BODY ARMOR
				elif value_tag == 'Body':
					Body_body_armor = df_body.loc[df_body.ID == value_id, 'Body Armor'].to_numpy()
					Body_body_armor = float(Body_body_armor)
					if Body_body_armor is None:
						Body_body_armor = 0

					Body_arm_armor = df_body.loc[df_body.ID == value_id, 'Arm Armor'].to_numpy()
					Body_arm_armor = float(Body_arm_armor)
					if Body_arm_armor is None:
						Body_arm_armor = 0

					Body_leg_armor = df_body.loc[df_body.ID == value_id, 'Leg Armor'].to_numpy()
					Body_leg_armor = float(Body_leg_armor)
					if Body_leg_armor is None:
						Body_leg_armor = 0

					weight = df_body.loc[df_body.ID == value_id, 'Weight'].to_numpy()
					weight = float(weight)

					body.append([Body_body_armor, Body_arm_armor, Body_leg_armor, weight])
				# ARM ARMOR
				elif value_tag == 'Gloves':
					Arm_arm_armor = df_arm.loc[df_arm.ID == value_id, 'Arm Armor'].to_numpy()
					Arm_arm_armor = float(Arm_arm_armor)
					if Arm_arm_armor is None:
						Arm_arm_armor = 0

					weight = df_arm.loc[df_arm.ID == value_id, 'Weight'].to_numpy()
					weight = float(weight)

					arm.append([Arm_arm_armor, weight])
				# LEG ARMOR
				elif value_tag == 'Leg':
					Leg_leg_armor = df_leg.loc[df_leg.ID == value_id, 'Leg Armor'].to_numpy()
					Leg_leg_armor = float(Leg_leg_armor)
					if Leg_leg_armor is None:
						Leg_leg_armor = 0

					weight = df_leg.loc[df_leg.ID == value_id, 'Weight'].to_numpy()
					weight = float(weight)

					leg.append([Leg_leg_armor, weight])

				# IF TROOP IS MOUNTED, THEN CHECKS FOR HORSE AND HARNESS
				if troop_group == 'Cavalry' or troop_group == 'HorseArcher':
					# print("ON HORSEBACK")
					if value_tag == 'Horse':
						horse_breed = df_horse.loc[df_horse.ID == value_id, 'Name'].to_string()
						print(value_tag)
						horse_chrg_dmg = float(df_horse.loc[df_horse.ID == value_id, 'Charge Dmg'].to_numpy())
						horse_speed = float(df_horse.loc[df_horse.ID == value_id, 'Speed'].to_numpy())
						horse_maneuver = float(df_horse.loc[df_horse.ID == value_id, 'Maneuver'].to_numpy())
						horse_health = float(df_horse.loc[df_horse.ID == value_id, 'Health'].to_numpy())
					elif value_tag == "HorseHarness":
						harness_armor = float(df_harn.loc[df_harn.ID == value_id, 'Armor'].to_numpy())

		head_armor = body_armor = arm_armor = leg_armor = 0
		total_weight = 0

		# AVERAGE HEAD ARMOR STATS
		h = wt = 0
		for i in head:
			h += i[0]
			wt += i[1]
		try:
			head_armor += h / len(head)
			total_weight += wt / len(head)
		except ZeroDivisionError:
			pass

		# AVERAGE SHOULDER ARMOR STATS
		b = a = wt = 0
		for i in shld:
			b += i[0]
			a += i[1]
			wt += i[2]
		try:
			body_armor += b / len(shld)
			arm_armor += a / len(shld)
			total_weight += wt / len(shld)
		except ZeroDivisionError:
			pass

		# AVERAGE BODY ARMOR STATS
		b = a = l = wt = 0
		for i in body:
			b += i[0]
			a += i[1]
			l += i[2]
			wt += i[3]
		try:
			body_armor += b / len(body)
			arm_armor += a / len(body)
			leg_armor += l / len(body)
			total_weight += wt / len(body)
		except ZeroDivisionError:
			pass

		# AVERAGE ARM ARMOR STATS
		a = wt = 0
		for i in arm:
			a += i[0]
			wt += i[1]
		try:
			arm_armor += a / len(arm)
			total_weight += wt / len(arm)
		except ZeroDivisionError:
			pass

		# AVERAGE LEG ARMOR STATS
		l = wt = 0
		for i in leg:
			l += i[0]
			wt += i[1]
		try:
			leg_armor += l / len(leg)
			total_weight += wt / len(leg)
		except ZeroDivisionError:
			pass

		### FOR TESTING ###
		# print(name)
		# print(head)
		# print(shld)
		# print(body)
		# print(arm)
		# print(leg)
		# print(head_armor, body_armor, arm_armor, leg_armor, total_weight)
		# print()

		troop_2D_list.append([name, head_armor, body_armor, arm_armor, leg_armor, total_weight, horse_breed, horse_chrg_dmg, horse_speed, horse_maneuver, horse_health, harness_armor])
		header_list = ["Name", "Head AR", "Body AR", "Arm AR", "Leg AR", "AR Weight", "Horse Breed", "Charge Damage", "Speed", "Maneuver", "Health", "Harness Armor"]

	df = pd.DataFrame(troop_2D_list)

	# with ExcelWriter('MB2.xlsx', mode='a') as writer:
	# 	df.to_excel(writer, sheet_name='npcAvgArmor', index=False, header=header_list)
	# with ExcelWriter('mb2_for_web.json', mode='w') as writer:
	# 	df.to_json(writer)

	df.to_json("mb2_web.json", orient="records")

	# print(df.to_json("mb2.json"))




def get_npc_for_json(xml_file):
	# CREATES TREE AND ROOT
	tree = ET.parse(xml_file)
	root = tree.getroot()

	# INITIALIZES A 2D LIST TO STORE NPC'S AND THEIR STATS/EQUIPMENT; WILL BE USED TO PUT INTO A PANDAS DATAFRAME
	npc_2D_list = []
	game_skill_list = ('OneHanded', 'TwoHanded', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics')
    
    # FOR EACH NPC IN THE XML FILE
	for npc in root.findall('NPCCharacter'):
		id_npc = npc.get('id')
		culture = npc.get('culture').partition(".")[2]
		name = npc.get('name').partition("}")[2]
		troop_type = npc.get('default_group')
		occupation = npc.get('occupation')
		
		if culture == "neutral_culture":
			culture = "neutral"

		# CREATES THE AN ENTRY LIST; EACH ENTRY LIST REPRESENTS AN NPC
		entry = [name, troop_type, culture, occupation]
		# INITIALIZES DICT FOR SKILLS
		skill_dict = {}
		
		template = npc.get('skill_template')
		print(template)
		# IF THEIR IS NO TEMPLATE, GET SKILLS AS NORMAL
		if template is None or template == '':
			print("NONE NONE NONE")
			skills = npc.find('skills')
    
			print(name)
			for skill in skills.findall('skill'):
				skill_id = skill.get('id')
				skill_value = skill.get('value')
				print(skill_id, skill_value)
				skill_dict[skill_id] = skill_value

				# Check if there is a missing skill; sometimes happens if skill value is zero
				for mia_skill in game_skill_list:
					if mia_skill not in skill_dict.keys():
						skill_dict[mia_skill] = "0"
		# IF THERE IS A TEMPLATE, FIND IT IN SEPARATE XML TO OBTAIN SKILLS
		else:
			print("YES YES YES")
			template = template.split('.')[1]
			print(template)

			temp_tree = ET.parse('sandboxcore_skill_sets.xml')
			temp_root = temp_tree.getroot()
			
			for skillset in temp_root.findall('SkillSet'):
				skillset_id = skillset.get('id')
				if skillset_id == template:
					print("FOUND")
					for skill in skillset.findall('skill'):
						skill_id = skill.get('id')
						skill_value = skill.get('value')
						print(skill_value, skill_id)
						skill_dict[skill_id] = skill_value

						# Check if there is a missing skill; sometimes happens if skill value is zero
						for mia_skill in game_skill_list:
							if mia_skill not in skill_dict.keys():
								skill_dict[mia_skill] = "0"


		entry.append(skill_dict['OneHanded'])
		entry.append(skill_dict['TwoHanded'])
		entry.append(skill_dict['Polearm'])
		entry.append(skill_dict['Bow'])
		entry.append(skill_dict['Crossbow'])
		entry.append(skill_dict['Throwing'])
		entry.append(skill_dict['Riding'])
		entry.append(skill_dict['Athletics'])

		# FOR EACH EQUIPMENT
		# equipments = npc.find('Equipments')
		# for eq_roster in equipments.findall('EquipmentRoster'):
		# 	for eq in eq_roster:
		# 		slot = eq.get('slot')
		# 		id_eq = eq.get('id').partition(".")[2]
		# 		entry.append(slot + "_" + id_eq)

		npc_2D_list.append(entry)


	df = pd.DataFrame(npc_2D_list)

	# with ExcelWriter('MB2.xlsx', mode='a') as writer:
	# 	df.to_excel(writer, sheet_name='npcs', index=False)

	df.to_json("mb2_skills.json", orient="records")



if __name__ == '__main__':
	wb = Workbook()
	ws = wb.active
	ws.title = "Sheet Sample"
	wb.save(filename='MB2.xlsx')

	get_armor('head_armors.xml')
	get_armor('shoulder_armors.xml')
	get_armor('body_armors.xml')
	get_armor('arm_armors.xml')
	get_armor('leg_armors.xml')
	# get_horses('horses.xml')
	# get_harness('harnesses.xml')
	get_npc('npcs.xml')
	# convert_id_to_name('all_equipment.xml')
	# get_npc_armor_avg()
	# get_npc_for_json("npcs.xml")
