# Welcome and Setting Up

*Tutorial by Yuan-Sen Ting*

*Astron 1221: Lecture 1*

## Introduction: The New Era of Astronomical Computing

### Why This Course, Why Now?

We're witnessing an extraordinary moment in the history. Artificial intelligence can now write functional code, debug complex algorithms, and even propose novel analysis strategies. Large Language Models like GPT, Claude, and Gemini have transformed from curiosities to essential research tools in just a few years. Meanwhile, astronomy itself is drowning in data. The Vera Rubin Observatory will generate 20 terabytes per night, Gaia has measured positions for nearly 2 billion stars, and the James Webb Space Telescope is revealing the universe in unprecedented detail.

This collision of AI capability and astronomical data creates both tremendous opportunity and a fundamental challenge: How do we train the next generation of astronomers to work effectively in this new landscape?

That's why this course exists. Not as a traditional programming course that ignores AI, nor as an AI course that skips fundamentals, but as something new—a course that teaches you to be an effective astronomical programmer in the age of AI assistance.




### The Paradox: Why Learn Coding When AI Can Code?

You might reasonably ask: "If AI can write code, why should I learn programming?" This is the central paradox of our time, and the answer shapes everything we'll do in this course.

Consider this scenario. You ask an AI to calculate the orbital period of an exoplanet, and it generates this code:

```python
import math

# Kepler's Third Law calculation
def orbital_period(semi_major_axis_au, star_mass_solar):
    """Calculate orbital period using Kepler's Third Law"""
    G = 6.67430e-11  # gravitational constant
    M_sun = 1.989e30  # solar mass in kg
    AU = 1.496e11    # astronomical unit in meters
    
    a = semi_major_axis_au * AU
    M = star_mass_solar * M_sun
    
    period_seconds = 2 * math.pi * math.sqrt(a**3 / (G * M))
    period_years = period_seconds / (365.25 * 24 * 3600)
    
    return period_years
```

The code looks reasonable. It has comments, uses scientific constants, and implements a familiar equation. But without understanding programming, you can't answer critical questions. Is the unit conversion correct? What happens if the star mass is given in Jupiter masses instead? Why might this give different results than your textbook formula? How would you modify it for a binary star system?

This is why we learn to code: not to compete with AI, but to collaborate with it effectively. Programming knowledge enables you to:

**Read and verify AI output** - When AI generates code using unfamiliar functions or libraries, you can trace through the logic and understand what's happening. You learn from AI's solutions while catching potential issues.

**Debug subtle errors** - AI code often runs without errors but produces wrong results. Unit confusion (milliarcseconds vs arcseconds), coordinate system mix-ups, or incorrect assumptions about data format are common. These aren't syntax errors Python catches—they require domain knowledge to spot.

**Decompose complex problems** - "Find variable stars in this dataset" is too vague for AI. But when you can break it down—load data, remove outliers, calculate variability metrics, apply thresholds—you can guide AI to build exactly what you need.

**Validate against physics** - Your intuition tells you when results seem wrong. Negative distances, stars brighter than supernovae, or orbits that violate Kepler's laws. With code understanding, you can add validation checks to catch these issues automatically.

**Learn from mistakes** - Every AI error becomes a learning opportunity. When you fix an AI's confusion between right ascension in hours versus degrees, you internalize that conversion. Debugging teaches deeper than memorization ever could.

Without these skills, you're limited to hoping AI understood your request correctly. With them, you become a true collaborator who can harness AI's power while ensuring scientific rigor.


### The Evolution: From Syntax to Logic

The way we teach programming has fundamentally changed. In the pre-AI era, students spent weeks memorizing exact syntax—was it `numpy.arcsin()` or `numpy.asin()`? Hours were lost to missing colons and incorrect indentation. Looking up documentation was constant. A single semester might cover just basic Python, and even then, students often felt overwhelmed by syntactic details.

Today, in the AI-augmented era, we focus on something different. Instead of memorizing whether it's `for i in range(len(array))` or `for item in array`, you learn to think "I need to iterate through each star and calculate its distance." Rather than remembering every matplotlib argument order, you understand that you need to create a figure, add axes, and plot your data. The emphasis shifts from syntax to logic, from memorization to understanding patterns.

The fundamental concepts remain unchanged. Loops still repeat operations, functions still encapsulate logic, arrays still store data efficiently. But AI handles the syntactic details while you focus on the scientific thinking. Think of it like the transition from hand-calculating logarithms to using calculators. We didn't stop teaching logarithms; we just stopped making students memorize log tables. Similarly, we're not abandoning programming education; we're freeing you from syntax memorization to focus on computational thinking.

This shift enables us to cover far more ground than traditional courses—basic Python, scientific computing with NumPy, data analysis with Pandas—we'll explore in one ambitious but manageable curriculum. This is only possible because AI eliminates the syntax struggles that traditionally consumed so much time and energy.



### Course Structure

This course follows a carefully designed progression. We begin with pure Python fundamentals, assuming no prior programming knowledge. In these early weeks, you'll learn about variables, lists, loops, and functions using everyday examples. As you build confidence with basic programming concepts, we'll gradually introduce scientific computing tools. NumPy arrays might initially seem abstract, but you'll soon see how they naturally represent time series observations or image data. Pandas DataFrames might appear complex at first, but they become intuitive when you realize they're perfect for stellar catalogs.

By the course's midpoint, astronomical applications become central. You won't just learn about Fourier transforms; you'll use them to find periods in variable star light curves. You won't just study database queries; you'll extract data from actual astronomical archives. The transition is deliberate and supportive—by the time you're analyzing real telescope data, you'll have the programming foundation to understand what you're doing and why.




### Your Learning Style, Your Choice

This course recognizes that students learn programming differently, and AI assistance creates new flexibility in your approach. Some of you will want to type every line yourself, using AI only for hints when stuck. This builds muscle memory and deep familiarity with syntax. If this describes you, use AI as a tutor who provides hints rather than solutions. Ask it "What's wrong with my approach?" instead of "Write this for me."

Others will prefer generating code with AI and then studying it carefully to understand how it works. This is equally valid! The key is active engagement—modify the code, break it intentionally to see what happens, combine pieces in new ways. Understanding code you didn't write is a crucial skill in collaborative research, where you'll often work with code from colleagues or previous students.

Most students find a middle ground, hand-coding simple functions to build intuition while using AI for boilerplate code, complex algorithms, or unfamiliar libraries. This mirrors how professional programmers actually work today. What matters isn't how much you type yourself, but how deeply you understand what's happening. Two students might produce identical code for analyzing a galaxy spectrum—one typing everything, another using AI extensively—but both should be able to explain why they chose this algorithm, what assumptions they're making, how to validate the results, and what could go wrong.



### The AI Quiz System

A unique feature of this course is our AI-administered quiz system, which comprises 40% of your grade. Starting from Lecture 2, you'll interact with an AI that generates personalized conceptual questions based on the previous lecture's material. This one-lecture delay gives you time to absorb and practice concepts before being tested.

Here's what makes our quiz system different from traditional programming tests. Rather than asking you to write code from scratch, the AI presents you with scenarios that test your understanding. It might show you code with a bug and ask why it fails. It might present two different approaches to storing astronomical data and ask you to explain the trade-offs. You might see a piece of code that modifies a list and be asked to predict what happens to other variables. The AI tests whether you understand *why* Python behaves the way it does, not whether you've memorized syntax.

For example, instead of "Write code to store star coordinates," the AI might ask: "You have `coords = (10.5, -30.2)` for a star's position. Why can't you do `coords[0] = 11.0`?" This tests whether you understand that tuples are immutable and why that matters for protecting data. Or it might show you code where someone writes `mags2 = mags` for a list of magnitude measurements, then modifies `mags2`, and ask you to explain why both lists changed. These questions reveal whether you grasp how Python handles memory and references.

Why this conceptual approach? Because in the real world with AI assistance, you'll rarely write code from scratch. Instead, you'll need to understand what AI generates, spot potential problems, choose between different approaches, and know why certain solutions work better than others. The quiz system prepares you for this reality. You have unlimited practice attempts, with the AI generating slightly different scenarios each time to reinforce concepts through variation. During class, you'll complete a graded submission in the final 10 minutes, demonstrating your understanding when it matters.

This isn't about memorization—it's about building mental models of how Python works. The AI quiz system recognizes that understanding comes from grappling with concepts, comparing approaches, and learning from mistakes. Just as you can't cram conceptual understanding the night before an exam, you can't fake your way through explaining why code behaves a certain way. Regular practice with immediate feedback builds real competence that goes beyond syntax to true understanding.




### Getting Help

Programming can be frustrating, especially when starting out. Error messages seem cryptic, code that should work doesn't, and sometimes you don't even know what question to ask. This is normal. Every professional programmer still encounters bewildering bugs. The difference is knowing where to get help.

Your first resource is the AI itself. Often, the AI can identify the issue immediately. But remember to understand the fix, not just apply it blindly.

Take advantage of office hours. The TAs hold office hours on Monday and Wednesday, complementing the Tuesday/Thursday lectures. This ensures help is available throughout the week. Come with specific questions when possible, but "I'm completely lost" is also a valid reason to attend. The TAs expect confusion—it's part of learning.

Use your classmates as resources. Create study groups, share debugging strategies, and learn from each other's approaches. Seeing how others solve problems broadens your problem-solving toolkit. Just remember that while collaboration on understanding is encouraged, submitted code should be your own work (though AI-assisted is fine).

Come prepared to code actively. Programming isn't a spectator sport—you learn by doing, making mistakes, and fixing them. Bring a laptop to class if possible, though you can also follow along and practice later. Most importantly, bring curiosity and patience. Everyone struggles at first, but with practice and the right tools, you'll be analyzing real astronomical data sooner than you think.




### Research Projects: 60% of Grade

The majority of your grade comes from three research projects that build progressively throughout the course. These aren't traditional homework assignments—they're opportunities to create real tools and analyses that you might actually use in astronomical research.

**Project 1 (Due ~Week 6):** Build AI-enhanced astronomical tools using LLM APIs. By this point, you'll have learned basic Python and how to interact with LLMs programmatically. The focus is on integrating AI as a component of larger systems.

**Project 2 (Due ~Week 11):** Statistical analysis and data fitting demonstration. You'll work with real astronomical datasets, applying statistical methods you've learned. The emphasis is on proper statistical methodology and clear visualization.

**Project 3 (Due ~Week 14):** Complete analysis pipeline using real astronomical data. This capstone project brings together everything you've learned. You'll start with data from actual telescopes or surveys, process it through multiple analysis steps, and present scientific conclusions. Think of it as a mini research paper implemented in code.

All projects are done in pairs. Collaborative coding is essential in modern astronomy—you'll rarely work alone on real research. Working with a partner teaches you to write readable code and divide complex problems into manageable pieces. You'll also present your projects to the class, explaining not just what you built but why you made specific design choices.

Documentation is crucial. Your project reports should explain how you used AI, what worked well, what failed, and what you learned. Critical evaluation of AI's contributions—including its mistakes—often earns bonus points. We want to see your thinking process, not just the final result.



## The Large Language Model Landscape for Astronomers

### AI, LLMs, and What We Really Mean

Throughout this course, we'll often say "AI" as shorthand, but let's be precise about what we mean. Artificial Intelligence encompasses everything from simple decision trees to complex neural networks. It includes the algorithms that classify galaxies in SDSS, the computer vision systems that identify asteroids, and the machine learning models that predict solar flares. 

What's revolutionizing programming education isn't AI broadly—it's specifically Large Language Models (LLMs). These are the systems like GPT, Claude, and Gemini that can understand and generate human language, including code. When we talk about "AI helping you code" in this course, we're talking about LLMs. They're trained on vast amounts of text and code from the internet, learning patterns of language and programming without explicitly being taught rules.

The distinction matters because LLMs have specific strengths and limitations. They excel at pattern recognition and can generate syntactically correct code in dozens of programming languages. They can explain complex concepts in simple terms and translate between different coding styles. But they don't actually run code, test hypotheses, or verify mathematical correctness. They predict what text should come next based on patterns they've learned. This is why they can generate beautiful code that violates conservation of energy or confuses astronomical coordinate systems.




### How LLMs Actually Work (The Simplified Version)

You don't need to understand neural networks to use LLMs effectively, but a basic mental model helps. Think of an LLM as having read millions of programming tutorials, Stack Overflow posts, GitHub repositories, and documentation pages. When you ask it a question, it's not searching a database or running calculations. Instead, it's predicting what a helpful response would look like based on all those patterns it has seen.

This explains both the magic and the limitations. The magic: an LLM can write a function to process FITS files because it has seen thousands of examples. The limitations: it might confidently mix up details from different examples or generate plausible-sounding nonsense for unusual requests. It's like a very well-read colleague who can quickly sketch solutions but might misremember specifics.

Understanding this helps you interact with LLMs more effectively. Instead of treating them as infallible oracles, you treat them as knowledgeable but imperfect collaborators. You verify their suggestions, especially for domain-specific details. You provide context about your specific problem. You iterate and refine rather than expecting perfect solutions on the first try.




### Beyond Chatbots: LLMs as Programming Infrastructure

Most people first encounter LLMs through chatbots like ChatGPT, having conversational interactions where they type questions and receive answers. This is just the tip of the iceberg. As you'll learn in this course, particularly in Lecture 7, LLMs can be integrated directly into your programming workflow through APIs (Application Programming Interfaces). In fact, we encourage you to build your first Research Project assignment with LLM APIs—so even by week 4 you should have a transformed understanding of LLMs.

Instead of copying and pasting between a chat window and your code editor, you can write Python scripts that automatically send problems to an LLM and process its responses. Imagine analyzing a thousand galaxy spectra and having an LLM help generate custom fitting functions for each one. Or building a system that automatically documents your code by asking an LLM to explain what each function does. Or creating a tool that translates astronomy papers into executable analysis pipelines.

This programmatic access transforms LLMs from assistants into components of your computational infrastructure. You might use traditional code for numerical calculations, SQL for database queries, and LLMs for tasks involving natural language or code generation. Learning basic Python enables you to orchestrate all these tools together, which is far more powerful than using them separately.



### The Current Players

The LLM landscape changes rapidly, with new models released every few weeks. Here are the major models you'll encounter as of 2025:

- **OpenAI's GPT models** (ChatGPT, latest GPT-5)
- **Anthropic's Claude** (latest Claude 4.1)
- **Google's Gemini** (latest Gemini 2.5)
- **Meta's Llama** (open source, LLaMA 4)
- **Mistral**
- **DeepSeek** (latest DeepSeek 3.1)
- **Qwen** (latest Qwen 3)

Each model has its own interface and API access. They all handle Python programming well enough for this course. The landscape evolves quickly—new models appear, existing ones improve, and capabilities that seem impressive today become standard tomorrow. Rather than picking a "best" model, you'll likely use different ones for different purposes as you discover what works for your workflow.




### Effective Prompting Guidelines

The key to getting helpful AI assistance is clear, specific communication. Here are guidelines that work well:

**Be specific about your goal.** Instead of "fix this," try "this function should convert RA from hours to degrees but returns negative values for RA > 12 hours."

**Provide context.** Rather than "write a function to process data," try "write a function that takes a list of stellar magnitudes and returns normalized values between 0 and 1, handling missing data as NaN."

**Include constraints.** Mention if you need to use specific libraries or avoid certain approaches: "optimize this loop using NumPy vectorization, not list comprehension."

**Ask for explanations.** When learning, request "explain why this approach works" or "what are the trade-offs of this solution?" Understanding is more valuable than just getting working code.

While these prompting strategies will become second nature as you use AI tools throughout the course, you'll see them in action most directly when working with code editors and development environments that integrate AI assistance.




### Practical Considerations for This Course

For this course, you don't need paid subscriptions to these services. Most AI coding tools use many of these same models (GPT, Claude, Gemini, and others) as their backbone, providing integrated coding assistance. However, having direct access to at least one standalone chatbot helps you understand different interaction modes and develop broader LLM literacy.

Google's Gemini offers 1 year free for students with .edu email verification at [gemini.google/students](https://gemini.google/students) - this is an excellent option that provides full access through the entire course and beyond. Most other major LLMs (ChatGPT, Claude, Llama, Mistral, DeepSeek, Qwen) offer free tiers that are more than adequate for the basic coding tasks we'll cover in this course. The free versions typically have usage limits but provide enough capacity for learning and experimentation.

As you progress, you might find certain models work better for your specific needs. Trying out and experimenting with different models and understanding their limitations is valuable—just like your colleagues have different strengths and weaknesses. The course is designed to be model-agnostic—the concepts you learn apply regardless of which LLM you use.

Understanding these boundaries helps you use LLMs as effective tools rather than hoping they'll magically solve all problems. In the following sections, we'll see how to set up our programming environment to work effectively with these AI collaborators.




## Setting Up Your Python Environment

### Why Anaconda?

To write Python code, you need Python installed on your computer. While you could install Python directly from python.org, we're going to use something called Anaconda. Why? When you install regular Python, you get just the core language. Need to plot data? Install matplotlib. Need arrays? Install NumPy. Need to read FITS files? Install astropy. Each installation might fail due to missing dependencies or version conflicts. Anaconda solves this by bundling everything scientists typically need—over 300 packages including NumPy, Pandas, Matplotlib, SciPy, Jupyter, and more—all tested to work together. It's the difference between buying a computer with all software pre-installed versus having to install each program yourself.




### Installing Anaconda

Go to https://www.anaconda.com/download to get Anaconda. The website will detect your operating system and show the appropriate installer. Download the full Anaconda Distribution (not Miniconda)—it's about 800 MB because it includes hundreds of packages.

Follow the installation instructions on the download page for your operating system. The installation takes about 5-10 minutes.

**Important:** Make sure to complete this installation before our next lecture, as we'll jump straight into coding in Lecture 2!




### Understanding the Terminal

After installation, we need to briefly use something called a terminal (or command line) to verify Python is working. Don't worry—this might look intimidating with its text-only interface, but we'll only use it for a few simple checks. In the rest of the course, we'll primarily work in more user-friendly environments.

The terminal is simply a text-based way to interact with your computer. Instead of clicking icons, you type commands. Think of it as texting with your computer—you send it a message (a command), and it responds with text.

On Windows, Anaconda installs something called "Anaconda Prompt"—look for it in your Start Menu. On Mac, you'll use the Terminal app (find it in Applications > Utilities). On Linux, you already know what a terminal is if you're using Linux!




### Verifying Your Installation

Let's verify everything works. Open Anaconda Prompt (Windows) or Terminal (Mac/Linux)—if on Mac/Linux, make sure to open a new terminal window for the installation changes to take effect.

In the terminal, type this command and press Enter:

```bash
python --version
```

You should see something like `Python 3.13.5`. The exact version doesn't matter as long as it's Python 3.x (likely 3.11 or newer with recent Anaconda distributions).

Next, verify that Anaconda's package manager works:
```bash
conda --version
```

This should show something like `conda 25.5.1`.

If both commands work, your installation is successful! While we used the terminal for these checks, don't worry—for the rest of the course, we'll primarily use more visual and user-friendly tools. The terminal is just our way of checking that the foundation is solid.



### Your First Python Program

Let's verify everything works with a simple astronomical calculation. Open Anaconda Prompt (Windows) or Terminal (Mac/Linux) and type `python` to start Python:

```bash
python
```

You'll see something like:
```
Python 3.13.5 | packaged by Anaconda | (main, Jun 2025) 
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` is Python's prompt, waiting for your commands. Type this line by line:

```python
import math
parallax_mas = 742  # Alpha Centauri's parallax in milliarcseconds
distance_pc = 1000 / parallax_mas
print(f"Alpha Centauri is {distance_pc:.2f} parsecs away")
```

You should see: `Alpha Centauri is 1.35 parsecs away`
 
To exit Python, type `exit()` or press Ctrl+D (Mac/Linux) or Ctrl+Z then Enter (Windows).
 
While we just used Python in the terminal, this is just for verification. Throughout the course, we'll primarily use more advanced tools. The terminal is just our way of checking that the foundation is solid.




### Saving and Running Python Scripts

While we just ran Python interactively in the terminal, most real programs are saved in files with a `.py` extension. These are called Python scripts, and they're just plain text files containing Python code.

#### Creating Your First Script

Open any text editor (Notepad on Windows, TextEdit on Mac). Create a new file and type:

```python
# my_first_script.py
# Calculate distance to Proxima Centauri

print("Distance Calculator")
print("==================")

parallax_mas = 768.13
distance_pc = 1000 / parallax_mas

print("Proxima Centauri parallax:", parallax_mas, "milliarcseconds")
print("Distance:", distance_pc, "parsecs")
```

Save this file as `my_first_script.py` in a folder you can find (perhaps create an `astro1221` folder).

#### Running Python Scripts

To run your script, navigate to the folder containing your file using the terminal:

```bash
cd path/to/your/astro1221/folder
```

Then run:

```bash
python my_first_script.py
```

You should see:
```
Distance Calculator
==================
Proxima Centauri parallax: 768.13 milliarcseconds
Distance: 1.3016963654049273 parsecs
```

That's it! You've created and run your first Python program. The key insight: Python code can be saved in `.py` files and run anytime, rather than typing everything interactively each time.

#### Script Files vs Interactive Mode

So far we've seen two ways to run Python:
- **Interactive mode**: Type `python` in terminal, then enter commands one at a time
- **Script files**: Save code in `.py` files and run the whole file at once

Scripts are better when you want to save your work and run it again later. Interactive mode is great for quick calculations or testing single lines. As we continue in this course, you'll learn even more powerful ways to write and run Python code.




### Understanding Package Managers: pip vs conda

As you progress in Python, you'll need to install additional packages—pre-written code that adds functionality. Anaconda provides two ways to install packages: `conda` and `pip`.

**conda** is Anaconda's package manager. It installs packages from Anaconda's curated repositories. The big advantage: conda manages not just Python packages but also the non-Python libraries they depend on. If a package needs a specific C++ library, conda handles it.

**pip** is Python's standard package installer. It accesses PyPI (Python Package Index). Some cutting-edge or specialized astronomy tools appear on PyPI first.

When do you use which? Simple rule: try conda first, use pip when necessary. If conda can't find a package, it will tell you "PackageNotFoundError"—that's when you try pip.

For astronomy-specific packages, sometimes you might need to specify the conda-forge channel:

```bash
conda install -c conda-forge astroquery
```

**conda-forge** is a community-led repository that provides a wider variety of packages than the default Anaconda repository. Think of it as a community library that supplements the official Anaconda collection. Many specialized scientific packages, including astronomy tools, are maintained there by the researchers who use them.

### Installing Additional Packages

While Anaconda includes most packages you'll need, here's how to install extras when needed:

```bash
# Using conda (preferred when available)
conda install package_name

# Using conda-forge for specialized scientific packages
conda install -c conda-forge package_name

# Using pip (when conda doesn't have it)
pip install package_name
```

For example:
```bash
# Standard scientific packages - usually in default conda
conda install scipy

# Astronomy packages - often in conda-forge
conda install -c conda-forge astroquery

# Cutting-edge packages - might only be on pip
pip install batman-package  # For exoplanet transit modeling
```
## Introduction to Jupyter Notebooks
 
### What Are Jupyter Notebooks?
 
Imagine writing a research paper where your paragraphs of explanation, mathematical equations, plots, and calculations all live in the same document, and the calculations actually run. That's a Jupyter notebook. It's an interactive document that combines text, code, equations, and visualizations in a single file that you can share with others.
 
The name "Jupyter" comes from combining Julia, Python, and R—three programming languages it supports—though we'll use it exclusively for Python. Jupyter mirrors how we actually think about problems. You don't just write code in isolation; you explain your reasoning, show your equations, run calculations, plot results, and interpret them, all in a natural flow.
 
Think of the difference between a traditional script and a notebook like the difference between a calculator and a lab notebook. A calculator (or script) just computes. A lab notebook documents your thinking, shows your work, includes sketches and notes, and tells a story. That's what Jupyter provides for computational work.
 
In fact, this very lecture note you're reading is written as a Jupyter notebook! Notice how it seamlessly combines explanations with executable code examples. This demonstrates exactly what makes Jupyter so powerful for astronomical work—you can document your thinking, show your calculations, and share your results all in one place.
 
### Launching Jupyter
 
Since you installed Anaconda, Jupyter is already on your computer. To launch it, open Anaconda Prompt (Windows) or Terminal (Mac/Linux) and type:

```bash
jupyter notebook
```

Press Enter, and two things happen. First, your terminal starts a local server (don't worry about what this means—just know Jupyter is running). Second, your default web browser opens to show the Jupyter interface. Yes, Jupyter runs in your web browser, but it's not on the internet—it's running locally on your computer, using the browser as its interface.

You'll see a file browser showing your computer's folders. Navigate to where you want to work (maybe create a folder called `astro1221` for this course), then click "New" → "Python 3" to create your first notebook.



### The Two Types of Cells

A Jupyter notebook consists of cells—individual units that contain either text or code. Understanding these two cell types is essential.

**Markdown cells** contain formatted text. They're where you write explanations, document your thinking, and provide context. Markdown is a simple formatting language where `**bold**` makes text bold, `*italic*` makes it italic, and `#` creates headers. But the real power for astronomy is that markdown cells support LaTeX for mathematical notation.

**Code cells** contain Python code that actually runs. When you execute a code cell (by pressing Shift+Enter), Python runs that code and shows the output directly below the cell. This immediate feedback makes Jupyter perfect for exploration and learning.

To see the difference, click on an empty cell and change its type using the dropdown menu that says "Code". Try changing it to "Markdown", type some text, and press Shift+Enter to render it. Change another cell to "Code", type `print("Hello astronomy!")`, and press Shift+Enter to run it.




### Mathematical Notation with LaTeX

One reason astronomers love Jupyter is its seamless LaTeX integration. In any markdown cell, you can write mathematical equations that render beautifully. Surround inline math with single dollar signs: `$v = H_0 d$` becomes $v = H_0 d$. For displayed equations, use double dollar signs:

```
$$L = 4\pi R^2 \sigma T^4$$
```

This renders as a centered equation showing the Stefan-Boltzmann law. You can write complex equations with subscripts, superscripts, Greek letters, and special symbols:

```
$$\Omega_\Lambda + \Omega_m + \Omega_k = 1$$
```

This ability to mix explanatory text, properly formatted equations, and executable code makes Jupyter notebooks ideal for astronomical calculations. You can derive an equation in LaTeX, implement it in code, and plot the results, all in one document.




### Documentation Through Structure: Comments vs Markdown

In traditional Python scripts, you document code with comments—lines starting with `#` that explain what the code does. In Jupyter notebooks, you have a more powerful approach: the combination of markdown cells and code comments creates layered documentation.

Use **markdown cells** for the big picture. Before a code cell, add a markdown cell explaining what you're about to calculate, why this approach makes sense, and what equations you're implementing. This high-level documentation helps readers understand your scientific reasoning.

Use **code comments** for the implementation details. Within your code cells, add comments that explain specific lines:

```python
# Load parallax data from Gaia DR3
parallax_mas = 768.13  # milliarcseconds
parallax_error = 0.05   # measurement uncertainty

# Convert parallax to distance using d = 1/p relationship
# Note: parallax in mas, so multiply by 1000 for parsecs
distance_pc = 1000 / parallax_mas
```

For longer explanations within code cells, you can also use triple quotes `'''` to create multi-line comments. While single-line comments starting with `#` are perfect for brief explanations, triple quotes are useful when you need several lines of explanation:

```python
'''
This section calculates stellar luminosity using the Stefan-Boltzmann law.
We start with surface temperature and radius measurements,
then compute the total energy output across all wavelengths.
The result will be in solar luminosities for easy comparison.
'''
```

This approach keeps longer documentation close to the relevant code while maintaining clean separation between explanation and implementation.

This dual-layer approach—markdown for "why" and comments for "how"—makes your notebooks self-documenting. Someone reading your notebook months later (often yourself!) can understand both the scientific logic and the computational implementation.

The notebook format naturally encourages good documentation habits. Because you're already switching between markdown and code cells, adding explanation becomes part of the workflow rather than an afterthought. Your future self will thank you when revisiting old analyses.




### Running Terminal Commands from Notebooks

Sometimes you need to run terminal commands without leaving your notebook. Jupyter provides a neat trick: prefix any terminal command with `!` and it runs in the system shell. This is useful for installing packages or checking your environment:

```python
!python --version
```

```python
!conda list numpy
```

```python
!pip install --upgrade astropy
```

The exclamation mark tells Jupyter "this isn't Python code, it's a terminal command". This feature is particularly handy when you're in the middle of analysis and realize you need to install a package—no need to switch to a separate terminal window.



### Notebook Best Practices

As you work with notebooks, you'll develop your own style, but here are practices that make notebooks more useful and shareable.

Run cells in order. Jupyter lets you run cells in any order, but this can create confusion. If cell 5 defines a variable that cell 2 uses, running them out of order causes errors. When sharing a notebook, always "Restart and Run All" from the Kernel menu to ensure it works from top to bottom.

Balance code and explanation. A notebook full of code with no explanation is hard to follow. A notebook that's all text with no code isn't useful. Aim for a narrative flow where each code cell has enough context to understand its purpose.

Keep cells focused. Each code cell should do one logical thing. Don't write hundred-line cells that do everything; break them into logical steps. This makes debugging easier and helps readers follow your thinking.

Save frequently. Jupyter auto-saves, but explicitly save (Ctrl+S or Cmd+S) after important changes. Your notebook is just a file with extension `.ipynb`, perfect for sharing projects and documentation.

For now, practice creating a simple notebook. Try mixing markdown explanations with code cells. Write some equations in LaTeX. Run some basic Python calculations. Get comfortable with the Shift+Enter rhythm of executing cells. This environment will be your computational laboratory throughout the course.



## Modern IDE: Cursor

### What is an IDE?

An IDE (Integrated Development Environment) is a sophisticated text editor designed specifically for programming. Unlike basic text editors, IDEs provide features that make coding more efficient: syntax highlighting to spot errors, autocomplete for function names, integrated documentation, and debugging tools. These features transform coding from tedious trial-and-error into structured problem-solving.

Cursor takes the IDE concept further by integrating AI assistance directly into the editor. Instead of switching between your code and a separate chatbot, you have AI help exactly where you're writing. This integration makes the AI aware of your entire project context, not just the current line you're typing.




### Getting Cursor for Free as a Student

Cursor offers students one full year of Cursor Pro completely free (normally $20/month). To get access:

1. Download Cursor from cursor.com and install it
2. Create an account using your osu.edu email address (or your university email)
3. Go to https://cursor.com/students and click "Verify Status"
4. The Pro features activate automatically after verification

With the student Pro plan, you get 500 fast premium requests per month plus unlimited slower requests—more than enough for coursework and projects.



### Core AI Features

Cursor's AI assistance comes in three main forms, each serving different purposes in your workflow.

**Inline completion** appears as you type. When you start writing `distance_pc = `, Cursor might suggest `1000 / parallax_mas` in gray text because it understands you're calculating stellar distance. Press Tab to accept or keep typing to ignore. You can toggle this feature on or off using the status bar at the bottom of the window. Experiment with having it on versus off to find what helps your learning—sometimes the constant suggestions help, sometimes they're distracting when you're trying to think through logic yourself.

**Chat interface (Cmd+L or Ctrl+L)** lets you have conversations about your code. Highlight problematic code first, then press the shortcut to ask questions like "Why does this return negative values?" or "How can I make this more efficient?" You can switch between different AI models (GPT-5, Claude, etc.) using the dropdown at the top of the chat panel—experiment to find which model works best for different tasks. The AI sees your highlighted code plus your entire project context, making its responses more relevant than generic chatbots.

**Edit mode (Cmd+K or Ctrl+K)** rewrites code while you watch. Highlight a function, press the shortcut, and type instructions like "add error handling for missing data" or "vectorize this loop using NumPy." Like with chat, you can select different AI models from the dropdown menu—some models are better at refactoring, others at generating new code. Cursor shows proposed changes in a diff view where additions appear in green and deletions in red. You can accept all changes at once or selectively accept specific parts.

With your student account, you have access to multiple AI models across all these features—chat, edit mode, and inline completion. The ability to switch models is particularly powerful because different models have different strengths. Some excel at explaining complex concepts, others at generating clean code, and still others at debugging tricky problems. Experiment with different models to build intuition about when to use each one. While the default setup works well for most people, exploring these options will help you find the most effective workflow for your learning style and the specific challenges you encounter in astronomical data analysis.


### The Importance of Typing Code Yourself

A [recent study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) from METR (July 2025) found something surprising: experienced developers using AI tools were actually about 20% slower at completing tasks, despite believing they were 20% faster. The study involved 16 experienced open-source developers working on their own projects with state-of-the-art AI tools including Cursor and Claude. While such studies always have limitations and the AI landscape changes rapidly, the finding highlights an important point: typing code yourself remains crucial for both learning and efficiency.

Why does typing matter? When you type the beginning of a function or the structure of a loop, you're thinking through the logic. You're deciding what variables you need, what the flow should be, how pieces connect. This mental engagement is where real learning happens. AI can then amplify your productivity by handling syntax details, suggesting completions, and catching errors.

Comments are particularly powerful for guiding AI. When you type out comments explaining what you plan to do, the AI understands your intent much better:

```python
def calculate_distance(parallax_mas):
    # Convert milliarcseconds to arcseconds first
    parallax_as = 
```

Now Cursor sees you want to convert units and can suggest `parallax_mas / 1000`. Or when working with lists:

```python
magnitudes = [15.2, 15.3, 15.1, 15.4]
# Calculate the average magnitude
average = 
```

The comment tells Cursor your specific goal, so it can suggest `sum(magnitudes) / len(magnitudes)` rather than some other operation. You've shown it your variable names and your intent. The AI completion will be more relevant and you'll understand it better because you set up the framework.

This approach—typing enough to establish intent, then using AI for assistance—builds genuine programming skill. You develop intuition for code structure, learn common patterns, and understand why solutions work. The AI quiz system you'll use throughout this course is designed to sharpen exactly these skills, testing your understanding of logic and structure rather than memorization. Combined with the research projects where you'll build real tools, this forms the core learning approach of the course.




### Working with Jupyter Notebooks in Cursor

Cursor can open and edit Jupyter notebooks (.ipynb files) directly. When you open a notebook in Cursor, it displays with familiar markdown and code cells, but now with AI assistance available throughout. You can ask the AI to explain cells, debug errors, or generate new analysis code while maintaining the notebook's structure. For this course, we'll primarily work with notebooks inside Cursor, combining structured documentation with intelligent code assistance.




### Getting Started

After installing Cursor with your student account, start by opening the Jupyter notebook you created earlier. Try these exercises to get comfortable:

1. Type a comment describing what you want to calculate and see what Cursor suggests
2. Practice using Cmd+L to ask questions about Python concepts
3. Toggle autocomplete on and off to see which mode helps you learn better

The more you use Cursor's features, the more natural they become. Throughout this course, Cursor will be your primary development environment, helping you focus on astronomical concepts while the AI handles routine syntax.

While Cursor accelerates coding, it shares the limitations of all LLMs. It might suggest code that seems correct but contains subtle errors. This is why understanding Python remains essential. Cursor helps with implementation, but you must verify the code. Always validate results against known references and test edge cases. The AI is a powerful tool, but you're the astronomer ensuring correctness.




## Academic Integrity in the Age of AI

Since this course encourages AI use, we need clear guidelines about academic integrity. The key principle is simple: use AI as a tool, not a substitute for understanding.

For the weekly quizzes, you'll use only the provided AI quiz system during the in-class period. No external chatbots or AI tools during graded attempts—the quiz bot is designed to guide you appropriately. Practice sessions outside class are unlimited and encouraged.

For projects, document how you used AI in your project report or notebook. Describe what you asked AI to help with, what approaches you tried, and critically evaluate the code it generated. Did the AI's solution work immediately? Did you need to fix errors or improve efficiency? What did you learn from the interaction? This documentation helps us understand your learning process, and thoughtful analysis of AI's strengths and limitations often earns bonus points.

Most importantly, think critically about AI-generated code. Does it make physical sense? Are the units correct? Could it be more efficient? You must be able to explain every line of code you submit. If asked about your project code during presentations, you should understand not just what the code does, but why that approach was chosen.

By following these guidelines, you'll develop genuine programming skills while leveraging AI's power responsibly. This approach will serve you well in research, where understanding your tools is as important as the results they produce.



