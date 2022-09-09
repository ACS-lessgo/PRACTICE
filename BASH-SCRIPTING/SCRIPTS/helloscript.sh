#! /usr/bin/bash

# to create a script file use command (touch script_name.sh)


#to write one line comment

#for multiline comment
: '
for multiline comment
for multiline comment
for multiline comment
for multiline comment
'
# cat> file.txt     -->rewrite data into a txt file

# cat >> file.txt   -->append new data into existing data

# echo "add ur comment" --> displays a comment in the terminal

# echo "add ur comment" > file.txt -->append comment or data onto a txt file

: '
cat << creative
this is my     #here-doc-delimeter to show multiple comments or info in terminal
hehe paimon hehe
creative
'
#conditional statements

#if,if-else-if loops

#-eq equal,-ne not equal,-gt greater than,-lt less than

: '
count=10
if (( $count < 1 ))
then
    echo  " the condition is true"
elif [ $count -eq 10 ]
then
    echo " this is the elif condition"
else
    echo " no no no"
fi
'
#AND OPERATOR -a or &&
#OR OPERATOR -o or ||
: '
age=32

if [ "$age" -gt 18 ] && [ "$age" -lt 40 ] #and operation
then
    echo "Age is Good"
else
    echo "Age is Bad"
fi   # to terminate the condtion
'

#CASE STATEMENTS
: '
echo -n "Enter the name of a country: "  #get input from user
read COUNTRY                             #read input

echo -n "The official language of $COUNTRY is " #displays

case $COUNTRY in

  Lithuania)
    echo -n "Lithuanian"
    ;;

  Romania | Moldova)
    echo -n "Romanian"
    ;;

  Italy | "San Marino" | Switzerland | "Vatican City")
    echo -n "Italian"
    ;;

  *)
    echo -n "unknown"
    ;;
esac
'

#LOOPS IN BASH

#WHILE LOOP

: '
number=1
while [ $number -le 10 ]     #less than or equal to
do
    echo "$number"
    number=$(( number+1))
done
'

#UNTIL LOOP
: '
number=1
until [ $number -ge 10 ]     #greater than or equal to
do
    echo $number
    number=$(( number+1))
done
'

#FOR LOOP

: '
#for (( i=0;i<=5:i++ )) # normal method
for i in {0..10..2}   # {range of numbers...increment}
do
    echo $i
done
'

#BREAK AND CONTINUE
: '
for i in {0..10}   # {range of numbers...increment}
do
    if [ $i -gt 5 ]
    then
        break
    fi
    echo $i
done
'
: '
for i in {0..10}   # {range of numbers...increment}
do
    if [ $i -eq 3 ] || [ $i -eq 7 ]
    then
        continue          #skips loop when i is 3 and 7
    fi
    echo $i
done
'

#echo $0 $1 $2 $3  --> take input in terminal and give output

#arge=("$@")      --> initializing an array

#echo ${@         --> giving out array

#echo $#          --> length of the array


#READING FILES // SCRIPT INPUT
: '
while read line
do
    echo "$line"
done < "${1:-/dev/stdin}"  #  --> asuming terminal as a file
'

#SCRIPT OUTPUT

# ls +al 1>file.txt 2>error.txt

#file 1 for input
#file 2 incase of any error

#ls -al >& file.txt
#output and input in same file using &









