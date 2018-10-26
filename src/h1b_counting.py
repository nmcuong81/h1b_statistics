# Python library for readin csv file
from csv import reader
# system module
import sys

occ_dict = {}
state_dict = {}
n_certified = 0
n_top = 10
with open(sys.argv[1]) as csvfin:
    fin = reader(csvfin, delimiter=';')
    iline=0
    for fields in fin:
        if iline == 0:
            # Getting the fields' indexes. This is important since data from different year may have different format and/or columns
            soc_name_ind = fields.index('SOC_NAME')
            soc_code_ind = fields.index('SOC_CODE')
            state_ind = fields.index('WORKSITE_STATE')
            status_ind = fields.index('CASE_STATUS')
            n_fields = len(fields)
        else:
            if len(fields) == n_fields: # ignore line with missing data
                # Occupation dictionary
                if fields[status_ind].strip().upper() == 'CERTIFIED':
                    occ_name = fields[soc_name_ind].strip().upper()+'__'+fields[soc_code_ind].strip().upper()
                    if occ_name not in occ_dict:
                        occ_dict[occ_name] = 1
                    else:
                        occ_dict[occ_name] += 1
                #if fields[status_ind].strip().upper() == 'CERTIFIED':
                    # State dictionary
                    state = fields[state_ind].strip().upper()
                    if state not in state_dict:
                        state_dict[state] = 1
                    else:
                        state_dict[state] += 1
                    n_certified += 1

        iline += 1

top_occ = []
for occ_name in occ_dict:
    name = occ_name.split('__')[0]
    top_occ.append((name, occ_dict[occ_name]))
top_occ = sorted(top_occ, key=lambda x: (-x[1], x[0]), reverse=False)[0:n_top] # limit to only n_top row

top_state = list(state_dict.items())
top_state = sorted(top_state, key=lambda x: (-x[1], x[0]), reverse=False)[0:n_top] # limit to only n_top row

# Writing output top occupations
with open(sys.argv[2],'w') as fout:
    fout.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for i in range(len(top_occ)):
        fout.write(top_occ[i][0]+';'+str(top_occ[i][1])+';'+str(round(top_occ[i][1]*100/n_certified,1))+'%\n')

# Writing output top states
with open(sys.argv[3],'w') as fout:
    fout.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for i in range(len(top_state)):
        fout.write(top_state[i][0]+';'+str(top_state[i][1])+';'+str(round(top_state[i][1]*100/n_certified,1))+'%\n')
