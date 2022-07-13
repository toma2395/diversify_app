# Diversify app!

Hi ! App is written from scratch by myself. To setup development pipeline and Kubernetes deployment please you need to configure your environment

# SetUp AWS
Go to GitHub.com project setup Settings/Secrets/Actions -> secret with names **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY_ID**

Setup **environment variables** in the code:

env:
`'REGION: us-east-1'` -> region to select
`'ACCOUNT_ID: '319876539559''` -> AWS Account id
`'DATABASE_UPDATE: True'` -> variable decides if we want to deploy DB into the K8s (keep True for the first deploy)
`'NLB_DNS_NAME: ad9b9797cea364c8cbca703612c91596-08fb8f1773b32ab4.elb.us-east-1.amazonaws.com'` -> Network load balancer DNS name -> need to be configured before

!!Please set up this env variables before running the Github Actions job.

# Testing

You can test working k8s application runing **./call.sh** script

# Enjoy
