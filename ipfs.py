import ipfsApi
import os

#connect to ipfs daemon running on localhost
try:
    api = ipfsApi.Client('127.0.0.1', 5001)
except:
    print("IPFS daemon could not be started")
    exit(0)

#same command line arguments as of ipfs
def add(file):
    res = api.add(file)
    return res

def pin(file):
    res = api.pin_ls(opts={'type':'all'})
    return res

def get_file(hash):
    cmd = "ipfs cat {hash} > res.txt".format(hash=hash)
    os.system(cmd)
    return "res.txt"