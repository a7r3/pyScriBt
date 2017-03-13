    {
        echo -e "\n${EXE} Saving Current Configuration";
        echo -e "\n${QN} Name of the Config\n${INF} Default : ${ROMNIS}_${SBDEV}\n";
        prompt NOC;
        [[ -z "$NOC" ]] && NOC="${ROMNIS}_${SBDEV}";
        if [[ ! -f "${NOC}.rc" ]]; then
            echo -e "${FLD} Configuration ${NOC} exists";
            echo -e "${QN} Overwrite it ${CL_WYT}[y/n]${NONE}";
            prompt OVRT;
            case "$OVRT" in
                [Yy]) echo -e "${EXE} Deleting ${NOC}"; rm -rf ${NOC}.rc ;;
                [Nn]) prefGen ;;
            esac
        fi
        (set -o posix; set) > ${TV2};
        echo -e "# ScriBt Automation Config File" >> ${NOC}.rc;
        echo -e "# ${ROM_FN} for ${SBDEV}\nAUTOMATE=\"true_dat\"\n" >> ${NOC}.rc;
        echo -e "#################\n#  Information  #\n#################\n\n" >> ${NOC}.rc;
        diff ${TV1} ${TV2} | grep SB | sed -e 's/[<>] /    /g' | awk '{print $0";"}' >> ${NOC}.rc;
        echo -e "\n\n#################\n#  Sequencing  #\n##################\n" >> ${NOC}.rc;
        echo -e "# Your Code goes here\n\ninit;\npre_build;\nbuild;\n\n# Some moar code eg. Uploading the ROM" >> ${NOC}.rc;
        echo -e "\n${SCS} Configuration file ${NOC} created successfully\n${INF} You may modify the config, and automate ScriBt next time";
