# update_proto.py
A quick script to update your C prototypes using cproto.

Use at your own risk ;)

## Installation
- Install [homebrew](https://docs.brew.sh/Installation#untar-anywhere-unsupported)
- Install [cproto](https://invisible-island.net/cproto/cproto.html) with `$ brew install cproto`

---

If you want to install it to your home directory:
```
$ cd
$ git clone https://github.com/triedel42/update_proto
```

then add this to your `~/.zshrc`

```bash
export PATH="$PATH:$HOME/update_proto"
```

## Usage
Add this to your header file where you want your prototypes to be.

```C
/* $$proto_start$$ */

// this will be replaced and updated
// by update_proto.py

/* $$proto_end$$ */
```

Now you can update myfile.h using auto-generated prototypes from myfile.c.
```bash
$ update_proto.py myfile.h
```

---

You can also use `$ update_proto.py *.h` or add a rule with it to your Makefile. `update_proto.py` accepts multiple arguments like `$ update_proto.py myfile1.h myfile2.h myfile3.h`.
