# 
# ---------------------------------------------------------------------------
# select_X.py
# Created by: Cobus Stals
# Created on: 2018-06-01 08:12:43.00000
#   
# Description: 
# This script is used to divide an input shapefile into equal defined amount 
# of polygons and output these polygons as new shp files. Note that in this 
# example the shp file is divided into sub groups (the variable amnt) of 
# 250 000 polygons. Also note that an identifier field (in this case the ID 
# field) is required with unique integer values ranging from 1 to X. Without 
# an ID field like this, the script will not work properly. Also note that 
# the last sub group of polygons will be the remainder and might be < amnt
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# The input file and location
inputFile = "E:/Cobus/NEW_DEVELOPMENTS/vectors/file_diff.shp"

#determine the amount of polys in the input shp file
count = arcpy.GetCount_management(inputFile)
val = int(count.getOutput(0))

# the max amount of polys that each sub section can contain
amnt = 250000

# determine amount of subsections for the input shp file
if val > 0 :
    tiles = (val / amnt) + 1
else:
    print "The shp file is empty"

# build a list for the subsections to select and process
tileLen = tiles + 1
tileList = range (1, tileLen)

# Run through the list of tiles and select and output each shp file subsection of the input
# Process: Select
for a in tileList:
	outName = inputFile[:-4] + "_" + str(a) + ".shp"
	low = (a - 1) * amnt
	high = a * amnt
	queryString = "\"ID\" > " + str(low) + " AND \"ID\" <= " + str(high)
	print queryString
	arcpy.Select_analysis(inputFile, outName, queryString)

