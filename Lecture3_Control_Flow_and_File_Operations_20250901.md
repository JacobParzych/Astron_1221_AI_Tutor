# Control Flow and File Operations

*Tutorial by Yuan-Sen Ting*

*Astron 1221: Lecture 3*

## Introduction

In astronomical research, we rarely work with single measurements or isolated calculations. Instead, we process thousands of images from a night's observations, analyze time series spanning years, or search through millions of stars to find rare objects. These tasks require programs that can make decisions and repeat operations efficiently.

This tutorial introduces the control structures that give your programs intelligence: the ability to make decisions with if/elif/else statements and repeat tasks with loops. You'll also learn to work with files - reading observational data and saving your results. Throughout, we'll develop essential debugging techniques that will save you hours of frustration when working with real astronomical data.

By the end of this lecture, you'll be able to write programs that can automatically process entire directories of observations, make intelligent decisions about data quality, and save results in formats that other astronomers can use.

## Control Flow: Making Decisions

### The if Statement

Programs need to make decisions based on data. In astronomy, we constantly ask questions: Is this star bright enough to observe? Is the seeing good enough for spectroscopy? Has this object moved since the last observation?

The `if` statement lets Python make these decisions. It works like a gatekeeper - only letting code run when a condition is met:

```python
magnitude = 15.3
limiting_magnitude = 18.0

if magnitude < limiting_magnitude:
    print(f"Star with mag {magnitude} is observable")
```

The code inside the `if` block only runs when the condition is True. Notice two crucial syntax elements:
- The colon `:` at the end of the if line - this tells Python "here comes a code block"
- The indentation (typically 4 spaces) - this shows Python which code belongs to the if statement

These aren't optional - Python uses indentation to define code blocks, unlike languages like C or Java that use curly braces `{}`. This makes Python code visually clean but requires careful attention to spacing.

### Adding else for Alternative Actions

Often we want to do one thing if a condition is true and something different if it's false. The `else` clause provides this alternative path:

```python
seeing_arcsec = 2.1  # Atmospheric seeing in arcseconds
```

Seeing measures how much stars twinkle due to atmospheric turbulence. Smaller numbers mean steadier air and sharper star images. Values below 1 arcsecond are excellent, while above 2 arcseconds makes detailed observations difficult.

```python
if seeing_arcsec < 1.5:
    print("Good conditions for high-resolution imaging")
else:
    print("Conditions only suitable for photometry")
```

The `else` block runs when the `if` condition is False. Think of it as "otherwise" - if the condition isn't met, do this instead.

### Multiple Conditions with elif

Real decisions often have multiple possibilities. The `elif` (short for "else if") lets us check multiple conditions in sequence:

```python
airmass = 1.8  # Atmospheric path length relative to zenith
```

Airmass measures how much atmosphere starlight passes through. At zenith (directly overhead), airmass = 1.0. As objects get lower in the sky, light passes through more air, increasing extinction and blurring.

```python
if airmass < 1.2:
    quality = "Excellent - near zenith"
elif airmass < 1.5:
    quality = "Good - acceptable for most observations"
elif airmass < 2.0:
    quality = "Fair"
else:
    quality = "Poor - only bright objects"

print(f"Airmass {airmass}: {quality}")
```

Python checks each condition in order, like going down a checklist. It runs the first block where the condition is True, then skips the rest. If none are True, the `else` block runs (if present).

### Combining Conditions with Logical Operators

Real-world decisions often depend on multiple factors. Python's logical operators let us combine conditions:

```python
ra_hours = 14.5  # Right ascension in hours
dec_deg = 45.0   # Declination in degrees
magnitude = 8.5
```

Right Ascension (RA) and Declination (Dec) are celestial coordinates - like longitude and latitude on Earth, but projected onto the sky. RA is measured in hours (0-24) because the sky rotates once per day. Dec is measured in degrees (-90 to +90) from the celestial equator.

```python
# Check if observable from northern hemisphere with small telescope
is_northern = dec_deg > 0
is_bright_enough = magnitude < 10
is_evening = 18 <= ra_hours or ra_hours <= 6  # Evening sky
```

Now combine these conditions:

```python
if is_northern and is_bright_enough and is_evening:
    print("Good target for tonight's public observing session")
```

The logical operators work like English:
- `and` - both/all conditions must be True
- `or` - at least one condition must be True  
- `not` - reverses True to False (and vice versa)

### The in Operator for Membership Testing

Python provides the `in` operator to check if a value exists in a collection. This is extremely useful for validation:

```python
# Check if filter is available
available_filters = ['B', 'V', 'R', 'I']
requested_filter = 'U'

if requested_filter in available_filters:
    print(f"Using {requested_filter} filter")
else:
    print(f"{requested_filter} filter not available")
```

The `in` operator also works with strings to check for substrings:

```python
observation_notes = "Clouds developing, seeing deteriorating"

if "cloud" in observation_notes.lower():
    print("Warning: Weather issues noted")
```

### Nested Conditions

Sometimes we need to make decisions within decisions. We can nest if statements inside each other:

```python
is_variable = True
period_days = 0.5
amplitude = 0.15
```

Variable stars change brightness over time. The period tells us how long one cycle takes, and amplitude measures how much the brightness changes.

```python
if is_variable:
    if period_days < 1.0:
        if amplitude > 0.1:
            star_type = "High-amplitude short-period variable"
        else:
            star_type = "Low-amplitude short-period variable"
    else:
        star_type = "Long-period variable"
else:
    star_type = "Non-variable star"

print(f"Classification: {star_type}")
```

Think of nested conditions like a decision tree - each level asks a more specific question. However, too many levels make code hard to read. Often it's clearer to combine conditions with `and`/`or`.

### Ternary Operator (Conditional Expressions)

Python provides a concise way to assign values based on conditions. The ternary operator puts a simple if/else on one line:

```python
magnitude = 8.5

# Long form
if magnitude < 10:
    classification = "bright"
else:
    classification = "faint"

# Ternary operator - same result in one line
classification = "bright" if magnitude < 10 else "faint"
print(f"Star is {classification}")
```

This is especially useful for setting parameters:

```python
# Set exposure time based on brightness
magnitude = 14.5
exposure_time = 30 if magnitude < 12 else 120
print(f"Exposure time: {exposure_time} seconds")
```

## Loops: Repeating Operations

### The for Loop

Astronomical data often comes in collections - multiple images, many stars, time series of measurements. The `for` loop lets us process each item without writing repetitive code:

```python
# List of filters used in photometry
filters = ['U', 'B', 'V', 'R', 'I']
```

These letters represent different colored filters astronomers place in front of detectors. U is ultraviolet, B is blue, V is visual (green), R is red, and I is infrared. Each reveals different stellar properties.

```python
print("Johnson-Cousins photometric system:")
for filter_name in filters:
    print(f"  Filter {filter_name}")
```

The loop variable (`filter_name`) acts like a pointer that moves through the list, taking on each value in turn. Python automatically handles moving to the next item.

### Looping with Indices using range()

Sometimes you need to know not just the value but also its position in the sequence. The `range()` function generates a sequence of numbers:

```python
for i in range(5):
    print(f"Index {i}")
```

Important: `range(5)` produces 0, 1, 2, 3, 4 - it stops before reaching 5. This matches Python's zero-based indexing where the first item is at position 0, not 1.

You can specify where to start and stop, and how much to step:

```python
for hour in range(20, 24):  # Start at 20, stop before 24
    print(f"{hour}:00 UT")
```

UT (Universal Time) is the time at Greenwich, England - astronomers worldwide use it to coordinate observations.

### Better Iteration with enumerate()

Python provides `enumerate()` to elegantly get both position and value:

```python
observations = [15.32, 15.28, 15.35]

for i, mag in enumerate(observations):
    print(f"Observation {i+1}: magnitude = {mag}")
```

The `enumerate()` function returns pairs like (0, 15.32), (1, 15.28), etc. We unpack each pair into two variables: `i` gets the index, `mag` gets the value. We add 1 to `i` when printing because humans count from 1, not 0.

### Looping Over Multiple Lists with zip()

Often we have related data in separate lists that belong together:

```python
star_names = ['Sirius', 'Vega', 'Arcturus']
magnitudes = [-1.46, 0.03, -0.05]
```

Remember: in astronomy, smaller (more negative) magnitudes mean brighter stars. Sirius at -1.46 is the brightest star in the night sky.

```python
for name, mag in zip(star_names, magnitudes):
    print(f"{name}: V = {mag:.2f}")
```

The `zip()` function is like a zipper - it pairs up corresponding elements from multiple sequences. If lists have different lengths, it stops at the shortest:

```python
# Example with different lengths
names = ['Star1', 'Star2', 'Star3']
mags = [10.5, 11.2]  # Only 2 values

for name, mag in zip(names, mags):
    print(f"{name}: {mag}")
# Only prints 2 pairs, stops at shortest list
```

### The while Loop

Use `while` when you don't know in advance how many repetitions you need. The loop continues as long as its condition remains True:

```python
# Simulate iterative convergence
position_change = 100.0  # Initial large value in arcseconds
iteration = 0
tolerance = 0.001  # Stop when change is less than this
```

Many astronomical calculations require iteration - repeatedly improving an answer until it's accurate enough. For example, calculating precise planetary orbits requires solving equations that can't be solved directly.
 
Note: The `+=` operator is a shorthand for incrementing. `iteration += 1` means `iteration = iteration + 1`. This is very common in loops for counting iterations.

```python
while position_change > tolerance:
    iteration += 1
    # Simulate convergence - each iteration reduces error by 30%
    # In real code, this would be a complex orbital calculation
    position_change = position_change * 0.7
    print(f"Iteration {iteration}: change = {position_change:.6f} arcsec")
```

The factor 0.7 simulates how iterative methods converge - each step gets us 30% closer to the true answer. Real astronomical calculations might use more advanced algorithms.

Warning: Always ensure your while loop can eventually end. If the condition never becomes False, you get an infinite loop that runs forever!

### Loop Control: break and continue

Sometimes you need finer control over loop execution.

The `break` statement immediately exits the entire loop:

```python
# Search for first detection above threshold
measurements = [0.5, 0.8, 1.2, 5.6, 2.3]
detection_threshold = 3.0

for i, flux in enumerate(measurements):
    if flux > detection_threshold:
        print(f"Detection at index {i}!")
        break  # Stop searching once found
```

The `continue` statement skips the rest of the current iteration and jumps to the next:

```python
# Process only positive values
values = [1.5, -0.3, 2.1, -0.8, 3.2]

for val in values:
    if val < 0:
        continue  # Skip to next value
    print(f"Processing: {val}")
```

### List Comprehensions

Python offers a concise way to create lists based on existing sequences. List comprehensions pack a loop and optional condition into a single line.

Traditional approach with a loop:

```python
magnitudes = [15.2, 14.8, 16.1, 13.9, 15.5]

bright_stars = []
for mag in magnitudes:
    if mag < 15.0:
        bright_stars.append(mag)
print(bright_stars)
```

The same operation as a list comprehension - it creates a new list by filtering the original:

```python
bright_stars = [mag for mag in magnitudes if mag < 15.0]
print(f"Bright stars: {bright_stars}")
```

Read it as: "Give me mag for each mag in magnitudes, but only if mag is less than 15.0"

You can also transform values:

```python
# Apply extinction correction (0.3 magnitudes)
corrected = [mag - 0.3 for mag in magnitudes]
print(f"Corrected magnitudes: {corrected}")
```

Extinction is the dimming of starlight by Earth's atmosphere. We subtract a correction factor to get the true brightness above the atmosphere.

## Understanding Truthy and Falsy Values

Python has a concept of "truthiness" - values that act as True or False in conditions. This is important for writing clean, Pythonic code:

```python
# Empty collections are "falsy"
observations = []

if observations:  # Empty list evaluates as False
    print("Processing observations")
else:
    print("No observations to process")
```

This is cleaner than checking `len(observations) > 0`. Common falsy values:

```python
# All of these are falsy
empty_list = []
empty_string = ""
zero = 0
none_value = None

# Check if data exists
data = None
if not data:
    print("No data loaded yet")
```

Non-empty collections, non-zero numbers, and non-empty strings are truthy:

```python
measurements = [15.3]  # Has one element

if measurements:  # Truthy - list has content
    print(f"Processing {len(measurements)} measurements")
```

## Exception Handling

### Understanding Exceptions

Real-world programs encounter problems: users enter invalid data, calculations produce impossible results, or we try to access data that doesn't exist. When Python encounters an error it can't handle, it "raises an exception" - essentially saying "I don't know what to do!"

Without exception handling, your program crashes:

```python
# # This will crash if user enters text instead of a number
# user_input = "bright"
# magnitude = float(user_input)  # Raises ValueError
```

### Try and Except Blocks

Exception handling lets your program recover gracefully from errors instead of crashing. The `try/except` structure acts as a safety net:

```python
user_input = "15.3"  # Valid number string

try:
    magnitude = float(user_input)
    print(f"Magnitude: {magnitude}")
except:
    print(f"'{user_input}' is not a valid number")
    magnitude = None
```

Think of `try/except` as "try to do this, but if it fails, do this instead." The `try` block contains code that might fail. If an exception occurs, Python jumps to the matching `except` block.

When the conversion fails, the except block takes over:

```python
user_input = "bright"  # Not a number!

try:
    magnitude = float(user_input)  # This raises ValueError
    print(f"Success!")  # Never reached!
except:
    print(f"'{user_input}' is not a valid number")
    # Program continues instead of crashing
```

### Catching Specific Exception Types
 
In the basic `try/except` examples above, we used a bare `except:` clause that catches any error. However, it's often better to catch specific exception types because different errors may need different handling:


```python
try:
    magnitude = float(user_input)
except ValueError:
    print("That's not a valid number!")

```

Different problems raise different exceptions. Each type tells you what went wrong:

- **ValueError** - Invalid conversion
  ```python
  float("abc")  # Can't convert text to number
  ```

- **TypeError** - Wrong type operation  
  ```python
  "5" + 10  # Can't add string and number
  ```

- **IndexError** - List index out of range
  ```python
  data = [1, 2, 3]
  data[10]  # No item at position 10
  ```

- **KeyError** - Dictionary key doesn't exist
  ```python
  star = {"name": "Vega"}
  star["distance"]  # Key not found
  ```

- **ZeroDivisionError** - Division by zero
  ```python
  result = 10 / 0  # Mathematical impossibility
  ```

- **NameError** - Using undefined variable
  ```python
  print(unknown_variable)  # Variable doesn't exist
  ```

- **AttributeError** - Calling non-existent method
  ```python
  my_list = [1, 2, 3]
  my_list.uppercase()  # Lists don't have this method
  ```

Different errors often require different responses. You can catch multiple exception types:

```python
data = [10, 20, 30]
index = 2
divisor = 0

try:
    result = data[index] / divisor
except IndexError:
    print("Index out of range - check your data size")
    result = None
except ZeroDivisionError:
    print("Cannot divide by zero - check your calculation")
    result = float('inf')  # Or handle it another way
```

Python checks exceptions in order - the first matching handler runs. This lets you provide specific responses to different problems.

You can also catch multiple exceptions with the same handler:

```python
try:
    # Some risky operation that could raise ValueError or TypeError
    magnitude = float("15.abc")  # This will raise ValueError
    result = "star" + magnitude   # This would raise TypeError if magnitude was a number
except (ValueError, TypeError):
    print("Invalid data type for calculation")
    result = None
```

### The Finally Block

The `finally` block always runs, whether an exception occurred or not. It's perfect for cleanup tasks:

```python
try:
    # Simulate processing observation data
    raw_data = "15.2,invalid,15.8"  # Some data with an invalid value
    data = [float(x) for x in raw_data.split(',')]  # This will raise ValueError on "invalid"
    result = sum(data) / len(data)  # Calculate average magnitude
    print(f"Average magnitude: {result:.2f}")
except ValueError:
    print("Invalid data encountered")
    result = None
finally:
    print("Analysis complete - cleaning up resources")
    # This runs regardless of success or failure
```

The finally block ensures important cleanup always happens, even if an error occurs.

### Using Assertions

Assertions are like safety checks - they verify your assumptions are true:

```python
altitude_deg = 45.0

# Check data validity
assert altitude_deg >= 0, "Altitude cannot be negative"
assert altitude_deg <= 90, "Altitude cannot exceed 90°"

print(f"Valid altitude: {altitude_deg}°")
```

Test with invalid data to see the assertion error:

```python
# This will stop the program with an error message
altitude_deg = -10.0
# assert altitude_deg >= 0, "Altitude cannot be negative"
# AssertionError: Altitude cannot be negative
```

Assertions catch bugs early, before they cause confusing problems later.

## File Input/Output

### Understanding File Operations

Files are how we save data permanently. Without files, all our calculations disappear when the program ends. In astronomy, we constantly read observation files and write analysis results.

The `with` statement is Python's recommended way to work with files. It automatically handles opening and closing files, even if errors occur:

```python
# Create some observation data
times = [20.0, 20.5, 21.0]  # Hours in UT
magnitudes = [15.32, 15.28, 15.35]  # Brightness measurements
```

### Writing to Text Files

Save data to a file using different modes:
- `'w'` - Write mode (creates new file or overwrites existing)
- `'r'` - Read mode (default, file must exist)
- `'a'` - Append mode (adds to end of existing file)

```python
filename = "photometry.txt"

with open(filename, 'w') as f:  # 'w' creates/overwrites file
    # Write header comments
    f.write("# Photometry Data\n")
    f.write("# Time(UT)  Magnitude\n")
    
    # Write each observation
    for i in range(len(times)):
        f.write(f"{times[i]:5.1f}  {magnitudes[i]:7.3f}\n")

print(f"Saved {len(times)} observations to {filename}")
```

The `with` statement creates a context - when the indented block ends, Python automatically closes the file, even if an error occurs. This prevents file corruption and resource leaks. The `\n` creates a new line - like pressing Enter.

### Reading from Text Files

Read data back from files:

```python
filename = "photometry.txt"

with open(filename, 'r') as f:  # 'r' means read mode
    lines = f.readlines()
    
print(f"Read {len(lines)} lines from file")
```

The `readlines()` method returns a list where each element is one line from the file.

Process the lines to extract data:

```python
times_read = []
mags_read = []

for line in lines:
    # Skip comments (lines starting with #)
    if line.startswith('#'):
        continue
    
    # Split line into words (we learned this in Lecture 2)
    parts = line.split()
    if len(parts) >= 2:
        times_read.append(float(parts[0]))
        mags_read.append(float(parts[1]))

print(f"Extracted {len(times_read)} measurements")
```

Remember from Lecture 2: the `split()` method breaks a string into a list of words, splitting at spaces by default.

### Appending to Files

Sometimes you want to add to existing files rather than overwriting:

```python
log_file = "observation_log.txt"

# Create initial log
with open(log_file, 'w') as f:
    f.write("Observation Log\n")
    f.write("===============\n")
```

Add entries using append mode:

```python
with open(log_file, 'a') as f:  # 'a' means append
    f.write("21:00 - Started observations\n")
```

```python
with open(log_file, 'a') as f:
    f.write("21:15 - Changed to V filter\n")
```

Each append adds to the end without erasing existing content.

### Working with CSV Files

CSV stands for "Comma-Separated Values" - a simple format where data is organized in rows and columns, with commas between values. It's like a simplified spreadsheet that any program can read.

```python
import csv

# Sample star data
star_data = [
    ['HD 209458', '330.795', '18.884', '7.65'],
    ['HD 189733', '300.178', '22.711', '7.67'],
]
```

"HD" stands for Henry Draper catalog - a list of over 200,000 stars with measured spectra.

Write CSV file:

```python
with open('stars.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write header row
    writer.writerow(['Name', 'RA', 'Dec', 'Magnitude'])
    
    # Write data rows
    for star in star_data:
        writer.writerow(star)

print("Created stars.csv")
```

Read CSV file back:

```python
with open('stars.csv', 'r') as f:
    reader = csv.reader(f)
    
    # Read and skip header
    header = next(reader)
    print(f"Columns: {header}")
    
    # Read data rows
    for row in reader:
        print(f"Star: {row[0]}, RA: {row[1]}°")
```

### Working with JSON Files

JSON stands for "JavaScript Object Notation" but don't let the name fool you - it's used by all programming languages. JSON stores structured data in a human-readable format using dictionaries and lists (which we learned in Lecture 2). 
 
#### Why JSON Matters
 
JSON has become the standard format for web APIs and data exchange, serving as the universal language of the internet. When you work with AI and Large Language Model APIs like GPT, Claude, and other AI services, you'll be communicating through JSON. It's also the go-to choice for configuration files that store settings for software and tools, and modern observatories rely on JSON for telescope control systems, commands, and logs. Perhaps most importantly, JSON enables seamless cross-platform data sharing, working equally well with Python, JavaScript, Java, and virtually every other programming language.
 
The key advantage of JSON is that it's both human-readable and machine-parseable, making it perfect for both debugging and automation.

```python
import json

# Create configuration dictionary (recall dictionaries from Lecture 2)
config = {
    'telescope': 'AAT',  # Anglo-Australian Telescope
    'date': '2024-03-15',
    'filters': ['g', 'r', 'i']  # Different color filters
}
```

Write JSON file:

The indent parameter makes the JSON human-readable by adding spaces and line breaks

```python
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)  # indent makes it readable
    
print("Saved configuration")
```

Read JSON file:

```python
with open('config.json', 'r') as f:
    loaded_config = json.load(f)
    
print(f"Telescope: {loaded_config['telescope']}")
print(f"Filters: {loaded_config['filters']}")
```

JSON preserves data types - lists stay lists, numbers stay numbers. Text files turn everything into strings. This makes JSON ideal for complex data structures and API communication.

### File Path Handling

Different operating systems use different path formats. Windows uses backslashes `\`, while Mac and Linux use forward slashes `/`. The `os` module handles these differences.

```python
import os

# Get current working directory
current_dir = os.getcwd()  # getcwd = "get current working directory"
print(f"Working in: {current_dir}")
```

The `os.path` submodule provides tools for working with file paths:

```python
# Check if files exist
if os.path.exists('photometry.txt'):
    print("Photometry file found")
    
    # Get file size
    size = os.path.getsize('photometry.txt')
    print(f"File size: {size} bytes")
```

Create directories safely:

```python
if not os.path.exists('data'):
    os.makedirs('data')  # Creates directory
    print("Created data directory")
```

Build file paths that work on any system:

```python
data_dir = 'data'
filename = 'observation.txt'
full_path = os.path.join(data_dir, filename)
print(f"Full path: {full_path}")
```

`os.path.join()` uses the correct separator (`/` or `\`) for your operating system.

### Listing Directory Contents

Process multiple files in a directory:

```python
import os

# List all files in current directory
files = os.listdir('.')  # '.' means current directory
print(f"Found {len(files)} files")

# Filter for specific file types
data_files = []
for filename in files:
    if filename.endswith('.txt'):
        data_files.append(filename)
        
print(f"Found {len(data_files)} text files")
```

The `glob` module provides more powerful pattern matching:

```python
import glob

# Find all CSV files
csv_files = glob.glob('*.csv')
print(f"CSV files: {csv_files}")

# Find photometry files with pattern
phot_files = glob.glob('*_phot_*.txt')
for filename in phot_files:
    print(f"Processing {filename}")
```

The `*` acts as a wildcard, matching any characters.

## Practical Example: Building an Observing List

Let's combine everything to build a practical tool for planning telescope observations.

### Step 1: Create Our Target Catalog

```python
# List of astronomical objects to observe
target_names = ['M31', 'M42', 'M13', 'Ring Nebula', 'Vega']
target_ra = [0.712, 5.588, 16.695, 18.893, 18.616]  # Hours
target_dec = [41.27, -5.39, 36.46, 33.03, 38.78]   # Degrees
target_mag = [3.4, 4.0, 5.8, 8.8, 0.0]              # Magnitude
```

"M" numbers refer to the Messier catalog - a list of bright nebulae, galaxies, and star clusters visible with small telescopes, compiled by Charles Messier in the 1700s.

### Step 2: Set Observatory Location and Time

```python
# Observatory location
obs_latitude = 40.0    # degrees North
obs_longitude = -110.0 # degrees East (negative = West)

# Current time
ut_hour = 3.0  # 3:00 AM Universal Time
```

Calculate Local Sidereal Time - this tells us which right ascension is currently overhead:

```python
# Simplified LST calculation
lst = (ut_hour + obs_longitude / 15.0) % 24
print(f"Local Sidereal Time: {lst:.1f} hours")
```

The sky rotates 360° in 24 hours, so 15° per hour. LST tells us which part of the sky is visible now.

### Step 3: Check Each Target's Visibility

```python
import math

observable_targets = []
min_altitude = 30.0  # Degrees above horizon

print("\nChecking visibility:")
print("-" * 40)
```

Process each target:

```python
for i in range(len(target_names)):
    # Calculate hour angle (how far from meridian)
    ha = lst - target_ra[i]
    
    # Keep hour angle between -12 and +12
    if ha < -12:
        ha += 24
    elif ha > 12:
        ha -= 24
    
    # Convert to radians for trigonometry
    ha_rad = math.radians(ha * 15)  # Hours to degrees to radians
    dec_rad = math.radians(target_dec[i])
    lat_rad = math.radians(obs_latitude)
    
    # Calculate altitude using spherical trigonometry
    sin_alt = (math.sin(dec_rad) * math.sin(lat_rad) + 
               math.cos(dec_rad) * math.cos(lat_rad) * math.cos(ha_rad))
    alt_rad = math.asin(sin_alt)
    altitude = math.degrees(alt_rad)
    
    # Check if high enough to observe
    if altitude > min_altitude:
        observable_targets.append(i)
        print(f"✓ {target_names[i]}: {altitude:.1f}° - Observable")
    else:
        print(f"✗ {target_names[i]}: {altitude:.1f}° - Too low")
```

Objects below 30° altitude suffer from atmospheric extinction and turbulence, making good observations difficult.

### Step 4: Create and Save the Observing List

```python
filename = f"observing_list_{ut_hour:.0f}UT.txt"

with open(filename, 'w') as f:
    f.write("="*50 + "\n")
    f.write("OBSERVING LIST\n")
    f.write(f"Time: {ut_hour:.1f} UT (LST: {lst:.1f}h)\n")
    f.write(f"Location: {obs_latitude}°N, {obs_longitude}°E\n")
    f.write("="*50 + "\n\n")
    
    if len(observable_targets) > 0:
        f.write("Observable Targets:\n")
        f.write("-"*30 + "\n")
        
        for idx in observable_targets:
            f.write(f"{target_names[idx]:<15} mag {target_mag[idx]:4.1f}\n")
    else:
        f.write("No targets observable at this time\n")

print(f"\nSaved observing list to {filename}")
```

The `<15` format means "left-align in a field 15 characters wide" - this creates neat columns.

## Summary

In this lecture, we have gone through the essential control structures and file operations for astronomical data processing:

### Control Flow
- **if/elif/else** - Making intelligent decisions based on data
- **Logical operators** - Combining conditions with and/or/not
- **in operator** - Testing membership in collections
- **Ternary operator** - Concise conditional assignments

### Loops for Data Processing
- **for loops** - Processing collections of data
- **range()** - Generating number sequences
- **enumerate()** - Getting both indices and values
- **zip()** - Pairing elements from multiple lists
- **while loops** - Repeating until a condition is met
- **break/continue** - Fine control over loop execution
- **List comprehensions** - Concise data transformations

### Robust Error Handling
- **try/except** - Gracefully handling errors without crashing
- **Multiple exceptions** - Different responses for different problems
- **finally blocks** - Ensuring cleanup always happens
- **Assertions** - Verifying assumptions

### File Operations
- **Text files** - Reading and writing observational data
- **CSV files** - Working with tabular data
- **JSON files** - Storing structured configurations and API communication
- **File paths** - Cross-platform file handling with os module
- **Directory operations** - Listing and processing multiple files
- **glob patterns** - Finding files with wildcards

These skills enable you to write programs that process real astronomical data, handle problems gracefully, and produce results other astronomers can use. The control structures orchestrate your analysis flow, while file operations connect your code to the vast world of astronomical data.
