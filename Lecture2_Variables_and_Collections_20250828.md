# Variables and Collections

*Tutorial by Yuan-Sen Ting*

*Astron 1221: Lecture 2*

## Introduction

In astronomy, we deal with diverse data types: brightness measurements from millions of stars, time series of variable objects, spectra with thousands of wavelength points, and catalogs with complex metadata. Python provides the foundation for handling all of this efficiently.

This tutorial covers essential Python concepts you'll use throughout your astronomical career. We'll focus on the basic building blocks: storing data, working with numbers, organizing information, and understanding how Python manages memory. By the end of this lecture, you'll understand the fundamental data types and operations that form the foundation of all astronomical computing.

## Your First Variables

### Creating Variables

Variables are like labeled containers for storing data. Think of them as boxes with names written on them. The `=` sign means "store this value" - it's not about mathematical equality, but about assignment:

```python
star_name = "Sirius"
magnitude = -1.46
distance_parsecs = 2.64
```

Each line creates a container (variable) and puts a value inside it. The variable name goes on the left, the value on the right. Once stored, we can use these values by referring to their names.

### How Python Knows the Type

Python automatically determines what type of data you're storing. You don't need to tell Python "this is a number" or "this is text" - it figures it out from the value itself:

```python
star_count = 1000        # Integer (whole number)
temperature = 5778.5     # Float (decimal number)  
star_name = "Betelgeuse" # String (text)
```

This automatic type detection makes Python very convenient for scientific computing. No need to declare types in advance - Python is smart enough to understand what you're giving it.

### Variable Names in Astronomy

Choosing good variable names is crucial in scientific computing. Your code should tell a story that other astronomers (including future you) can understand. Here's how to choose good names:

```python
# Good astronomical variable names - self-explanatory
right_ascension = 150.5  # degrees - celestial longitude
declination = -30.2      # degrees - celestial latitude
apparent_magnitude = 15.3  # brightness as seen from Earth
absolute_magnitude = -21.5  # intrinsic brightness
redshift = 0.05  # measure of distance for galaxies
```

Compare this to unclear names that require you to remember what they mean:

```python
# Bad - unclear what these represent
r = 150.5
d = -30.2
m = 15.3
```

The descriptive names immediately tell you what each number represents. When you're analyzing data from thousands of stars, this clarity becomes essential.

Some naming guidelines for astronomy:
- Use full words rather than abbreviations: `parallax` not `plx`
- Include units in comments: `distance_parsecs = 50.2  # parsecs`
- Be specific: `v_band_magnitude` not just `magnitude`
- Use underscores to separate words: `proper_motion_ra` not `propermotionra`


### Constants and Naming Conventions

Constants are values that never change during your program. In astronomy, these are often physical constants or survey parameters. The Python convention is to use ALL_CAPITAL_LETTERS for constants:

```python
# Physical constants used in astronomy
SPEED_OF_LIGHT = 299792458    # m/s
SOLAR_MASS = 1.989e30         # kg
PARSEC_TO_METERS = 3.086e16   # meters per parsec
HUBBLE_CONSTANT = 70.0        # km/s/Mpc
```

By using capital letters, you immediately know these values shouldn't change. This helps prevent bugs where you accidentally modify an important constant.

## Working with Numbers

### Basic Operations and Power

Python handles mathematical operations with familiar symbols, plus one special operator for exponentiation:

```python
distance = 50.0 * 3.26  # Parsecs to light-years
flux = 10 ** (-0.4 * magnitude)  # The ** means exponentiation
```

The double asterisk `**` is Python's way of writing powers. So `10**2` equals 100, and `2**3` equals 8. This is essential for astronomical calculations where we often work with powers of 10.

### Operator Precedence and Parentheses

Python follows standard mathematical order of operations, but in complex astronomical formulas, always use parentheses to make your intent clear:

```python
magnitude = 15.0
extinction = 0.3  # Light absorption by interstellar dust
distance_modulus = 5.0  # Related to distance

# Without parentheses - follows standard order
result1 = magnitude - extinction + distance_modulus
print(f"Without parentheses: {result1}")  # 19.7

# With parentheses to change order
result2 = magnitude - (extinction + distance_modulus)
print(f"With parentheses: {result2}")  # 9.7

# Complex formula with clear parentheses
flux = 10**(-0.4 * (magnitude - extinction))
```

Parentheses make your calculations explicit and prevent order-of-operations errors.

### Import math for Advanced Functions

Basic Python can add, subtract, multiply, and divide. For more advanced math, we need to import the `math` module - think of it as opening a more sophisticated calculator:

```python
import math
math.sqrt(16)          # 4.0
math.log10(100)        # 2.0 (useful for magnitude calculations)
math.radians(45)       # Convert degrees to radians
```

The word `import` loads a toolbox of pre-written functions. The `math.` prefix tells Python to use a function from that toolbox. Python keeps basic operations simple and lets you add complexity only when needed.

### Mathematical Functions

The `math` module provides functions for common astronomical calculations. Let's explore the most useful ones:

```python
distance = 50.0
angle_deg = 45.0

# Square roots - essential for distance calculations and error propagation
print(f"Square root: {math.sqrt(distance)}")

# Logarithms - crucial for magnitude calculations
print(f"Natural log: {math.log(distance)}")
print(f"Log base 10: {math.log10(distance)}")

# Other useful functions
print(f"Absolute value: {abs(-25.7)}")

# Rounding for output
print(f"Rounded: {round(15.3456, 2)}")  # 2 decimal places

# Trigonometry - angles must be in radians
angle_rad = math.radians(angle_deg)
print(f"Sine: {math.sin(angle_rad):.3f}")
print(f"Cosine: {math.cos(angle_rad):.3f}")
```

The `math.radians()` function converts degrees to radians, essential since Python's trig functions expect radians.

## Importing Modules

### Modules are Toolboxes

Modules are collections of pre-written code that add functionality to Python. Think of them as specialized toolboxes - you wouldn't carry every tool you own everywhere, just the ones you need for the job:

```python
import math    # Mathematical functions
import sys     # System functions
```

Once imported, you access functions using dot notation:

```python
math.sqrt(16)  # Use sqrt from the math module
math.pi        # Constants are available too!
```

Python starts minimal - you add capabilities as needed by importing modules. This keeps programs efficient and clear about what tools they're using.

## Special Values: None, NaN, inf

### Real Data Has Missing Values

Perfect data doesn't exist in astronomy. Detectors fail, weather interrupts observations, and some measurements are simply impossible. Python provides special values to handle these realities:

```python
redshift = None           # Not measured yet
bad_mag = float('nan')    # Failed measurement (Not a Number)
saturated = float('inf')  # Detector overflow (infinity)
negative_inf = float('-inf')  # Negative infinity
```

Display these values to see how they look:

```python
print(f"Good: {15.3}")
print(f"Missing: {bad_mag}")
print(f"Saturated: {saturated}")
```

### Testing for Special Values

You can't test for NaN using `==` because NaN is defined to not equal anything, even itself! Use special functions instead:

```python
good_magnitude = 15.3
missing_magnitude = float('nan')
saturated = float('inf')

print(f"Is good_magnitude NaN? {math.isnan(good_magnitude)}")  # False
print(f"Is missing_magnitude NaN? {math.isnan(missing_magnitude)}")  # True
print(f"Is saturated infinite? {math.isinf(saturated)}")  # True
```

These special values help track data quality issues throughout your analysis pipeline.

### Working with None

`None` is Python's way of representing "nothing" or "missing data". It's different from NaN because None can represent any type of missing information:

```python
# Some measurements might not exist
redshift = None
proper_motion = None  # Star's motion across the sky
parallax = 5.2  # This one was measured

print(f"Redshift: {redshift}")
print(f"Proper motion: {proper_motion}")
print(f"Parallax: {parallax}")

# Check for None using 'is'
print(f"Redshift is None: {redshift is None}")  # True
print(f"Parallax is None: {parallax is None}")  # False
```

Use `is None` rather than `== None` - it's more reliable and considered better Python style.

## Strings: Text Data

### Storing Text

Strings are sequences of characters enclosed in quotes. They're perfect for storing names, IDs, and any text information:

```python
star_name = "Alpha Centauri"
catalog_id = "HD 128620"
notes = "Closest star system"
```

Strings are fundamental because much of our astronomical metadata is text: object names, filter bands, telescope configurations, and observation notes.

### String Properties

Check string length and type:

```python
star_name = "Alpha Centauri"
print(f"Length: {len(star_name)} characters")  # 14 characters
print(f"Type: {type(star_name)}")  # <class 'str'>
```

The `len()` function tells us how many characters are in the string. This is our first encounter with `len()` - it works on any collection of items.

### Common String Mistake

Here's a critical distinction that trips up many beginners. These look similar but are completely different:

```python
magnitude_num = 15.3   # This is a number
magnitude_str = "15.3" # This is text!

# You can do math with the number:
magnitude_num + 5      # Works: gives 20.3

# But not with the string:
# magnitude_str + 5    # Error! Can't add text and number

# String multiplication repeats the string!
distance = "50"
result = distance * 3  # "505050" NOT 150!
```

The quotes make all the difference. With quotes, Python sees text. Without quotes, Python sees a number.

## Type Checking and Conversion

### Finding Out the Type

When unsure about data types, ask Python directly using `type()`:

```python
type(15.3)     # <class 'float'>
type("15.3")   # <class 'str'>
type(15)       # <class 'int'>
```

This is especially useful when debugging - many errors come from unexpected data types.

### Converting Between Types

Data often arrives in the wrong format, especially when reading from files. Python provides conversion functions:

```python
# String to number
magnitude_str = "15.3"
magnitude_num = float(magnitude_str)  # Now it's 15.3 as a number

# Number to string
result = 15.3
result_str = str(result)  # Now it's "15.3" as text

# String to integer
count_str = "1000"
count_int = int(count_str)  # Now it's 1000 as an integer

# Integer conversion truncates decimals
int(15.9)  # 15 - decimal part removed!
```

Data read from files usually comes as strings, so conversion is essential before calculations.

## The Print Function

### Displaying Results

The `print()` function is your window into what Python is doing. It displays values on screen:

```python
star_name = "Sirius"
print(star_name)  # Shows: Sirius

magnitude = -1.46
print(star_name, magnitude)  # Shows: Sirius -1.46
```

Using commas in print automatically adds spaces between items. But for complex output, we need something better...

## F-strings: Formatted Output

### Building Readable Output

F-strings let you embed variables directly in text. Put an `f` before the quotes and wrap variables in curly braces:

```python
star_name = "Betelgeuse"
magnitude = 0.42

print(f"The star {star_name} has magnitude {magnitude}")
# Output: The star Betelgeuse has magnitude 0.42
```

The `f` tells Python to look inside the string for `{}` and substitute variables. This creates much more readable output than trying to combine strings and numbers manually.

## Formatting Numbers in F-strings

### Controlling Decimal Places

Real measurements have limited precision. F-strings let you control how numbers display:

```python
distance = 47.3821

# Two decimal places
print(f"Distance: {distance:.2f} pc")
# Output: Distance: 47.38 pc

# Scientific notation
flux = 0.000000123
print(f"Flux: {flux:.2e}")
# Output: Flux: 1.23e-07

# Field width for tables
print(f"Padded: {magnitude:8.3f}")  # 8 characters wide, 3 decimals
```

After the colon comes the format specification (with rounding):
- `.2f` means "floating point with 2 decimal places"
- `.2e` means "scientific notation with 2 decimal places"
- `8.3f` means "8 characters wide with 3 decimals"

This is essential for creating professional-looking output and data tables.


## Python's Indexing System

### Counting from Zero

Python counts positions starting from 0, not 1. This might seem odd, but it's consistent and has mathematical advantages:

```python
# Position:  0    1    2    3    4
# Element:  1st  2nd  3rd  4th  5th
```

Think of positions as offsets from the beginning. The first element is at offset 0 (the very start), the second is at offset 1, and so on.

### Negative Indices

Python also lets you count backwards from the end using negative numbers:

```python
# Positive:   0    1    2    3    4
# Element:   1st  2nd  3rd  4th  5th
# Negative:  -5   -4   -3   -2   -1
```

So `-1` always means "last element", `-2` means "second to last", and so on. This is incredibly useful when you don't know how long a sequence is but need the last few elements.

## Indexing Strings

### Accessing Individual Characters

Apply indexing to extract specific characters from strings:

```python
star = "Sirius"
star[0]   # 'S' - first character
star[1]   # 'i' - second character
star[-1]  # 's' - last character
star[-2]  # 'u' - second to last
```

Each character has a position, and you access it using square brackets with the index.

### String Slicing

Extract portions of strings using slice notation `[start:stop]`:

```python
catalog = "HD209458"
catalog[:2]   # 'HD' - first 2 chars
catalog[2:]   # '209458' - from position 2 onward
catalog[2:5]  # '209' - positions 2, 3, 4
```

Key insight: `[start:stop]` goes from `start` up to but NOT including `stop`. This seems strange but makes the math work out nicely: the number of characters extracted is always `stop - start`.

## String Methods

### Length and Cleaning

Find string length and remove unwanted whitespace:

```python
messy = "  VEGA  "
len(messy)         # 8 (includes the spaces!)
clean = messy.strip()  # "VEGA" (spaces removed)
len(clean)         # 4
```

The `strip()` method removes spaces, tabs, and newlines from both ends only - it does NOT remove spaces between words. This is essential when processing data files where extra spaces often creep in.

### Case Conversion and Replacement

Standardize string formats for consistency:

```python
name = "Alpha Centauri"
name.lower()           # "alpha centauri"
name.upper()           # "ALPHA CENTAURI"
name.replace(" ", "_") # "Alpha_Centauri"
```

These methods don't change the original string - they create new ones. This is because strings are immutable (unchangeable). Since `strip()` only removes spaces from the beginning and end. To remove ALL spaces (including those between words), use `replace(' ', '')`.

### String Split and Join

The `split()` method breaks strings at specified characters:

```python
coordinates = "10:23:45.6"
parts = coordinates.split(':')
print(parts)  # ['10', '23', '45.6']
```

The opposite is `join()` - it combines list elements into a string:

```python
values = ['15.3', '14.8', '15.1']
csv_line = ','.join(values)
print(csv_line)  # "15.3,14.8,15.1"
```

These are essential for parsing and creating data files.

### String Testing Methods

Check string properties to validate data:

```python
target = "NGC1234"  # NGC = New General Catalogue
coords = "10:23:45.6"

# Test beginning and end
target.startswith('NGC')  # True
target.endswith('34')     # True

# Test character types
target.isupper()          # False (has numbers too)
target.isdigit()          # False (has letters too)
"1234".isdigit()         # True (all digits)

# Check for substring
':' in coords            # True
```

These return boolean values for filtering and validation.

### Building Filenames and IDs

Combine strings to create standardized names:

```python
# Using f-strings for complex names
object_id = "HD"
number = "209458"
full_name = f"{object_id}{number}"
print(full_name)  # "HD209458"

# Create observation filenames
observation_date = "2024-03-15"
target = "M31"  # Andromeda Galaxy
filter_name = "V"  # Visual band

filename = f"{target}_{observation_date}_{filter_name}.fits"
print(filename)  # "M31_2024-03-15_V.fits"
```

Systematic naming ensures your files are organized and easily identified.

## Booleans

### Why Booleans Matter

So far we've stored numbers and text. But astronomy is full of yes/no questions:
- Is this star bright enough to observe?
- Does this measurement look valid?
- Is this object in the northern sky?

Booleans store these `True`/`False` decisions, and they're essential for filtering and analyzing data.

## Boolean Values: True and False

### Defining Booleans

Create boolean variables using `True` and `False` (note the capital letters!):

```python
is_bright = True
is_variable = False  
has_companion = True
```

These values help track binary properties of astronomical objects - characteristics that are either present or absent.

## Creating Booleans with Comparisons

### Comparison Operators

Most booleans come from comparing values:

```python
magnitude = 15.3

# Test different conditions
magnitude < 10     # False - not brighter than 10
magnitude > 20     # False - not fainter than 20
magnitude == 15.3  # True - exactly 15.3
```

### Critical Distinction: = vs ==

This confuses many beginners:
- Single `=` means "store this value" (assignment)
- Double `==` means "are these equal?" (comparison)

```python
magnitude = 15.3   # ASSIGNS 15.3 to magnitude
magnitude == 15.3  # TESTS if magnitude equals 15.3
```

Mixing these up is a common source of bugs!

## Logical Operators: and, or, not

### Combining Conditions

Real astronomical queries often involve multiple criteria:

```python
magnitude = 11.5
declination = 30.2  # Positive = northern sky

# BOTH must be true (and)
northern_and_bright = (declination > 0) and (magnitude < 12)
print(northern_and_bright)  # True

# AT LEAST ONE must be true (or)
interesting = (magnitude < 5) or (declination > 80)
print(interesting)  # False

# Flip the result (not)
not_too_faint = not (magnitude > 15)
print(not_too_faint)  # True
```

These operators let you build complex selection criteria from simple comparisons.

## Bitwise Operators: & and |

### Similar but Different

Bitwise operators look similar to `and`/`or` but have crucial differences:

```python
# Requires parentheses around comparisons!
bright = (magnitude < 12) & (declination > 0)
special = (magnitude < 5) | (declination > 80)
```

Why learn both? When you work with NumPy arrays later, only `&` and `|` work element-wise. The parentheses are essential because `&` and `|` have different precedence than comparisons.

## Lists: Storing Multiple Values

### Creating Lists

In astronomy, we rarely work with single numbers. Lists store sequences of related values:

```python
magnitudes = [15.2, 15.3, 15.1, 15.4, 15.2]
star_names = ["Sirius", "Vega", "Betelgeuse"]
```

Square brackets `[]` create lists. Items are separated by commas. Lists can hold any type of data, even mixed types.

### Accessing List Elements

Lists use the same zero-based indexing we learned:

```python
print(magnitudes[0])   # 15.2 - first observation
print(magnitudes[-1])  # 15.2 - last observation
print(magnitudes[2])   # 15.1 - third observation
```

Think of the index as telling Python how many positions to count from the start (or from the end if negative).

## Lists are Mutable (Changeable)

### Modifying Existing Elements

Unlike strings, you can change list contents after creation:

```python
observations = [15.2, 15.3, 15.1]
print(f"Original: {observations}")

observations[0] = 15.0  # Change first element
print(f"After change: {observations}")
```

This mutability makes lists perfect for accumulating data during observations or processing.

### Adding Elements

Grow lists dynamically as new data arrives:

```python
observations.append(15.4)  # Add to the end
print(f"After append: {observations}")
```

The `append()` method is how you build up lists one element at a time - essential for reading data files line by line.

## List Methods

### Insertion and Removal

Control exactly where elements go and which ones to remove:

```python
mags = [15.2, 15.3, 15.1]
mags.insert(1, 15.25)  # Insert at position 1
print(mags)  # [15.2, 15.25, 15.3, 15.1]

deleted = mags.pop()   # Remove and return last element  
print(f"Deleted: {deleted}")
print(f"Remaining: {mags}")
```

The `insert()` method takes two arguments: where to insert and what to insert. The `pop()` method both removes and returns an element, letting you save it if needed.

## List Slicing and Functions

### Extracting Portions

Use slicing to analyze subsequences:

```python
mags = [10.5, 11.2, 9.8, 12.3, 10.7]
first_three = mags[:3]   # [10.5, 11.2, 9.8]
last_two = mags[-2:]     # [12.3, 10.7]
```

### Built-in Analysis Functions

Python provides essential statistical functions:

```python
len(mags)   # 5 - count elements
min(mags)   # 9.8 - brightest (smallest magnitude)
max(mags)   # 12.3 - faintest
sum(mags)   # 54.5 - total

# Calculate average
average = sum(mags) / len(mags)
```

Remember: in astronomy, smaller magnitude means brighter!

## List Search and Sort

### Finding Elements

Locate and count specific values:

```python
mags = [10.5, 11.2, 9.8, 12.3, 9.8]

mags.index(9.8)   # 2 - position of FIRST 9.8
mags.count(9.8)   # 2 - number of times 9.8 appears
mags.remove(9.8)  # Removes FIRST 9.8 only
```

### Sorting Without Destruction

The `sorted()` function creates a new sorted list, preserving the original:

```python
original = [10.5, 11.2, 9.8, 12.3, 10.7]
bright_to_faint = sorted(original)
faint_to_bright = sorted(original, reverse=True)

print(f"Original unchanged: {original}")
print(f"Sorted: {bright_to_faint}")
```

This preserves time-ordering while allowing magnitude-based analysis.

## Lists: Reference vs Copy

### The Hidden Danger

This behavior surprises many beginners. Assignment doesn't copy lists - it creates another name for the SAME list:

```python
list1 = [15.2, 15.3, 15.1]
list2 = list1  # NOT a copy - same list, different name!

list2[0] = 99.9
print(list1)  # [99.9, 15.3, 15.1] - list1 changed too!
```

Both variables point to the same list in memory. Changing one changes both!

### Creating True Copies

Use `.copy()` when you need independent lists:

```python
list1 = [15.2, 15.3, 15.1]
list2 = list1.copy()  # TRUE copy

list2[0] = 99.9
print(list1)  # [15.2, 15.3, 15.1] - unchanged!
print(list2)  # [99.9, 15.3, 15.1] - only this changed
```

Always use `.copy()` when you want to modify a list without affecting the original. This prevents subtle bugs that can be hard to track down.

## Tuples: Immutable Sequences

### Creating Unchangeable Sequences

Tuples are like lists that can't be modified. Perfect for data that should stay constant:

```python
coords = (101.287, -16.716)  # RA and Dec in degrees
star_info = ("Vega", 0.03, "A0V")  # name, magnitude, spectral type
```

Parentheses create tuples (though they're sometimes optional). Once created, the contents cannot change.

### Accessing but Not Modifying

Access tuple elements just like lists:

```python
ra = coords[0]
dec = coords[1]
print(f"RA: {ra}, Dec: {dec}")

# But you cannot modify:
# coords[0] = 102.0  # TypeError! Tuples are immutable
```

Use tuples for coordinate pairs, RGB colors, or any data that represents a fixed set of related values.

## Tuple Unpacking

### Elegant Value Extraction

One of Python's most beautiful features - extract all tuple values at once:

```python
ra, dec = coords  # Unpack both values
print(f"RA: {ra}, Dec: {dec}")

# Works with any number of elements
name, magnitude, spectral_type = star_info
print(f"{name}: magnitude {magnitude}, type {spectral_type}")
```

This makes code more readable by giving meaningful names to each component.

### Multiple Assignment

Tuples enable assigning multiple variables in one line:

```python
# Create multiple variables at once
star_name, magnitude, distance = "Sirius", -1.46, 2.64
print(f"{star_name}: {magnitude} mag at {distance} pc")
```

This is actually creating a tuple on the right and unpacking it on the left.

### Value Swapping Magic

Tuple unpacking enables elegant variable swapping:

```python
mag1 = 15.3
mag2 = 14.8
print(f"Before: mag1={mag1}, mag2={mag2}")

mag1, mag2 = mag2, mag1  # Swap in one line!
print(f"After: mag1={mag1}, mag2={mag2}")
```

No temporary variable needed! Python creates a tuple on the right, then unpacks it on the left.

## Dictionaries: Labeled Data

### From Positions to Names

Lists store data by position, but astronomical objects have named properties. Dictionaries use descriptive keys instead of numeric positions:

```python
star = {
    "name": "Betelgeuse",
    "magnitude": 0.42,
    "type": "M1-2Ia-Ib"
}
```

Curly braces `{}` create dictionaries. Each entry pairs a key (label) with a value (data).

### Comparing Lists and Dictionaries

Consider storing information about a star:

```python
# Using a list - hard to remember what each position means
star_list = ["Betelgeuse", 88.793, 7.407, 0.42]  # name, RA, Dec, magnitude

# Using a dictionary - self-documenting
star_dict = {
    'name': 'Betelgeuse',
    'ra': 88.793,
    'dec': 7.407,
    'magnitude': 0.42
}

# Compare accessing data
print(star_list[0])      # What's at position 0 again?
print(star_dict['name'])  # Obviously the name!
```

Dictionaries make your code self-documenting.

## Dictionary Keys and Values

### Understanding Key-Value Pairs

Each dictionary entry has two parts:

```python
# "magnitude": 0.42
#    ↑         ↑
#   KEY     VALUE
```

Access values using their keys:

```python
print(star["name"])       # "Betelgeuse"
print(star["magnitude"])  # 0.42

# Modify values
star["magnitude"] = 0.45  # Betelgeuse is variable!

# Add new key-value pairs
star["distance"] = 197    # parsecs
```

Keys are like labels on filing folders - they tell you what's inside without having to remember positions.

## Safe Dictionary Access

### Handling Missing Keys

Accessing a non-existent key causes an error. Use `.get()` for safe access with a default:

```python
star = {"name": "Vega", "mag": 0.03}

# This would error:
# print(star["distance"])  # KeyError!

# Safe access with default
distance = star.get("distance", "unknown")
print(distance)  # "unknown"

# When key exists, get returns the actual value
magnitude = star.get("mag", 99)
print(magnitude)  # 0.03 (not 99)
```

The second argument to `.get()` is the default value returned if the key doesn't exist.

### Checking for Keys

Test if a key exists before using it:

```python
"mag" in star       # True - key exists
"distance" in star  # False - key doesn't exist
```

This returns a boolean you can use in if-statements (which you'll learn next lecture).

## Dictionary Methods

### Exploring Dictionary Structure

Extract and analyze dictionary components:

```python
star = {"name": "Vega", "mag": 0.03, "type": "A0V"}

list(star.keys())    # ["name", "mag", "type"]
list(star.values())  # ["Vega", 0.03, "A0V"]
list(star.items())   # [("name", "Vega"), ("mag", 0.03), ("type", "A0V")]

len(star)  # 3 - counts key-value pairs
```

These methods help you understand and process dictionary contents programmatically.

## Nested Dictionaries

### Building Complex Catalogs

Dictionaries can contain other dictionaries, perfect for star catalogs:

```python
catalog = {
    "sirius": {
        "mag": -1.46,
        "dist": 2.64,
        "type": "A1V"
    },
    "vega": {
        "mag": 0.03,
        "dist": 7.68,
        "type": "A0V"
    }
}

# Access nested data with multiple brackets
sirius_mag = catalog["sirius"]["mag"]  # -1.46
vega_dist = catalog["vega"]["dist"]    # 7.68
```

Each bracket level goes deeper into the structure. First bracket gets the star, second bracket gets the property.

### Dictionary References

Like lists, dictionaries use references:

```python
star = {"name": "Vega"}
backup = star  # Reference, not copy!
star["mag"] = 0.03
print(len(backup))  # 2 - backup changed too!
```

Use `.copy()` for dictionaries too when you need independence.

## Practical Examples

### Example 1: Complete Coordinate Conversion

Let's combine string processing, type conversion, and calculation to convert right ascension from hours:minutes:seconds to decimal degrees:

```python
ra_hms = "14:23:15.2"
print(f"Converting {ra_hms} to decimal degrees")

# Split at colons and unpack
h, m, s = ra_hms.split(':')
print(f"Components: h={h}, m={m}, s={s}")

# Convert strings to numbers
hours = float(h)
minutes = float(m)
seconds = float(s)

# Calculate decimal hours
decimal_hours = hours + minutes/60 + seconds/3600
print(f"Decimal hours: {decimal_hours:.6f}")

# Convert to degrees (Earth rotates 360° in 24 hours)
decimal_degrees = decimal_hours * 15
print(f"Result: {decimal_degrees:.4f} degrees")
```

This example integrates string methods, type conversion, arithmetic, and formatted output - all essential skills for processing astronomical data.

### Example 2: Building and Analyzing a Star Catalog

Create a multi-level data structure and extract statistics:

```python
stars = {
    'sirius': {'mag': -1.46, 'distance_pc': 2.64, 'type': 'A1V'},
    'vega': {'mag': 0.03, 'distance_pc': 7.68, 'type': 'A0V'},
    'betelgeuse': {'mag': 0.42, 'distance_pc': 197, 'type': 'M1-2Ia-Ib'}
}

# Extract all star names
star_names = list(stars.keys())
print(f"Stars in catalog: {star_names}")

# Build magnitude list
magnitudes = []
for name in star_names:
    magnitudes.append(stars[name]['mag'])
print(f"Magnitudes: {magnitudes}")

# Find brightest (minimum magnitude)
brightest_mag = min(magnitudes)
brightest_idx = magnitudes.index(brightest_mag)
brightest_star = star_names[brightest_idx]
print(f"Brightest: {brightest_star} at magnitude {brightest_mag}")

# Calculate statistics
mean_mag = sum(magnitudes) / len(magnitudes)
mag_range = max(magnitudes) - min(magnitudes)
print(f"Mean magnitude: {mean_mag:.2f}")
print(f"Magnitude range: {mag_range:.2f}")
```

This demonstrates how dictionaries, lists, and built-in functions work together to organize and analyze astronomical data.

## Summary

You've mastered the fundamental building blocks of Python for astronomy:

### Core Data Types
- **Numbers**: Integers for counts, floats for measurements
- **Strings**: Text for names, IDs, and metadata
- **Booleans**: True/False for filtering and logic
- **None**: Representing missing or undefined data

### Collections
- **Lists**: Mutable sequences for time-series and observations
- **Tuples**: Immutable sequences for coordinates and fixed data
- **Dictionaries**: Key-value pairs for labeled properties

### Key Concepts
- **Zero-based indexing**: Counting from 0, negative indices from end
- **Type conversion**: Moving between strings, numbers, and other types
- **References vs copies**: Understanding when data is shared vs independent
- **Safe access patterns**: Using `.get()` and checking for None

### Essential Operations
- **String methods**: split, strip, replace, join for text processing
- **List methods**: append, insert, pop for data management
- **Comparison operators**: Creating booleans with <, >, ==, !=
- **Logical operators**: Combining conditions with and, or, not

These fundamentals prepare you for Lecture 3, where you'll learn control structures (if/else statements and loops) and functions to automate complex astronomical analysis workflows.
