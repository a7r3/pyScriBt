    # change terminal title
    [ ! -z "$automate" ] && teh_action 1;
    rom_select;
    sleep 1;
    echo -e "${EXE} Detecting Available Branches in ${ROM_FN} Repository";
    RCT=$[ ${#ROM_NAME[*]} - 1 ];
    for CT in `eval echo "{0..$RCT}"`; do
        echo -e "\nOn ${ROM_NAME[$CT]} (ID->$CT)\n";
        BRANCHES=`git ls-remote -h https://github.com/${ROM_NAME[$CT]}/${MAN[$CT]} |\
            awk '{print $2}' | awk -F "/" '{if (length($4) != 0) {print $3"/"$4} else {print $3}}'`;
        if [[ ! -z "$CNS" && "$SBRN" < "35" ]]; then
            echo "$BRANCHES" | grep --color=never 'caf' | column;
        else
            echo "$BRANCHES" | column;
        fi
    done
    unset CT;
    echo -e "\n${INF} These Branches are available at the moment\n${QN} Specify the ID and Branch you're going to sync\n${INF} Format : [ID] [BRANCH]\n";
    ST="Branch"; shut_my_mouth NBR "$ST";
    RC=`echo "$SBNBR" | awk '{print $1}'`; SBBR=`echo "$SBNBR" | awk '{print $2}'`;
    MNF=`echo "${MAN[$RC]}"`;
    RNM=`echo "${ROM_NAME[$RC]}"`;
    echo -e "${QN} Any Source you have already synced ${CL_WYT}[y/n]${NONE}\n"; gimme_info "refer";
    ST="Use Reference Source"; shut_my_mouth RF "$ST";
    if [[ "$SBRF" == [Yy] ]]; then
        echo -e "\n${QN} Provide me the Synced Source's Location from /\n";
        ST="Reference Location"; shut_my_mouth RFL "$ST";
        REF=--reference\=\"${SBRFL}\";
    else
        REF=" ";
    fi
    echo -e "${QN} Set clone-depth ${CL_WYT}[y/n]${NONE}\n"; gimme_info "cldp";
    ST="Use clone-depth"; shut_my_mouth CD "$ST";
    if [[ "$SBCD" =~ (Y|y) ]]; then
        echo -e "${QN} Depth Value [1]\n";
        ST="clone-depth Value"; shut_my_mouth DEP "$ST";
        [ -z "$SBDEP" ] && SBDEP=1;
        CDP=--depth\=\"${SBDEP}\";
    fi
    # Check for Presence of Repo Binary
    if [[ ! $(which repo) ]]; then
        echo -e "${EXE} Looks like the Repo binary isn't installed. Let's Install it.\n";
        [ ! -d "${HOME}/bin" ] && mkdir -pv ${HOME}/bin;
        curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo;
        chmod a+x ~/bin/repo;
        echo -e "${SCS} Repo Binary Installed\n${EXE} Adding ~/bin to PATH\n";
        if [[ $(grep 'PATH=*' ~/.profile | grep -c '$HOME/bin') != "0" ]]; then
            echo -e "${SCS} $HOME/bin is in PATH";
        else
            echo -e "\n# set PATH so it includes user's private bin if it exists" >> ~/.profile;
            echo -e "if [ -d \"\$HOME/bin\" ]; then\n\tPATH=\"\$HOME/bin:\$PATH\"\nfi" >> ~/.profile;
            . ~/.profile;
            echo -e "${SCS} $HOME/bin added to PATH"
        fi
        echo -e "${SCS} Done. Ready to Init Repo.\n";
    fi
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    echo -e "${EXE} Initializing the ROM Repo\n";
    repo init ${REF} ${CDP} -u https://github.com/${RNM}/${MNF} -b ${SBBR};
    if [[ "$?" == "0" ]]; then
        echo -e "\n${SCS} ${ROM_NAME[$RC]} Repo Initialized\n";
    else
        echo -e "\n${FLD} Failed to Initialize Repo";
        export RINIT="FLD";
    fi
    echo -e "${CL_WYT}=======================================================${NONE}\n";
    if [ -z "$RINIT" ]; then
        [ ! -f .repo/local_manifests ] && mkdir -pv .repo/local_manifests;
        if [ -z "$automate" ]; then
            echo -e "${INF} Create a Device Specific manifest and Press ENTER to start sync\n";
            read ENTER;
            echo;
        fi
        export action_1="init";
        sync
    else
        unset RINIT;
        quick_menu;
    fi
