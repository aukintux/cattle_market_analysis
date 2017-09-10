#! /bin/bash

cd "../pdfs"
   	for PHOTO in *.pdf
   	do
       	BASE=`basename $PHOTO`
       	filename=${BASE%.pdf}
		convert -density 400 "$PHOTO" "../img/$filename.jpg"
   	done