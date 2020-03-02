#!/usr/bin/python

# test lanternapi module

import argparse
import json
import lanternapi

# Example:
#  ./notifyTest.py -n 10.0.0.10 -e test1@lantern.com -p ******** -i 5 --message "i want to send an alert"


def main():

    parser = argparse.ArgumentParser(description='Test the lanternapi module using the notify request.')
    parser.add_argument('-n','--hostname', default='lantern.com',
                    help='Hostname|IP of data lantern server',
                    required=True)
    parser.add_argument('-i','--deviceId', help='Device ID',required=True)
    parser.add_argument('-e', '--email', help='email for login')
    parser.add_argument('-p', '--password', help='password for login')
    parser.add_argument('-m', '--message', help='message or alert to send',
                        required=True)
    args = parser.parse_args()

    la = lanternapi.lanternapi()
    la.setHostname(args.hostname)

    code, body = la.login(args.email, args.password)
    print('\nlogin status: %d' % code)
    print('response body: %r' % body)

    code, body = la.notify(args.deviceId, args.message)
    print('\nnotify status:  %d' % code)
    print json.dumps(json.loads(body), sort_keys=True, indent=4, separators=(',', ': '))

    #print('response body: %r' % body)

    code, body = la.logout()
    print('\nlogout status: %d' % code)
    print('response body: %r' % body)

if __name__ == "__main__":
	main()
