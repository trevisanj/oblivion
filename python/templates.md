# Python templates

## Script

```
#!/usr/bin/env python
"""..."""

import argparse
import a107

def main():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=a107.SmartFormatter)
    parser.add_argument(...)
    args = parser.parse_args()
    main()
```