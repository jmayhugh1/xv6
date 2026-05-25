# Load debug symbols (run from repo root, after target remote).
symbol-file kernel/kernel
set directories user kernel
source gdb-user.gdb
