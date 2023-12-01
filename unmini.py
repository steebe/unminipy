import argparse
import json
import pyperclip

def main():
  cli_args = parse_args()
  try:
    unminified = None

    if cli_args.clip:
      try:
        unminified = json.loads(pyperclip.paste())
      except:
        print("No valid JSON found in clipboard")
        return
    elif cli_args.file:
      try:
        json_file = open(cli_args.file)
        unminified = json.loads(json_file.read())
      except:
        print("File provided is not a valid JSON file")
        return

    unminifiedPayload = json.dumps(unminified, indent = 2)

    if not cli_args.no_copy:
      pyperclip.copy(unminifiedPayload)
    if cli_args.verbose:
      print(unminifiedPayload)
  except:
    print("The string provided is not valid JSON.")

# Bootstraps the argparse library for providing readable docs & CLI argument handling
def parse_args():
  parser = argparse.ArgumentParser(
    prog="unminipy",
    description="""
      Unminify your JSON data for visibility. Provide valid JSON via your clipboard
      or a local file, and its unminified form will be provided in your clipboard.
    """
  )
  parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="print the unminified JSON after unminifying",
    required=False
  )
  parser.add_argument(
    "-n",
    "--no-copy",
    action="store_true",
    help="do not update the clipboard with the unminified JSON",
    required=False
  )
  standalone_args = parser.add_mutually_exclusive_group(required=True)
  standalone_args.add_argument(
    "--clip",
    action="store_true",
    help="use the data stored in the clipboard as the input"
  )
  standalone_args.add_argument(
    "--file",
    help="provide the JSON via a file"
  )
  return parser.parse_args()

main()
