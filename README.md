For this problem, I first read the data and store to 2 dictionaries:

   - occ_dict: key is the OCCUPATIONS, a combination of Standard Occupational Classification (SOC)_NAME and SOC_CODE, and value is a list consisting of [number of CERTIFIED application, number of total application].
	
   - state_dict: key is the STATE code (WORKSITE_STATE), and value is number of CERTIFIED applications.

Dictionary is the optimal data structure choice for this task since the dictionary uses hash-table so accessing to a dictionary item is fast and scalable, at order of O(1).

I create a list for top OCCUPATIONS with each element is a list of [OCCUPATIONS, number of CERTIFIED applications, percentage of number of CERTIFIED applications wrt total number of CERTIFIED applications]. A smimilar list for top STATE with each element is a list of [STATE, number of CERTIFIED applications]. These 2 lists are then will be sorted (by Python sorted() function) and select only n_top=10 first elements to write out to output files.
