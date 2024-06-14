import json

input = "/root/autodl-tmp/HA-DPO/ha_dpo/data/hadpo/llava-v1.5/pope_data.json"

with open(input, "r")as f:
    file = json.load(f)
    with open(input.replace(".json", "_copy.json"), "w")as o:
        json.dump(file, o, indent=2)