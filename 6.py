import re
for test_string in ['555-1212', 'ILL-EGAL', '1234-555-1212']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    elif re.match(r'^\d{4}-\d{3}', test_string):
        print "happy"
    else:
        print test_string, 'rejected'