#! /bin/zsh

#input
fname="/Users/ben/programming/BWINF41/Aufgabe 1 Störung/Alice_im_Wunderland.txt";
input="wollen _ so _ sein";

#change "_" in 
for (( i=0; i<${#input}; i++ )); do
    char=${input:$i:1};
    if [ $char = "_" ]; then
        input=${input/_/.*};
    fi
done


#first check if result stores any values, if not its because the first char isnt upper letter
#use grep, search = Das.*mir.*vor.*, fname = Alice_im_Wunderland.txt 
result=`grep -E "$input" $fname`
if [ -z $result ]; then
    search="$(tr '[:lower:]' '[:upper:]' <<< ${input:0:1})${input:1}";      #upper first char
    result=`grep -E "$search" $fname`
    echo $result
else
    echo $result                                                            # if result has value, echo it
fi


#greb ist laut https://www.einstieg-informatik.de/community/forums/topic/877/41-1-a1-storung-shell erlaubt zu benutzen.