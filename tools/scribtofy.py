    {
        echo -e "\n${INF} This Function allows ScriBt to be executed under any directory";
        echo -e "${INF} Temporary Files would be present at working directory itself";
        echo -e "${INF} Older ScriBtofications, if present, would be overwritten";
        echo -e "\n${QN} Shall I ScriBtofy ${CL_WYT}[y/n]${NONE}\n";
        prompt SBFY;
        case "$SBFY" in
            [Yy])
                    echo -e "\n${EXE} Adding ScriBt to PATH";
                    echo -e "# ScriBtofy\nexport PATH=\"${CALL_ME_ROOT}:\$PATH\";" > ${HOME}/.scribt;
                    [[ $(grep 'source ${HOME}/.scribt' ${HOME}/.bashrc) ]] && echo -e "\n#ScriBtofy\nsource \${HOME}/.scribt;" >> ${HOME}/.bashrc;
                    echo -e "\n${EXE} Executing ~/.bashrc";
                    source ~/.bashrc;
                    echo -e "\n${SCS} Done\n\n${INF} Now you can ${CL_WYT}bash ROM.sh${NONE} under any directory";
                ;;
            [Nn])
                echo -e "${FLD} ScriBtofication cancelled";
                ;;
        esac
