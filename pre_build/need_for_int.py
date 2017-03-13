    {
        if [ -f ${CALL_ME_ROOT}/${DEVDIR}/${INTF} ]; then
            echo "$NOINT";
        else
            interactive_mk "$SBRN";
        fi
