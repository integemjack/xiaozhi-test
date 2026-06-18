import json, sys
data = json.load(sys.stdin)
for j in data['jobs']:
    print(f"{j['name']}: {j['conclusion']}")
    if 'Windows' in j['name']:
        for s in j['steps']:
            print(f"  {s['name']}: {s['conclusion']}")
