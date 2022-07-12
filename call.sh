#!/bin/bash
dns_name=$(aws elbv2 describe-load-balancers --region us-east-1 | jq -r '.LoadBalancers[0].DNSName')
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}First dummy call ${NC}"
curl  $dns_name/diversify

echo -e "\n${GREEN}Second dummy call - LIST VOLUNTEERS 1${NC}"
curl  $dns_name/diversify/volunteer

echo -e "\n${GREEN}Third dummy call - VOLUNTEER 1${NC}"
curl  $dns_name/diversify/volunteer/1


echo -e "\n${GREEN}Third dummy call - VOLUNTEER 2${NC}"
curl  $dns_name/diversify/volunteer/2

echo -e "\n${GREEN}Forth dummy call - ADDING VOLUNTEER 3${NC}"
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Fabio","surname": "Ramon","city": "Porto","country": "Portugal"}' \
    $dns_name/diversify/volunteer

echo -e "\n${GREEN}What time is it ???${NC}"
curl  $dns_name/diversify/get-current-date
