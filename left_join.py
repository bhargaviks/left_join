import csv

emp_dict ={}
sal_dict={}
headers=''
def store_dict(filename,i):
	dict_var={}
	fp=open(filename,'rb')
	with fp as lines:
		reader=csv.reader(lines)
		global headers
		headers=headers + str(next(reader)[i:])
        	for row in reader:
			ssplit=str(row).split(",")
                	key=ssplit.pop(0)
                	dict_var[key]=ssplit
	return dict_var

def clean_output(string_input):
	char_set={'\'\'':'NULL','(':'',')':'','"':'','[':'',']':'',':':',',' ':'','\'':''}
	for k in char_set.keys():
                string_input=str(string_input).replace(k,char_set[k])
        print string_input

def print_lines():
	print "------------------------------------------------------------------"

emp_dict=store_dict('employee_names.csv',0)
headers=headers + ','
sal_dict=store_dict('employee_pay.csv',1)
count=0
for key in emp_dict.keys():
        if key in sal_dict.keys():
            emp_dict[key]=emp_dict[key] + sal_dict[key]
	count=count+1

print_lines()
clean_output(headers)
print_lines()
for key, value in emp_dict.items():
	strings=key,emp_dict[key]
	clean_output(strings)
print_lines()
print count," number of rows"
print_lines()
