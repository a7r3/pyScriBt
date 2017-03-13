
    echo -e "\n${INF} Specify the Size (Number) for Reservation of CCACHE (in GB)\n${INF} CCACHE Size must be >15-20 GB for ONE ROM\n";
    prompt CCSIZE;
    echo -e "\n${INF} Create a New Folder for CCACHE and Specify it's location from /\n";
    prompt CCDIR;
    for RC in .profile .bashrc; do
        if [ -f ${HOME}/${RC} ]; then
            if [[ $(grep -c 'USE_CCACHE\|CCACHE_DIR' ${HOME}/${RC}) == 0 ]]; then
                echo -e "export USE_CCACHE=1\nexport CCACHE_DIR=${CCDIR}" >> ${HOME}/${RC};
                . ${HOME}/${RC};
                echo -e "\n${SCS} CCACHE Specific exports added in ${CL_WYT}${RC}${NONE}";
            else
                echo -e "\n${SCS} CCACHE Specific exports already enabled in ${CL_WYT}${RC}${NONE}";
            fi
            break; # One file, and its done
        fi
    done
    set_ccache;
