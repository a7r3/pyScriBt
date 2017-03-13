
    if [ ! -z "$automate" ]; then
        RST="SB$1";
        echo -e "${CL_PNK}[!]${NONE} ${ATBT} $2 : ${!RST}";
    else
        prompt SB2;
        [ -z "$3" ] && export SB$1="${SB2}" || eval SB$1=${SB2};
    fi
    echo;
