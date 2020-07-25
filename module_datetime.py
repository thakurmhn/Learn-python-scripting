#!/usr/bin/env python3.7

import datetime

print(dir(datetime))
print(dir(datetime.datetime))

print(datetime.datetime.now())
print(datetime.datetime.today())

## print date from differrent timezones

import pytz

utc=pytz.timezone('utc')

print(datetime.datetime.now(utc))


print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().second)

## Format time

## https://strftime.org/

print(datetime.datetime.now().strftime("%c"))
print(datetime.datetime.now().strftime("%d-%m-%Y"))
