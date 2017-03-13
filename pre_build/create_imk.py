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
