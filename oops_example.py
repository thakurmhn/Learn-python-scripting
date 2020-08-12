#!/usr/bin/env python3.7

# Finds tomcat installations and display tomcat home and tomcat conf
# create /home/user/tomcat[79]/conf/server.xml

import os

class Tomcat():
    def get_tomcat_config(self,tconfig):
        self.tc_config=tconfig
        self.tc_home=os.path.dirname(os.path.dirname(tconfig))
        return None

    def display_details(self):
        print(f"Tomcat Config is: {self.tc_config}\nTomcat Home is: {self.tc_home}")
        return None
        
def get_all_tomcat():
    all_tomcat_config=[]
    for r,d,f in os.walk('/'):
        for each_file in f: 
            if each_file=='server.xml':
                all_tomcat_config.append(os.path.join(r,each_file))
    return all_tomcat_config

def main():
    list_tomcat_config=get_all_tomcat()
    #print(list_tomcat_config)
    list_objects=[]
    for each_item in list_tomcat_config: 
        tc_object=Tomcat()
        tc_object.get_tomcat_config(each_item)
        list_objects.append(tc_object)
        #print(list_objects)
    
    for each_obj in list_objects:
        each_obj.display_details()
    

if __name__=="__main__":
	main()
