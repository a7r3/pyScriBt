
    echo -ne "\033]0;ScriBt : Device Info\007";
    [[ ! -z ${ROMV} ]] && export ROMNIS="${ROMV}"; # Change ROMNIS to ROMV if ROMV is non-zero
    if [ -d ${CALL_ME_ROOT}/vendor/${ROMNIS}/config ]; then
        CNF="vendor/${ROMNIS}/config";
    elif [ -d ${CALL_ME_ROOT}/vendor/${ROMNIS}/configs ]; then
        CNF="vendor/${ROMNIS}/configs";
    else
        CNF="vendor/${ROMNIS}";
    fi
    rom_names "$SBRN"; # Restore ROMNIS
    echo -e "${CL_WYT}=====================${NONE} ${CL_PRP}Device Info${NONE} ${CL_WYT}=====================${NONE}\n";
    echo -e "${QN} What's your Device's CodeName \n${INF} Refer Device Tree - All Lowercases\n";
    ST="Your Device Name is"; shut_my_mouth DEV "$ST";
    echo -e "${QN} Your Device's Company/Vendor \n${INF} All Lowercases\n";
    ST="Device's Vendor"; shut_my_mouth CM "$ST";
    echo -e "${QN} Build type \n${INF} [userdebug/user/eng]\n";
    ST="Build type"; shut_my_mouth BT "$ST";
    if [ -z "$SBBT" ]; then SBBT="userdebug"; fi;
    echo -e "${QN} Choose your Device type among these. Explainations of each file given in README.md\n"; gimme_info "device-type";
    TYPES=( common_full_phone common_mini_phone common_full_hybrid_wifionly \
    common_full_tablet_lte common_full_tablet_wifionly common_mini_tablet_wifionly common_tablet \
    common_full_tv common_mini_tv );
    CNT=0;
    for TYP in ${TYPES[*]}; do
        if [ -f ${CNF}/${TYP}.mk ]; then echo -e "${CNT}. $TYP"; ((CNT++)); fi;
    done
    echo;
    ST="Device Type"; shut_my_mouth DTP "$ST";
    [ -z $SBDTP ] && SBDTP="common" || SBDTP="${TYPES[${SBDTP}]}";
    echo -e "${CL_WYT}=======================================================${NONE}\n";
