#!/bin/python
import os,sys
import uuid
import shutil


release_date="2020-10-20"
fm_number=3478
pid="C2"
build_path=os.getcwd()+"/.build_temp"
binary_path=os.getcwd()
mfw_version=3273255
updatetype=1
config_id2=0
config_version=9
xml_filename="prometheus.metainfo.xml"
cab_filename="test.cab" #will override later

### update type
updatetype=input("Enter update type: 1:MFW; 2:IOTA "+"<"+str(updatetype)+">") or str(updatetype)
if updatetype.isdigit():
    updatetype=int(updatetype)
print("type is "+str(updatetype))
if not (updatetype == 1 or updatetype ==2):
    print("invalid input")
    sys.exit()


if updatetype==1:
    mfw_filename="prometheus-10.01."+str(mfw_version)+"_prod.pkg"
    print("mfw name= "+mfw_filename)
elif updatetype==2:
    ### FM number
    fm_number=input("Enter FM number: "+"<"+str(fm_number)+">") or str(fm_number)
    if fm_number.isdigit():
        fm_number=int(fm_number)
    else:
        print("input error")
        sys.exit()

    fm_valid=0
    if fm_number < 10000 and fm_number > 999:
        print("valid")
        fm_valid=1
            
    if fm_valid ==1:
        print("FM number is "+str(fm_number))
    else:
        print("invalid FM number")
        sys.exit()
#prometheus-FM-03478-000_IOTA-Rev0009_prod.pkg
    config_id2=input("Enter config ID2: "+"<"+str(config_id2)+">") or str(config_id2)
    if config_id2.isdigit():
        config_id2=int(config_id2)
    else:
        print("input error")
        sys.exit()
    config_version=input("Enter config version: "+"<"+str(config_version)+">") or str(config_version)
    if config_version.isdigit():
        config_version=int(config_version)
    else:
        print("input error")
        sys.exit()
    mfw_filename="prometheus-FM-%05d-%03d_IOTA-Rev%04d_prod.pkg"%(fm_number,config_id2,config_version)
mfw_file_fullpath=binary_path+"/"+mfw_filename
if not os.path.exists(mfw_file_fullpath):
    print("Cannot find "+mfw_file_fullpath)
    sys.exit()
else:
    print("Successfuly find "+mfw_file_fullpath)
###





##pid
pid=input("Enter PID: "+"<"+pid+">") or pid

if not len(pid)==2:
    pid_valid=0
else:
    pid_valid=1
    try:
        hexval = int(pid, 16)
    except:
        pid_valid=0

if pid_valid ==1 :
        pid=pid.upper()
        print("PID is "+pid)
else:
    print("invalid pid")
    sys.exit()
    
 
if os.path.exists(build_path):
    print("path already exist, delete the folder")
    shutil.rmtree(build_path, ignore_errors=True)
    sys.exit()
else:
    print("ok")
    os.mkdir(build_path)
guid_string=""
if updatetype==1:
    guid_string="USB\\VID_06CB&PID_00"+pid
elif updatetype==2:
    guid_string="USB\\VID_06CB&PID_00"+pid+"&CFG1_%d&CFG2_%d"%(fm_number,config_id2)
    
if not guid_string=="":
    guid_result=str(uuid.uuid5(uuid.NAMESPACE_DNS, guid_string))
    guid_prefix=guid_result.split('-')[0]
    print("guid src= "+guid_string)
    print("guid= "+guid_result)
    print("guid prefix= "+guid_prefix)
    if updatetype == 1:
        id_prefix="0x"+pid
        print("id prefix= "+id_prefix)
    elif updatetype == 2:
        id_prefix="0x"+pid+"_%d_%d"%(fm_number,config_id2)
        print("id prefix= "+id_prefix)

if updatetype==1:    
    cab_filename="Synaptics-Prometheus-10.01."+str(mfw_version)+"-0x"+pid+".cab"
elif updatetype==2:
    cab_filename="Synaptics-Prometheus_config-%04d-%05d-%03d-0x%s.cab"%(config_version,fm_number,config_id2,pid)
print("cab name is "+cab_filename)



str_xml=[
"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<!-- Copyright 2019 Richard Hughes <richard@hughsie.com> -->\n"
"<component type=\"firmware\">\n"
"  <id>com.synaptics.prometheus."+id_prefix+".firmware</id>\n"
"  <name>Prometheus Fingerprint Reader</name>\n"
"  <summary>Firmware for the Synaptics Prometheus Fingerprint Reader device</summary>\n"
"  <description>\n"
"    <p>\n"
"      Updating the firmware on your fingerprint reader improves performance and adds\n"
"      new features.\n"
"    </p>\n"
"  </description>\n"
"  <provides>\n"
"    <!-- "+guid_string+" -->\n"
"    <firmware type=\"flashed\">"+guid_result+"</firmware>\n"
"  </provides>\n"
"  <requires>\n"
"    <id compare=\"ge\" version=\"1.3.6\">org.freedesktop.fwupd</id>\n"
"  </requires>\n"
"  <url type=\"homepage\">https://www.synaptics.com/products/biometrics</url>\n"
"  <metadata_license>CC0-1.0</metadata_license>\n"
"  <project_license>Proprietary</project_license>\n"
"  <developer_name>Synaptics Inc.</developer_name>\n"
"  <releases>\n"
"    <release urgency=\"medium\" version=\"10.01."+str(mfw_version)+"\" date=\""+release_date+"\">\n"
"      <checksum filename=\""+mfw_filename+"\" target=\"content\"/>\n"
"      <description>\n"
"        <p>\n"
"          New features and enhancements:\n"
"        </p>\n"
"        <ul>\n"
"          <li>Support Linux system</li>   \n"
"        </ul>\n"
"      </description>\n"
"    </release>\n"
"  </releases>\n"
"  <categories>\n"
"    <category>X-Device</category>\n"
"  </categories>\n"
"  <custom>\n"
"    <value key=\"LVFS::UpdateProtocol\">com.synaptics.prometheus</value>\n"
"    <value key=\"LVFS::VersionFormat\">triplet</value>\n"
"  </custom>\n"
"</component>\n"
]


str_xml_config=[
"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<!-- Copyright 2019 Richard Hughes <richard@hughsie.com> -->\n"
"<component type=\"firmware\">\n"
"  <id>com.synaptics.prometheus."+id_prefix+".config</id>\n"
"  <name>Prometheus Fingerprint Reader Configuration</name>\n"
"  <summary>Configuration for the Synaptics Prometheus Fingerprint Reader device</summary>\n"
"  <description>\n"
"    <p>\n"
"      Updating the firmware on your fingerprint reader improves performance and adds\n"
"      new features.\n"
"    </p>\n"
"  </description>\n"
"  <provides>\n"
"    <!-- "+guid_string+" -->\n"
"    <firmware type=\"flashed\">"+guid_result+"</firmware>\n"
"  </provides>\n"
"  <requires>\n"
"    <id compare=\"ge\" version=\"1.4.6\">org.freedesktop.fwupd</id>\n"
"  </requires>\n"
"  <url type=\"homepage\">https://www.synaptics.com/products/biometrics</url>\n"
"  <metadata_license>CC0-1.0</metadata_license>\n"
"  <project_license>Proprietary</project_license>\n"
"  <developer_name>Synaptics Inc.</developer_name>\n"
"  <releases>\n"
"	  <release urgency=\"medium\" version=\""+"%04d"%(config_version)+"\" date=\""+release_date+"\">\n"
"      <checksum filename=\""+mfw_filename+"\" target=\"content\"/>\n"
"      <description>\n"
"        <p>\n"
"          New features and enhancements:\n"
"        </p>\n"
"        <ul>\n"
"          <li>Support Linux system</li>  \n"
"        </ul>\n"
"      </description>\n"
"    </release>\n"
"  </releases>\n"
"  <categories>\n"
"    <category>X-Device</category>\n"
"  </categories>\n"
"  <custom>\n"
"    <value key=\"LVFS::UpdateProtocol\">com.synaptics.prometheus.config</value>\n"
"    <value key=\"LVFS::VersionFormat\">plain</value>\n"
"  </custom>\n"
"</component>\n"
]

#if updatetype==1:
 #   for line in str_xml:
  #      print(line)
#elif updatetype==2:
 #   for line in str_xml_config:
  #      print(line)
    

file_xml=open(build_path+"/"+xml_filename,"w")
if updatetype == 1:
    for line in str_xml:
        file_xml.write(line)
elif updatetype == 2:
    for line in str_xml_config:
        file_xml.write(line)
file_xml.close()

os.system("gcab --create --nopath "+" "+cab_filename+" "+mfw_file_fullpath+" "+build_path+"/"+xml_filename)

shutil.rmtree(build_path, ignore_errors=True)




