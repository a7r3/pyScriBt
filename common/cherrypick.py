
    echo -ne '\033]0;ScriBt : Picking Cherries\007';
    echo -e "${CL_WYT}=======================${NONE} ${CL_LRD}Pick those Cherries${NONE} ${CL_WYT}======================${NONE}\n";
    echo -e "${EXE} ${ATBT} Attempting to Cherry-Pick Provided Commits\n";
    cd ${CALL_ME_ROOT}/$1;
    git fetch ${2/\/tree\// };
    git cherry-pick $3;
    cd ${CALL_ME_ROOT};
    echo -e "\n${INF} It's possible that the pick may have conflicts. Solve those and then continue.";
    echo -e "${CL_WYT}==================================================================${NONE}";
