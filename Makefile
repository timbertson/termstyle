0:
	mkzero-gfxmonk \
		-v `cat VERSION` \
		-p termstyle \
		-p setup.py \
		python-termstyle.xml

pypi:
	./setup.py register
