
    # VROOM!
    DNT=`date +'%d/%m/%y %r'`;
    echo -ne "\033]0;ScriBt : The Beginning\007";

    # I ez Root
    [[ "$(pwd)" != "/" ]] && export CALL_ME_ROOT="$(pwd)" || export CALL_ME_ROOT="";

    #   tempfile      repo sync log       rom build log        vars b4 exe     vars after exe
    TMP=${CALL_ME_ROOT}/temp.txt; STMP=${CALL_ME_ROOT}/temp_sync.txt; RMTMP=${CALL_ME_ROOT}/temp_compile.txt; TV1=${CALL_ME_ROOT}/temp_v1.txt; TV2=${CALL_ME_ROOT}/temp_v2.txt;
    rm -rf ${CALL_ME_ROOT}/temp{,_sync,_compile,_v{1,2}}.txt;
    touch ${CALL_ME_ROOT}/temp{,_sync,_compile,_v{1,2}}.txt;

    # Load RIDb and Colors
    if [[ "$0" == "./ROM.sh" ]] && [ -f ROM.rc ]; then
        source ./ROM.rc; # Load Local ROM.rc
    elif [ ! -z "${PATHDIR}" ]; then
        source ${PATHDIR}ROM.rc; # Load ROM.rc under PATH
    else
        echo "[F] ROM.rc isn't present in ${PWD} OR PATH please make sure repo is cloned correctly";
        exitScriBt 1;
    fi
    color_my_life;

    # Relevant_Coloring
    if [[ $(tput colors) < 2 ]]; then
        export INF="[I]" SCS="[S]" FLD="[F]" EXE="[!]" QN="[?]";
    else
        export INF="${CL_LBL}[!]${NONE}" SCS="${CL_LGN}[!]${NONE}" \
               FLD="${CL_LRD}[!]${NONE}" EXE="${CL_YEL}[!]${NONE}" \
               QN="${CL_LRD}[?]${NONE}";
    fi

    # is the distro supported ??
    pkgmgr_check;

    if [ ! -d ${PATHDIR}.git ]; then # tell the user to re-clone ScriBt
        echo -e "\n${FLD} Folder ${CL_WYT}.git${NONE} not found";
        echo -e "${INF} ${CL_WYT}Re-clone${NONE} ScriBt for upScriBt to work properly\n";
        echo -e "${FLD} Update-Check Cancelled\n\n${INF} No modifications have been done\n";
    fi

    [ ! -z "${PATHDIR}" ] && cd ${PATHDIR};
    # Check Branch
    export BRANCH=`git rev-parse --abbrev-ref HEAD`;
    cd ${CALL_ME_ROOT};

    if [[ "$BRANCH" =~ (master|staging) ]]; then
        # Download the Remote Version of Updater, determine the Internet Connectivity by working of this command
        curl -fs -o ${PATHDIR}upScriBt.sh https://raw.githubusercontent.com/a7r3/ScriBt/${BRANCH}/upScriBt.sh && \
            (echo -e "\n${SCS} Internet Connectivity : ONLINE"; bash ${PATHDIR}upScriBt.sh $0 $1) || \
            echo -e "\n${FLD} Internet Connectivity : OFFINE\n\n${INF} Please connect to the Internet for complete functioning of ScriBt";
    else
        echo -e "\n${INF} Current Working Branch is neither 'master' nor 'staging'\n";
        echo -e "${FLD} Update-Check Cancelled\n\n${INF} No modifications have been done\n";
    fi

    # Where am I ?
    echo -e "\n${INF} ${CL_WYT}I'm in $(pwd)${NONE}\n";

    # are we 64-bit ??
    if ! [[ $(uname -m) =~ (x86_64|amd64) ]]; then
        echo -e "\n\033[0;31m[!]\033[0m Your Processor is not supported\n";
        exitScriBt 1;
    fi

    # AutoBot
    ATBT="${CL_WYT}*${NONE}${CL_LRD}AutoBot${NONE}${CL_WYT}*${NONE}";

    # CHEAT CHEAT CHEAT!
    if [ -z "$automate" ]; then
        echo -e "${QN} Before Starting off, shall I remember the responses you'll enter from now \n${INF} So that it can be Automated next time\n";
        prompt RQ_PGN;
        (set -o posix; set) > ${TV1};
    else
        echo -e "\n${CL_LRD}[${NONE}${CL_YEL}!${NONE}${CL_LRD}]${NONE} ${ATBT} Cheat Code shut_my_mouth applied. I won't ask questions anymore";
    fi
    echo -e "\n${EXE} ./action${CL_LRD}.SHOW_LOGO${NONE}";
    sleep 2;
    clear;
    echo -e "\n\n                 ${CL_LRD}╔═╗${NONE}${CL_YEL}╦═╗${NONE}${CL_LCN}╔═╗${NONE}${CL_LGN} ╦${NONE}${CL_LCN}╔═╗${NONE}${CL_YEL}╦╔═${NONE}${CL_LRD}╔╦╗${NONE}";
    echo -e "                 ${CL_LRD}╠═╝${NONE}${CL_YEL}╠╦╝${NONE}${CL_LCN}║ ║${NONE}${CL_LGN} ║${NONE}${CL_LCN}║╣ ${NONE}${CL_YEL}╠╩╗${NONE}${CL_LRD} ║ ${NONE}";
    echo -e "                 ${CL_LRD}╩  ${NONE}${CL_YEL}╩╚═${NONE}${CL_LCN}╚═╝${NONE}${CL_LGN}╚╝${NONE}${CL_LCN}╚═╝${NONE}${CL_YEL}╩ ╩${NONE}${CL_LRD} ╩${NONE}";
    echo -e "      ${CL_LRD}███████${NONE}${CL_RED}╗${NONE} ${CL_LRD}██████${NONE}${CL_RED}╗${NONE}${CL_LRD}██████${NONE}${CL_RED}╗${NONE} ${CL_LRD}██${NONE}${CL_RED}╗${NONE}${CL_LRD}██████${NONE}${CL_RED}╗${NONE} ${CL_LRD}████████${NONE}${CL_RED}╗${NONE}";
    echo -e "      ${CL_LRD}██${NONE}${CL_RED}╔════╝${NONE}${CL_LRD}██${NONE}${CL_RED}╔════╝${NONE}${CL_LRD}██${NONE}${CL_RED}╔══${NONE}${CL_LRD}██${NONE}${CL_RED}╗${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██${NONE}${CL_RED}╔══${NONE}${CL_LRD}██${NONE}${CL_RED}╗╚══${NONE}${CL_LRD}██${NONE}${CL_RED}╔══╝${NONE}";
    echo -e "      ${CL_LRD}███████${NONE}${CL_RED}╗${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}     ${CL_LRD}██████${NONE}${CL_RED}╔╝${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██████${NONE}${CL_RED}╔╝${NONE}   ${CL_LRD}██${NONE}${CL_RED}║${NONE}";
    echo -e "      ${CL_RED}╚════${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}     ${CL_LRD}██${NONE}${CL_RED}╔══${NONE}${CL_LRD}██${NONE}${CL_RED}╗${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██${NONE}${CL_RED}╔══${NONE}${CL_LRD}██${NONE}${CL_RED}╗${NONE}   ${CL_LRD}██${NONE}${CL_RED}║${NONE}";
    echo -e "      ${CL_LRD}███████${NONE}${CL_RED}║╚${NONE}${CL_LRD}██████${NONE}${CL_RED}╗${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}  ${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██${NONE}${CL_RED}║${NONE}${CL_LRD}██████${NONE}${CL_RED}╔╝${NONE}   ${CL_LRD}██${NONE}${CL_RED}║${NONE}";
    echo -e "      ${CL_RED}╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═════╝    ╚═╝${NONE}\n";
    sleep 1.5;
    echo -e "                         ${CL_WYT}v`cat ${PATHDIR}VERSION`${NONE}\n";
