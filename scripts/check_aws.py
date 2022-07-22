#output all running AWS machines.
import json, sys, subprocess

# requires AWS CLI
all_region = subprocess.check_output("aws ec2 describe-regions --region us-east-1 --output text | cut -f4", shell=True).decode().strip()

for reg in all_region.split("\n"):
	res = subprocess.check_output("aws ec2 describe-instances --region "+reg, shell=True)
	obj = json.loads(res)
	if(len(obj['Reservations']) != 0):
		for i in obj['Reservations']:
			for j in i['Instances']:
				if j['State']['Name'] == 'running':
					print(reg, j['KeyName'], j['InstanceType'],j['State']['Name'])
