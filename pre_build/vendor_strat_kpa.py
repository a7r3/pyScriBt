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
