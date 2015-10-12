#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
enron_data.pop('TOTAL', 0)

max_stock_options_exercised = 0
min_stock_options_exercised = 2 ** 32

feature = "salary"

for person in enron_data:
	try:
		if int(enron_data[person][feature]) > max_stock_options_exercised:
			max_stock_options_exercised = int(enron_data[person][feature])
		if int(enron_data[person][feature]) < min_stock_options_exercised:
			min_stock_options_exercised = int(enron_data[person][feature])
	except Exception, e:
		# Skip all 'NaN' entries
		pass

print "MAX: " + str(max_stock_options_exercised)
print "MIN: " + str(min_stock_options_exercised)
