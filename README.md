# Website Change Detector

This Python script monitors specified websites for changes and generates an HTML report highlighting the differences.

## Features

- Checks multiple websites for content changes
- Compares current website content with previously saved versions
- Generates an HTML report with highlighted changes
- Supports headless browsing for efficient checking
- Configurable wait time for loading website content
- Customizable input file for specifying URLs to check

## Requirements

- Python 3.x
- Required Python packages: `selenium 4.23.1`, `redlines 0.4.2`
- Chrome WebDriver

## Installation

1. Clone this repository:
   ```cmd
   git clone https://github.com/kelvinq0xff/website-change-detector.git
   cd website-change-detector
   ```

2. Install the required packages:
   ```cmd
   pip install selenium==4.23.1 redlines==0.4.2
   ```

3. Download and install the Chrome WebDriver that matches your Chrome browser version.

## Usage

1. Create a text file named `urls.txt` in the same directory as the script, with one URL per line.

2. Run the script:
   ```cmd
   python website-change-detector.py
   ```

   Optional arguments:
   - `--file`: Specify a different input file (default: 'urls.txt')
   - `--wait`: Set the wait time in seconds for loading website content (default: 10)

   Example with custom arguments:
   ```cmd
   python website-change-detector.py --file my_urls.txt --wait 15
   ```

3. The script will generate an HTML report named `result-YYYY-MM-DD.html` in the same directory, showing any detected changes.

## Output

The generated HTML report includes:
- Links to the checked websites
- Highlighted text showing additions and deletions

## Author

Kelvin Q (kelvinq0xff)
