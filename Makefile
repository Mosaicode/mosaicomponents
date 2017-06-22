clean:

	rm -rfv mosaicomponents/*.pyc mosaicomponents/*.py,cache mosaicomponents/__pycache__
	rm -rfv *.pyc *.py,cache __pycache__
	rm -rfv test/*.pyc test/*.py,cache test/__pycache__
	rm -rfv test/mosaicomponents/*.pyc test/mosaicomponents/*.py,cache test/mosaicomponents/__pycache__
	sudo rm -rfv mosaicomponents.egg-info
	clear

coverage:
	sudo coverage run --source=. setup.py test
	coverage report -m
	coverage html
