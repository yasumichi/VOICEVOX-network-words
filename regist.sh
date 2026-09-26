#!/bin/sh

curl -X POST "http://127.0.0.1:50021/import_user_dict?override=true" \
  -H "Content-Type: application/json" \
  -d @network-words.json
