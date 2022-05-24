import socket
import sys
sys.path.append("/Users/anon.ong/Documents/02_CP_3_year/INDIV/indiv-android-testing/")
sys.path.append("/Users/anon.ong/Documents/02_CP_3_year/INDIV/indiv-android-testing/lib/")

from config import result

from mitmproxy import io, http
from mitmproxy.exceptions import FlowReadException
import time
from vulpix import checkPrivacyLeakage, PII_TYPE_2
#from flask import request

class Dump_Controller():
    def __init__(self, path) -> None:
        self.path = path

        self.result_path = result[:-4]+"_"
        self.number_result = 0
        self.result_file = open(self.result_path+str(self.number_result)+".csv", "w")
        self.result_file.write(",Email,Video,Audio,Photo,LocationGPS,IP,AdId,TimeZone,Country,MACAddr\n")

        self.pos = 0     
        self.count = 0

    def open_dump_file(self):
        time.sleep(0.5)
        with open(self.path, "rb") as logfile:
            freader = io.FlowReader(logfile)
            output = {}
            try:
                i = 0
                temp = []

                for f in freader.stream():
                    if i>=self.pos and isinstance(f, http.HTTPFlow):
                        output = output | checkPrivacyLeakage(f)
                    i += 1
                    
                for pi_type in PII_TYPE_2:
                    temp.append("1" if pi_type in output else "0")

                temp = str(self.count)+","+",".join(temp)+"\n"
                self.count += 1

                self.result_file.write(temp)
                self.pos = i
            except FlowReadException as e:
                print(f"Flow file corrupted: {e}")
        return output, len(output)

    def new_record(self):
        self.result_file.close()
        self.number_result += 1
        self.result_file = open(self.result_path+str(self.number_result)+".csv", "w")
        self.result_file.write(",Email,Video,Audio,Photo,LocationGPS,IP,AdId,TimeZone,Country,MACAddr\n")
        self.count = 0


