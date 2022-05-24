import os,sys
from time import sleep
from lib import dump_controller
from config import path_reader, package
sys.path.append("/Users/anon.ong/Documents/02_CP_3_year/INDIV/indiv-android-testing/lib/")

print("Attemp to connect with mitm_writer")

connector = dump_controller.Dump_Controller(path_reader)

number = 5
number = str(number)
cmd = "adb shell monkey -p %s %s" % (package, number)

print("We are running this command : ", cmd)

for i in range(50):
    os.system(cmd)
    output, len_output = connector.open_dump_file()
    print(output)

#df = pd.DataFrame(pi_leakage_output)
#df.to_csv("./result/"+package+"_monkey.csv")
