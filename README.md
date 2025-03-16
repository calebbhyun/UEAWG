# Username & Email Address Wordlist Generator

## Overview
This script generates wordlists of potential usernames or email addresses based on provided names. Optionally, it can append a specified domain to generate email addresses.

## Features
- Generate usernames or email addresses for a single name.
- Process a file containing multiple names to generate wordlists.
- Save results to a file or display them in the console.

## Prerequisites
- Python 3.x

## Usage

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

## Example Output
- `firstlast@example.com`
- `firstl@example.com`
- `flast@example.com`
- `lastfirst@example.com`
- `lastf@example.com`
- `lfirst@example.com`
- `first.last@example.com`
- `first.l@example.com`
- `f.last@example.com`
- `last.first@example.com`
- `last.f@example.com`
- `l.first@example.com`
- `first_last@example.com`
- `first_l@example.com`
- `f_last@example.com`
- `last_first@example.com`
- `last_f@example.com`
- `l_first@example.com`
