#!/usr/bin/python
#
# Data Lantern Inc confidential
# ______________________________
#
#  [2014] - [2020] Data Lantern Inc
#  All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Data Lantern Inc and its suppliers, if any.
# The intellectual and technical concepts contained herein
# are proprietary to Data Lantern Inc and its suppliers and
# may be covered by U.S. and Foreign Patents, patents in
# process, and are protected by trade secret or copyright
# law. Dissemination of this inforamtion or reproduction of
# this material is strictly forbidden unless prior written
# permission is obtained from Data Lantern Inc.
#
# Sample python code for getting a user profile from the
# Data Lantern server after the user login.
#

import argparse
import json
import lanternapi
import datetime
import time

# Example:
# ./sampleGetProfile.py  -n 10.0.0.10 -e login_email -p password


def main():

    parser = argparse.ArgumentParser(description='Register a new user.')
    parser.add_argument('-n','--hostname', help='Hostname|IP of data lantern server',
                    required=True)
    parser.add_argument('-e', '--email', help='Email for the account', required=True)
    parser.add_argument('-p', '--password',
                        help='password for the account',
                        required=True)
    args = parser.parse_args()

    # set up lanternapi object
    la = lanternapi.lanternapi()
    la.setHostname(args.hostname)

    code, body = la.login(args.email, args.password)
    print('login status: %d' % code)
    print('response body: %r' % body)
    print('\n')

    # get user's profile
    code, body = la.getProfile()
    print('getProfile status: %d' % code)
    print('getProfile response body: %r' % body)
    print('\n')

    code, body = la.logout()
    print('logout status: %d' % code)
    print('response body: %r' % body)
    print('\n')
if __name__ == "__main__":
	main()
