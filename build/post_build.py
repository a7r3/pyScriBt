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
