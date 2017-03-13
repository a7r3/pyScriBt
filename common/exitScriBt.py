
    function prefGen()
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
    } # prefGen

    if type patcher &>/dev/null; then # Assume the patchmgr was used if this function is loaded
        if show_patches | grep -q '[Y]'; then # Some patches are still applied
            echo -e "\n${INF} Applied Patches detected. Do you want to reverse them?\n"
            prompt ANSWER;
            [[ "$ANSWER" == [Yy] ]] && patcher;
        fi
    fi
    [[ "$RQ_PGN" == [Yy] ]] && prefGen || ((set -o posix; set) > ${TV2});
    echo -e "\n${EXE} Unsetting all variables";
    unset `diff temp_v1.txt temp_v2.txt | grep SB | sed -e 's/[<>] /    /g' | awk -F "=" '{print $1}'`;
    echo -e "\n${SCS:-[:)]} Thanks for using ScriBt.\n";
    [[ "$1" == "0" ]] && echo -e "${CL_LGN}[${NONE}${CL_LRD}<3${NONE}${CL_LGN}]${NONE} Peace! :)\n" ||\
        echo -e "${CL_LRD}[${NONE}${CL_RED}<${NONE}${CL_LGR}/${NONE}${CL_RED}3${NONE}${CL_LRD}]${NONE} Failed somewhere :(\n";
    rm ${CALL_ME_ROOT}/temp_v1.txt ${CALL_ME_ROOT}/temp_v2.txt ${CALL_ME_ROOT}/temp.txt
    [ -s ${CALL_ME_ROOT}/temp_sync.txt ] || rm ${CALL_ME_ROOT}/temp_sync.txt # If temp_sync.txt is empty, delete it
    [ -s ${CALL_ME_ROOT}/temp_compile.txt ] || rm ${CALL_ME_ROOT}/temp_compile.txt # If temp_compile.txt is empty, delete it
    exit $1;
