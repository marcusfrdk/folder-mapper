import os, argparse, re, collections
excluded_dot_txt = os.path.abspath(os.path.join(os.path.dirname(__file__), "excluded.txt"))

def syslog(msg:str, log:bool) -> None:
    if log:
        print(msg)

def excluded_files(arg:list, log:bool=False) -> list:
    if os.path.exists(excluded_dot_txt):
        syslog("Found excluded.txt, reading...", log)
        f = open('excluded.txt')
        content = re.sub("[^\w]", " ", f.read()).split()
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
        return True
    else:
        syslog(f"{name} could not be created, it was not found.", log)
        return False
    # Check if string contains . and add .txt to end

def mapper(path:str, files:bool=False, exclude:list=[], log:bool=False) -> str:
    data = ""

    if os.path.exists(path):
        excluded = excluded_files(exclude, log)
        for path, folder, file in os.walk(path):
            folder[:] = [f for f in folder if f not in excluded]

            depth = collections.Counter(path)["/"] - 1
            name = path.split("/")[-1]
            clean_name = path.split("/")[-1]
            syslog(f"Found {clean_name.upper()}.", log)
            
            for tab in range(depth):
                name = "\t" + name

            name = name + "\n"
            data = data + name
            syslog(f"Successfully added {clean_name.upper()}!", log)
    else:
        syslog("Error adding path.", log)

    if data:
        return data.split("\n", 1)[1]
    else:
        return ""

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map a folder tree by specifying the path to the root of the tree. By default it only maps out folders, but can include files with the -if flag.")
    parser.add_argument("path", help="root of the tree you want to scan.")
    parser.add_argument("-if", "--include-files", help="include files in output.", action="store_true")
    parser.add_argument("-o", "--output", metavar="name", help="name of the output file txt file.", default="output")
    parser.add_argument("-e", "--exclude", metavar="folder", help="exclude folder/s from map.", nargs="*")
    parser.add_argument("-l", "--log", help="output system logs.", action="store_true")
    args = parser.parse_args()

    data = mapper(args.path, args.include_files, args.exclude, args.log)
    create_file(data, args.output, args.log)

