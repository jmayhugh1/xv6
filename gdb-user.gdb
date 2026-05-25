# Helper commands for debugging xv6 user programs in QEMU.
# User ELFs are linked at virtual address 0 in each process's page table.

define reload-user
  if $argc != 1
    help reload-user
    printf "Usage: reload-user <prog>   e.g. reload-user zombie\n"
  else
    add-symbol-file user/_$arg0 0
    printf "Loaded user/_%s at address 0\n", $arg0
  end
end

document reload-user
  Load debug symbols for user/_<prog> at virtual address 0.
  Run after the target program is running (or before continuing into it).
  Example: reload-user zombie
end

# init is the first user process after boot.
add-symbol-file user/_init 0
