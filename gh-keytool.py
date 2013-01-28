import json
import getpass
import os.path
import pprint
import requests
import sys

GITHUB_API_URL = "https://api.github.com"

def main():
    try:
        if os.path.exists(sys.argv[1]):
            keyfile = sys.argv[1]
    except KeyError:
        print >> sys.stderr, "Must provide keyfile"
        sys.exit(1)

    extension = os.path.splitext(keyfile)[1]
    if extension != ".pub":
        print >> sys.stderr, "Keyfile %s does not end in .pub, refusing to proceed." % keyfile
        sys.exit(1)

    username = raw_input("User: ")
    password = getpass.getpass()
    name = raw_input("Keyname: ")

    with open(keyfile) as fh:
        data = json.dumps({"title": name, "key": fh.read()})

    r = requests.post(GITHUB_API_URL + "/user/keys", data, auth=(username, password))
    print "Status Code: %d" % r.status_code
    pprint.pprint(r.headers)
    print r.json()


if __name__ == '__main__':
    main()
