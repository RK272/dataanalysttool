function uploadCSV() {
    const fileInput = document.getElementById('file-input');
    const columnNames = document.getElementById('column-names').value;
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('columns', columnNames);

    fetch('/train', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // Parse JSON directly
    .then(data => {
        if (data.error) {
            alert('Error: ' + data.error);
        } else {
            // Redirect to results page
            const imageParams = encodeURIComponent(data.images.join(','));
            window.location.href = `/results?images=${imageParams}`;
        }
    })
    .catch(error => {
        console.error('Error uploading CSV:', error);
        alert('An error occurred while uploading the CSV.');
    });
}
