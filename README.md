# Folder Mapper
Map folders and files in a folder tree by specifying the path to the root. Simplify organization by knowing how it looks like.

## Installation
To run the script, it only required the main.py script.

## Usage

```
python3 main.py PATH
```

## Files
**main.py**<br/>
Main script file.

**excluded.txt**<br/>
Ignore folders or files by including them is this file, NOT LINE SENSITIVE. Can also be done using the -e, --exclude flag.

**output.txt**<br/>
Output file, this is where the final result appears. The name can be changed using the -o, --output flag.

## Flags

**Required:**
```
path                            the specified path to be mapped.
```

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
**Modules:** Python native modules<br/>

## Todo
- [x] Folder support
- [x] File support
- [ ] Regex support
- [ ] Improve documentation
- [ ] Error handling
- [ ] Search
- [ ] Sorting
- [ ] File- and foldersize
