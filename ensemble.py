import os
os.system('cd /home/aistudio/data/resultfinal/ && python ensemble.py')
os.system('cd /home/aistudio/data/resultfinal/result && zip -r -oq /home/aistudio/result.zip ./')
print('finish the job')