    {
        echo -e "\n${QN} Enter the User name [$(whoami)]\n";
        ST="Custom Username"; shut_my_mouth CU "$ST";
        export KBUILD_BUILD_USER=${SBCU:-$(whoami)};
        echo -e "\n${QN} Enter the Host name [$(hostname)]\n";
        ST="Custom Hostname"; shut_my_mouth CH "$ST";
        export KBUILD_BUILD_HOST=${SBCH:-$(hostname)};
        echo -e "\n${INF} You're building on ${CL_WYT}${KBUILD_BUILD_USER}@${KBUILD_BUILD_HOST}${NONE}";
        echo -e "\n${SCS} Done\n";
        [ -z "$automate" ] && [ "$SBKO" != "5" ] && kbuild;
