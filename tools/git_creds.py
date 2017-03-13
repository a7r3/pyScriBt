    {
        echo -e "\n${INF} Enter the Details with reference to your ${CL_WYT}GitHub account${NONE}\n\n";
        sleep 2;
        echo -e "${QN} Enter the Username";
        echo -e "${INF} Username is the one which appears on the GitHub Account URL\n${INF} Ex. https://github.com/[ACCOUNT_NAME]\n";
        prompt GIT_U;
        echo -e "\n${QN} Enter the E-mail ID\n";
        prompt GIT_E;
        git config --global user.name "${GIT_U}";
        git config --global user.email "${GIT_E}";
        echo -e "\n${SCS} Done.\n"
        quick_menu;
