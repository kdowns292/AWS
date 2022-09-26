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
