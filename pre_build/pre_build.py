
    # To prevent missing information, if user starts directly from here
    [ -z "$action_1" ] && rom_select;
    init_bld;
    device_info;
    # Change terminal title
    [ ! -z "$automate" ] && teh_action 3;
    DEVDIR="device/${SBCM}/${SBDEV}";

    function vendor_strat_all()
    {
        [[ ! -z "$ROMV" ]] && cd vendor/${ROMV} || cd vendor/${ROMNIS};
        echo -e "${CL_WYT}=======================================================${NONE}\n";

        function dtree_add()
        {   # AOSP-CAF|RRO|F-AOSP|Flayr|OmniROM|Zephyr
            echo -e "${EXE} Adding Lunch Combo in Device Tree";
            [ ! -f vendorsetup.sh ] && touch vendorsetup.sh;
            if [[ $(grep -c "${ROMNIS}_${SBDEV}" ${DEVDIR}/vendorsetup.sh ) == "0" ]]; then
                echo -e "add_lunch_combo ${ROMNIS}_${SBDEV}-${SBBT}" >> vendorsetup.sh;
            else
                echo -e "${SCS} Lunch combo already added to vendorsetup.sh\n";
            fi
        } # dtree_add

        [[ "$ROMNIS" == "du"  && "$CAF" == "y" ]] && VSTP="caf-vendorsetup.sh" | VSTP="vendorsetup.sh";
        echo -e "${EXE} Adding Device to ROM Vendor";
        for STRT in "${ROMNIS}.devices" "${ROMNIS}-device-targets" "${VSTP}"; do
            #    Found file   &&  Strat Not Performed
            if [ -f "$STRT" ] && [ -z "$STDN" ]; then
                if [[ $(grep -c "${SBDEV}" $STRT) == "0" ]]; then
                    case "$STRT" in
                        ${ROMNIS}.devices)
                            echo -e "${SBDEV}" >> $STRT ;;
                        ${ROMNIS}-device-targets)
                            echo -e "${TARGET}" >> $STRT ;;
                        ${VSTP})
                            echo -e "add_lunch_combo ${TARGET}" >> $STRT ;;
                    esac
                else
                    echo -e "${INF} Device already added to $STRT";
                fi
                export STDN="y"; # File Found, Strat Performed
            fi
        done
        [ -z "$STDN" ] && dtree_add; # If none of the Strats Worked
        echo -e "${SCS} Done.\n";
        croot;
        echo -e "${CL_WYT}=======================================================${NONE}";
    } # vendor_strat

    function vendor_strat_kpa() # AOKP-4.4|AICP|PAC-5.1|Krexus-CAF|AOSPA|Non-CAFs
    {
        croot;
        cd vendor/${ROMNIS}/products;

        function bootanim()
        {
            echo -e "${INF} Device Resolution\n";
            if [ ! -z "$automate" ]; then
                gimme_info "bootres";
                echo -e "${QN} Enter the Desired Highlighted Number\n";
                prompt SBBTR;
            else
                echo -e "${INF} ${ATBT} Resolution Chosen : ${SBBTR}";
            fi
        } # bootanim

        #Vendor-Calls
        case "$ROMNIS" in
            "aicp")
                VENF="${SBDEV}.mk";
                echo -e "\t\$(LOCAL_DIR)/${VENF}" >> AndroidProducts.mk;
                echo -e "\n# Inherit telephony stuff\n\$(call inherit-product, vendor/${ROMNIS}/configs/telephony.mk)" >> $VENF;
                echo -e "\$(call inherit-product, vendor/${ROMNIS}/configs/common.mk)" >> $VENF;
                ;;
            "aokp")
                bootanim;
                VENF="${SBDEV}.mk";
                echo -e "\t\$(LOCAL_DIR)/${VENF}" >> AndroidProducts.mk;
                echo -e "\$(call inherit-product, vendor/${ROMNIS}/configs/common.mk)" >> $VENF;
                echo -e "\nPRODUCT_COPY_FILES += \\ " >> $VENF;
                echo -e "\tvendor/${ROMNIS}/prebuilt/bootanimation/bootanimation_${SBBTR}.zip:system/media/bootanimation.zip" >> $VENF;
                ;;
            "krexus")
                VENF="${ROMNIS}_${SBDEV}.mk";
                echo -e "\$( call inherit-product, vendor/${ROMNIS}/products/common.mk)" >> $VENF;
                echo -e "\n\$( call inherit-product, vendor/${ROMNIS}/products/vendorless.mk)" >> $VENF;
                ;;
            "pa")
                VENF="${SBDEV}/${ROMNIS}_${SBDEV}.mk";
                echo -e "# ${SBCM} ${SBDEV}" >> AndroidProducts.mk
                echo -e "\nifeq (${ROMNIS}_${SBDEV},\$(TARGET_PRODUCT))" >> AndroidProducts.mk;
                echo -e "\tPRODUCT_MAKEFILES += \$(LOCAL_DIR)/${VENF}\nendif" >> AndroidProducts.mk;
                echo -e "\ninclude vendor/${ROMNIS}/main.mk" >> $VENF;
                mv -f ${CALL_ME_ROOT}/${DEVDIR}/*.dependencies ${SBDEV}/pa.dependencies;
                ;;
            "pac")
                bootanim;
                VENF="${ROMNIS}_${SBDEV}.mk";
                echo -e "\$( call inherit-product, vendor/${ROMNIS}/products/pac_common.mk)" >> $VENF;
                echo -e "\nPAC_BOOTANIMATION_NAME := ${SBBTR};" >> $VENF;
                ;;
            "pure") # PureNexus and ABC rom
                VENF="${SBDEV}.mk";
                echo -e "# Include pure configuration\ninclude vendor/pure/configs/pure_phone.mk" >> $VENF;
                ;;
        esac
        find_ddc "pb";
        echo -e "\n# Inherit from ${DDC}" >> $VENF;
        echo -e "\$(call inherit-product, ${DEVDIR}/${DDC})" >> $VENF;
        # PRODUCT_NAME is the only ROM-specific Identifier, setting it here is better.
        echo -e "\n# ROM Specific Identifier\nPRODUCT_NAME := ${ROMNIS}_${SBDEV}" >> $VENF;
    } # vendor_strat_kpa

    function find_ddc() # For Finding Default Device Configuration file
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
    } # find_ddc

    function interactive_mk()
    {
        init_bld;
        echo -e "\n${EXE} Creating Interactive Makefile for getting Identified by the ROM's BuildSystem\n";
        sleep 2;

        function create_imk()
        {
            cd ${DEVDIR};
            INTM="interact.mk";
            [ -z "$INTF" ] && INTF="${ROMNIS}.mk";
            echo "#                ##### Interactive Makefile #####
#
# Licensed under the Apache License, Version 2.0 (the \"License\");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an \"AS IS\" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License." >> ${INTM};
            echo -e "\n# Inherit ${ROMNIS} common stuff\n\$(call inherit-product, ${CNF}/${VNF}.mk)" >> ${INTM};
            echo -e "\n# Calling Default Device Configuration File" >> ${INTM};
            echo -e "\$(call inherit-product, ${DEVDIR}/${DDC})" >> ${INTM};
            # To prevent Missing Vendor Calls in DDC-File
            sed -i -e 's/inherit-product, vendor\//inherit-product-if-exists, vendor\//g' $DDC;
            # Add User-desired Makefile Calls
            echo -e "${QN} Missed some Makefile calls\n${INF} Enter number of Desired Makefile calls\n${INF} Enter 0 if none";
            ST="No of Makefile Calls"; shut_my_mouth NMK "$ST";
            for (( CT=0; CNT<"${SBNMK}"; CT++ )); do
                echo -e "\n${QN} Enter Makefile location from Root of BuildSystem";
                ST="Makefile"; shut_my_mouth LOC[$CNT] "$ST" array;
                if [ -f ${CALL_ME_ROOT}/${SBLOC[$CNT]} ]; then
                    echo -e "\n${EXE} Adding Makefile `$[ $CNT + 1 ]` ";
                    echo -e "\n\$(call inherit-product, ${SBLOC[$CNT]})" >> ${INTM};
                else
                    echo -e "${FLD} Makefile ${SBLOC[$CNT]} not Found. Aborting";
                fi
            done
            unset CT;
            echo -e "\n# ROM Specific Identifier\nPRODUCT_NAME := ${ROMNIS}_${SBDEV}" >> ${INTM};
            # Make it Identifiable
            mv ${INTM} ${INTF};
            echo -e "${EXE} Renaming .dependencies file\n";
            [ ! -f ${ROMNIS}.dependencies ] && mv -f *.dependencies ${ROMNIS}.dependencies;
            echo -e "${SCS} Done.";
            croot;
        } # create_imk

        find_ddc "intm";
        if [[ "$DDC" != "NULL" ]]; then create_imk; else echo "$NOINT"; fi;
    } # interactive_mk

    function need_for_int()
    {
        if [ -f ${CALL_ME_ROOT}/${DEVDIR}/${INTF} ]; then
            echo "$NOINT";
        else
            interactive_mk "$SBRN";
        fi
    } # need_for_int

    echo -e "\n${EXE} ${ROMNIS}-fying Device Tree\n";
    NOINT=$(echo -e "${SCS} Interactive Makefile Unneeded, continuing");

    case "$SBRN" in
        aosp|eos|omni|zos) # AOSP-CAF/RRO|Euphoria|F-AOSP|Flayr|OmniROM|Parallax|Zephyr
            VNF="common";
            [[ "$SBRN" == "13" ]] && INTF="${ROMNIS}.mk" || INTF="${ROMNIS}_${SBDEV}.mk";
            need_for_int;
            rm -rf ${DEVDIR}/AndroidProducts.mk;
            echo -e "PRODUCT_MAKEFILES :=  \\ \n\t\$(LOCAL_DIR)/${INTF}" >> AndroidProducts.mk;
            ;;
        aosip) # AOSiP-CAF
            if [ ! -f vendor/${ROMNIS}/products ]; then
                VNF="common";
                INTF="${ROMNIS}.mk";
                need_for_int;
            else
                echo "$NOINT";
            fi
            ;;
        aokp|pac) # AOKP-4.4|PAC-5.1
            if [ ! -f vendor/${ROMNIS}/products ]; then
                VNF="$SBDTP";
                INTF="${ROMNIS}.mk"
                need_for_int;
            else
                echo "$NOINT";
            fi
            ;;
        aicp|krexus|pa|pure|krexus|nitrogen|pure) # AICP|Krexus-CAF|AOSPA|Non-CAFs except DU
            echo "$NOINT";
            ;;
        *) # Rest of the ROMs
            VNF="$SBDTP";
            INTF="${ROMNIS}.mk"
            need_for_int;
            ;;
    esac

    choose_target;
    if [ -d vendor/${ROMNIS}/products ]; then # [ -d vendor/aosip ] <- Temporarily commented
        if [ ! -f vendor/${ROMNIS}/products/${ROMNIS}_${SBDEV}.mk ||
             ! -f vendor/${ROMNIS}/products/${SBDEV}.mk ||
             ! -f vendor/${ROMNIS}/products/${SBDEV}/${ROMNIS}_${SBDEV}.mk ]; then
            vendor_strat_kpa; #if found products folder, go ahead
        else
            echo -e "\n${SCS} Looks like ${SBDEV} has been already added to ${ROM_FN} vendor. Good to go\n";
        fi
    else
        vendor_strat_all; # if not found, normal strategies
    fi
    croot;
    sleep 2;
    export action_1="init" action_2="pre_build";
    [ -z "$automate" ] && quick_menu;
