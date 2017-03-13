    {
        function kinit()
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
        } # kinit

        function settc()
        {
            echo -e "\n${INF} Make sure you have downloaded (synced) a Toolchain for compiling the kernel";
            echo -e "\n${QN} Point me to the location of the toolchain\n";
            ST="Toolchain Location"; shut_my_mouth KTL "$ST";
            if [[ -d "${SBKTL}" ]]; then
                KCCP=$(ls ${SBKTL}/bin/${SBKA}*gcc | sed -e 's/gcc//g' -e 's/.*bin\///g');
                if [[ ! -z "${KCCP}" ]]; then
                    echo -e "\n${SCS} Toolchain Detected\n";
                    echo -e "${INF} Toolchain Prefix : ${KCCP}\n";
                else
                    echo -e "${FLD} Toolchain Binaries not found\n";
                fi
            else
                echo -e "${FLD} Directory not found\n";
            fi
            [ -z "$automate" ] && [ "$SBKO" != "5" ] && kbuild;
        } # settc

        function kclean()
        {
            export ARCH="${SBKA}" CROSS_COMPILE="${SBKTL}/bin/${KCCP}";
            echo -e "\n${INF} Cleaning Levels\n";
            echo -e "1. Clean Intermediate files";
            echo -e "2. 1 + Clean the Current Kernel Configuration\n";
            ST="Clean Method"; shut_my_mouth CK "$ST";
            case "${SBCK}" in
                1) make clean -j${SBNT} ;;
                2) make mrproper -j${SBNT} ;;
            esac
            echo -e "\n${SCS} Kernel Cleaning done\n\n${INF} Check output for details\n";
            export action_kcl="done";
            [ -z "$automate" ] && [ "$SBKO" != "5" ] && kbuild;
        } # kclean


        function mkkernel()
        {
            # Execute these before building kernel
            [ -z "${action_kinit}" ] && kinit;
            [ -z "${KCCP}" ] && settc;
            [ -z "${action_kcl}" ] && kclean;
            [ ! -z "${SBCUH}" ] && custuserhost;

            echo -e "\n${EXE} Compiling the Kernel\n";
            export ARCH="${SBKA}" CROSS_COMPILE="${SBKTL}/bin/${KCCP}";
            [ ! -z "$SBNT" ] && SBNT="-j${SBNT}";
            make ${SBKD};
            make ${SBNT} && echo -e "\n${SCS} Compiled Successfully\n" || echo -e "${FLD} Compilation failed\n";
            [ -z "$automate" ] && kbuild;
        } # mkkernel

        echo -ne "\033]0;ScriBt : KernelBuilding\007";
        echo -e "===============${CL_LCN}[!]${NONE} ${CL_WYT}Kernel Building${NONE} ${CL_LCN}[!]${NONE}=================";
        echo -e "Building on : ${KBUILD_BUILD_USER:-$(whoami)}@${KBUILD_BUILD_HOST:-$(hostname)}";
        echo -e "Arch : ${SBKA:-Not Set}";
        echo -e "Definition Config : ${SBKD:-Not Set}";
        echo -e "Toolchain : ${SBKTL:-Not Set}\n";
        echo -e "1. Initialize the Kernel";
        echo -e "2. Setup Toolchain";
        echo -e "3. Clean Kernel output";
        echo -e "4. Set Custom User and Host Names";
        echo -e "5. Build the kernel";
#       echo -e "X. Setup Custom Toolchain";
        echo -e "0. Quick Menu";
        echo -e "=======================================================\n";
        ST="Selected Option"; shut_my_mouth KO "$ST";
        case "$SBKO" in
            0)
                cd ${CALL_ME_ROOT};
                quick_menu;
                ;;
            1) kinit ;;
            2) settc ;;
            3) kclean ;;
            4) custuserhost ;;
            5) mkkernel ;;
#           X) dwntc ;;
            *) echo -e "${FLD} Invalid Selection" ;;
        esac
