# Regular expressions lets you define a string patter and then search
# a string to find the patter you defined.
# They are used to validate strings, e.g, email address or social security number
# or they are used to pick out the parts of the strings you are interested in from a larger string.

# References --
# https://www.rexegg.com/regex-quickstart.html
# https://www.w3schools.com/python/python_regex.asp
# https://medium.com/factory-mind/regex-cookbook-most-wanted-regex-aa721558c3c1
# https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
# https://regex101.com/

# Example 1 -- Check if SSN number is valid


import re

def is_ssn_valid(ssn):
    pattern = '^\d{3}-\d{2}-\d{4}$'
    if re.findall(pattern, ssn):
        return True
    else:
        return False

ssn_list = ['111-22-3333', '1111-22-3333', 'abc-ef-ghij', 'abc']

# for ssn in ssn_list:
#     print(ssn, is_ssn_valid(ssn))


def split_ssn(ssn):
    pattern = '^(?P<part1>\d{3})-(?P<part2>\d{2})-(?P<part3>\d{4})$'
    match = re.search(pattern, ssn)
    if match:
        return match.groupdict()
    else:
        return False


for ssn in ssn_list:
    print(ssn, split_ssn(ssn))




def is_ipaddress_valid(ipaddress):
    # https://www.regular-expressions.info/ip.html
    pattern = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.findall(pattern, ipaddress):
        return True
    else:
        return False


ipaddress_list = ['127.0.0.1', '192.128.34.456', '129.34.ab.344']

for ip in ipaddress_list:
    print(ip, is_ipaddress_valid(ip))




# ## https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs




