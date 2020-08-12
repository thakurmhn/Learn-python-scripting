#!/usr/bin/env python3.7

'''
two applications with different properties/attributes
display tomcat7 and tomcat9 attribute
'''

import os

'''
def get_tomcat_config(conffile):
    global tc_conf,tc_home
    tc_conf=conffile
    tc_home=os.path.dirname(os.path.dirname(conffile))

def display_tomcat_details():
    print(f"Tomcat config file is: {tc_conf}")
    print(f"Tomcat Home is: {tc_home}")

def main():
    tomcat7_cf='/home/mohan/tomcat7/conf/server.xml'
    tomcat9_cf='/home/mohan/tomcat9/conf/server.xml'
    get_tomcat_config(tomcat7_cf)
    get_tomcat_config(tomcat9_cf)
    display_tomcat_details()
    return None


if __name__=="__main__":
    main()
'''

# Inside of class
class Tomcat:

    def get_tomcat_config(self,conffile):		# Always pass 'self' to the classs function 
        self.tc_conf=conffile
        self.tc_home=os.path.dirname(os.path.dirname(conffile))
        return None

    def display_tomcat_details(self):
        print(f"Tomcat config file is: {self.tc_conf}")
        print(f"Tomcat Home is: {self.tc_home}")
        return None

# Outside of class

def main():
    tomcat7=Tomcat()
    tomcat9=Tomcat()
      
    tomcat7.get_tomcat_config("/home/mohan/tomcat7/conf/server.xml")
    tomcat9.get_tomcat_config("/home/mohan/tomcat9/conf/server.xml") 

    #print(tomcat9.tc_conf)	# Outside calss call object and do not call self 
    #print(tomcat9.tc_home)
    #print(tomcat7.tc_conf)
    #print(tomcat7.tc_home)

    tomcat7.display_tomcat_details()
    tomcat9.display_tomcat_details()

if __name__=="__main__":
        main()
