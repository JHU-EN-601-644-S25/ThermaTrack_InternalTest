import requests
import random
import string

BASE_URL = "http://192.168.56.1:4000"

def fuzz_payload():
    return {
        "patient_id": random.choice([
            None,
            "",
            "abc",
            -1,
            1.5,
            99999999,
            "' OR 1=1 --",
            "😊",
            [],
            {},
        ])
    }

for i in range(50):
    payload = fuzz_payload()
    try:
        res = requests.post(f"{BASE_URL}/temperature", json=payload)
        print(f"[{i}] Payload: {payload} → Status: {res.status_code}, Body: {res.text[:100]}")
    except Exception as e:
        print(f"[{i}] Payload: {payload} → Exception: {e}")