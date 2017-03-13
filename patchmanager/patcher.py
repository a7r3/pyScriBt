        {
            show_patches;
            echo -e "\n=======================================================\n";
            prompt PATCHNR;
            case "$PATCHNR" in # Process śpecial actions
                0) quick_menu ;; # Exit the Patch Manager and return to Quick Menu
                1)
                    patch_creator;
                    patcher;
                    ;;
                *)
                    [ "${PATCHES[$PATCHNR]}" ] && apply_patch "${PATCHES[$PATCHNR]}" ||
                    echo -e "\n${FLD} Invalid selection: $PATCHNR";
                    patcher;
                    ;;
            esac
