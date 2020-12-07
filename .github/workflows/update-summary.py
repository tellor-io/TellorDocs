import os, sys, re, glob

def doc_to_index(doc_name):
    x = doc_name.split("_")[1]
    x = x.lower().replace("-", " ")
    x = x.capitalize()
    return x.split(".")[0]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("USAGE: update-summary.py <path/to/INDEX.md>")
    new_content = []
    with open(sys.argv[1], "r") as fcontent:
        lines = fcontent.readlines()
        headings = [line.strip() for line in lines if len(line.strip()) != 0 and line.startswith("*")]
        # Handle README.md file from telliot repo: rename README.md -> telliot-documentation.md
        readme = headings[0]
        new_content.append(re.sub(r'(\()(.*)(\.md)', '(telliot-documentation/telliot-documentation.md', readme))
        # Handle other headings
        for line in headings[1:]:
            line = line.strip()
            line = re.sub(r'(\()(.*)(\.md)', '(telliot-documentation/\\2.md', line)
            new_content.append(line.strip())
    new_content = "\n".join(new_content)
    fname = 'SUMMARY.md'
    orig_data = None
    with open(fname, 'r') as f:
       orig_data = f.read()
    if "## Telliot Documentation" not in orig_data:
        sys.exit("We expect a '## Telliot Documentation' heading in SUMMARY.md file, so we can update it's content!")
    data = re.sub(r'(?<=## Telliot Documentation).*?(?<=##)', 
      r'\n\n' +
      new_content + 
      r'\n\n##', orig_data, flags=re.DOTALL)
    if '--check-only' in sys.argv:
        sys.exit(int(data == orig_data))
    with open(fname, 'w') as fout:
        fout.write(data)
