import argparse
import json
from  multiprocessing import Pool
import subprocess

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file",help="config file.",required=True)
    args = parser.parse_args()
    return args

def run_invocation(args):
    project_name, page_url, no_of_thread = args
    invocation = "python main.py  --project_name {0} --page_url {1} --no_of_thread {2} > {0}_crawler.log 2>&1".format(project_name,page_url,no_of_thread)
    print("Executing Invocation : ",invocation)
    try:
        subprocess.call(invocation,shell=True)
    except Exception as e:
        raise e

def main():
    options = parse_argument()
    config_file = options.config_file

    with open(config_file) as f:
        data = json.load(f)

    project_name = []
    page_url = []
    no_of_threads = []

    for d  in  data['parameters']:
        project_name.append(d['project_name'])
        page_url.append(d['page_url'])
        no_of_threads.append(d['no_of_threads'])

    pool = Pool(len(data['parameters']))
    pool.map(run_invocation,zip(project_name,page_url,no_of_threads))

if __name__ == '__main__':
    main()