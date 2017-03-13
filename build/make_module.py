    {
        if [ -z "$1" ]; then
            echo -e "\n${QN} Know the Location of the Module : \n";
            prompt KNWLOC;
        fi
        if [[ "$KNWLOC" == "y" || "$1" == "y" ]]; then
            make_it;
        else
            echo -e "${INF} Do either of these two actions:\n1. Google it (Easier)\n2. Run this command in terminal : sgrep \"LOCAL_MODULE := <Insert_MODULE_NAME_Here> \".\n\n Press ENTER after it's Done..\n";
            read ENTER;
            make_it;
        fi
