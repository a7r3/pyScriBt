        {
            cd $CALL_ME_ROOT;
            unset PATCHES;
            unset PATCHDIRS;
            PATCHDIRS=("device/*/*/patch" "patch");
            echo -e "\n${EXE} Searching for patches\n";
            echo -e "==================== ${CL_LRD}Patch Manager${NONE} ====================\n";
            echo -e "0. Exit the Patch Manager";
            echo -e "1. Launch the Patch Creator";
            COUNT=2;
            for PATCHDIR in "${PATCHDIRS[@]}"; do
                if find ${PATCHDIR}/* 1> /dev/null 2>&1; then
                    while read PATCH; do
                        if [ -s "$PATCH" ]; then
                            PATCHES[$COUNT]=$PATCH;
                            echo -e ${COUNT}. $(visual_check_patch "$PATCH") $PATCH;
                            ((COUNT++));
                        fi
                    done <<< "$(find ${PATCHDIR}/* | grep -v '\/\*')";
                fi
            done
