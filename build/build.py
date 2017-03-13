
    # Change terminal title
    [ ! -z "$automate" ] && teh_action 4;

    function hotel_menu()
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
    } # hotel_menu

    function post_build()
    {
        NRT_0=`tac $RMTMP | grep -m 1 'No rule to make target\|no known rule to make it'`;
        if [[ $(tac $RMTMP | grep -c -m 1 '#### make completed successfully') == "1" ]]; then
            echo -e "\n${SCS} Build completed successfully! Cool. Now make it Boot!";
            the_response COOL Build;
            teh_action 6 COOL;
        elif [[ ! -z "$NRT_0" ]]; then
#           if [[ ! -z "$DMNJ" ]]; then
#               # ninja: error: 'A', needed by 'B', missing and no known rule to make it
# W             NRT_1=(`echo "$NRT_0" | awk '{print $3 $6}' | awk -F "'" '{print $2" "$4}'`);
# i         else
# P             # make[X]: *** No rule to make target 'A', needed by 'B'.
#               NRT_1=(`echo "$NRT_0" | awk -F "No rule to make target" '{print $2}' | awk -F "'" '{print $2" "$4}'`);
#           fi
            if [ ! -z "$automate" ]; then
                the_response FAIL Build;
                teh_action 6 FAIL;
            fi
        else
            the_response FAIL Build;
            teh_action 6 FAIL;
        fi
    } # post_build

    {
        if [[ "$1" != "brunch" ]]; then
            START=$(date +"%s"); # Build start time
            # Showtime!
            BCORES="-j${BCORES}";
            if [ $(grep -q "^${ROMNIS}:" "${CALL_ME_ROOT}/build/core/Makefile") ]; then
                $SBMK $ROMNIS $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            elif [ $(grep -q "^bacon:" "${CALL_ME_ROOT}/build/core/Makefile") ]; then
                $SBMK bacon $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            else
                $SBMK otapackage $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            fi
            END=$(date +"%s"); # Build end time
            SEC=$(($END - $START)); # Difference gives Build Time
            if [ -z "$BLDSCS" ]; then
                echo -e "\n${FLD} Build Status : Failed";
            else
                echo -e "\n${SCS} Build Status : Success";
            fi
            echo -e "\n${INF} ${CL_WYT}Build took $(($SEC / 3600)) hour(s), $(($SEC / 60 % 60)) minute(s) and $(($SEC % 60)) second(s).${NONE}" | tee -a rom_compile.txt;
            #post_build; # comment it please xD
        fi
    {
        echo -e "\n${CL_WYT}=======================================================${NONE}\n";
        echo -e "${QN} Select a Build Option:\n";
        echo -e "1. Start Building ROM (ZIP output) (Clean Options Available)";
        echo -e "2. Make a Particular Module";
        echo -e "3. Setup CCACHE for Faster Builds";
        echo -e "4. Kernel Building";
        echo -e "5. Patch Manager";
        echo -e "0. Quick Menu\n";
        echo -e "${CL_WYT}=======================================================\n";
        ST="Option Selected"; shut_my_mouth BO "$ST";
