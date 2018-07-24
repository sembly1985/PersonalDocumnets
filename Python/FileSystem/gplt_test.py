from wp_gplt import *
test=gplt(r'd:\gnuplot\gnuplot')
test.start()
test.plot([[[1,2,3],[20,20,30],"with linespoints lt 1 pt 9 lc 0 title 'test'"],\
	[[1,2,3],[20,30,40],"with linespoints lt 1 pt 9 lc 1 title 'test'"]])
time.sleep(1);