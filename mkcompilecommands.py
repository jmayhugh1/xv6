#!/usr/bin/env python3
"""Regenerate compile_commands.json for kernel and user sources."""

import glob
import json
import os

CC = "/opt/homebrew/bin/riscv64-unknown-elf-gcc"
DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

CFLAGS = [
    CC,
    "-Wall", "-Werror", "-Wno-unknown-attributes", "-O",
    "-fno-omit-frame-pointer", "-ggdb", "-gdwarf-2",
    "-march=rv64gc", "-MD", "-mcmodel=medany", "-ffreestanding",
    "-fno-common", "-nostdlib",
    "-fno-builtin-strncpy", "-fno-builtin-strncmp", "-fno-builtin-strlen",
    "-fno-builtin-memset", "-fno-builtin-memmove", "-fno-builtin-memcmp",
    "-fno-builtin-log", "-fno-builtin-bzero", "-fno-builtin-strchr",
    "-fno-builtin-exit", "-fno-builtin-malloc", "-fno-builtin-putc",
    "-fno-builtin-free", "-fno-builtin-memcpy", "-Wno-main",
    "-fno-builtin-printf", "-fno-builtin-fprintf", "-fno-builtin-vprintf",
    "-I.", "-fno-stack-protector", "-fno-pie", "-no-pie",
    "-c",
]

KERNEL_CFLAGS = CFLAGS + ["-o"]
USER_CFLAGS = CFLAGS + ["-o"]

def entry(src, out, flags):
    obj = out
    args = flags + [obj, src]
    return {
        "file": src,
        "arguments": args,
        "directory": DIR,
        "output": obj,
    }

commands = []

for path in sorted(glob.glob("kernel/*.c")):
    base = os.path.splitext(os.path.basename(path))[0]
    commands.append(entry(path, f"kernel/{base}.o", KERNEL_CFLAGS))

for path in sorted(glob.glob("user/*.c")):
    base = os.path.splitext(os.path.basename(path))[0]
    commands.append(entry(path, f"user/{base}.o", USER_CFLAGS))

for path in sorted(glob.glob("kernel/*.S")):
    base = os.path.splitext(os.path.basename(path))[0]
    commands.append({
        "file": path,
        "arguments": [CC, "-march=rv64gc", "-g", "-c", "-o", f"kernel/{base}.o", path],
        "directory": DIR,
        "output": f"kernel/{base}.o",
    })

# IDE-only: type-check defs.h (included after types.h/riscv.h in real builds).
commands.append({
    "file": "kernel/defs.h",
    "arguments": [
        CC,
        "-Wall", "-Wno-unknown-attributes", "-ffreestanding",
        "-march=rv64gc", "-mcmodel=medany",
        "-I.", "-Ikernel",
        "-fsyntax-only",
        "-include", "types.h",
        "-include", "riscv.h",
        "kernel/defs.h",
    ],
    "directory": DIR,
})

with open("compile_commands.json", "w") as f:
    json.dump(commands, f, indent=2)
    f.write("\n")

print(f"Wrote {len(commands)} entries to compile_commands.json")
