# AWS

codes used for AWS services


######################

VPN Access Restriction:
JSON used in the aws console to write a policy that will restrict access to resources. Can be applied to users so they can only access resources if they have the VPN on.

######################


######################

Cloudwatch alarm creation:
These are lambdas that use python code to auto create alarms when a new server is brought up
The Slack notification lambda one will require a SNS sunscription to send a notification to slack when the alarm is created and ready
The ec2 in alarm and ec2 ok will also require sns subscritpions
ec2-tag-has-changed will also need an sns subscription

######################


######################

 AWS/Cloudformation/sftp username and password authentication stack 
 This cloudformation stack allows you to authenticate users to an sftp server via username and password
 The stack will create an API Gateway , Lambda function, three IAM Roles, API Logging Role, API Gateway Access Role and Lambda Role for you
 https://cloudsbaba.com/enabling-password-authentication-for-aws-sftp-transfer-family-service-using-aws-secrets-manager/
 
######################


######################

network_usage.sh
This script identifies the network usage of all EC2 instances in an AWS Region.
Make sure to run sudo chmod a+x network_usage.sh to make it executable.
Run the following syntax to run the script:
bash network_usage.sh ap-south-1 NetworkOut 2020-06-01T00:00:00.000Z 2020-06-30T23:59:59.000Z
 *Replace ap-south-1 with the Region where your instances are located
 *Specify either NetworkIn or NetworkOut to calculate the traffic flow direction.
 *Replace 2020-06-01T00:00:00.000Z and 2020-06-30T23:59:59.000Z with the start and end timestamps in the range that you want to calculate the network usage for.
 
 ######################
