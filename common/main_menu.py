
    echo -ne '\033]0;ScriBt : Main Menu\007';
    echo -e "${CL_WYT}===================${NONE}${SCS} ${CL_LBL}Main Menu${NONE} ${SCS}${CL_WYT}===================${NONE}\n";
    echo -e "1                 Choose ROM & Init*                  1";
    echo -e "2                       Sync                          2";
    echo -e "3                     Pre-Build                       3";
    echo -e "4                       Build                         4";
    echo -e "5                   Various Tools                     5\n";
    echo -e "6                        EXIT                         6\n";
    echo -e "* - Sync will Automatically Start after Init'ing Repo";
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    echo -e "\n${QN} Select the Option you want to start with\n";
    prompt ACTION;
    teh_action $ACTION "mm";
