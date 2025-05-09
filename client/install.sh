while read line
do
    packwiz modrinth install "$line"
    BACK_PID=$!
    wait $BACK_PID
done < modlist.txt
