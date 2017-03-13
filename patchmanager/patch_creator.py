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
