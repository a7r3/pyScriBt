        {
            (patch -p1 -N --dry-run < $1 1> /dev/null 2>&1 && echo -n 0) || # Patch is not applied but can be applied
            (patch -p1 -R --dry-run < $1 1> /dev/null 2>&1 && echo -n 1) || # Patch is applied
            echo -n 2; # Patch can not be applied
