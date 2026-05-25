#!/usr/bin/env bash
# Wait until QEMU's GDB stub is accepting connections on 127.0.0.1.
set -euo pipefail
cd "$(dirname "$0")/.."
PORT=$(make -s print-gdbport)
for _ in $(seq 1 30); do
  if nc -z 127.0.0.1 "$PORT" 2>/dev/null; then
    echo "GDB_STUB_READY"
    exit 0
  fi
  sleep 1
done
echo "ERROR: Nothing listening on 127.0.0.1:$PORT — run 'make qemu-gdb' first." >&2
exit 1
