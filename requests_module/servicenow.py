#!/usr/bin/env python3


import requests 

snow_user='username'
snow_pw='password'
snow_headers={"Content-Type":"application/json", "Accept":"application/json"}


# Notification contact api
url='example.servicenow.com/api/now/table/cmdb_ci_linux_server?sysparam_fields=u_notification_contacts&sysparam_query=name='
