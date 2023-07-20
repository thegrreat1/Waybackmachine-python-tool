#!/usr/bin/python
#Simple script to scrape urls from waybackmachine

#Importing required modules
import requests
import colorama
import sys

# Define colors for better looking code...
red = colorama.Fore.RED
white = colorama.Fore.WHITE

print(red, '\n'
          '-----------------------------------------------------------\n'
          '_ _ _               __    __         ____ ||            3AT \n'
          '\\/\/aybac[]/machin[|-  s[|-arching   L|ooL_]             S3ARCH\n'
          '            `       `-    `-                               R3PEAT \n'
           '-----------------------------------------------------------\n'
          '    ')

if len(sys.argv) > 1:
    wayback_api = "https://web.archive.org/cdx/search/cdx?url="
    if len(sys.argv) > 3:
        wayback_date = "&from=" + str(sys.argv[2]) + "&to=" + str(sys.argv[3]) + "&gzip=false"
    else:
        print(red, 'Error:', white, 'Missing DATE-FROM DATE-TO')
        print(red, 'Example:', white, './wayback.py www.google.com 2020 2023')
        sys.exit(1)

    print(red, "NOTICE:", white, "This might take a while.. Go grab a coffee!!")
    website_url = str(sys.argv[1])
    full_url = wayback_api + website_url + '/*' + wayback_date

    wayback = requests.request('get', full_url)
    print(wayback.text)
else:
    print(red, 'Error:', white, 'Invalid usage....')
    print(red, 'Error:', white, 'To search google.com from 2020 to 2023 use following example')
    print(red, 'Example usage:', white, './wayback.py www.google.com 2020 2023')
