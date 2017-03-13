
    echo -ne '\033]0;ScriBt : Quick Menu\007';
    echo -e "${CL_WYT}\n=====================${NONE} ${CL_PNK}Quick-Menu${NONE} ${CL_WYT}======================${NONE}";
    echo -e "1. Init | 2. Sync | 3. Pre-Build | 4. Build | 5. Tools";
    echo -e "                      6. Exit";
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    prompt ACTION;
    teh_action $ACTION "qm";
