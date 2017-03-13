    {
        function check_patch()
        {
            (patch -p1 -N --dry-run < $1 1> /dev/null 2>&1 && echo -n 0) || # Patch is not applied but can be applied
            (patch -p1 -R --dry-run < $1 1> /dev/null 2>&1 && echo -n 1) || # Patch is applied
            echo -n 2; # Patch can not be applied
        } # check_patch

        function apply_patch()
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
        } # apply_patch

        function visual_check_patch()
        {
            case $(check_patch "$1") in
                0) echo -en "[${CL_RED}N${NONE}]" ;; # Patch is not applied but can be applied
                1) echo -en "[${CL_GRN}Y${NONE}]" ;; # Patch is applied
                2) echo -en "[${CL_BLU}X${NONE}]" ;; # Patch can not be applied
            esac
        } # visual_check_patch

        function show_patches()
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
        } # show_patches

        function patch_creator()
        {
            if [ ! -d ".repo" ]; then # We are not inside a repo
                echo -e "\n${FLD} You are not inside a repo (or the .repo folder was not found)";
            else
                echo -e "\n${QN} Do you want to generate a patch file out of unstaged changes (May take a long time)";
                echo -e "${INF} WARNING: Changes outside of the repos listed in the manifest will NOT be recognized!\n";
                prompt CREATE_PATCH;
                if [[ "$CREATE_PATCH" =~ [Yy] ]]; then
                    echo -e "\n${INF} Where do you want to save the patch?\n${INF} Make sure the directory exists\n\n";
                    prompt PATCH_PATH;
                    PROJECTS="$(repo list -p)"; # Get all teh projects
                    PROJECT_COUNT=$(wc -l <<< "$PROJECTS"); # Count all teh projects
                    [ -f "${CALL_ME_ROOT}/${PATCH_PATH}" ] && rm -rf ${CALL_ME_ROOT}/${PATCH_PATH} # Delete existing patch
                    COUNT=1;
                    echo "";
                    while read PROJECT; do # repo foreach does not work, as it seems to spawn a subshell
                        cd ${CALL_ME_ROOT}/${PROJECT}
                        git diff |
                          sed -e "s@ a/@ a/${PROJECT}/@g" |
                          sed -e "s@ b/@ b/${PROJECT}/@g" >> ${CALL_ME_ROOT}/${PATCH_PATH}; # Extend a/ and b/ with the project's path, as git diff only outputs the paths relative to the git repository's root
                        echo -en "\033[KGenerated patch for repo $COUNT of $PROJECT_COUNT\r";  # Count teh processed repos
                        ((COUNT++));
                    done <<< "$PROJECTS";
                    cd ${CALL_ME_ROOT};
                    echo -e "\n\n${SCS} Done.";
                    [ ! -s "${CALL_ME_ROOT}/${PATCH_PATH}" ] &&
                      rm ${CALL_ME_ROOT}/${PATCH_PATH} &&
                      echo -e "${INF} Patch was empty, so it was deleted";
                fi
            fi
        } # patch_creator

        function patcher()
        {
            show_patches;
            echo -e "\n=======================================================\n";
            prompt PATCHNR;
            case "$PATCHNR" in # Process śpecial actions
                0) quick_menu ;; # Exit the Patch Manager and return to Quick Menu
                1)
                    patch_creator;
                    patcher;
                    ;;
                *)
                    [ "${PATCHES[$PATCHNR]}" ] && apply_patch "${PATCHES[$PATCHNR]}" ||
                    echo -e "\n${FLD} Invalid selection: $PATCHNR";
                    patcher;
                    ;;
            esac
        } # patcher

        patcher;
