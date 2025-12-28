# Copyright (C) 2020 @HirMtsd. All Rights Reserved.
# coding: utf-8
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
# 2020/08/08

import json ,sys
from jsonschema import  ValidationError, FormatChecker, Draft202012Validator
from referencing import Registry, Resource

with open('Prefecture_schema.json', encoding="utf-8") as file_schema:
    json_schema = json.load(file_schema)

with open('Prefecture_list.json', encoding="utf-8") as file_json:
    json_data = json.load(file_json)

registry = Registry().with_resources({
    # LocalPublicEntityCode.json
    f"file://{('common\\LocalPublicEntityCode.json').as_posix()}":
        Resource.from_contents(
            json.loads((COMMON / 'LocalPublicEntityCode.json').read_text(encoding="utf-8"))
        ),

    # LocalPublicEntityCommonProperties.json
    f"file://{('common\\LocalPublicEntityCommonProperties.json').as_posix()}":
        Resource.from_contents(
            json.loads((COMMON / 'LocalPublicEntityCommonProperties.json').read_text(encoding="utf-8"))
        ),
})

try:
    Draft202012Validator(json_data, json_schema,registry=registry, format_checker=FormatChecker())
except ValidationError as e:
    print(e.message)
    sys.exit(1)

print('CHECK END')
sys.exit(0)
