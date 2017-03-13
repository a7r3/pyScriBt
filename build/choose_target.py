
    case "$ROMNIS" in
        eos|pure) TARGET="${SBDEV}-${SBBT}" ;;
        *) TARGET="${ROMNIS}_${SBDEV}-${SBBT}" ;;
    esac
