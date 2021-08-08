import jsonschema
from jsonschema import validate

json_schema_user = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 0,
        },
        "first_name": {
            "type": "string",
            "pattern": "^[\\sa-zA-z-]+$"
        },
        "second_name": {
            "type": "string",
            "pattern": "^[\\sa-zA-z-]+$"
        },
        "age": {
            "type": "integer",
            "minimum": 0,
            "maximum": 120
        }
    },
    "required": [
        "id",
        "first_name",
        "second_name",
        "age"
    ]
}


def validate_json(response_json, schema_json):
    try:
        validate(instance=response_json, schema=schema_json)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True
