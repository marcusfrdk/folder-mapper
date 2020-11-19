import os, argparse, collections, datetime, sys, time
excluded_dot_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), "excluded.txt"))

def syslog(msg:str, log:bool) -> None:
    if log:
        print(msg)

def excluded_files(arg:list, log:bool=False) -> list:
    if os.path.exists(excluded_dot_txt):
        syslog("Found excluded.txt, reading...", log)
        f = open('excluded.txt')
        content = f.read().split()
        f.close()
        syslog("Closed excluded.txt.", log)

        if arg:
            syslog("Excluded files where provided, adding to list.", log)
            content = content + arg

        return content
    else:
        return []

def create_file(data:str, name:str, log:bool=False) -> bool:
    if os.path.exists("output.txt"):
        syslog("Found existing output.txt file, deleting.", log)
        os.remove("output.txt")

    if "." in name:
        syslog("A dot was provided in the output filename, deleting everything after the first dot.", log)
        name = name.split(".")[0]

    name = name + ".txt"
    syslog(f"Creating {name}.", log)
    f = open(name, "w+")
    f.write(data)
    f.close()
    syslog(f"Closed {name}.", log)
    
    if os.path.exists(name):
        syslog(f"{name} was successfully created.", log)
        print(f"Output: {name}.")
        return True
    else:
        syslog(f"{name} could not be created, it was not found.", log)
        return False


def mapper(path:str, files:bool=False, exclude:list=[], log:bool=False) -> str:
    data = ""
    abs_path = os.path.abspath(path)
    basepath = path

    if os.path.exists(path):
        excluded = excluded_files(exclude, log)
        for path, folder, file in os.walk(path):
            folder[:] = [f for f in folder if f.lower() not in [l.lower() for l in excluded]] # Add regex support here

            path = path.split(basepath)[1]

            depth = collections.Counter(path)["/"] - 1
            tab_depth = depth + 1

            name = path.split("/")[-1]
            clean_name = path.split("/")[-1]

            if clean_name != "":
                syslog(f"Found {clean_name.upper()}.", log)
            
            for tab in range(tab_depth):
                name = "\t" + name

            name = f"[{depth}]" + name + "\n"
            data = data + name

            if files:
                for file_name in file:
                    if file_name not in excluded:
                        file_row = file_name
                        for x in range(tab_depth + 1):
                            file_row = "\t" + file_row
                        data = data + f"[{depth + 1}]" + file_row + "\n" 
                        syslog(f"Successfully added {file_name.upper()}.", log)

            if clean_name:
                syslog(f"Successfully added {clean_name.upper()}.", log)
    else:
        syslog("Error adding path.", log)

    data = data.split("\n", 1)[1]
    data = f"Path: {abs_path}\nTime: {datetime.datetime.utcnow()}\n\n" + data

    if data:
        return data
    else:
        return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map a folder tree by specifying the path to the root of the tree. By default it only maps out folders, but can include files with the -if flag.")
    parser.add_argument("path", help="root of the tree you want to scan.")
    parser.add_argument("-if", "--include-files", help="include files in output.", action="store_true")
    parser.add_argument("-o", "--output", metavar="name", help="choose a name for the output file (default output.txt).", default="output")
    parser.add_argument("-e", "--exclude", metavar="folder", help="exclude one or more folders from being mapped.", nargs="*")
    parser.add_argument("-l", "--log", help="output system logs.", action="store_true")
    args = parser.parse_args()

    if args.include_files:
        print("Scanning folders and files...")
    else:
        print("Scanning folders...")

    data = mapper(args.path, args.include_files, args.exclude, args.log)
    print("Creating file...")
    create_file(data, args.output, args.log)
