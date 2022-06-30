# golfcoursedata = {'hole 1':[],'hole 2':[],'hole 3':[],'hole 4':[],'hole 5':[],'hole 6':[],'hole 7':[],'hole 8':[],'hole 9':[],'hole 10':[],'hole 11':[],'hole 12':[],'hole 13':[],'hole 14':[],'hole 15':[],'hole 16':[],'hole 17':[],'hole 18':[]}
# fakescorelist = [5,5,4,5,8,6,4,3,7,5,6,7,5,8,5,5,3,6]

# #have user manually enter a hole-by-hole score for a golf round
# #for hole in golfcoursedata.keys():
# 	#score = input('Enter you score for ' + hole + ':')
# 	#realscorelist.append(score)

# #storing scores into a json file by player
# score_posting = {}
# dailyscorelist = []
# name = input('Please enter your first name:')
# import datetime
# date = datetime.datetime.now()
# datestr = date.strftime('%c')
# #for hole in list(golfcoursedata.keys()): #<----------START HERE
# 	#funky_num = 0
# 	#active = True
# 	#while active == True:
# 		#if funky_num == 0:
# 			#score = int(input("Enter your score for " + hole + ":"))
# 		#passvar = input("Is this score correct for " + hole + " (enter yes/no)? " + str(score) + ':')
# 		#if passvar.upper() == 'YES':
# 			#dailyscorelist.append(score)
# 			#active = False
# 			#continue
# 		#if passvar.upper() == 'NO':
# 			#pass
# 		#else:
# 			#print('Please enter yes or no')
# 			#funky_num = 1
# score_posting[datestr] = fakescorelist

# import json

# if name.upper() == 'WILL':
# 	filename = 'willtestgolfdata.csv'
# if name.upper() == 'CLAY':
# 	filename = 'claygolfdata.csv'
# if name.upper() == 'JEFF':
# 	filename = 'jeffgolfdata.csv'

# #append a new line of scores with a timestamp to the json file
# from csv import writer
# with open(filename, 'a') as file_object:
# 	file_object.write(str(score_posting))
# 	#json.dump(score_posting,file_object, indent = 1)

# 	#json_file = json.load(file_object)
# 	#lines = json_file.readlines()
# 	#for line in lines:
# 		#for value in line.values():
# 			#line_list = value

# #takes the list of daily scores and appends them to each hole of the golf course hole dictionary
# #for hole in list(golfcoursedata.keys()): 
# 	#elementnumber = list(golfcoursedata.keys()).index(hole)
# 	#golfcoursedata[hole].append(line_list[elementnumber])

# #print(golfcoursedata)
index_list = list(range(0,9))
print(index_list)











				


