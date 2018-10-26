For this problem, I first read the data and store to 2 dictionaries:

   - occ_dict: key is the OCCUPATIONS, a combination of Standard Occupational Classification (SOC)_NAME and SOC_CODE, and value is the number of CERTIFIED for that OCCUPATIONS.
	
   - state_dict: key is the STATE code (WORKSITE_STATE), and value is number of CERTIFIED applications for that STATE.

Dictionary is the optimal data structure choice for this task since the dictionary uses hash-table so accessing to a dictionary item is fast and scalable, at order of O(1). Together with those 2 dictionary, there is another variable n_certified to hold total number of certified applications.

Next, I create a list for top OCCUPATIONS with each element is a list of [OCCUPATIONS, number of CERTIFIED applications for that OCCUPATIONS]. A smimilar list for top STATES with each element is a list of [STATE, number of CERTIFIED applications for that STATE]. These 2 lists then will be sorted by 2 fields (NUMBER_CERTIFIED_APPLICATIONS and then TOP_OCCUPATIONS, NUMBER_CERTIFIED_APPLICATIONS and then TOP_STATES, respectively for top OCCUPATIONS and top STATES) (by Python sorted() function) and select only n_top=10 first elements to write out to output files.
