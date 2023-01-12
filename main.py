import sys
from htmlparser import Parser
from pprint import pprint

args = sys.argv
args_len = len(args)
#print(args_len)

if args_len < 2 or args_len > 2:
    print("Pass only 1 argument.")
    exit(0)
else:
    file_path = args[1]

    with open(f'{file_path}', 'r') as f:
        p = Parser().parse(f)
        Parser().__jsonify()
        with open('json_output.json', 'w') as out:
            out.write(p)
            

    