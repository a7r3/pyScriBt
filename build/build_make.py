    {
        if [[ "$1" != "brunch" ]]; then
            START=$(date +"%s"); # Build start time
            # Showtime!
            BCORES="-j${BCORES}";
            if [ $(grep -q "^${ROMNIS}:" "${CALL_ME_ROOT}/build/core/Makefile") ]; then
                $SBMK $ROMNIS $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            elif [ $(grep -q "^bacon:" "${CALL_ME_ROOT}/build/core/Makefile") ]; then
                $SBMK bacon $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            else
                $SBMK otapackage $BCORES && BLDSCS="yay" 2>&1 | tee $RMTMP;
            fi
            END=$(date +"%s"); # Build end time
            SEC=$(($END - $START)); # Difference gives Build Time
            if [ -z "$BLDSCS" ]; then
                echo -e "\n${FLD} Build Status : Failed";
            else
                echo -e "\n${SCS} Build Status : Success";
            fi
            echo -e "\n${INF} ${CL_WYT}Build took $(($SEC / 3600)) hour(s), $(($SEC / 60 % 60)) minute(s) and $(($SEC % 60)) second(s).${NONE}" | tee -a rom_compile.txt;
            #post_build; # comment it please xD
        fi
