        {
            echo -e "${QN} Enter the location of the Kernel source\n";
            ST="Kernel Location"; shut_my_mouth KL "$ST";
            if [ -f ${SBKL}/Makefile ]; then
                echo -e "\n${SCS} Kernel Makefile found";
                cd ${SBKL};
            else
                echo -e "\n${FLD} Kernel Makefile not found. Aborting";
                quick_menu;
            fi
            echo -e "\n${QN} Enter the codename of your device\n";
            ST="Codename"; shut_my_mouth DEV "$ST";
            KDEFS=( `ls arch/*/configs/*${SBDEV}*_defconfig` );
            for((CT=0;CT<${#KDEFS[*]};CT++)); do
                echo -e "$((${CT}+1)). ${KDEFS[$CT]}";
            done
            unset CT;
            echo -e "\n${INF} These are the available Kernel Configurations\n\n${QN} Select the one according to the CPU Architecture\n";
            if [ -z "$automate" ]; then
                prompt CT;
                SBKD=`eval echo "\${KDEFS[$(($CT-1))]}" | awk -F "/" '{print $4}'`;
                SBKA=`eval echo "\${KDEFS[$(($CT-1))]}" | awk -F "/" '{print $2}'`;
            fi
            echo -e "\n${INF} Arch : ${SBKA}";
            echo -e "\n${QN} Number of Jobs / Threads\n";
            BCORES=$(grep -c ^processor /proc/cpuinfo); # CPU Threads/Cores
            echo -e "${INF} Maximum No. of Jobs -> ${CL_WYT}${BCORES}${NONE}\n";
            ST="Number of Jobs"; shut_my_mouth NT "$ST";
            if [[ "$SBNT" > "$BCORES" ]]; then # Y u do dis
                echo -e "\n${FLD} Invalid Response\n";
                SBNT="$BCORES";
                echo -e "${INF} Using Maximum no of threads : $BCORES";
            fi
            export action_kinit="done";
            [ -z "$automate" ] && [ "$SBKO" != "5" ] && kbuild;
