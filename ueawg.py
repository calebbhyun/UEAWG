import argparse
import sys

def generate_wordlist(name, domain=None):
    try:
        first, last = name.split()
    except ValueError:
        raise ValueError(f"Invalid name format: '{name}'. Please provide 'FIRSTNAME LASTNAME'.")
    
    patterns = [
        f"{first}{last}", f"{first[0]}{last}", f"{first}{last[0]}",
        f"{last}{first}", f"{last[0]}{first}", f"{last}{first[0]}",
        f"{first}.{last}", f"{first[0]}.{last}", f"{first}.{last[0]}",
        f"{last}.{first}", f"{last[0]}.{first}", f"{last}.{first[0]}",
        f"{first}_{last}", f"{first[0]}_{last}", f"{first}_{last[0]}",
        f"{last}_{first}", f"{last[0]}_{first}", f"{last}_{first[0]}"
    ]
    return [f"{pattern}@{domain}".lower() for pattern in patterns] if domain else [pattern.lower() for pattern in patterns]

def process_file(file, domain):
    with open(file, "r") as f:
        return [
            word 
            for line in f 
            for word in generate_wordlist(line.strip(), domain) 
            if line.strip()
        ]

def main():
    parser = argparse.ArgumentParser(description="Username & Email Address Wordlist Generator")
    parser.add_argument("-n", "--name", help="FIRSTNAME LASTNAME")
    parser.add_argument("-f", "--file", help="File with names (one per line)")
    parser.add_argument("-d", "--domain", help="(Optional) Domain for email addresses")
    parser.add_argument("-o", "--output", help="(Optional) Output file name")
    args = parser.parse_args()

    if not args.name and not args.file:
        sys.exit("Error: Provide a name (-n) or a file (-f).")

    wordlist = []
    try:
        if args.name:
            wordlist = generate_wordlist(args.name, args.domain)
        if args.file:
            wordlist.extend(process_file(args.file, args.domain))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w") as out_file:
            out_file.write("\n".join(wordlist))
    else:
        print("\n".join(wordlist))

if __name__ == "__main__":
    main()
