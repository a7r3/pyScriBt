        {
            case $(check_patch "$1") in
                0) echo -en "[${CL_RED}N${NONE}]" ;; # Patch is not applied but can be applied
                1) echo -en "[${CL_GRN}Y${NONE}]" ;; # Patch is applied
                2) echo -en "[${CL_BLU}X${NONE}]" ;; # Patch can not be applied
            esac
