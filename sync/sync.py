
    # Change terminal title
    [ ! -z "$automate" ] && teh_action 2;
    # If   Repo not inited          then do it else                        get rom info
    if [ ! -f .repo/manifest.xml ]; then init; elif [ -z "$action_1" ]; then rom_select; fi;
    echo -e "\n${EXE} Preparing for Sync\n";
    echo -e "${QN} Number of Threads for Sync \n"; gimme_info "jobs";
    ST="Number of Threads"; shut_my_mouth JOBS "$ST";
    echo -e "${QN} Force Sync needed ${CL_WYT}[y/n]${NONE}\n"; gimme_info "fsync";
    ST="Force Sync"; shut_my_mouth F "$ST";
    echo -e "${QN} Need some Silence in the Terminal ${CL_WYT}[y/n]${NONE}\n"; gimme_info "ssync";
    ST="Silent Sync"; shut_my_mouth S "$ST";
    echo -e "${QN} Sync only Current Branch ${CL_WYT}[y/n]${NONE}\n"; gimme_info "syncrt";
    ST="Sync Current Branch"; shut_my_mouth C "$ST";
    echo -e "${QN} Sync with clone-bundle ${CL_WYT}[y/n]${NONE}\n"; gimme_info "clnbun";
    ST="Use clone-bundle"; shut_my_mouth B "$ST";
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    #Sync-Options
    [[ "$SBS" == "y" ]] && SILENT=-q || SILENT=" ";
    [[ "$SBF" == "y" ]] && FORCE=--force-sync || FORCE=" ";
    [[ "$SBC" == "y" ]] && SYNC_CRNT=-c || SYNC_CRNT=" ";
    [[ "$SBB" == "y" ]] && CLN_BUN=" " || CLN_BUN=--no-clone-bundle;
    echo -e "${EXE} Let's Sync!\n";
    repo sync -j${SBJOBS:-1} ${SILENT:--q} ${FORCE} ${SYNC_CRNT:--c} ${CLN_BUN} \
    && the_response COOL Sync || the_response FAIL Sync;
    echo -e "\n${SCS} Done.\n";
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    [ -z "$automate" ] && quick_menu;
