import re
file = open("controltower_access.log", "r")

# regex to catch ip addresses of strings in a apache log file
ip_regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# regex to catch the dates and time of a line in apache log file
date_regex = re.compile(r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})]')


ip_array=[]
date_array=[]

for line in file:
    if not re.match(ip_regex, line).group(1) in ip_array:
        ip_array.append(re.match(ip_regex, line).group(1))
    if not re.match(date_regex, line).group(4) in date_array:
        date_array.append((re.match(date_regex, line).group(4), 1))

print(date_array=)



### DEBUG ###

#debug_line = '20.203.142.208 - - [09/Nov/2021:12:05:51 +0100] "GET /en/index.php?controller=\"><script%20>alert(String.fromCharCode(88,83,83))</script> HTTP/1.1" 301 4932 "https://controltower.fr/en/index.php?controller=\"><script >alert(String.fromCharCode(88,83,83))</script>" "Mozilla/5.0 (Windows NT 10.0; WOW64; Rv:50.0) Gecko/20100101 Firefox/50.0"'
# debug_line1 = '66.249.66.75 - - [09/Nov/2021:00:00:06 +0100] "GET /fr/sak-dub-i/1537-sak-dub-i-raw-dubz.html HTTP/1.1" 200 15217 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'
# debug_line2 = '[09/Nov/2021:12:05:51 +0100]'

# debug_date_regex = re.compile(r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-])\]')
# debug_date_regex1 = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\]'
# regex = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}|-) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?$'

# print(re.match(regex, debug_line1).group(11))