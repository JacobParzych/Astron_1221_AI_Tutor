# NumPy

*Tutorial by Yuan-Sen Ting*

*Part of Astron 1221: Astronomical Data Analysis*

## Introduction

In astronomy, we work with vast amounts of numerical data. Think about a single telescope image from a modern CCD camera - it might contain 4096×4096 pixels, giving us over 16 million brightness values to analyze. Or consider a spectroscopic survey that measures thousands of wavelength points for millions of stars. Even a "simple" star catalog might list positions, brightnesses, colors, and proper motions for billions of objects.

Python lists can store these numbers, but they have a fundamental problem: they're painfully slow when we need to perform mathematical operations on thousands or millions of values. This slowness comes from Python checking the type of each element and handling each operation individually.

NumPy (Numerical Python) solves this problem elegantly. It's a library that provides a powerful N-dimensional array object and tools for working with these arrays. NumPy arrays store data in contiguous memory and perform operations in compiled C code, making them orders of magnitude faster than Python lists.

## Getting Started

Let's import NumPy. We'll use the nickname 'np' which is the universal convention in the astronomy community - you'll see this in almost every astronomical Python script:
 
The `import numpy as np` syntax means we're importing the entire numpy library but giving it a shorter alias 'np'. This allows us to access all NumPy functions by typing `np.function_name()` instead of the longer `numpy.function_name()`. The 'np' abbreviation is so standard that it's considered the official convention - using anything else would confuse other astronomers reading your code!

```python
import numpy as np
```

We'll also import the time module to measure and demonstrate just how much faster NumPy really is:

```python
import time
```

Let's verify everything is working and check what version we have:

```python
print(f"NumPy version: {np.__version__}")
```

## Why NumPy? A Speed Comparison

To understand why NumPy is essential for astronomy, let's work through a realistic example. Imagine we have brightness measurements for 10,000 stars from a photometric survey. We want to convert these brightnesses (called magnitudes in astronomy) to another unit called flux.

A quick primer on the magnitude system: In astronomy, the magnitude scale is logarithmic and runs backwards - brighter stars have smaller magnitude numbers! A magnitude 1 star is about 100 times brighter than a magnitude 6 star (the faintest visible to the naked eye). The relationship between magnitude (m) and flux (F) is:
$F = 10^{-0.4 \times m}$

This backwards, logarithmic scale has historical roots dating back to ancient Greek astronomers, but it remains the standard in modern astronomy.

First, let's create some fake star magnitude data using a Python list:

```python
n_stars = 10000
magnitudes_list = [12.5 + i*0.001 for i in range(n_stars)]
```

Now let's convert magnitudes to fluxes the traditional Python way, using a loop:

```python
start_time = time.time()
fluxes_list = []
for mag in magnitudes_list:
    flux = 10**(-0.4 * mag)
    fluxes_list.append(flux)
list_time = time.time() - start_time
```

Let's see how long that took:

```python
print(f"Python list took: {list_time:.4f} seconds")
```

Now let's try the same calculation with NumPy. First, we convert our list to a NumPy array:

```python
magnitudes_array = np.array(magnitudes_list)
```

Now perform the calculation - notice there's no loop! NumPy operates on the entire array at once:

```python
start_time = time.time()
fluxes_array = 10**(-0.4 * magnitudes_array)
numpy_time = time.time() - start_time
```

Compare the execution times:

```python
print(f"NumPy took: {numpy_time:.4f} seconds")
print(f"NumPy is {list_time/numpy_time:.1f}x faster!")
```

NumPy is much faster for this kind of operation! This speed difference becomes crucial when processing telescope images with millions of pixels or analyzing time series data from surveys monitoring the sky continuously for years. The key insight is that NumPy performs the operation in compiled C code on contiguous memory, while Python lists require interpreted Python code with type checking at each step.

## Creating NumPy Arrays

NumPy provides many ways to create arrays, each optimized for different scenarios you'll encounter in astronomical data analysis.

### From Python Lists

The most straightforward way to create an array is from a Python list. The `np.array()` function takes a list (or list of lists) as input and returns a NumPy array:

```python
brightness_list = [100.5, 89.2, 156.7, 45.3, 78.9]
```

Convert it to a NumPy array:

```python
brightness_array = np.array(brightness_list)
```

Let's examine what we created:

```python
print("List:", brightness_list)
print("Array:", brightness_array)
```

They look similar when printed, but they're fundamentally different objects in memory:

```python
print("List type:", type(brightness_list))
print("Array type:", type(brightness_array))
```

The list stores references to Python objects scattered in memory, while the array stores raw numbers in a contiguous block - this is why arrays are so much faster.

### Creating Arrays of Zeros

When processing telescope images, we often need to start with an empty frame to accumulate data - for example, when co-adding multiple exposures or creating master calibration frames. The `np.zeros()` function creates an array filled with zeros:

```python
empty_data = np.zeros(5)
```

This creates a 1D array with 5 zeros:

```python
print(empty_data)
```

For 2D arrays (like images), pass a tuple specifying (rows, columns). Let's create a small mock CCD frame. A CCD (Charge-Coupled Device) is the electronic sensor in astronomical cameras that converts photons from stars into digital numbers:

```python
small_image = np.zeros((3, 4))  # 3 rows, 4 columns
```

```python
print("3x4 CCD frame:")
print(small_image)
```

Note the double parentheses - we're passing a single tuple argument (3, 4), not two separate arguments.

### Creating Arrays of Ones

The `np.ones()` function works identically to `np.zeros()` but fills the array with ones. This is particularly useful for creating weight arrays when combining multiple observations - for instance, when all observations have equal quality:

```python
weights = np.ones(5)
print(weights)
```

### Arrays with Specific Values

The `np.full()` function creates an array filled with a specific value you choose. It takes two arguments: the size (or shape) and the fill value.

For example, CCD detectors have a "bias level" - a constant electronic offset added to all pixel values to ensure the analog-to-digital converter never receives negative values:

```python
bias_level = np.full(5, 1000.0)
```

This creates 5 elements, all with value 1000.0:

```python
print("Bias level array:", bias_level)
```

### Creating Sequences of Numbers

NumPy's `np.arange()` function is like Python's `range()`, but creates an array directly. It's perfect for creating pixel indices or time stamps:

```python
pixel_numbers = np.arange(5) 
```

or equivalently,

```python
pixel_numbers = np.arange(0, 5)  # Start at 0, stop before 5

```

```python
print("Pixel indices:", pixel_numbers)
```

You can specify a step size - useful for selecting every Nth observation or creating regularly spaced samples:

```python
every_third = np.arange(0, 10, 3)  # Start 0, stop before 10, step by 3
```

```python
print("Every third value:", every_third)
```

This is useful when you want to subsample data, perhaps taking every 3rd frame from a time series to reduce data volume while maintaining temporal coverage.

### Creating Evenly Spaced Numbers

The `np.linspace()` function creates an exact number of evenly spaced points between a start and stop value. Unlike `arange` where you specify the step size, with `linspace` you specify how many points you want.

This is particularly useful for creating wavelength grids for spectra:

```python
wavelengths = np.linspace(4000, 5000, 5)
```

This creates exactly 5 wavelengths from 4000 to 5000 Angstroms (inclusive of both endpoints):

```python
print("Wavelengths:", wavelengths)
```

Notice the spacing between points is automatically calculated to be uniform:

```python
spacing = wavelengths[1] - wavelengths[0]
print(f"Wavelength spacing: {spacing} Angstroms")
```

### Logarithmic Spacing

The `np.logspace()` function creates points evenly spaced on a logarithmic scale. The arguments are the log₁₀ of the start value, the log₁₀ of the stop value, and the number of points.

This is invaluable when studying objects that span vast scales - like stellar masses that range from 0.08 solar masses (the minimum for hydrogen fusion) to over 100 solar masses:

```python
masses = np.logspace(-1, 2, 5)  # From 10^-1 to 10^2
```

```python
print("Stellar masses (solar units):", masses)
```

This creates 5 points from 0.1 to 100 solar masses, evenly distributed in log space. This logarithmic spacing is natural for many astronomical quantities that span orders of magnitude.

## Understanding Data Types and Memory

One of NumPy's key advantages is explicit control over how numbers are stored in memory. This becomes crucial when working with large astronomical datasets where memory efficiency matters.

### Data Types (dtype)

Every NumPy array has a data type (dtype) that specifies how its numbers are stored in memory. Unlike Python lists where each element can be a different type, all elements in a NumPy array must have the same type:

```python
# Let's create arrays with different data types
integers = np.array([1, 2, 3, 4, 5])
floats = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
```

```python
print(f"Integer array dtype: {integers.dtype}")
print(f"Float array dtype: {floats.dtype}")
```

The default integer type is usually `int64` (64-bit integer) and the default float type is `float64` (64-bit floating point, also called "double precision").

### Specifying Data Types

You can explicitly specify the data type when creating an array. This is important for memory efficiency:

```python
# Create arrays with specific data types
small_ints = np.array([1, 2, 3], dtype=np.int8)  # 8-bit integers
big_ints = np.array([1, 2, 3], dtype=np.int64)   # 64-bit integers
```

```python
print(f"8-bit integers: {small_ints}, dtype: {small_ints.dtype}")
print(f"64-bit integers: {big_ints}, dtype: {big_ints.dtype}")
```

### Common Data Types in Astronomy

Here are the most commonly used dtypes in astronomical applications:

```python
# For CCD data (often 16-bit integers from the ADC)
ccd_data = np.array([32000, 32100, 31950], dtype=np.uint16)
print(f"CCD data (uint16): {ccd_data}")
```

```python
# For processed images (usually 32-bit floats for memory efficiency)
processed = np.array([1.523, 1.524, 1.522], dtype=np.float32)
print(f"Processed data (float32): {processed}")
```

```python
# For high-precision calculations (64-bit floats)
precise = np.array([1.523, 1.524, 1.522], dtype=np.float64)
print(f"High precision (float64): {precise}")
```

### Checking Precision Limits

Different dtypes have different precision and range limits:

```python
# See the limits of different integer types
print(f"int8 can store: {np.iinfo(np.int8).min} to {np.iinfo(np.int8).max}")
print(f"int16 can store: {np.iinfo(np.int16).min} to {np.iinfo(np.int16).max}")
print(f"uint16 can store: {np.iinfo(np.uint16).min} to {np.iinfo(np.uint16).max}")
```

For floating point types, we care about precision:

```python
print(f"float32 precision: ~{np.finfo(np.float32).precision} decimal digits")
print(f"float64 precision: ~{np.finfo(np.float64).precision} decimal digits")
```

This matters for photometry! If you're measuring stellar brightnesses to 1% accuracy, float32 is fine. But for high-precision measurements, you need float64.

### Type Casting

You can convert between types using the `.astype()` method:

```python
# Start with integers
pixel_values = np.array([100, 200, 300], dtype=np.int32)
print(f"Original integers: {pixel_values}, dtype: {pixel_values.dtype}")
```

```python
# Convert to float for processing
pixel_float = pixel_values.astype(np.float32)
print(f"Converted to float: {pixel_float}, dtype: {pixel_float.dtype}")
```

Be careful when converting from float to integer - NumPy truncates (rounds toward zero):

```python
measurements = np.array([1.7, 2.3, 3.9])
as_integers = measurements.astype(np.int32)
print(f"Float {measurements} becomes int {as_integers}")
```

## Array Properties

Every NumPy array has properties that describe its structure. These properties are essential for understanding your data and debugging code.

### Size Property

The `.size` property tells us the total number of elements in the array:

```python
data = np.array([1.5, 2.3, 3.7, 4.1])
```

```python
print(f"Number of elements: {data.size}")
```

For a 2D array, size is the total count of all elements:

```python
image = np.zeros((100, 100))
print(f"100x100 image has {image.size} pixels total")
```

### Shape Property

The `.shape` property tells us the dimensions of the array as a tuple. This is probably the most important property you'll use:

```python
print(f"Shape of 1D array: {data.shape}")
```

For a 1D array, shape is `(n,)` where n is the number of elements. Note the comma - it's a tuple with one element.

Let's examine a 2D array representing a small star catalog:

```python
star_catalog = np.array([[25.3, 1.2, 10.5],   # Star 1: RA, Dec, Mag
                         [48.7, -5.3, 11.2]])  # Star 2: RA, Dec, Mag
```

```python
print(f"Shape of catalog: {star_catalog.shape}")
```

The shape `(2, 3)` means 2 rows (stars) and 3 columns (properties per star). In astronomy, we often think of the first axis as the "object axis" and the second as the "property axis."

### Number of Dimensions

The `.ndim` property tells us how many dimensions (axes) the array has:

```python
print(f"1D array dimensions: {data.ndim}")
print(f"2D catalog dimensions: {star_catalog.ndim}")
```

You'll typically work with:
- 1D arrays (spectra, time series)
- 2D arrays (images, catalogs)
- 3D arrays (spectral cubes, multiple images)

### Data Type Property

We've already seen `.dtype`, but it's worth emphasizing its importance:

```python
print(f"Data type: {data.dtype}")
```

Always check dtype when debugging - many errors come from unexpected type conversions.

## Broadcasting

Broadcasting is NumPy's "magic" that allows operations between arrays of different shapes. Understanding broadcasting is essential because it's what enables NumPy to perform operations on entire arrays without loops. This fundamental concept underlies all the mathematical operations we'll explore next.

### Scalar Broadcasting

When you combine a scalar (single number) with an array, NumPy "broadcasts" the scalar to match the array's shape:

```python
mags = np.array([10.5, 11.2, 9.8])
extinction = 0.3  # Atmospheric extinction in magnitudes
```

```python
corrected = mags + extinction
print("Original:", mags)
print("Add", extinction, "to each:", corrected)
```

Behind the scenes, NumPy treats this as if extinction were `[0.3, 0.3, 0.3]`, but without actually creating that array in memory. This is why you can perform mathematical operations on entire arrays without writing loops!

### Broadcasting Rules

NumPy's broadcasting follows specific rules that determine whether arrays can be operated on together:

**Rule 1: Dimension Padding** - When arrays have different numbers of dimensions, NumPy conceptually pads the smaller-dimensional array with dimensions of size 1 on the **left** (not the right).

**Rule 2: Dimension Compatibility** - After padding, NumPy compares the dimensions of both arrays element by element. Two dimensions are compatible when:
- They are equal, OR
- One of them is 1 (in which case that dimension will be broadcast/stretched to match the other)
   
What does "broadcast/stretched" mean? When NumPy encounters a dimension of size 1, it conceptually repeats that dimension's data to match the larger dimension. For example, if you have shapes (3, 1) and (3, 4), the dimension of size 1 gets "stretched" by repeating its single value 4 times to create an effective shape of (3, 4). Importantly, NumPy doesn't actually copy the data in memory - it just acts as if the data were repeated, making this operation very memory efficient.

If any dimension pair doesn't satisfy these conditions, you get an error.

Let's see this in action with a practical example:

```python
# 2 stars observed in 3 filters (g, r, i bands)
observations = np.array([[10.5, 10.8, 10.3],  # Star 1
                        [11.2, 11.5, 11.0]])   # Star 2
print("observations.shape:", observations.shape)  # (2, 3)

# Each filter has a different zero-point correction
zero_points = np.array([0.1, 0.2, 0.15])
print("zero_points.shape:", zero_points.shape)    # (3,)

# Broadcasting applies each correction to its column
calibrated = observations - zero_points
print("Calibrated shape:", calibrated.shape)      # (2, 3)
print("Calibrated values:")
print(calibrated)
```

Why does this work? Let's trace through NumPy's thought process:
1. NumPy sees arrays with shapes (2, 3) and (3,)
2. It pads the smaller-dimensional array on the left: (3,) becomes (1, 3)
3. Now it compares dimensions element by element: (2, 3) vs (1, 3)
   - First dimension: 2 vs 1 → dimension of 1 broadcasts to 2 ✓
   - Second dimension: 3 vs 3 → equal, compatible ✓
4. Result has shape (2, 3)

The 1D array `zero_points` is broadcast across each row of the 2D array. This is exactly what you want - each filter's correction applied to all stars.

### When Broadcasting Fails

Let's explore what happens when broadcasting rules aren't satisfied:

```python
# This won't work:
obs = np.array([[1, 2], [3, 4], [5, 6]])  # Shape (3, 2)
correction = np.array([0.1, 0.2, 0.3])     # Shape (3,)

# If we try: obs - correction
# NumPy pads the 1D array on the left: (3,) becomes (1, 3)
# Now comparing: (3, 2) vs (1, 3)
# First dimension: 3 vs 1 → 1 would broadcast to 3 ✓
# Second dimension: 2 vs 3, neither is 1 → ERROR!
```

The error message will say something like "operands could not be broadcast together with shapes (3,2) (3,)". This is NumPy telling you the dimensions don't align properly.

### Using np.newaxis to Fix Broadcasting

The `np.newaxis` (which is actually `None`) adds a dimension of size 1, making broadcasting possible in cases where it wouldn't work otherwise:

```python
# Fix the broadcasting problem:
obs = np.array([[1, 2], [3, 4], [5, 6]])  # Shape (3, 2)
correction = np.array([0.1, 0.2, 0.3])     # Shape (3,)

# Add newaxis to make correction a column vector
correction_col = correction[:, np.newaxis]  # Shape becomes (3, 1)
print("correction_col shape:", correction_col.shape)

# Now it works!
result = obs - correction_col  # (3, 2) - (3, 1) works
print("Result shape:", result.shape)
print("Result:")
print(result)
```

Now the comparison works:
- (3, 2) and (3, 1)
- First dimension: 3 = 3 ✓
- Second dimension: 2 vs 1 → 1 broadcasts to 2 ✓

This technique is essential when you need to apply per-star corrections (along rows) rather than per-filter corrections (along columns).

### Broadcasting with Different Shapes

Let's explore what happens when we combine a row array with a column array:

```python
x = np.array([0, 1, 2])  # Shape (3,)
print("x shape:", x.shape)
print("x:", x)
```

```python
y = np.array([0, 10, 20])
y_column = y[:, np.newaxis]  # Convert to column vector
print("y_column shape:", y_column.shape)
print("y_column:")
print(y_column)
```

```python
# Broadcasting creates a 2D grid
grid = x + y_column
print("Result of broadcasting (x + y_column):")
print(grid)
```

NumPy effectively extends x to match each row and y-column to match each column, creating all pairwise sums. Let's trace through why this works using the broadcasting rules:
 
- We have x with shape (3,) and y_column with shape (3, 1)
- NumPy pads the smaller-dimensional array on the left: x becomes (1, 3)
- Now comparing dimensions: (1, 3) vs (3, 1)
    - First dimension: 1 vs 3 → 1 broadcasts to 3 ✓
    - Second dimension: 3 vs 1 → 1 broadcasts to 3 ✓
- Result has shape (3, 3)

The broadcasting creates a 3×3 grid where:
- x is repeated across 3 rows: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
- y_column is repeated across 3 columns: [[0, 0, 0], [10, 10, 10], [20, 20, 20]]
- The addition gives all pairwise sums
 
This technique is useful for creating coordinate grids or computing all pairwise combinations.

## Math with Arrays - No Loops Needed!

Now that we understand broadcasting, we can fully appreciate NumPy's vectorized operations. These operations apply to entire arrays at once, leveraging broadcasting when needed, and run in compiled C code for maximum speed.

### Adding a Number to Every Element

Thanks to scalar broadcasting, operations between arrays and single numbers apply to every element:

```python
magnitudes = np.array([10.5, 11.2, 9.8, 12.3])
```

Let's correct for atmospheric extinction. When starlight passes through Earth's atmosphere, it gets dimmed by about 0.3 magnitudes at sea level (more for stars near the horizon):

```python
corrected = magnitudes + 0.3
```

```python
print("Original:", magnitudes)
print("After extinction:", corrected)
```

No loop needed! Broadcasting automatically applies 0.3 to each element.

### All Basic Math Operations Work

Every arithmetic operation works element-wise, with broadcasting handling any shape mismatches:

```python
doubled = magnitudes * 2
print("Multiplied by 2:", doubled)
```

```python
halved = magnitudes / 2
print("Divided by 2:", halved)
```

```python
squared = magnitudes ** 2
print("Squared:", squared)
```

### Complex Calculations

Real astronomical calculations often involve multiple operations. The magnitude system is logarithmic, and to convert to linear flux units, we use:
flux = 10^(-0.4 × magnitude)

This formula comes from the definition that a difference of 5 magnitudes corresponds to a factor of 100 in flux.

```python
fluxes = 10**(-0.4 * magnitudes)
```

```python
print("Magnitudes:", magnitudes)
print("Fluxes:", fluxes)
```

Notice how smaller magnitude numbers give larger flux values - the magnitude scale runs backwards! Vega (magnitude 0) is much brighter than a magnitude 15 galaxy. Broadcasting ensures the scalar -0.4 multiplies every element, then 10 is raised to each resulting power.

### Math Between Two Arrays

When you perform operations between arrays of the same size, NumPy operates element-by-element:

```python
v_band = np.array([10.5, 11.2, 9.8])   # Visual band magnitudes
b_band = np.array([10.8, 11.5, 10.1])  # Blue band magnitudes
```

The color index (B-V) tells us about a star's temperature. Blue stars are hot, red stars are cool:

```python
color = b_band - v_band
```

```python
print("B-V color:", color)
```

Positive B-V means the star is redder (cooler), like our Sun with B-V ≈ 0.65. Negative B-V indicates a hot, blue star like Rigel with B-V ≈ -0.03.

### NumPy Math Functions

NumPy provides optimized versions of all common mathematical functions that work on entire arrays.

For example, parallax is the tiny apparent shift in a star's position as Earth orbits the Sun. The Gaia satellite measures parallaxes in milliarcseconds, and we convert to distance using:
distance (parsecs) = 1000 / parallax (milliarcseconds)

```python
parallaxes = np.array([10, 5, 2, 1])  # in milliarcseconds
```

```python
distances = 1000 / parallaxes  # Distance in parsecs
```

```python
print("Parallaxes (mas):", parallaxes)
print("Distances (pc):", distances)
```

A parallax of 1 milliarcsecond corresponds to 1000 parsecs (about 3260 light-years). Here, broadcasting divides the scalar 1000 by each array element.

For trigonometry, NumPy provides sin, cos, tan, and more. These functions expect angles in radians, not degrees:

```python
angles_deg = np.array([0, 30, 45, 60, 90])
```

Convert degrees to radians using `np.deg2rad()`:

```python
angles_rad = np.deg2rad(angles_deg)
```

Now calculate trigonometric functions:

```python
sines = np.sin(angles_rad)
cosines = np.cos(angles_rad)
```

```python
print("Angles (degrees):", angles_deg)
print("Sines:", sines)
print("Cosines:", cosines)
```

These trigonometric functions are essential for coordinate transformations, calculating angular separations, and many other astronomical calculations.

## Array Indexing and Slicing

Accessing and extracting data from arrays is fundamental to data analysis. NumPy provides powerful and flexible indexing.

### Basic Indexing

Arrays use zero-based indexing just like Python lists:

```python
data = np.array([10.5, 11.2, 9.8, 12.3, 10.9])
```

```python
print(f"First element (index 0): {data[0]}")
print(f"Third element (index 2): {data[2]}")
print(f"Last element (index -1): {data[-1]}")
```

Remember: Python counts from 0, and negative indices count backwards from the end.

### Slicing with Start:Stop:Step

Array slicing uses the syntax `[start:stop:step]`. This extracts a portion of the array:

```python
print("First three:", data[:3])       # Start=0, stop=3, step=1 (defaults)
print("From index 1 to 4:", data[1:4])   # Elements at indices 1, 2, 3
print("Every other element:", data[::2]) # Step=2 skips elements
print("Reversed:", data[::-1])        # Step=-1 reverses the array
```

The stop index is exclusive - we get elements up to but not including the stop position.

### 2D Array Indexing

For 2D arrays, use a comma to separate dimensions. Think of it as [row, column]:

```python
catalog = np.array([[25.3, 1.2, 10.5],   # Star 1: RA, Dec, Mag
                    [48.7, -5.3, 11.2],   # Star 2: RA, Dec, Mag
                    [102.4, 15.6, 9.8]])  # Star 3: RA, Dec, Mag
```

Get a single element with [row, column]:

```python
star2_dec = catalog[1, 1]  # Row 1 (second star), column 1 (declination)
print(f"Star 2 declination: {star2_dec}")
```

Get an entire row (all data for one star):

```python
star_1 = catalog[0]  # Could also write catalog[0, :]
print("First star data:", star_1)
```

Get an entire column (one property for all stars):

```python
all_mags = catalog[:, 2]  # All rows, column 2 (magnitude)
print("All magnitudes:", all_mags)
```

The colon `:` means "all elements along this dimension."

### Advanced Indexing with Integer Arrays

You can select specific elements using an array of indices. This is powerful for selecting subsets of data:

```python
indices = np.array([0, 2])  # Want 1st and 3rd stars
selected = catalog[indices]
```

```python
print("Selected stars:\n", selected)
```

This is extremely useful when you have a list of interesting objects to extract from a larger catalog.

## Selecting Data with Conditions

One of NumPy's most powerful features is boolean indexing - selecting data based on conditions. This is how you filter astronomical catalogs.

### Boolean Masks

A boolean mask is an array of True/False values. When used as an index, it selects only the True elements:

```python
mags = np.array([10.5, 11.2, 9.8, 12.3, 10.9])
```

Create a condition (remember: smaller magnitude = brighter star):

```python
is_bright = mags < 11.0
```

```python
print("Magnitudes:", mags)
print("Is bright?:", is_bright)
print("Type:", type(is_bright))
```

Use the boolean mask to select only the bright stars:

```python
bright_stars = mags[is_bright]
print("Bright stars only:", bright_stars)
```

Count how many stars meet the condition: `np.sum()` works because Python treats True as 1 and False as 0 in arithmetic operations. So summing a boolean array counts the `True` values - an elegant way to count!

```python
n_bright = np.sum(is_bright)  # True=1, False=0 in arithmetic
print(f"Number of bright stars: {n_bright}")
```

This is how you'd select all stars brighter than a certain limit for follow-up observations!

### Combining Multiple Conditions

Use `&` for AND, `|` for OR. Important: Don't use the Python keywords 'and'/'or' - they don't work with arrays!


```python
# Find stars with magnitude between 10 and 11
moderate = (mags > 10.0) & (mags < 11.0)
```

```python
print("Between 10 and 11:", mags[moderate])
```

Always use parentheses around each condition to ensure proper precedence.

```python
# Find very bright OR very faint stars
extreme = (mags < 10.0) | (mags > 12.0)
print("Extreme brightness:", mags[extreme])
```

This is how you'd select outliers or interesting objects from a catalog.

<!-- #region -->


### The np.where() Function

The `np.where()` function is used to find indices where a condition is True
<!-- #endregion -->

```python
bright_indices = np.where(mags < 11.0)
```

```python
print("Indices tuple:", bright_indices)
print("Actual indices:", bright_indices[0])
```

Note that `np.where` returns a tuple (to handle multi-dimensional arrays), so we use [0] to get the actual indices for a 1D array. For a 2D array, it would return (row_indices, col_indices).



## Arrays: Copies vs Views

Understanding when NumPy creates a copy of data versus a "view" that shares memory with the original is crucial. This concept prevents subtle bugs and helps you write memory-efficient code.

### What is a View?

A view is similar to the concept of "reference" we discussed with Python lists, but with some distinctions that are not particularly important for our purposes. While a reference is simply another name pointing to the same object, a NumPy view is actually a **new array object** that looks at the same underlying data. Think of it as a different window into the same data buffer - it can have its own shape, its own slicing. But like reference for a python list, any changes to the data through either the view or the original will affect both.

### Views Share Memory

When you slice an array, NumPy creates a view rather than copying the data. This is efficient but can lead to surprises:

```python
original = np.array([1, 2, 3, 4])
```

```python
view = original[1:3]  # This is a view, not a copy
print("View:", view)
```

If we modify the view, it changes the original array too:

```python
view[0] = 999
print("View after change:", view)
print("Original also changed:", original)
```

This behavior is actually useful when you want to modify a portion of a large image without duplicating memory. But it can cause bugs if you're not expecting it!

### Copies are Independent

To create an independent copy that won't affect the original, use the `.copy()` method explicitly:

```python
original = np.array([1, 2, 3, 4])
copy = original[1:3].copy()  # Explicit copy
```

```python
copy[0] = 999
print("Copy after change:", copy)
print("Original unchanged:", original)
```

When working with large astronomical images, be mindful of whether you need a copy (independent data) or if a view (shared memory) is sufficient.

## Array Reshaping (Creates View)

Sometimes we need to reorganize our data without changing the values themselves. NumPy provides several methods for reshaping arrays.

The `reshape()` method changes an array's dimensions while keeping all the same elements. The total number of elements must remain constant:

```python
data_1d = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D array:", data_1d)
```

Reshape to 2 rows and 3 columns:

```python
data_2d = data_1d.reshape(2, 3)
```

```python
print("Reshaped to 2D:")
print(data_2d)
```

**Important:** Reshaping creates a VIEW, not a copy! This means the reshaped array shares memory with the original:

```python
data_2d[0, 0] = 99
print("Modified reshaped array:")
print(data_2d)
print("Original also changed:", data_1d)
```

This is useful when reading data from files - often data comes in as a 1D stream that you need to reshape into an image. Since it's a view, no memory is wasted on copies.

You can use -1 to have NumPy automatically calculate one dimension:

```python
data_1d = np.array([1, 2, 3, 4, 5, 6])
auto_reshape = data_1d.reshape(-1, 2)  # Auto-calculates rows
print("Auto-calculated shape:")
print(auto_reshape)
```

## Flattening Arrays (Creates Copy or View)

Sometimes you need to convert a multi-dimensional array back to 1D. NumPy provides two methods with different memory behaviors.

The `flatten()` method **always creates a copy**:

```python
image = np.array([[1, 2, 3], 
                  [4, 5, 6]])
```

```python
flat = image.flatten()
print("Flattened:", flat)
```

Since it's a copy, modifying it doesn't affect the original:

```python
flat[0] = 99
print("Modified flat:", flat)
print("Original unchanged:", image)
```

The `ravel()` method also flattens but **might return a view** instead of a copy (more memory efficient):

```python
raveled = image.ravel()
print("Raveled:", raveled)
```

Use `flatten()` when you need to ensure the result is independent of the original. Use `ravel()` when you want to be memory-efficient and don't mind if it's a view.

## Transpose (Creates View)

The `.T` attribute swaps rows and columns - essentially rotating the array by 90 degrees:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
```

```python
print("Original shape:", matrix.shape)
print("Original:\n", matrix)
```

```python
transposed = matrix.T
print("\nTransposed shape:", transposed.shape)
print("Transposed:\n", transposed)
```

**Important:** Transpose creates a VIEW:

```python
transposed[0, 0] = 99
print("Modified transpose:\n", transposed)
print("Original also changed:\n", matrix)
```

This is particularly useful when you need to switch between "stars × properties" and "properties × stars" organizations of your data. Just remember that modifications will affect the original array!

## Array Stacking and Combining (Creates Copy)

When working with multiple observations or datasets, you often need to combine arrays. Unlike reshaping operations, stacking creates new arrays with copies of the data.

### Vertical Stacking

The `np.vstack()` function stacks arrays vertically (adds rows):

```python
night1 = np.array([10.5, 11.2, 9.8])  # 3 stars on night 1
night2 = np.array([10.6, 11.1, 9.9])  # Same 3 stars on night 2
```

```python
both_nights = np.vstack([night1, night2])
```

```python
print("Combined observations:")
print(both_nights)
print("Shape:", both_nights.shape)
```

Now you have a 2D array where each row is a night of observations. Since this creates a copy, modifying `both_nights` won't affect the original arrays.

### Column Stacking

The `np.column_stack()` function combines arrays as columns:

```python
mags = np.array([10.5, 11.2, 9.8])
colors = np.array([0.3, 0.5, 0.2])  # B-V color indices
```

```python
star_data = np.column_stack([mags, colors])
```

```python
print("Magnitudes and colors:")
print(star_data)
```

Each row now represents a star with multiple properties. This is perfect for building catalogs from separate measurements.

### Concatenate

The `np.concatenate()` function is the most general combining function. It joins arrays along any axis you specify:

```python
batch1 = np.array([1, 2, 3])
batch2 = np.array([4, 5, 6])
```

```python
# Join along axis 0 (default for 1D arrays)
joined = np.concatenate([batch1, batch2])
print("Joined:", joined)
```

For 2D arrays, you can specify the axis:
- `axis=0` concatenates vertically (adds rows)
- `axis=1` concatenates horizontally (adds columns)

This is useful when you're accumulating data from multiple sources or building up a dataset incrementally.

## Sorting Arrays

Sorting is essential for finding extremes, computing percentiles, and organizing data.

### Basic Sorting

The `np.sort()` function returns a sorted copy of the array:

```python
mags = np.array([11.2, 9.8, 12.3, 10.5])
```

```python
sorted_mags = np.sort(mags)
print("Original:", mags)
print("Sorted (bright to faint):", sorted_mags)
```

The original array is unchanged. If you want to sort in-place, use the `.sort()` method instead.

### Getting Sort Indices

Often you don't just want to sort one array - you want to reorder multiple related arrays the same way. The `np.argsort()` function returns the indices that would sort the array:

```python
sort_indices = np.argsort(mags)
```

```python
print("Original magnitudes:", mags)
print("Sort indices:", sort_indices)
print("This means:")
print(f"  Brightest star is at index {sort_indices[0]} with mag {mags[sort_indices[0]]}")
```

Now use these indices to sort related data:

```python
star_names = np.array(['Alpha', 'Beta', 'Gamma', 'Delta'])
sorted_names = star_names[sort_indices]
```

```python
print("Stars from brightest to faintest:", sorted_names)
```

This is how you'd create a ranked list of targets for observation, sorted by brightness.

### Finding Extrema Indices

NumPy provides direct functions to find the indices of minimum and maximum values:

```python
mags = np.array([11.2, 9.8, 12.3, 10.5])

brightest_idx = np.argmin(mags)  # Index of minimum (brightest)
faintest_idx = np.argmax(mags)   # Index of maximum (faintest)

print(f"Brightest star at index {brightest_idx}: magnitude {mags[brightest_idx]}")
print(f"Faintest star at index {faintest_idx}: magnitude {mags[faintest_idx]}")
```

Note: if there are multiple occurrences of the minimum/maximum, `argmin` and `argmax` return the index of the first occurrence.

### Finding Unique Values

The `np.unique()` function finds all unique values in an array and optionally returns additional information:

```python
obs = np.array([10.5, 11.2, 10.5, 9.8, 11.2, 10.5])

# Just get unique values
unique_mags = np.unique(obs)
print("Unique magnitudes (sorted):", unique_mags)
```

Get counts of each unique value:

```python
unique, counts = np.unique(obs, return_counts=True)
print("Values:", unique)
print("Counts:", counts)

# Find the most common value (mode)
most_common_idx = np.argmax(counts)
print(f"Mode: {unique[most_common_idx]} appears {counts[most_common_idx]} times")
```

This is useful for understanding the distribution of discrete values in your data, like finding the most common spectral type in a stellar sample.
 
## Matrix Operations
 
For linear algebra operations like coordinate transformations or least-squares fitting, NumPy provides specialized matrix operations.
 
### Matrix Multiplication vs Element-wise Multiplication
 
It's crucial to understand the difference between matrix multiplication and element-wise multiplication:
 
- `*` performs **element-wise** multiplication (multiplies corresponding elements at the same positions in arrays, like [a,b] * [c,d] = [a*c, b*d]).



```python
# Element-wise multiplication example
a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

# Element-wise multiplication (*)
element_wise = a * b
print("Array a:", a)
print("Array b:", b)
print("Element-wise (a * b):", element_wise)  # [2*5, 3*6, 4*7] = [10, 18, 28]

# This also works with 2D arrays
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

element_wise_2d = matrix_a * matrix_b
print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Element-wise multiplication:\n", element_wise_2d)

```

- `@` performs **matrix** multiplication (dot product), which follows the mathematical rules of linear algebra where the number of columns in the first matrix must equal the number of rows in the second matrix. This is essential for operations like coordinate transformations, solving systems of equations, and computing projections.

```python
# Rotation matrix for 30 degrees
angle = np.deg2rad(30)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
```

```python
# Initial position vector
position = np.array([1, 0])
```

```python
# Apply rotation
new_position = rotation @ position
print("Original position:", position)
print("Rotated position:", new_position)
```

You can also use `np.matmul()` or `np.dot()` for matrix multiplication:

```python
same_result = np.matmul(rotation, position)
print("Using matmul:", same_result)
```

The `@` operator is preferred for clarity in modern code.

## Random Numbers for Simulations

Simulations are crucial in astronomy for understanding instruments, testing pipelines, and making predictions. NumPy's random module provides all the tools you need.

### The Random Seed

Setting a seed makes random numbers reproducible - essential for debugging and sharing results:

```python
np.random.seed(42)
print("First random number:", np.random.random())
print("Second random number:", np.random.random())
```

Reset the seed to get the same sequence again:

```python
np.random.seed(42)
print("First random number again:", np.random.random())
print("Second random number again:", np.random.random())
```

Without setting a seed, you get different numbers each time:

```python
print("Without seed:", np.random.random())
print("Different each time:", np.random.random())
```

Always set a seed at the beginning of simulations to ensure reproducibility! This is crucial for:
- Debugging your code
- Sharing results with collaborators
- Publishing reproducible research

### Uniform Distribution

The `np.random.uniform()` function generates random numbers uniformly distributed between two values. Perfect for generating random positions:

```python
# Generate 5 random RA values between 0 and 360 degrees
ra = np.random.uniform(0, 360, 5)
print("Random RA values:", ra)
```

```python
# Generate 5 random Dec values between -90 and +90 degrees
dec = np.random.uniform(-90, 90, 5)
print("Random Dec values:", dec)
```

Note that this isn't quite right for simulating uniform sky coverage - you need to account for the spherical geometry. Points near the poles are overrepresented because the area of a spherical cap decreases toward the poles.

### Normal (Gaussian) Distribution

Most measurement errors in astronomy follow a Gaussian (normal) distribution. The `np.random.normal()` function generates these:

```python
# Simulate measuring a star's magnitude 5 times
true_mag = 10.5
measurement_error = 0.1  # Standard deviation of 0.1 magnitudes

observed = np.random.normal(true_mag, measurement_error, 5)
```

```python
print(f"True magnitude: {true_mag}")
print(f"5 measurements: {observed}")
print(f"Mean of measurements: {np.mean(observed):.3f}")
```

The mean of many measurements approaches the true value - this is why we take multiple observations! This is the foundation of observational astronomy:
- Multiple exposures reduce random noise
- Combining observations improves precision
- Statistical analysis reveals true values

```python
# Generate sample magnitudes from a stellar population
np.random.seed(42)
mags = np.random.normal(12, 2, 1000)  # 1000 stars with mean mag 12
```

```python
# Compute histogram with 10 bins
counts, bins = np.histogram(mags, bins=10)
```

```python
print(f"We have {len(bins)} bin edges and {len(counts)} counts")
print(f"First bin: {bins[0]:.1f} to {bins[1]:.1f} contains {counts[0]} stars")
```

Note that `bins` has one more element than `counts` - it contains the edges of all bins. This makes sense: for 10 bins, you need 11 edges (think of fence posts and fence panels).

Find the peak of the distribution:

```python
peak_bin = np.argmax(counts)
print(f"Most stars ({counts[peak_bin]}) are in bin {peak_bin}")
print(f"This corresponds to magnitude range {bins[peak_bin]:.1f} to {bins[peak_bin+1]:.1f}")
```

## Computing Statistics

NumPy provides a comprehensive suite of statistical functions optimized for array operations. These are the workhorses of astronomical data analysis.

### Basic Statistics Functions

Let's analyze magnitudes from a star cluster:

```python
cluster_mags = np.array([10.2, 11.5, 9.8, 12.1, 10.7])
```

```python
print(f"Mean (average): {np.mean(cluster_mags):.2f}")
print(f"Median (middle value): {np.median(cluster_mags):.2f}")
print(f"Standard deviation (spread): {np.std(cluster_mags):.2f}")
print(f"Minimum (brightest): {np.min(cluster_mags):.2f}")
print(f"Maximum (faintest): {np.max(cluster_mags):.2f}")
```

### Percentiles

The `np.percentile()` function finds the value below which a given percentage of data falls. This is useful for understanding data distributions:

```python
percentile_25 = np.percentile(cluster_mags, 25)
percentile_75 = np.percentile(cluster_mags, 75)
```

```python
print(f"25th percentile: {percentile_25:.2f}")
print(f"75th percentile: {percentile_75:.2f}")
print("This means 25% of stars are brighter than", percentile_25)
```

The range from 25th to 75th percentile (the interquartile range) is a robust measure of spread that's less sensitive to outliers than standard deviation.

### The Crucial Axis Parameter

For multi-dimensional arrays, you often want statistics along specific dimensions. The `axis` parameter is crucial for controlling this.

Consider a realistic scenario: monitoring variable stars over multiple nights:

```python
observations = np.array([[10.5, 10.6, 10.4, 10.5],  # Star 1 over 4 nights
                        [11.2, 11.3, 11.1, 11.2],   # Star 2 over 4 nights
                        [9.8,  9.9,  9.7,  9.8]])    # Star 3 over 4 nights
```

```python
print("Data shape:", observations.shape)
print("This is 3 stars (rows) × 4 nights (columns)")
```

To get the mean magnitude for each star (averaging across all nights), use `axis=1`:

```python
mean_per_star = np.mean(observations, axis=1)
print("Mean per star:", mean_per_star)
```

To get the mean for each night (averaging across all stars), use `axis=0`:

```python
mean_per_night = np.mean(observations, axis=0)
print("Mean per night:", mean_per_night)
```

Remember the axis convention:
- `axis=0` operates down columns (across rows) - collapses the row dimension
- `axis=1` operates across columns (along rows) - collapses the column dimension

This can be confusing at first! Think of it this way: the axis you specify is the one that disappears. When you use `axis=0`, you're collapsing along the first dimension (rows), leaving you with one value per column.

## Handling Missing Data

Real astronomical observations are messy. Weather happens, instruments fail, cosmic rays hit detectors. NumPy uses NaN (Not a Number) to represent missing or invalid data:

```python
obs = np.array([10.5, np.nan, 11.2, 10.8, np.nan])
print("Observations with bad data:", obs)
```

### Check for NaN

The `np.isnan()` function returns True where values are NaN:

```python
is_bad = np.isnan(obs)
print("Bad data mask:", is_bad)
```

### Count Good Data

Use `~` (tilde) to invert a boolean array - True becomes False and vice versa. This is the same as `not` that we've seen with boolean variables, but for multiple entries in an array, NumPy uses `~`:

```python
is_good = ~is_bad
n_good = np.sum(is_good)
print(f"Good observations: {n_good} out of {len(obs)}")
```

This tells you your data completeness - crucial for understanding the quality of your dataset.

### Statistics Ignoring NaN

Regular statistical functions fail when arrays contain NaN - they return NaN as the result:

```python
print(f"Regular mean: {np.mean(obs)}")  # Returns nan - not helpful!
print(f"NaN-aware mean: {np.nanmean(obs):.2f}")  # Ignores NaN values
print(f"NaN-aware std: {np.nanstd(obs):.2f}")
```

NumPy provides `nan`-versions of most statistical functions: `nanmean`, `nanmedian`, `nanstd`, `nanmin`, `nanmax`, etc. These compute statistics using only the valid data points.

## Saving and Loading Arrays

NumPy provides efficient binary formats for saving arrays. These formats preserve the exact data type and shape of your arrays, and are much faster than text files.

### Single Arrays (.npy format)

The `.npy` format is perfect for saving individual arrays:

```python
# Save a single array
photometry = np.array([10.5, 11.2, 9.8, 12.3])
np.save('photometry.npy', photometry)

# Load it back
loaded = np.load('photometry.npy')
print("Loaded array:", loaded)
print("Preserved dtype:", loaded.dtype)
```

The `.npy` format:
- Preserves the exact data type (float64, int32, etc.)
- Maintains array shape
- Is much smaller than text files
- Loads much faster than parsing text

### Multiple Arrays (.npz format)

When you have multiple related arrays, use the `.npz` format to save them together:

```python
# Save multiple related arrays
mags = np.array([10.5, 11.2, 9.8])
errors = np.array([0.1, 0.15, 0.08])
names = np.array(['Star1', 'Star2', 'Star3'])

np.savez('observations.npz', 
         mags=mags, errors=errors, names=names)

# Load them back
data = np.load('observations.npz')
print("Magnitudes:", data['mags'])
print("Errors:", data['errors'])
print("Names:", data['names'])
```

The `.npz` format is perfect for:
- Saving complete observational datasets
- Storing related arrays together
- Creating checkpoint files in long computations
- Sharing processed data with collaborators

You can also use `np.savez_compressed()` for compressed storage, which is useful for large arrays that compress well.



## Practical Example: Complete Star Cluster Analysis

Let's combine everything we've learned to analyze a simulated globular cluster observation. This example mimics a real analysis pipeline.

### Generate Realistic Data

```python
np.random.seed(42)  # For reproducibility
```

Create cluster member positions with a concentrated core:

```python
n_cluster = 200
# Cluster centered at RA=150°, Dec=2°
# Normal distribution gives concentrated core (King profile approximation)
cluster_ra = 150.0 + np.random.normal(0, 0.1, n_cluster)
cluster_dec = 2.0 + np.random.normal(0, 0.1, n_cluster)
```

Add field stars uniformly distributed across the field:

```python
n_field = 50
# Field stars spread uniformly across 1° × 1° region
field_ra = np.random.uniform(149.5, 150.5, n_field)
field_dec = np.random.uniform(1.5, 2.5, n_field)
```

Combine all stars into one catalog:

```python
all_ra = np.concatenate([cluster_ra, field_ra])
all_dec = np.concatenate([cluster_dec, field_dec])
print(f"Total stars: {len(all_ra)}")
```

Generate realistic magnitudes. In stellar clusters, the brightest stars evolve and die first, leaving a characteristic "main sequence turnoff" where stars are just beginning to exhaust their hydrogen fuel:

```python
# Cluster: main sequence turnoff at mag 14, fainter stars follow exponential
cluster_mags = 14 + np.random.exponential(1, n_cluster)

# Field: random brightnesses across full range
field_mags = np.random.uniform(12, 18, n_field)

# Combine
all_mags = np.concatenate([cluster_mags, field_mags])
```

Add realistic observational effects:

```python
# Measurement errors (Gaussian noise)
mag_errors = np.random.normal(0, 0.05, len(all_mags))
observed_mags = all_mags + mag_errors
```

```python
# Some observations fail (weather, cosmic rays, etc.)
bad_fraction = 0.05  # 5% failure rate typical for ground-based obs
bad_obs = np.random.random(len(all_mags)) < bad_fraction
observed_mags[bad_obs] = np.nan
print(f"Bad observations: {np.sum(bad_obs)}")
```

### Clean and Analyze the Data

First, remove bad observations:

```python
good_mask = ~np.isnan(observed_mags)
clean_ra = all_ra[good_mask]
clean_dec = all_dec[good_mask]
clean_mags = observed_mags[good_mask]
```

```python
print(f"Started with {len(all_mags)} stars")
print(f"Have {len(clean_mags)} good observations")
```

Find the cluster center using median (more robust than mean against outliers):

```python
center_ra = np.median(clean_ra)
center_dec = np.median(clean_dec)
print(f"Cluster center: RA={center_ra:.3f}°, Dec={center_dec:.3f}°")
```

Calculate angular distance from center. For small angles, we can use the flat-sky approximation:

```python
# Angular separation in degrees (flat-sky approximation)
delta_ra = clean_ra - center_ra
delta_dec = clean_dec - center_dec
distances_deg = np.sqrt(delta_ra**2 + delta_dec**2)

# Convert to arcseconds (3600 arcsec = 1 degree)
distances_arcsec = distances_deg * 3600
```

Define cluster membership based on distance (typical cluster radius ~200 arcsec):

```python
cluster_mask = distances_arcsec < 200
n_cluster_region = np.sum(cluster_mask)
n_field_region = np.sum(~cluster_mask)
```

```python
print(f"Stars in cluster region: {n_cluster_region}")
print(f"Stars in field region: {n_field_region}")
```

### Statistical Comparison

Compare the stellar populations:

```python
cluster_mags_region = clean_mags[cluster_mask]
field_mags_region = clean_mags[~cluster_mask]
```

```python
print("Cluster region statistics:")
print(f"  Mean magnitude: {np.mean(cluster_mags_region):.2f}")
print(f"  Std deviation: {np.std(cluster_mags_region):.2f}")
print(f"  Brightest: {np.min(cluster_mags_region):.2f}")
print(f"  Faintest: {np.max(cluster_mags_region):.2f}")
```

```python
print("\nField region statistics:")
print(f"  Mean magnitude: {np.mean(field_mags_region):.2f}")
print(f"  Std deviation: {np.std(field_mags_region):.2f}")
```

The cluster should show a distinct magnitude distribution compared to the field.

### Find the Main Sequence Turnoff

The magnitude distribution of cluster stars peaks at the main sequence turnoff:

```python
# Create magnitude histogram for cluster region
mag_hist, mag_bins = np.histogram(cluster_mags_region, bins=20)
```

```python
# Find peak
turnoff_bin = np.argmax(mag_hist)
turnoff_mag = (mag_bins[turnoff_bin] + mag_bins[turnoff_bin+1]) / 2
```

```python
print(f"Main sequence turnoff at magnitude {turnoff_mag:.1f}")
print("This can be used to estimate the cluster's age!")
```

The turnoff magnitude is a powerful age indicator - more massive stars evolve faster, so older clusters have fainter turnoffs.

### Identify Brightest Stars for Follow-up

```python
# Sort all stars by brightness
sort_idx = np.argsort(clean_mags)
brightest_5 = sort_idx[:5]
```

```python
print("5 Brightest stars in field:")
for i, idx in enumerate(brightest_5):
    print(f"  {i+1}. RA={clean_ra[idx]:.3f}°, Dec={clean_dec[idx]:.3f}°, Mag={clean_mags[idx]:.2f}")
```

Check if they're cluster members or field stars:

```python
for i, idx in enumerate(brightest_5):
    dist = distances_arcsec[idx]
    if cluster_mask[idx]:
        print(f"  Star {i+1} is a cluster member ({dist:.1f} arcsec from center)")
    else:
        print(f"  Star {i+1} is a field star ({dist:.1f} arcsec from center)")
```

Bright cluster members might be blue stragglers or horizontal branch stars - interesting targets for spectroscopy!

## Summary

You've mastered the complete NumPy toolkit for astronomical data analysis:

### Core Array Operations
- **Array creation** - Multiple methods optimized for different scenarios
- **Data types** - Control memory usage and precision with dtype
- **Broadcasting** - Smart handling of operations between different shaped arrays
- **Array math** - Vectorized operations that are 10-100× faster than loops
- **Indexing & slicing** - Powerful and flexible data selection

### Data Analysis Tools
- **Statistics** - Complete suite of statistical functions with axis control
- **Boolean masks** - Conditional selection for filtering catalogs
- **Missing data** - Proper handling of NaN values in real observations
- **Sorting** - Organizing and ranking astronomical objects
- **Histograms** - Understanding data distributions

### Advanced Features
- **Reshaping** - Reorganizing data without copying (creates views)
- **Stacking** - Combining multiple observations or datasets (creates copies)
- **Matrix operations** - Linear algebra for coordinate transforms and fitting
- **Views vs copies** - Memory-efficient operations on large datasets
- **Random numbers** - Simulating observations with realistic noise
- **File I/O** - Efficient saving/loading with .npy and .npz formats

These tools form the foundation for all astronomical data analysis in Python. Combined with domain-specific libraries like Astropy, you can tackle any astronomical data challenge efficiently.

Remember: Think in arrays, not loops. NumPy makes your code both faster and cleaner! The key to mastering NumPy is practice - try to solve problems without writing any explicit loops.



