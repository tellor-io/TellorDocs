import os, sys, re, glob

def doc_to_index(doc_name):
    x = doc_name.split("_")[1]
    x = x.lower().replace("-", " ")
    x = x.capitalize()
    return x.split(".")[0]

if len(sys.argv) < 2:
    sys.exit("USAGE: update-summary.py <path/to/INDEX.md>")
new_content = []
with open(sys.argv[1], "r") as fcontent:
    lines = fcontent.readlines()
    for line in lines:
        if len(line.strip()) != 0 and line.startswith("*"):
            line = line.strip()
            line = re.sub(r'(\()(.*)(\.md)', '(telliot-documentation/\\2.md', line)
            new_content.append(line.strip())
new_content = "\n".join(new_content)
fname = 'SUMMARY.md'
with open(fname, 'r') as f:
   data = f.read()
with open(fname, 'w') as fout:
    if "## Telliot Documentation" not in data:
        sys.exit("We expect a '## Telliot Documentation' heading in SUMMARY.md file, so we can update it's content!")
    data = re.sub(r'(?<=## Telliot Documentation).*?(?<=##)', 
      r'\n\n' +
      new_content + 
      r'\n\n##', data, flags=re.DOTALL)
    fout.write(data)
