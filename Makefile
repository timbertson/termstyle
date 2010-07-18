egg:
	./setup.py bdist_egg

0:
	mkzero-gfxmonk \
		-v `cat VERSION` \
		-p termstyle \
		python-termstyle.xml

0copy:
	mkzero-gfxmonk \
		-v `cat VERSION` \
		-c \
		python-termstyle.xml
