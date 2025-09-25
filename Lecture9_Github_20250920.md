---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region -->
# GitHub and Professional Coding Development

*Tutorial by Yuan-Sen Ting*

*Astron 1221: Lecture 9*

*A sample GitHub repository following the instructions in this tutorial can be found at [https://github.com/tingyuansen/Astron1221_Github_Tutorial](https://github.com/tingyuansen/Astron1221_Github_Tutorial)*
 

## Introduction: Your Code Deserves Better Than Your Desktop

### The Midnight Crisis

It's 2 AM. You've been working on your Project 1 analysis for the past six hours. Your LLM function tools finally work perfectly, your RAG system is finding the right documents, and the API calls are returning exactly what you need. You save your file—`llm_project_FINAL_working.py`—and close your laptop with satisfaction.

The next morning, disaster strikes. Your laptop won't turn on. That beautiful code, those carefully crafted function schemas, that clever embedding search you figured out at 1:47 AM—all of it exists only on a dead hard drive.

This scenario has happened to countless students. Today, we ensure it never happens to you.

### From Desktop to Universe

Over the past four weeks, you've built an impressive foundation. You've mastered Python fundamentals, created NumPy arrays that slice through data like light through a prism, visualized patterns with matplotlib, and just last week, you taught Claude to execute your calculations and search through documents. But right now, all of that work lives in isolation on your computer—invisible to advisors, inaccessible to collaborators, and vulnerable to a single spilled coffee.

Today changes everything. By the end of this lecture, your code will be:
- **Safe**: Backed up automatically in the cloud
- **Shareable**: Accessible to collaborators with a single link  
- **Professional**: Part of your academic portfolio
- **Discoverable**: Visible to the global programming community

And here's the best part: you'll do all of this without leaving Cursor. No complex terminal commands, no arcane git incantations—just clicks, commits, and code that lives forever in the cloud.
<!-- #endregion -->

### Why Your Code Needs a Home

Think about how you currently manage your code files. If you're like most students four weeks into programming, you probably have:
- Multiple versions of the same file scattered across folders
- Files named `project_v1.py`, `project_v2_fixed.py`, `project_final_ACTUALLY_FINAL.py`
- That one working version you're afraid to modify because you might break it
- Code you emailed to yourself "just in case"

Professional programmers and researchers solved this problem decades ago with a tool called Git, and today you'll learn to use it—not through intimidating command lines, but through Cursor's friendly interface.

### What You'll Build Today

By the end of this lecture, you'll transform your Project 1—whether it's a stellar parallax calculator, an LLM function tool system, or a RAG document searcher—into a professional repository that:

1. **Lives safely in the cloud**: Your code survives even if your laptop doesn't
2. **Shows your journey**: Every change you made, when you made it, and why
3. **Builds your portfolio**: A professional presence that grad schools and employers can see
4. **Enables collaboration**: Share your code with a link instead of a zip file
5. **Hosts documentation**: Turn your README into a website showcasing your work

The best part? Every astronomy researcher, from grad students to seasoned researchers, uses these exact same tools. The skills you learn today will serve you throughout your entire scientific career.

Let's begin by understanding what Git and GitHub actually are—two related but distinctly different tools that, together, will revolutionize how you work with code.


## Part 1: Understanding Git and GitHub (Starting from Zero)

### What is Git? What is GitHub?

Let's clear up the confusion right away—Git and GitHub are not the same thing, though they work beautifully together.

**Git** is a version control system that runs on your computer. Think of it as a highly sophisticated "undo" system that:
- Remembers every change you've ever made to your code
- Lets you travel back in time to any previous version
- Tracks who changed what, when, and why
- Works entirely on your local machine (no internet required)

**Why is it called "Git"?** The name was chosen by Linus Torvalds (who also created Linux) when he built Git in 2005. In British slang, "git" is a mild insult meaning "unpleasant person"—Torvalds jokingly named it after himself! He also said it can stand for any acronym you like: "Global Information Tracker" when it's working well, or "Goddamn Idiotic Truckload of sh*t" when it breaks. The name stuck because it's short, easy to type, and impossible to confuse with existing commands.

**GitHub** is a website that hosts Git repositories in the cloud. Think of it as:
- Google Drive, but specifically designed for code
- A social network for programmers
- A backup service that saves your Git history online
- A collaboration platform where multiple people can work on the same code

Here's the key relationship: Git tracks your changes locally, GitHub stores those changes online.

### Why Version Control Is Revolutionary

You've actually seen Git-like behavior in many tools you use daily. When you edit a Google Doc, it automatically saves every change—you can click "Version history" to see who wrote what and when. Overleaf does the same for LaTeX documents. These tools use the same principle as Git: instead of saving entire copies of your document, they save only the *differences* between versions.

This approach is brilliant because:
- **It's lightweight**: Storing differences takes far less space than storing full copies
- **It's informative**: You can see exactly what changed between any two versions
- **It's collaborative**: Multiple people can work on the same document without chaos

Git brings this power to your code. And while it might seem like extra work at first, it becomes essential when you're working on larger projects. Imagine working on a telescope control system with 10 people, or contributing to astropy with 100+ developers worldwide—without version control, it would be chaos!

### A Simple Analogy

Imagine you're writing a research paper:
- **Git** is like keeping a detailed lab notebook where you record every draft, every edit, and every revision with timestamps and notes about why you made each change
- **GitHub** is like a library where you can publish your lab notebook so others can read it, learn from it, and even suggest improvements

You can use Git without GitHub (just keeping your version history local), but you can't use GitHub without Git (GitHub needs Git's version tracking to work).


### Why Scientists Need Version Control

Let's be honest about how you currently save your work. You probably have a folder that looks something like this:

```
Project1/
├── llm_tools.py
├── llm_tools_backup.py
├── llm_tools_old.py
├── llm_tools_v2.py
├── llm_tools_v2_fixed.py
├── llm_tools_v2_final.py
├── llm_tools_v2_final_ACTUALLY_WORKING.py
├── llm_tools_v2_final_submitted.py
└── test.py
```

We've all been there. But this approach fails us in critical ways:

**The Problems with "Save As" Science:**
1. **Which version actually works?** You know `v2_final_ACTUALLY_WORKING.py` was good, but what exactly did you change from `v2_final.py`?
2. **When did that bug appear?** Something broke between Tuesday and Thursday, but you have no idea what you changed
3. **Why did you make that change?** Three weeks later, you can't remember why you commented out that section
4. **How do you share specific versions?** Your advisor wants to see "the version from last week's meeting"—which file is that?
5. **How do you merge improvements?** Your collaborator fixed one bug while you fixed another—now what?

**Git Solves All of This:**
- Every change is tracked with a timestamp and a description
- You can see exactly what changed between any two versions
- You can return to any previous state instantly
- Multiple people can work on the same code without chaos
- You have a complete history of your project's evolution

For astronomers specifically, this means tracking the evolution of your analysis, documenting every decision in your data processing, and creating reproducible research that others can verify and build upon.


### Creating Your First GitHub Account

Before we dive into version control, you need a GitHub account. This isn't just another website signup—this will become part of your professional identity as a researcher and programmer.

**Step 1: Sign Up at GitHub**

Navigate to [https://github.com/signup](https://github.com/signup) and follow the signup process. GitHub will ask you for:
- A username (choose wisely—see below!)
- Your email address (you can add your .edu email later)
- A password (make it strong and unique)
- A verification puzzle to prove you're human

**Choosing Your Username Wisely**

Your GitHub username will follow you throughout your career. It will appear on:
- Every piece of code you share
- Research papers that cite your software
- Your CV and grad school applications
- Professional collaborations

Choose something professional and memorable:
- ✅ Good: `jsmith-astro`, `maria-chen`, `stellar-observer`
- ❌ Avoid: `cooldude420`, `temporary123`, `ihatephysics`

Many astronomers use variations of their real name, making it easier for colleagues to find their work. Remember, you can't easily change this later without breaking links to your repositories.

**Setting Up Your Profile for Academia**

Once you've created your account, click on your avatar in the top-right corner and select "Your profile". Add:
- Your real name (so people can find you)
- Your university affiliation
- A brief bio mentioning your interests (e.g., "Astronomy undergraduate interested in stellar variability and computational methods")
- Your location (optional)
- A link to your university webpage or LinkedIn (if you have one)

**Quick Note: Student Benefits**

As a student with a `.edu` email, you're eligible for free GitHub Pro features through the Student Developer Pack at [education.github.com/pack](https://education.github.com/pack). This includes unlimited private repositories and other perks, but the free GitHub account is perfectly fine for this course. You can explore student benefits later if interested.


## Part 2: Git Basics in Cursor

### Cursor's Built-in Git Magic

When professional developers use Git, they often type commands in a terminal that look like cryptic incantations: `git add -A && git commit -m "message" && git push origin main`. These commands are powerful, but also intimidating for beginners.

Here's the beautiful thing: Cursor has built-in Git support that handles all of this complexity for you. Instead of memorizing commands, you'll use buttons and visual indicators. It's like the difference between using a modern camera app on your phone versus manually adjusting f-stops and shutter speeds—both take photos, but one is much friendlier for beginners.

**Finding the Source Control Panel**

Open Cursor and look at the left sidebar. If you don't see the sidebar, press `Cmd+B` (Mac) or `Ctrl+B` (Windows) to toggle it. You'll see several icons along the left edge:
- 📁 Explorer (files)
- 🔍 Search
- **📊 Source Control** (looks like a branch/fork icon) ← This is where the Git magic happens
- ▶️ Run and Debug
- 🧩 Extensions

Click on the Source Control icon. This panel is your command center for all things Git.

**First: Create a Folder for Your Project**

Before we can use Git, we need a folder to track. You have two ways to do this:

**Method 1: Using File Menu**
1. Click File → Open Folder (or press `Cmd+O` on Mac, `Ctrl+O` on Windows)
2. Navigate to your Desktop or Documents folder
3. Click "New Folder" and name it something like `my-first-repo` or `project1-github`
4. Click "Open" to open this folder in Cursor

**Method 2: Using Explorer (More Visual)**
1. If you already have Cursor open, click the Explorer icon (📁) in the sidebar
2. If you have a parent folder open, right-click in the Explorer panel
3. Select "New Folder" from the context menu
4. Name your folder and press Enter
5. You can also right-click to create "New File" when needed

The Explorer's right-click menu is powerful—you can:
- **New File**: Create any type of file (.py, .md, .txt, etc.)
- **New Folder**: Organize your project with subdirectories
- **Rename**: Change file or folder names
- **Delete**: Remove files (be careful!)
- **Copy/Paste**: Duplicate files or move them around

**What You'll See in Source Control**

With your new folder open, click on the Source Control icon. You'll see:

```
CHANGES

The folder currently open doesn't have a Git repository. 
You can initialize a repository which will enable source 
control features powered by Git.

[Initialize Repository]

You can directly publish this folder to a GitHub 
repository. Once published, you'll have access to 
source control features powered by Git and GitHub.

[Publish to GitHub]
```

You have two options here:
- **Initialize Repository**: Creates a local Git repository on your computer only
- **Publish to GitHub**: Creates a repository and immediately connects it to GitHub

For now, let's choose **Initialize Repository** to understand the basics first. We'll connect to GitHub in the next section.

<!-- #region -->
### Your First Repository

Now let's initialize your repository and understand what happens.

**Step 1: Initialize the Repository**

Click the blue "Initialize Repository" button. Something magical just happened—though you might not see much change at first. Cursor has created a hidden folder called `.git` inside your project folder. This hidden folder is where Git stores all the history of your project.

**Step 2: Create Your First File**

Let's create something to track:
1. Click on the Explorer icon (📁) in the sidebar to switch from Source Control to the file view
2. In the Explorer panel, right-click in the empty space
3. Select "New File"
4. Name it `hello_astronomy.py`
5. Add this simple code:

```python
# My first tracked Python file
import numpy as np

def calculate_distance(parallax_arcsec):
    """Calculate distance from parallax."""
    return 1.0 / parallax_arcsec

# Test with Proxima Centauri
distance = calculate_distance(0.768)
print(f"Distance to Proxima Centauri: {distance:.2f} parsecs")
```

**Step 3: Watch the Source Control Panel React**

Save the file (`Cmd+S` or `Ctrl+S`), then click the Source Control icon (📊) to switch back. You can toggle between these panels anytime—Explorer for managing files, Source Control for managing versions. 

In Source Control, you'll now see:

```
CHANGES (1)
  U  hello_astronomy.py
```

The "U" stands for "Untracked"—Git sees this new file but isn't tracking it yet. The file name might also appear in green, indicating it's new.

**Understanding the Git Workflow: Stage and Commit**

Think of Git like taking photographs of your project's progress:

- **Working Directory**: This is your project folder where you actively edit files—like setting up a scene for a photo
- **Staging Area**: This is where you select which changes to include in your next snapshot—like choosing which people to include in a group photo
- **Repository History**: This is your album of all past snapshots—permanent records of your project at different points in time

The workflow goes: Edit files → Stage changes → Commit (take snapshot)

**The States of Your Files**

In Git, files can exist in different states:

1. **Untracked** (U): Git sees this file exists but has never tracked it before—like a new person who just walked into your photo scene
2. **Modified** (M): You've changed a file that Git already knows about—like someone in your photo changed their outfit
3. **Staged** (A for "Added"): You've selected this change to be included in your next commit—like saying "yes, this person will be in the photo"
4. **Committed**: The change is permanently saved in your Git history—the photo has been taken and added to the album

Right now, your `hello_astronomy.py` file is **Untracked**. Git sees it but isn't tracking its changes yet. You need to stage it (select it for the photo) and then commit it (take the photo).
<!-- #endregion -->

<!-- #region -->
### The Basic Workflow in Cursor

Now let's actually track your file by staging and committing it.

**Step 1: Stage Your File**

In the Source Control panel, hover over your `hello_astronomy.py` file. You'll see a `+` button appear to its right. Click it.

Watch what happens:
- The file moves from "Changes" section to a new "Staged Changes" section
- The "U" changes to "A" (meaning "Added")
- The file is now ready to be committed

You've just told Git: "I want to include this file in my next snapshot."

**Step 2: Write a Commit Message**

Above the file list, you'll see a text box that says "Message (Ctrl+Enter to commit)". This is where you describe what you're saving. Your commit message is like writing a caption for your snapshot—it helps you (and others) understand what changed and why.

Type a meaningful message:
```
Add initial parallax calculation script
```

**Important**: You cannot commit without a message! Git requires you to describe what you're committing. If you try to commit with an empty message box, nothing will happen. This forces you to document your work—a good habit that you'll appreciate later.

**Step 3: Commit (Take the Snapshot)**

Press `Ctrl+Enter` (Windows) or `Cmd+Enter` (Mac) to commit. Or click the checkmark button (✔) above the message box.

Your Source Control panel will suddenly look empty! Don't panic—this is good. It means all your changes are committed (saved to history). Your file is now part of your repository's permanent record.

**Step 4: Make a Change to See the Workflow Again**

Let's modify your file to see how Git tracks changes:
1. Switch to Explorer (📁) and open `hello_astronomy.py`
2. Add these lines at the bottom:

```python
# Calculate distance to Alpha Centauri A
alpha_cen_distance = calculate_distance(0.754)
print(f"Distance to Alpha Centauri A: {alpha_cen_distance:.2f} parsecs")
```

3. Save the file and switch back to Source Control (📊)

Now you'll see:
```
CHANGES (1)
  M  hello_astronomy.py
```

The "M" means "Modified"—Git knows this file changed since your last commit. If you click on the file name, Cursor will show you exactly what changed, with removed lines in red and added lines in green.
<!-- #endregion -->

### Writing Good Commit Messages

Your commit messages are the story of your project. Six months from now, when you're trying to understand why your code changed, these messages will be your guide. Let's learn to write them well from the start.

**The Difference Good Messages Make**

Imagine returning to your project after winter break and seeing this history:

❌ **Bad commit messages:**
```
- fixed stuff
- asdfasdf
- working now
- update
- changes
- final version
```

What did you fix? What was broken? What changed? You have no idea.

✅ **Good commit messages:**
```
- Fix magnitude calculation for negative flux values
- Add error handling for missing FITS headers
- Refactor parallax function to use NumPy arrays
- Update plotting to include error bars
- Add documentation for stellar luminosity function
```

Now you know exactly what each change accomplished!

**The Simple Rules for Good Messages**

1. **Start with a verb**: "Add", "Fix", "Update", "Remove", "Refactor"
2. **Be specific**: Say what you changed, not just that you changed something
3. **Keep it short**: Aim for under 50 characters for the first line
4. **Explain why if needed**: For complex changes, add a blank line then more detail

**Examples for Your Projects**

For your LLM and astronomy projects, here are commit message patterns:

```
✔ Add function schema for parallax calculation
✔ Fix embedding dimension mismatch in RAG search
✔ Update temperature parameter to reduce hallucination
✔ Implement chunk overlap for document splitting
✔ Remove hardcoded API key from source file
✔ Refactor search function to use vectorized operations
```

**When to Commit?**

Think of commits as save points in a video game. Good times to commit:
- After adding a new function that works
- After fixing a bug
- After completing a section of documentation
- Before trying something risky (so you can undo if needed)
- At the end of each work session

Don't wait until your entire project is done to make your first commit! Small, frequent commits are better than one massive commit at the end.

<!-- #region -->
## Part 3: Connecting to GitHub from Cursor

### Setting Your Git Identity (One-Time Setup)

Before pushing any code to GitHub, Git needs to know what name and email to attach to your commits. This is just local configuration—it doesn't connect to GitHub or require any password.

**On Mac:**
1. Open Terminal (press `Cmd+Space`, type "Terminal", press Enter)
2. Type this command and press Enter:
```bash
git config --global user.name "Your Name"
```
3. Type this command and press Enter:
```bash
git config --global user.email "your-email@example.com"
```
4. Close Terminal

**On Windows:**
1. Open Command Prompt (press Windows key, type "cmd", press Enter)
2. Type this command and press Enter:
```bash
git config --global user.name "Your Name"
```
3. Type this command and press Enter:
```bash
git config --global user.email "your-email@example.com"
```
4. Close Command Prompt

Use your actual name and the same email you used for GitHub. These commands run silently—no output means they worked!

**Important:** These commands just tell Git what name/email to label your commits with. They don't connect to GitHub or verify you own that email. The actual authentication happens in the next step when you click "Publish Branch."

### Publishing Your Repository to GitHub

Now back in Cursor, look at the Source Control panel. You'll see a blue "Publish Branch" button (☁️). This is your one-click solution to get your code on GitHub.

**Click "Publish Branch" and here's where the real authentication happens:**
1. Your browser will open automatically
2. GitHub will ask you to sign in (if you're not already)
3. GitHub will ask "Authorize Cursor to access your account?"
4. Click "Authorize" to allow Cursor to push code to your GitHub
5. Return to Cursor, name your repository, and choose public or private
6. Cursor pushes your code to GitHub

The browser step is where you actually prove you own the GitHub account. Cursor uses OAuth—you log in through GitHub's website, not through Cursor itself, which is more secure.

**That's it!** Your code is now safely backed up on GitHub.
<!-- #endregion -->

### Publishing Your First Repository

Let's actually publish your code to GitHub now.

**Step 1: Click "Publish Branch"**

In the Source Control panel, click the blue "Publish Branch" button. A dialog will appear asking you to name your repository and choose its visibility.

**Step 2: Name Your Repository**

Cursor will suggest a repository name based on your folder name (like `my-first-repo`). You can:
- Keep the suggested name
- Change it to something more descriptive like `astro-python-project1`
- Add a description (optional but helpful)

**Step 3: Choose Visibility - Public vs Private**

You'll see two options:

**Public Repository**:
- Anyone on the internet can see your code
- Great for building your portfolio
- Shows you're learning and growing
- Required for GitHub Pages (free website hosting)
- Use for: completed projects, coursework you're proud of, anything you want to showcase

**Private Repository**:
- Only you and people you invite can see it
- Good for work-in-progress or sensitive research
- You can make it public later when ready
- Use for: unfinished projects, experimental code, anything with sensitive data

For this course, choose **Public**—it builds your portfolio and shows your learning journey to future employers or grad schools.

**Step 4: Watch the Magic Happen**

Click "OK" or "Publish". Your browser will open if this is your first time:
1. Sign in to GitHub if prompted
2. You'll see "Authorize Cursor" page—click the green "Authorize" button
3. Return to Cursor

You'll see activity in the bottom status bar as Cursor pushes your code. When it's done, you'll see a notification: "Successfully published to GitHub!"

**Step 5: View Your Repository Online**

After publishing, a notification appears with a link to view your repository on GitHub. Click it! You'll see:
- All your files
- Your commit history
- A nice interface to browse your code

Your code is now safely in the cloud, backed up forever, and part of your professional portfolio!


### The GitHub Website Tour

Now your repository is live on GitHub! Let's understand what you're looking at:

**Understanding Your Repository Page**

At the top, you'll see `[your-username]/[repository-name]`—this shows:
- Your GitHub username
- Your repository name (probably `Astron1221` or whatever you chose)
- A "Public" badge showing everyone can see this

**The Main Navigation Tabs**

Below your repository name, you see several tabs:
- **Code**: Where you browse your files (you're here now)
- **Issues**: Where people can report bugs or suggest features
- **Pull requests**: Where collaborators propose changes
- **Actions**: For automated workflows (advanced topic)
- **Projects**: For organizing tasks (like a to-do board)
- **Security**: Security alerts and settings
- **Insights**: Statistics about your repository

For now, you'll mainly use the **Code** tab.

**Your Repository Content**

In the main area, you can see:
- Your latest commit message (whatever you wrote when you committed)
- When it was made (probably "a few minutes ago")
- Number of commits (showing your project's history)
- Your file: `hello_astronomy.py`

Click on your Python file to view your code directly on GitHub. You can even edit it here (though we'll keep using Cursor for that).

**The About Section**

On the right side, you'll see "No description, website, or topics provided." Let's fix that:
1. Click the gear icon ⚙️ next to "About"
2. Add a description like "Python code for Astronomy 1221 course"
3. Add topics like `python`, `astronomy`, `education`
4. Click "Save changes"

This helps people understand what your project is about when they discover it.

**Changing Visibility Later**

Made your repository public but want to make it private? Or vice versa?
1. Go to Settings tab
2. Scroll to the "Danger Zone" at the bottom
3. Click "Change repository visibility"
4. Follow the prompts

You can switch between public and private anytime, though making a popular public repo private might disappoint users who depend on it!

<!-- #region -->
## Part 4: Essential GitHub Workflows in Cursor

### Making Changes and Syncing

Now that your code is on GitHub, let's learn the daily workflow you'll use from now on. Every time you work on your project, you'll follow this pattern: Pull → Edit → Commit → Push.

**Understanding Pull (Why We Sync First)**

"Pull" means downloading the latest version from GitHub to your computer. But wait—didn't you just push your code? Why would you need to pull?

Here's why pulling matters:
- You might work on multiple computers (laptop and desktop)
- You might edit files directly on GitHub's website
- Later, collaborators might make changes
- You might forget what version you have locally after a few days

Think of it like this: GitHub has the "official" version. Before you start working, you want to make sure you have that official version. Pulling ensures you're not working on an outdated copy.

**The Daily Workflow**

Let's add a new feature to practice the complete workflow:

1. **First, always sync** - Click the sync button (🔄) in the bottom status bar. This pulls any changes from GitHub and pushes any local commits you have.

2. **Make your changes** - Switch to Explorer, open `hello_astronomy.py`, and add this at the bottom:

```python
# Calculate distance to Betelgeuse
betelgeuse_distance = calculate_distance(0.00522)  
print(f"Distance to Betelgeuse: {betelgeuse_distance:.2f} parsecs")
```

3. **Save your file** (`Cmd+S` or `Ctrl+S`)
4. **Switch to Source Control** - You'll see your file marked with "M" for Modified
5. **Stage your changes** - Click the `+` next to the file
6. **Write a commit message** - "Add Betelgeuse calculation"
7. **Commit** - Press `Cmd+Enter` or click the checkmark
8. **Push to GitHub** - Click the sync button (🔄) again

After pushing, refresh your GitHub page in the browser. Your new commit appears instantly!
<!-- #endregion -->

<!-- #region -->
### Seeing Version Control in Action

Let's actually see what version control does for you. This is the magic of Git—it remembers everything.

**Viewing Your Project History in Cursor**

Look at the bottom of your Source Control panel. You'll see a "GRAPH" section you can expand. Click on it to see your project's history visually:

```
○ [your latest commit]      main ☁
│
● [your second commit]
│
● [your first commit]
```

Each dot represents a commit (a saved snapshot of your project). The lines show how your project evolved over time, with the newest at the top. This is your complete history—every save point you've created.

**Understanding What Git Tracks**

Make a small change to your file to see Git in action:

```python
# Change this line:
print(f"Distance to Proxima Centauri: {distance:.2f} parsecs")
# To this:
print(f"Distance to Proxima Centauri: {distance:.2f} parsecs ({distance * 3.26:.2f} light-years)")
```

Save the file and click on `hello_astronomy.py` in Source Control. Cursor shows you:
- **Red lines (-)**: What was removed
- **Green lines (+)**: What was added

This is called a "diff" (difference). Git tracks exactly what changed, not entire file copies. This is efficient—even with hundreds of commits, your project stays small.

**Recovering Old Code (The Simple Way)**

Made a mistake and want to get back some old code? Here's the easiest method:

1. Go to your GitHub repository in your browser
2. Click on your file (`hello_astronomy.py`)
3. Click "History" button (shows all versions of this file)
4. Click on any past version to view it
5. Select and copy the code you need
6. Paste it back in Cursor and make a new commit

The key insight: every commit is a permanent snapshot. Your old code is never truly lost—it's always there in your history on GitHub. Instead of trying to "undo" commits (which can get complicated), just make new commits that fix problems.
<!-- #endregion -->

### Creating a .gitignore File

Some files should never be tracked by Git. Since you're already familiar with keeping `.env` files secure from Lecture 7, let's set up a `.gitignore` file to automatically exclude files that shouldn't be in your repository.

**Why GitHub Limits File Sizes**

First, let's understand why GitHub has a 100MB file size limit (with warnings at 50MB). Git isn't just storing your current files—it's storing the complete history of every change to every file. If you commit a 100MB data file and then modify it 10 times, Git stores all 10 versions, potentially using 1GB of space! This makes:
- Repository downloads extremely slow
- Cloning take forever for collaborators
- GitHub's servers overwhelmed with data storage

Git was designed for code (text files), not data. Code files are typically small and their changes are easy to track. Large binary files like FITS images or CSV datasets belong elsewhere.

**Solutions for Large Files:**
- **Best option**: Store data on Google Drive, Box, or your university's storage, then link to it in your README
- **Alternative**: Use Git LFS (Large File Storage) for files you absolutely must version—but this is more complex
- **For this course**: Keep data files local and use `.gitignore` to exclude them from Git

**Files That Don't Belong in Git:**
- `.env` files with API keys (you know this from Lecture 7!)
- Python cache files (`__pycache__/` folders that Python creates)
- System files (`.DS_Store` on Mac, `Thumbs.db` on Windows)
- Large data files (astronomical observations, FITS files, big CSVs)
- Any file with sensitive information

**Creating Your .gitignore:**

1. In Explorer, create a new file named `.gitignore` (yes, it starts with a dot!)
2. Add these lines:
```
# Python
__pycache__/
*.pyc

# Environment variables
.env

# Data files (too large for Git)
*.fits
*.csv
data/

# System files
.DS_Store
Thumbs.db

# Jupyter Notebook checkpoints
.ipynb_checkpoints/
```

3. Save, stage, and commit this `.gitignore` file with message "Add .gitignore"
4. Push to GitHub

**Testing That .gitignore Works:**

Let's verify that Git actually ignores files:

1. Create a new file called `.env` in your project folder
2. Add some fake API keys:
```
ANTHROPIC_API_KEY=sk-fake-key-123456789
SECRET_PASSWORD=this-should-never-be-on-github
```
3. Save the file

Now look at Source Control—notice that `.env` doesn't appear at all! Even though you just created and saved it, Git completely ignores it because it's listed in your `.gitignore`. This is automatic protection against accidentally sharing secrets.

Try creating a `test_data.csv` file too—it will also be invisible to Git. The `.gitignore` file is your safety net, preventing common mistakes before they happen.

**The key point:** Once `.gitignore` is set up, you can work freely without constantly worrying about what files to commit. Git handles it automatically!


### What to Do When Push Fails
 
Sometimes when you try to push, things go wrong. Don't panic! Here are the most common issues and how to fix them:
 
**Problem 1: "Repository not found"**
  
This means Cursor is trying to push to a repository that doesn't exist on GitHub.
- **Solution**: Use the "Publish Branch" button instead of sync. This will create the repository first.
 
**Problem 2: "File too large"**
 
GitHub has a 100MB file size limit (with warnings starting at 50MB). If you try to commit a large data file:
```
remote: error: File data.fits is 150 MB; this exceeds GitHub's file size limit of 100 MB
```
 
**Why does GitHub limit file sizes?**
- Git tracks every version of every file in your repository's history
- Large files make the entire repository huge and slow to download
- Git was designed for code, not large data storage
- Every time someone clones your repository, they download ALL versions of ALL files
 
**Solution for large files:**
  1. Remove the file from your staging area
  2. Add it to `.gitignore` to prevent future accidents
  3. Commit the `.gitignore` instead
  4. Store large files elsewhere (Google Drive, Box, etc.) and add a link in your README
  5. For files you must version control, consider Git LFS (Large File Storage) - advanced topic
 
**Problem 3: "Authentication failed"**
 
This means Cursor lost connection to your GitHub account.
- **Solution**: 
  1. Try clicking sync again—it may prompt for re-authentication
  2. If that doesn't work, sign out and sign in again through Cursor's account settings
 
**Problem 4: "Updates were rejected"**
 
This happens when GitHub has changes you don't have locally (maybe you edited on the website).
```
! [rejected] main -> main (fetch first)
```
- **Solution**: Pull first (sync button), then push again
 
**Golden Rule**: When in doubt, save your work elsewhere (copy to a text file), pull the latest version from GitHub, then re-apply your changes and commit again. This always works!

<!-- #region -->
## Part 5: Writing a Professional README

### Your Project's Front Door

Right now, when people visit your GitHub repository, they see "No description, website, or topics provided." Let's fix that by creating a README file—the first thing visitors see when they find your project.

**What is a README?**

A README.md file is like the cover page of your project. The `.md` stands for Markdown—the same formatting you use in Jupyter notebook text cells. It appears automatically on your repository's main page, formatted beautifully by GitHub.

**Creating Your First README:**

1. In Cursor's Explorer, create a new file called `README.md` (must be exactly this name)
2. Add this content:

```markdown
# Astronomy 1221 Projects

Python code for astronomical calculations and analysis.

## What This Project Does

This repository contains Python scripts for:
- Calculating stellar distances from parallax measurements
- Converting between parsecs and light-years
- Learning Git and GitHub for scientific computing

## How to Use

Run the main script:
`python hello_astronomy.py`

## Requirements

- Python 3.8 or higher
- NumPy

## Author

Albert Einstein - Astronomy undergraduate at The Ohio State University

## Course Information

This code was developed for Astronomy 1221: Astronomical Data Analysis
```

3. Save the file, stage it, commit with message "Add README", and push

**See the Magic:**

Refresh your GitHub repository page. Your README now appears below your file list, beautifully formatted! The `#` symbols became headers, the code block is syntax-highlighted, and everything looks professional.

This README is simple but complete—it tells visitors what your project does, how to use it, and who made it. As your project grows, your README grows too.
<!-- #endregion -->

<!-- #region -->
### Creating requirements.txt

After your README, the next professional touch is a `requirements.txt` file. This file lists all the Python packages your code needs to run, making it easy for others (or future you) to recreate your environment.

**Why requirements.txt Matters**

Imagine someone wants to run your Project 1 code. They clone your repository, try to run it, and get:
```
ImportError: No module named 'anthropic'
```

Without knowing what packages you used, they're stuck. A `requirements.txt` file solves this—it's a shopping list of everything needed to run your code.

**Creating Your requirements.txt**

1. In Cursor's Explorer, create a new file called `requirements.txt`
2. Add the packages your project uses. For a typical Project 1, it might look like:

```
numpy==1.24.3
anthropic==0.7.0
python-dotenv==1.0.0
sentence-transformers==2.2.2
matplotlib==3.7.1
```

3. Save, stage, commit with "Add requirements.txt", and push

**Finding Your Current Package Versions**

Not sure what versions you have? In your terminal, run:
```bash
pip list
```

This shows all installed packages and their versions. Pick out the ones your project actually uses.

**How Others Use Your requirements.txt**

When someone clones your repository, they can install all dependencies with one command:
```bash
pip install -r requirements.txt
```

This installs exactly the versions you specified, ensuring your code works the same way on their computer as it does on yours.

**Pro Tip**: Update this file whenever you add a new import to your project. Future you will appreciate having this record of what packages you used!
<!-- #endregion -->

## Part 6: Creating Your Portfolio Website with GitHub Pages

### Free Website Hosting for Your Projects

GitHub offers something amazing: free website hosting for every repository. This feature, called GitHub Pages, can turn your repository into a live website. Perfect for showcasing your projects to grad schools or future employers!

**Enabling GitHub Pages:**

1. Go to your repository on GitHub
2. Click "Settings" (in the tabs, far right)
3. Scroll down to the "Pages" section
4. Under "Source", select "Deploy from a branch"
5. Choose "main" branch and "/ (root)" folder
6. Click "Save"

**Checking Your Deployment:**

After enabling Pages, return to your main repository page. Look at the right sidebar under "Deployments"—you'll see:
- ✅ **github-pages** now

This green checkmark means your site is live! Click on "github-pages" to see your deployment history and get the direct link to your website.

Your site will be at: `https://[your-username].github.io/[repository-name]`

**What Will People See?**

By default, GitHub Pages will show your README.md file as a beautifully formatted webpage—no extra work needed! The Markdown is automatically converted to HTML with professional styling. This is perfect for:
- Project documentation
- Course portfolios
- Personal homepages

**Advanced Option: Custom HTML (Optional)**

If you want more control over the design, you can create an `index.html` file. Important: if you add `index.html`, it will override your README display. For most projects, the README is sufficient and much easier to maintain!

### Your Personal Homepage Opportunity

Here's something powerful for your career development: you can create a special repository named `[your-username].github.io` (exactly your username followed by .github.io). This becomes your personal GitHub Pages homepage at `https://[your-username].github.io`—no repository name in the URL!

**Why Create a Personal Homepage?**
- **Professional presence**: A central place to showcase all your projects
- **Easy to maintain**: Just edit Markdown files, no complex web development
- **Free forever**: GitHub hosts it at no cost
- **Impressive to employers**: Shows you understand modern development practices

**Setting Up Your Personal Homepage:**
1. Create a new repository named exactly `[your-username].github.io`
2. Add a README.md with your bio, project links, and achievements
3. Enable GitHub Pages (same process as above)
4. Your site appears at `https://[your-username].github.io`

You can link to all your project repositories from this central homepage, creating a professional portfolio that grows with your career. Start simple with Markdown—you can always enhance it later as you learn more web development!

**Connecting to Next Week**: In Lecture 10, you'll learn to create interactive Streamlit apps. You can link to these from your GitHub Pages site, creating a complete portfolio of interactive astronomical tools!


## Part 7: Collaboration Basics

### Working with Others on GitHub

So far, you've been working solo on your repository. But one of GitHub's superpowers is enabling collaboration. Let's learn the basics of working with others—essential for group projects and future research.

**Inviting Collaborators**

If you're working on Project with a coursework partner, you can give them access to your repository:

1. Go to your repository on GitHub
2. Click "Settings" → "Collaborators"
3. Click "Add people"
4. Enter their GitHub username or email
5. They'll receive an invitation to accept

Once they accept, they can:
- Clone your repository to their computer
- Make changes and push directly
- See all the code and history

**The Simple Collaboration Flow**

When two people work on the same repository, coordination is key. Here's the simplest approach that avoids conflicts:

**The "Take Turns" Method:**
1. **Before you start working**: Always sync (pull) first
2. **While working**: Let your collaborator know you're making changes
3. **After you finish**: Commit and push immediately
4. **Communication is key**: Message your collaborator when you're done

Example workflow:
- Monday: You work on the data analysis functions → push when done
- Tuesday: Your coursework partner pulls your changes, adds visualization → pushes when done  
- Wednesday: You pull their changes, add documentation → push when done

**What If You Both Edit at the Same Time?**

If you and your collaborator accidentally edit the same file simultaneously, Git will warn you when you try to sync. You'll see a "merge conflict" message. Don't panic! For now, the simplest solution:

1. Save your work somewhere else (copy to a text file)
2. Discard your local changes
3. Pull your collaborator's version
4. Re-add your changes manually
5. Commit and push

As you get more experienced, you'll learn to resolve conflicts directly, but taking turns is much easier for beginners!

**Pro Tip for Project 1**: If you're feeling ambitious and want to collaborate with your Project 1 coursework partner using Git, start simple—take turns working on different files rather than the same file. This avoids most conflicts!


## Conclusion: You're Now Git-Powered!

### What You've Accomplished Today

Take a moment to appreciate what you've just done:

- **Created your first GitHub account** - You now have a professional presence in the coding world
- **Learned Git basics in Cursor** - You can track changes, commit your work, and see your project history
- **Published code to the cloud** - Your work is backed up and accessible from anywhere
- **Created a README** - Your project has proper documentation
- **Added requirements.txt** - Others can recreate your environment
- **Set up .gitignore** - Your sensitive files stay private automatically
- **Built a portfolio website** - Your work is showcased on GitHub Pages
- **Learned to collaborate** - You can work with others on shared code

### Your New Daily Workflow

From now on, whenever you work on code:
1. **Sync first** (pull any changes)
2. **Write code** as usual
3. **Commit often** with clear messages
4. **Push before closing** your laptop

That's it! This simple workflow keeps your code safe and your history clean.

### For Project 1 and Beyond

Now that you understand GitHub:
- Upload your completed Project 1 to its own repository
- Create a nice README explaining what it does
- Add a `requirements.txt` so others can run it
- Add a `.gitignore` to keep your `.env` file private
- Share the link with your instructors

For future projects, start with GitHub from day one. Create the repository first, then build your project with regular commits. Your future self (and your instructors) will thank you!

### Remember: Git is Your Safety Net

Never again will you lose code to a crashed laptop or accidental deletion. Every commit is a permanent save point. Every push is a backup. GitHub is your code's forever home.

The version control skills you learned today are used by every professional programmer and researcher. Whether you're contributing to astropy, collaborating on a telescope control system, or sharing your research code with the world, you now have the tools to do it professionally.

Welcome to the world of version control—you're now coding like a professional!
