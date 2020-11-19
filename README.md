# Folder Mapper
Map folders and files in a folder tree by specifying the path to the root. Simplify organization by knowing how it looks like.

## Usage

**How to use:**
```
python3 main.py PATH
```

**Explanations:**<br/>
excluded.txt
- Ignore folder or file in mapping by adding the name of the object to the list.

output.txt
- Output file of the script, this is where you will find the final result. Name can be changed using -o or --output flag.

## Flags

**Required:**<br/>
main.py PATH

**Optional:**
```
-if, --include-files            include files in the output.
-o, --output                    choose a name for the output file (default output.txt).
-e FOLDER, --exclude FOLDER     exclude one or more folders from being mapped.
-l, --log                       output system logs.
```

## Info
**Language:** Python<br/>
**Version:** 3.9<br/>
**Modules:** Native<br/>

## Todo
- [x] Folder support
- [x] File support
- [ ] Regex support
- [ ] Improve documentation
- [ ] Error handling
- [ ] Search
- [ ] Sorting
- [ ] File- and foldersize
