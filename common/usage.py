
    [ ! -z "$1" ] && echo -e "\n\033[1;31m[!]\033[0m Incorrect Parameter : \"$1\"";
    echo -e "\n\033[1;34m[!]\033[0m Usage:\n";
    ZEROP=( ./ROM.sh ROM.sh );
    CT="0";
        for presence in "Current Directory" "PATH"; do
            echo -e "To use ScriBt situated in ${presence}\n";
            echo -e "\tbash ${ZEROP[$CT]} (Interactive Usage)";
            echo -e "\tbash ${ZEROP[$CT]} automate (Automated Usage)";
            echo -e "\tbash ${ZEROP[$CT]} version (For showing Version of ScriBt)";
            echo -e "\tbash ${ZEROP[$CT]} usage (To get these usage statements)\n";
            (( CT++ ));
        done
    unset CT ZEROP;
    [ ! -z "$1" ] && exitScriBt 1;
