    {
        echo -e "${QN} ENTER the Directory where the Module is made from : \n";
        prompt MODDIR;
        echo -e "\n${QN} Do you want to push the Module to the Device (Running the Same ROM) ${CL_WYT}[y/n]${NONE} : \n";
        prompt PMOD;
        echo;
        case "$PMOD" in
            [yY]) mmmp -B $MODDIR ;; # make module and push it to device
            [nN]) mmm -B $MODDIR ;; # make module only
            *) echo -e "${FLD}Invalid Selection.\n"; make_it ;;
        esac
