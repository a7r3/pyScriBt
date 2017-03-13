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
