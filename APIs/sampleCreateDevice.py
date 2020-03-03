#!/usr/bin/python
#
# Data Lantern Inc confidential
# ______________________________
#
#  [2014] - [2018] Data Lantern Inc
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
# Sample python code for getting data from the Data Lantern server.
#

import argparse
import json
import lanternapi
import datetime
import time

# Example:
# ./sampleCreateDevice.py  -n 10.0.0.10 -u username -p password -n NewCar -t 3


def main():

    parser = argparse.ArgumentParser(description='Create, update, and delete a device.')
    parser.add_argument('-i','--hostname', help='Hostname|IP of data lantern server',
                    required=True)
    parser.add_argument('-e', '--email', help='email for login', required=True)
    parser.add_argument('-p', '--password', help='password for login', required=True)
    parser.add_argument('-n','--name', help='Name of device', required=True)
    parser.add_argument('-t','--type', help='Device type ID', required=True)
    parser.add_argument('-d', '--description',
                        help='Description of your device',
                        required=False, default=None)
    parser.add_argument('-m', '--manufacturer_name',
                        help='Manufacturer of the device', required=False,
                        default=None)
    parser.add_argument('-o', '--model',
                        help='Model number',
                        required=False, default=None)
    parser.add_argument('-s','--serial_number', help='Serial number',
                        required=False, default=None)
    parser.add_argument('-v','--version', help='Device version number',
                        required=False, default=None)
    parser.add_argument('-b','--barcode', help='Barcode',
                        required=False, default=None)
    parser.add_argument('-c','--config', help='Other config values related to the device in JSON format',
                        required=False, default='')
    parser.add_argument('-f','--custom_fields',
                        help='Other custom fields for device in JSON format',
                        required=False, default='')
    args = parser.parse_args()

    # create initial control data and store in variable
    control = { 'standard' : { } }

    # set up lanternapi object
    la = lanternapi.lanternapi()
    la.setHostname(args.hostname)

    code, body = la.login(args.email, args.password)
    print('\nlogin status: %d' % code)
    print('response body: %r' % body)

    code, body = la.createDevice(args.name, args.type, args.description,
                                args.manufacturer_name, args.model,
                                args.serial_number, args.version, args.barcode,
                                args.config, args.custom_fields)
    print('\ncreate device status: %d' % code)
    print('response body: %r' % body)

    # get device id from response body
    bodyJson = json.loads(body)
    deviceId = bodyJson['data']['id']

    code, body = la.updateDevice(deviceId,
                                args.name, args.type, 'not a new Bolt anymore',
                                args.manufacturer_name, args.model,
                                args.serial_number, args.version, args.barcode,
                                args.config, args.custom_fields)
    print('\nupdate device status: %d' % code)
    print('response body: %r' % body)

    code, body = la.deleteDevice(deviceId)
    print('\ndelete device status: %d' % code)
    print('response body: %r' % body)

    code, body = la.logout()
    print('\nlogout status: %d' % code)
    print('response body: %r' % body)
    print('\n')
if __name__ == "__main__":
	main()
