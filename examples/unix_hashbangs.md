```python
#!/usr/bin/env python3

import rynargs
args = rynargs.RynParse(
  "util",
  "My Utility",
  "-_-",
  "ok",
  True,
  False
)
descriptions = args.description(
  "My utility is very functional! But it’s still under development and in beta testing.",
  "red+bold",
  "magenta",
  False,
  5,
  3,
  5
)
done = args.prefix + args.done
args.add_argument(
  "my_first_arg",
  "\"message_to_write\" <url>",
  "Send message to required url",
  "red+bold",
  "cyan+bold",
  "red",
  "",
  True,
  False,
  False
)
args.add_argument(
  "my_second_arg",
  f"**args {done}",
  "Creating cmd shortcut",
  "orange+bold",
  "mint+bold",
  "chocolate+bold",
  "peach",
  False,
  True,
  False
)
args.add_argument(
  "my_third_arg",
  f"**urls {done}",
  "\033[1;31mCreating urls shortcut",
  "mint+bold",
  "chocolate+bold",
  "peach+bold",
  "orange",
  False,
  True,
  True
)
args.parent_add({"my_second_arg", "my_third_arg"})

g = args.parsing(descriptions)
g = dict(g)
if "my_third_arg" in g.keys():
  print(g)
```
[](../assets/unix_hashes/screen1.png)
