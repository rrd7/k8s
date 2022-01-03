import os
import subprocess

containers = os.popen("kubectl get pods -n falco -l app=falco | grep falco | cut -d ' ' -f 1").read().strip()
containers_list = containers.split("\n")
print(containers_list)


for items in containers_list:
    cmd = 'kubectl cp /home/vagrant/temp/abc.txt falco/'+items+':/abc.txt'
    output = os.popen(cmd).read().strip()
    print(output)