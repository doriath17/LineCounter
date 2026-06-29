import os
import argparse

# default values -- they will be overridden by command line arguments if provided
path = '.'
exclude_dirs = ['.git', '__pycache__', 'node_modules', 'venv', 'env', 'dist', 'build']
file_extensions = ('.py', '.js', '.ts', '.java', '.c', '.cpp', '.h', '.hpp', '.rs', '.go')

def count_lines(path: str, exclude_dirs, file_extensions):
    lines = 0
    files_counted = 0
    for (root, dirs, filenames) in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for filename in filenames:
            if filename.endswith(file_extensions):
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        files_counted += 1
                        for line in file:
                            clean_line = line.strip()
                            
                            if clean_line and not clean_line.startswith('import'):
                                lines += 1
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Skipping file '{file_path}' due to a read error: {e}")
    return [lines, files_counted]

def main():
    parser = argparse.ArgumentParser(description="Count lines of code in a directory.")
    parser.add_argument("-p", "--paths", nargs='*', default=path, help="Path to the directory (default: current directory)")
    parser.add_argument("-ed", "--exclude-dirs", nargs='*', default=exclude_dirs, help="Directories to exclude (default: .git __pycache__ node_modules venv env dist build)")
    parser.add_argument("-ext", "--extensions", nargs='*', default=file_extensions, help="File extensions to include (default: .py .js .ts .java .c .cpp .h .hpp .rs .go). ")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    print("-" * 40)
    for p in args.paths:
        if not os.path.exists(p):
            print(f"Error: The path '{p}' does not exist.")
            return
        if args.verbose:
            print(f"Counting lines of code in '{p}'")
            print(f"Excluding directories: {args.exclude_dirs}")
            print(f"Counting files with extensions: {args.extensions}\n")

        total_lines, files_counted = count_lines(p, args.exclude_dirs, tuple(args.extensions))
        
        print(f"Path: {p}")
        print(f"Total lines of code (excluding imports): {total_lines}")
        print(f"Total files counted: {files_counted}")
        print("-" * 40)

if __name__ == "__main__":
    main()
