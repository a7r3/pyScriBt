        {
            case $(check_patch "$1") in
                0) echo -en "\n${EXE} Patch is being applied\n";
                   patch -p1 -N < $1 > /dev/null;
                   ([ "$?" == 0 ] && echo -e "${SCS} Patch Successfully Applied") || echo -e "${FLD} Patch Application Failed";; # Patch is being applied
                1) echo -en "\n${EXE} Patch is being reversed\n";
                   patch -p1 -R < $1 > /dev/null;
                   ([ "$?" == 0 ] && echo -e "${SCS} Patch Successfully Reversed") || echo -e "${FLD} Patch Reverse Failed";  # Patch is being reversed
                   ;;
                2) echo -e "\n${EXE} Patch can't be applied." ;; # Patch can not be applied
            esac
