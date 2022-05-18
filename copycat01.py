#!/usr/bin/env python3
import shutil
import os

os.chdir("/home/student/mycode/")
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")

os.system("rm -rf /home/student/mycode/5g_research_backup/")
if __name__ == "__main__":
    main()

