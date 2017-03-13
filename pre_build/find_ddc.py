    {
        ROMC=( aicp aokp aosp bliss candy carbon crdroid cyanide cm du eos lineage \
                orion ownrom radium slim tesla tipsy to validus vanir xenonhd xosp );
        for ROM in ${ROMC[*]}; do
            # Possible Default Device Configuration (DDC) Files
            DDCS=( ${ROM}_${SBDEV}.mk full_${SBDEV}.mk aosp_${SBDEV}.mk ${ROM}.mk );
            # Makefiles are arranged according to their priority of Usage
            # ROM.mk is the most used, ROM_DEVICE.mk is the least used.
            # Inherit DDC
            for ACTUAL_DDC in ${DDCS[*]}; do
                if [ -f ${DEVDIR}/${ACTUAL_DDC} ]; then
                    case "$1" in
                        "pb") export DDC="$ACTUAL_DDC" ;;
                        "intm") # Interactive Makefile not found -vv
                            if [[ $(grep -c '##### Interactive' ${DEVDIR}/${ACTUAL_DDC}) == "0" ]] \
                            && [[ "$ACTUAL_DDC" != "${ROMNIS}.mk" ]]; then # ROM Specific Makefile not Present
                                export DDC="$ACTUAL_DDC"; # Interactive makefile not present for that particular ROMNIS
                                continue; # searching for more relevant makefile
                            else
                                export DDC="NULL"; # Interactive Makefile already created, under ROMNIS name
                                break; # What now ? Get out!
                            fi
                            ;;
                    esac
                fi
            done
            [[ "$DDC" == "NULL" ]] && break; # It's Done, Get out!
        done
