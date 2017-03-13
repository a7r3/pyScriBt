    {
        # If util is repo then concatenate the file else execute it as a binary
        [[ "$1" == "repo" ]] && CAT="cat " || unset CAT;
        case "$2" in
            "utils") BIN="${CAT}utils/$1" ;; # Util Version that ScriBt has under utils folder
            "installed") BIN="${CAT}$(which $1)" ;; # Util Version that has been installed in the System
        esac
        case "$1" in # Installed Version
            "ccache") VER=`${BIN} --version | head -1 | awk '{print $3}'` ;;
            "make") VER=`${BIN} -v | head -1 | awk '{print $3}'` ;;
            "ninja") VER=`${BIN} --version` ;;
            # since repo is a python script and not a binary
            "repo") VER=`${BIN} | grep -m 1 VERSION |\
                        awk -F "= " '{print $2}' |\
                        sed -e 's/[()]//g' |\
                        awk -F ", " '{print $1"."$2}'`;
                    ;;
        esac
