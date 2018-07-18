from django.shortcuts import render


def mainpage_list(request):
	slides = (
		{'id': 1,
		'name': 'Slide_1',
		'image': '../static/img/slide-1.jpg'},
		{'id': 2,
		'name': 'Slide_3',
		'image': '../static/img/slide-2.jpg'},
		{'id': 3,
		'name': 'Slide_3',
		'image': '../static/img/slide-3.jpg'},
		{'id': 4,
		'name': 'Slide_4',
		'image': '../static/img/slide-4.jpg'},
		{'id': 5,
		'name': 'Slide_5',
		'image': '../static/img/slide-5.jpg'},
		)

	programing = (
		{'id': 1,
		 'image': '../static/img/blog-featured-01.jpg',
		  'title': u'At vero eos et accusamus et iusto ',
		  'createdate': '9.11.2012',
		  'author': u'Admin',
		  'commentscnt': 7,
		  'smallcontent': u'Vivamus sollicitudin libero auctor arcu pulvinar commodo.'},
		)

	databases = (
		{'id': 2,
		 'image': '../static/img/blog-featured-02.jpg',
		  'title': u'Deleniti atque corrupti quos ',
		  'createdate': '9.11.2012',
		  'author': u'Admin',
		  'commentscnt': 15,
		  'smallcontent': u'Vestibulum volutpat urna sed sapien vehicula varius.'},
		)

	work = (
		{'id': 3,
		 'image': '../static/img/blog-featured-03.jpg',
		  'title': u'Similique sunt in culpa qui official ',
		  'createdate': '9.11.2012',
		  'author': u'Admin',
		  'commentscnt': 9,
		  'smallcontent': u'Pellentesque mi justo, laoreet non bibendum non, auctor imperdiet eros.'},
		)

	other = (
		{'id': 4,
		 'image': '../static/img/blog-featured-04.jpg',
		  'title': u'Similique sunt in culpa qui official ',
		  'createdate': '9.11.2012',
		  'author': u'Admin',
		  'commentscnt': 1,
		  'smallcontent': u'Vestibulum volutpat urna sed sapien vehicula varius.'},
		)

	return render(request, 'index.html', {'slides': slides, 'programing': programing, 'databases': databases, 'work':work, 'other': other})