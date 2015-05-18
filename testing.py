"""
This program is to print the number of files in a directory with files having a spcecific keywords
which is matched under each directory recursively starting from Root directory
Author: diwakar Sharma
date: 04/22/2015
""" 

import re #imported for regular expression matching
import os # for all the OS directory listings
from os.path import expanduser #for getting the root user
import matplotlib.pyplot as plt 
root = expanduser("~") #keyword to get the root dir
regex = '^[a-z][a-z]+_TESTResult.*' #any regular expression to be searched in filename
my_list = {}
for dirpath, dirs, files in os.walk(root):
	count = 0
	for f in files:
                m = re.match(regex, f)
                #if the match is found, count is increased by one
                if m:
                	count = count + 1
        		#updating the dictionary with KEY VALUE pairs
        		my_list.update({dirpath: count})
print "Printing directories with files in it"
print my_list

#Plotting the values from Dictionary onto Graph

plt.bar(range(len(my_list)), my_list.values(), align = 'center')
plt.xticks(range(len(my_list)), my_list.keys())

plt.show()
