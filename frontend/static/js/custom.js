document.querySelector('.img-btn').addEventListener('click', function()
	{
		document.querySelector('.main-content').classList.toggle('s-signup')
		document.querySelector('.vendor').classList.add('active')
		document.querySelector('.sing-in').classList.remove('active')
		document.querySelector('.m-3').classList.add('active')
		document.querySelector('.m-1').classList.remove('active')

	}
);