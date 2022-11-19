#! /bin/zsh

#input
echo "Bitte PFAD zu 'Alice_im_Wunderland.txt' eingeben"
read fname
echo "Bitte Satz zum Suchen eingeben (alles kleingeschrieben)"
read input
search="$(tr '[:lower:]' '[:upper:]' <<< ${input:0:1})${input:1}"

#change "_" in 
for (( i=0; i<${#search}; i++ )); do
    char=${search:$i:1};
    if [ $char = "_" ]; then
        search=${search/_/.*};
    fi
done

#use grep, pattern = Das.*mir.*vor.*, fname = Alice_im_Wunderland.txt 
result=`grep -E "$search", $fname`
echo $result;

#greb ist laut https://www.einstieg-informatik.de/community/forums/topic/877/41-1-a1-storung-shell erlaubt zu benutzen.