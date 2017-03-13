    {
        echo -e "${CL_WYT}=====================${NONE} ${CL_LBL}Hotel Menu${NONE} ${CL_WYT}======================${NONE}";
        echo -e " Menu is only for your Device, not for you. No Complaints pls.\n";
        echo -e "[*] lunch - Setup Build Environment for the Device";
        echo -e "[*] breakfast - Download Device Dependencies and lunch";
        echo -e "[*] brunch - breakfast + lunch then Start Build\n";
        echo -e "${QN} Type in the Option you want to select\n";
        echo -e "${INF} Building for the first time ? select lunch";
        echo -e "${CL_WYT}=======================================================${NONE}\n";
        ST="Selected Option"; shut_my_mouth SLT "$ST";
        case "$SBSLT" in
            "lunch") ${SBSLT} ${TARGET} ;;
            "breakfast") ${SBSLT} ${SBDEV} ${SBBT} ;;
            "brunch")
                echo -e "\n${EXE} Starting Compilation - ${ROM_FN} for ${SBDEV}\n";
                ${SBSLT} ${SBDEV};
                ;;
            *) echo -e "${FLD} Invalid Selection.\n"; hotel_menu ;;
        esac
        echo;
