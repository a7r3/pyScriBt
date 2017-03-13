
    if which apt &> /dev/null; then
        echo -e "\n${SCS} Package manager ${CL_WYT}apt${NONE} detected.\033[0m";
        PKGMGR="apt";
    elif which pacman &> /dev/null; then
        echo -e "\n${SCS} Package manager ${CL_WYT}pacman${NONE} detected.\033[0m";
        PKGMGR="pacman";
    else
        echo -e "${FLD} No supported package manager has been found.";
        echo -e "\n${INF} Arch Linux or a Debian/Ubuntu based Distribution is required to run ScriBt.";
        exitScriBt 1;
    fi
