import os
import argparse

# default values -- they will be overridden by command line arguments if provided
path = '.'
exclude_dirs = ['.git', '__pycache__', 'node_modules', 'venv', 'env', 'dist', 'build']
file_extensions = ('.py', '.js', '.ts', '.java', '.c', '.cpp', '.h', '.hpp', '.rs', '.go')

def count_lines(path: str, exclude_dirs, file_extensions):
    lines = 0
    for (root, dirs, filenames) in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for filename in filenames:
            if filename.endswith(file_extensions):
                file_path = os.path.join(root, filename)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        for line in file:
                            clean_line = line.strip()
                            
                            if clean_line and not clean_line.startswith('import'):
                                lines += 1
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Skipping file '{file_path}' due to a read error: {e}")
    return lines

def main():
    parser = argparse.ArgumentParser(description="Count lines of code in a directory.")
    parser.add_argument("-p", "--path", nargs='?', default=path, help="Path to the directory (default: current directory)")
    parser.add_argument("-e", "--exclude-dirs", nargs='*', default=exclude_dirs, help="Directories to exclude (default: .git __pycache__ node_modules venv env dist build)")
    parser.add_argument("-ext", "--extensions", nargs='*', default=file_extensions, help="File extensions to include (default: .py .js .ts .java .c .cpp .h .hpp .rs .go)")

    args = parser.parse_args()

    total_lines = count_lines(args.path, args.exclude_dirs, tuple(args.extensions))
    print(f"Total lines of code (excluding imports): {total_lines}")

if __name__ == "__main__":
    main()
