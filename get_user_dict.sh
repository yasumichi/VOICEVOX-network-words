#!/bin/sh

curl http://127.0.0.1:50021/user_dict | jq > network-words.json
