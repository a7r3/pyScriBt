
    case "$1" in
    1)
        echo -ne '\033]0;ScriBt : Init\007';
        [ -z "$automate" ] && init;
        ;;
    2)
        echo -ne "\033]0;ScriBt : Syncing ${ROM_FN}\007";
        [ -z "$automate" ] & sync;
        ;;
    3)
        echo -ne '\033]0;ScriBt : Pre-Build\007';
        [ -z "$automate" ] && pre_build;
        ;;
    4)
        if [[ -z "$ROMNIS" ]] || [[ -z "$SBDEV" ]]; then
            echo -ne "\033]0;ScriBt : Build\007";
        else
            echo -ne "\033]0;${ROMNIS}_${SBDEV} : In Progress\007";
        fi
        [ -z "$automate" ] && build;
        ;;
    5)
        echo -ne '\033]0;ScriBt : Installing Dependencies\007';
        [ -z "$automate" ] && tools;
        ;;
    6)
        case "$2" in
            "COOL") echo -ne "\033]0;${ROMNIS}_${SBDEV} : Success\007"; [ -z "$automate" ] && exitScriBt 0 ;;
            "FAIL") echo -ne "\033]0;${ROMNIS}_${SBDEV} : Fail\007"; [ -z "$automate" ] && exitScriBt 1 ;;
            [qm]m) exitScriBt 0 ;;
        esac
        ;;
    *)
        echo -e "\n${FLD} Invalid Selection.\n";
        case "$2" in
            "qm") quick_menu ;;
            "mm") main_menu ;;
        esac
        ;;
    esac
