        {
            export ARCH="${SBKA}" CROSS_COMPILE="${SBKTL}/bin/${KCCP}";
            echo -e "\n${INF} Cleaning Levels\n";
            echo -e "1. Clean Intermediate files";
            echo -e "2. 1 + Clean the Current Kernel Configuration\n";
            ST="Clean Method"; shut_my_mouth CK "$ST";
            case "${SBCK}" in
                1) make clean -j${SBNT} ;;
                2) make mrproper -j${SBNT} ;;
            esac
            echo -e "\n${SCS} Kernel Cleaning done\n\n${INF} Check output for details\n";
            export action_kcl="done";
            [ -z "$automate" ] && [ "$SBKO" != "5" ] && kbuild;
