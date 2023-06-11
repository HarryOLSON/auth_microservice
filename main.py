import uvicorn
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", default=False, help="debug let's you see sql commands. Not for prod!")
args = parser.parse_args()


if __name__ == "__main__":
    uvicorn.run("server:server", host=args.host, port=args.port)
