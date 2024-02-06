const contentId = document.getElementById('content');
const tocNav = document.getElementById('toc');

// Function to load content and update TOC
function loadContent(filename, headingText) {
	fetch(filename)
			.then(response => response.text())
			.then(htmlContent => {
		contentId.innerHTML = htmlContent; // Update content

	    // Create TOC item and append
		const tocItem = document.createElement('a');
		tocItem.href = `#${headingText}`;
		tocItem.textContent = headingText;
		tocNav.appendChild(tocItem);
	});
}

// Load initial content (replace with your logic)
loadContent('/pages/content1.html', 'Content 1');

// Optionally, add event listeners for dynamic content loading
// based on user interactions or page navigation