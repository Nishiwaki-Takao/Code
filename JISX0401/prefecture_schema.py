# Copyright (C) 2020 @HirMtsd. All Rights Reserved.
# coding: utf-8
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
# 2020/08/08

import json ,sys
from jsonschema import validate, ValidationError, FormatChecker, Draft2020Validator, RefResolver

with open('Prefecture_schema.json', encoding="utf-8") as file_schema:
    json_schema = json.load(file_schema)

with open('Prefecture_list.json', encoding="utf-8") as file_json:
    json_data = json.load(file_json)

resolver = RefResolver(
    base_uri=f"file://{BASE.as_posix()}/",
    referrer=schema,
)

try:
    Draft2020Validator(json_data, json_schema,resolver=resolver, format_checker=FormatChecker())
except ValidationError as e:
    print(e.message)
    sys.exit(1)

print('CHECK END')
sys.exit(0)
