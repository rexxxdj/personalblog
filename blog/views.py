from django.shortcuts import render


def article_list(request):
	articles = (
		{'id': 1,
		 'category':'Programming',
		 'image': '../static/img/blog-1.jpg',
		  'title': u'Why Is Python Such a Popular Programming Language?',
		  'createdate': '11.06.2018',
		  'author': u'Rexxx',
		  'commentscnt': 11,
		  'middlecontent': u'Why is Python so popular?\
		  					 <br>To the surprise of absolutely nobody, \
		  					 the language continues to rank highly on various lists of the world’s most popular programming languages, \
		  					 including the TIOBE Index and the PyPL PopularitY of Programming Language Index.\
                    		<br>Many programmers view Python as a language with a clean syntax and an expansive \
                    		library; thanks to its longevity, there’s also a plethora of third-party documentation, \
                    		meaning that anyone with a problem or question can (usually) find an answer \
                    		fairly quickly.'},
        {'id': 2,
         'category':'Databases',
		 'image': '../static/img/blog-2.jpg',
		  'title': u'Duis autem vel eum iriure dolor',
		  'createdate': '8.11.2012',
		  'author': u'Admin',
		  'commentscnt': 9,
		  'middlecontent': u'Morbi ullamcorper, leo eget varius elementum, orci leo feugiat lectus, vitae lobortis \
		  					 mauris velit tempor erat. Etiam eget orci at massa pretium fringilla ac non tortor. \
		  					 Fusce sed velit risus, vitae vehicula quam. Cras at turpis urna, eget volutpat neque. \
		  					 Nullam porttitor, est interdum placerat pharetra, erat sapien aliquet urna, at commodo \
		  					 risus tellus eu nunc.'},
        {'id': 3,
         'category':'Other',
		 'image': '../static/img/blog-3.jpg',
		  'title': u'Nullam porttitor est interdum placerat pharetra',
		  'createdate': '11.06.2018',
		  'author': u'Admin',
		  'commentscnt': 18,
		  'middlecontent': u'Morbi ullamcorper, leo eget varius elementum, orci leo feugiat lectus, \
		  					 vitae lobortis mauris velit tempor erat. Etiam eget orci at massa pretium fringilla \
		  					 ac non tortor. Fusce sed velit risus, vitae vehicula quam. Cras at turpis urna, eget \
		  					 volutpat neque. Nullam porttitor, est interdum placerat pharetra, erat sapien aliquet \
		  					 urna, at commodo risus tellus eu nunc.'},
	)

	return render(request, 'blog.html', {'articles': articles})