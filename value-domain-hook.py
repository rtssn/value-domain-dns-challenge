#!/usr/bin/env python3

import os
import sys
import json
import requests
import time

api_key = ""
api_endpoint = "https://api.value-domain.com/v1/domains/"

domain = os.environ.get('CERTBOT_DOMAIN')
validation = os.environ.get('CERTBOT_VALIDATION')

f = open("apikey.txt", "r")
api_key = f.read()
f.close()
api_key = api_key.strip()

def get_dns_record(domain):
    get_dns_record_url = api_endpoint + domain + "/dns"

    headers = {
        "Authorization": "Bearer " + api_key
    }

    response = requests.get(get_dns_record_url, headers=headers, timeout=60)
    json_response = json.loads(response.text)
    records = json_response['results']['records']

    return records

def update_dns_record(domain, records):
    update_dns_record_url = api_endpoint + domain + "/dns"

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    data = {
        "ns_type": "valuedomain1",
        "records": records,
        "ttl": "3600"
    }

    json_data = json.dumps(data)
    response = requests.put(update_dns_record_url, json_data, headers=headers, timeout=60)

def main():    
    print("Domain: " + domain)
    print("Validation: " + validation)

    cmd = "REGEST"

    if len(sys.argv) > 1:
        cmd = sys.argv[1]

    if cmd == "REGEST":
        records = get_dns_record(domain)
        records = records + f"\ntxt _acme-challenge {validation}"

        update_dns_record(domain, records)
        time.sleep(60)

    if cmd == "DELETE":
        records = get_dns_record(domain)
        records = records.replace(f"\ntxt _acme-challenge {validation}", "")
        print(records)
        update_dns_record(domain, records)

        print("DNS AUTH DONE.")

        print("Nginx reload...")
        os.system("systemctl reload nginx")
        print("Nginx reload DONE.")

if __name__ == "__main__":
    main()

