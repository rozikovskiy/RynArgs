<div align="center">

# Ryn Args

Python Argument Parser

---

## Usage Examples
</div>

### Default
```python
import rynargs

# Instantiate a class

args = rynargs.RynParse(
    "cmd",
    "CLI - Utility", # Optionally but recommended
    "-", # By default
    "done", # By default
    True, # By default
    False, # By default
)

# Creating description

description = args.description(
    "A very good cli utility",
    "red", # Optionally
    "red+bold", # Optionally
    False, # By default
    5, # By default
    4, # 2 by default
    5, # BY default
    "Flagy Help" # "Flag Help" by default
)

# Adding the first argument

args.add_argument(
    "types",
    "<type>",
    "Returnes list of types",
    "dark_cyan", # Optionally, 'cmd' in my case
    "cyan+bold", # Optionally, 'add-types' in my case
    "dark_cyan", # Optionally, '<type1> <value1> -done' in my case
    "red", # Optionally 'Adds types' in my case
    True, # By default
    True, # False by default
    False # By default
)
# Setting up a convenient variable

done = {args.prefix}+{args.done}

# Adding a second argument

args.add_argument(
    "add-types",
    f"<type1> <value1> {done}",
    "Adds types",
    "dark_cyan", # Optionally, 'cmd' in my case
    "cyan+bold", # Optionally, 'add-types' in my case
    "dark_cyan", # Optionally, '<type1> <value1> -done' in my case
    "red", # Optionally 'Adds types' in my case
    True, # By default
    False, # By default
    False # By default
)

# As this is a verbose argument, add it to the parents.

args.parent_add(["add-types"])

# Now we can run argument parsing.

g = args.parsing(description) # Added description
```
#### Output
```cmd
[user@OS] python3 cmd.py -help
                    CLI - Utility
                A very good CLI Utility
                    Flagy Help
    cmd -types <type> - Returnes list of types
0.1s
[user@OS] python3 cmd.py -help -add-types
    cmd -add-types <type1> <value1> -done - Adds types
0.1s
```
<div align="center">

## For more examples look in examples/

</div>
