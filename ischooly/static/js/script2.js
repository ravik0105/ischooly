const tocLinks = document.querySelectorAll('#toc-container a');

tocLinks.forEach(link => {
	link.addEventListener('click', (event) => {
		event.preventDefault();

	// Load content using AJAX or fetch (replace with your preferred method)
		fetch(link.href)
				.then(response => response.text())
				.then(content => {
			const contentContainer = document.getElementById('content-container');
			contentContainer.innerHTML = content;

		// Scroll to target element if specified in the href (optional)
			const targetId = link.href.split('#')[1];
			if (targetId) {
				const targetElement = document.getElementById(targetId);
				if (targetElement) {
					targetElement.scrollIntoView({ behavior: 'smooth' });
				}
			}
		})
				.catch(error => {
			console.error(error); // Handle errors, e.g., display an error message
		});
	});
});
