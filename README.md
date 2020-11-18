# Folder Mapper
Map folders and files in a folder tree by specifying the path to the root. Simplify organization by knowing how it looks like.

## Usage

**Use:**
```
python3 main.py PATH
```

**Explanations:**
excluded.txt
: Ignore folder or file in mapping by adding the name of the object to the list.

output.txt[^1]
: Output file of the script, this is where you will find the final result.

[^1]: The name of the output file can be changes using the -o or --output flag.

## Flags

**Required:**
main.py PATH

**Optional:**
```
-if, --include-files            include files in the output.
-o, --output                    choose a name for the output file (default output.txt).
-e FOLDER, --exclude FOLDER     exclude one or more folders from being mapped.
-l, --log                       output system logs.
```

## Info
**Language:** Python
**Version:** 3.9
**Modules:** os, argparse, re and collections (python native)

## Todo
- [x] Add support for folders
- [ ] Add support for files
- [ ] Add support for excluding names using regex.
- [ ] Find a simpler way of using the script.
- [ ] Improve the logs and their effectiveness
- [ ] Add more error handling
