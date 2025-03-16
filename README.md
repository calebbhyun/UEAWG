# Username & Email Address Wordlist Generator

This script generates wordlists of potential usernames or email addresses based on provided names. Optionally, it can append a specified domain to generate email addresses.

## Features
- Generate usernames or email addresses for a single name.
- Process a file containing multiple names to generate wordlists.
- Save results to a file or display them in the console.

## Usage

### Requirements
- Python 3.x

### Command Examples

#### Single Name
Generate a wordlist for a single name:
```
python ueawg.py -n "John Doe"
```

Add a domain to generate email addresses:
```
python script.py -n "John Doe" -d example.com
```

Save the results to an output file:
```
python script.py -n "John Doe" -d example.com -o output.txt
```

#### Multiple Names (File Input)
Process a file containing names (one name per line):
```
python script.py -f names.txt
```

Add a domain to generate email addresses for names in the file:
```
python script.py -f names.txt -d example.com
```

Save the results to an output file:
```
python script.py -f names.txt -d example.com -o output.txt
```
