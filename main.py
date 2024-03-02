import argparse
import os
import sys

from utils.format_content import format_content

def main(path: str) -> None:
  if not os.path.exists(path):
    print(f"supercat: {path}: No such file.", file=sys.stderr, flush=True)
    return None

  with open(path, "r") as f:
    content = format_content(f.readlines())
    
    for text in content:
      if text == "\n":
        print("")
        continue
      print(text)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Display file contents.")
  parser.add_argument("path", help="Path of the file to display.")

  args = parser.parse_args()
  main(args.path)