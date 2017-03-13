
    echo -e "\n${EXE} Searching for Automatable Configs\n";
    for AF in `ls *.rc | sed -e 's/ROM.rc//g'`; do
        grep 'AUTOMATOR\=\"true_dat\"' --color=never $AF -l >> ${TMP};
        sed -i -e 's/.rc//g' ${TMP}; # Remove the file format
    done
    if [[ $(echo "$?") ]]; then
        NO=1;
        # Adapted from lunch selection menu
        for CT in `cat ${TMP}`; do
            CMB[$NO]="$CT";
            ((NO++));
        done
        unset CT;
        for CT in `eval echo "{1..${#CMB[*]}}"`; do
            echo -e " $CT. ${CMB[$CT]} ";
        done | column
        unset CT;
        echo -e "\n${QN} Which would you like\n";
        prompt ANO;
        echo -e "\n${EXE} Running ScriBt on Automation Config ${CMB[$ANO]}\n";
        sleep 2;
        . ${CMB[${ANO}]}.rc;
    else
        echo -e "\n${FLD} No Automation Configs found\n";
        exitScriBt 1;
    fi
