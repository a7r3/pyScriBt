        {
            echo -e "${INF} Device Resolution\n";
            if [ ! -z "$automate" ]; then
                gimme_info "bootres";
                echo -e "${QN} Enter the Desired Highlighted Number\n";
                prompt SBBTR;
            else
                echo -e "${INF} ${ATBT} Resolution Chosen : ${SBBTR}";
            fi
