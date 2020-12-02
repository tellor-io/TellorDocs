import os, sys, re, glob

def doc_to_index(doc_name):
    x = doc_name.split("_")[1]
    x = x.lower().replace("-", " ")
    x = x.capitalize()
    return x.split(".")[0]

if len(sys.argv) < 2:
    sys.exit("USAGE: update-summary.py path/to/docs")
docs = [os.path.basename(x) for x in sorted(glob.glob("%s/[!README]*.md"%sys.argv[1]))]
docs = map(lambda x: "* [%s](telliot-documentation/%s)" % (doc_to_index(x), x), docs)
docs = ["* [Introduction](telliot-documentation/README.md)"] + docs
new_content = "\n".join(docs)
fname = 'SUMMARY.md'
with open(fname, 'r') as f:
   data = f.read()
with open(fname, 'w') as fout:
    if "## Telliot Documentation" not in data:
        sys.exit("We expect a '## Telliot Documentation' heading in SUMMARY.md file, so we can update it's content!")
    data = re.sub(r'(## Telliot Documentation).*?(##)', 
      r'\1\n\n' +
      new_content + 
      r'\2\n\n##', data, flags=re.DOTALL)
    fout.write(data)
