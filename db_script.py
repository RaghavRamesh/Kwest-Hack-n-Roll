'''
Python script for inserting Product objects from Inventory files
'''
import database
import codecs, time, datetime
file_object=codecs.open("data.txt", 'r', 'utf-8')
for line in file_object:
	line_split=line.split(',')
	name=line_split[0]
	xp=line_split[1]
	money=line_split[2]
	level=line_split[3]
	password=line_split[4].strip()
	email=line_split[5]
	new_transaction_detail=database.Users(email=email)
	database.db.session.add(new_transaction_detail)
	database.db.session.commit()